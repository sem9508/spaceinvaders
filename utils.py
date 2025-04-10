
import base64
import pygame
import numpy as np
import cv2

def encode_frame(surface):
    """Convert Pygame surface to a Base64 image."""
    frame = pygame.surfarray.array3d(surface)
    frame = np.rot90(frame)  # Rotate to match expected orientation
    frame = np.flipud(frame)  # Flip vertically
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)  # Convert to OpenCV format
    _, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 70])
    return base64.b64encode(buffer).decode('utf-8')