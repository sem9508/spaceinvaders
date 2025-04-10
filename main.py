import pygame
from constants import *
from screens.game import Game
from screens.menu import Menu
from screens.options import Options
import sys
from utils import encode_frame
from flask import Flask, request, render_template, Response
import threading
import time

frame_lock = threading.Lock()
app = Flask(__name__)
current_frame = None

def generate():
    """Stream JPEG frames als MJPEG."""
    while True:
        with frame_lock:
            if current_frame is None:
                continue
            frame = current_frame
        header = '--frame\r\nContent-Type: image/jpeg\r\n\r\n'.encode('utf-8')
        yield header + frame + b'\r\n'

        time.sleep(1 / 30)

@app.route('/current_frame')
def current_frame_route():
    """Serve the current frame as an image."""
    if current_frame is None:
        print(1)
        return "No frame available", 404
    
    return f'<img src="data:image/jpeg;base64,{current_frame}" />'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/video_feed')
def video_feed():
    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')

def set_current_frame(surface):
    global current_frame
    with frame_lock:
        current_frame = encode_frame(surface)

pygame.init()

def game_loop():
    global current_frame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Only in game loop
    run = True
    active_screen = 0

    while run:
        if active_screen == 0:
            window_instance = Menu(screen, set_current_frame)
            active_screen = window_instance.loop()

        elif active_screen == 1:
            window_instance = Game(screen, set_current_frame)
            active_screen = window_instance.loop()

        elif active_screen == 2:
            window_instance = Options(screen, set_current_frame)
            active_screen = window_instance.loop()

        else:  # window closure
            pygame.quit()
            sys.exit()

if __name__ == '__main__':
    # Run the game loop in a separate thread
    t = threading.Thread(target=game_loop)
    t.daemon = True  # Ensures the thread will exit when the main program exits
    t.start()

    # Run Flask app in the main thread
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)  # Disable Flask's reloader since we're using threads
