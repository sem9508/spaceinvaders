import pygame

def handle_movement(keys, obj, left_key, right_key, up_key, down_key):
    if keys[left_key]:
        pass
    if keys[right_key]:
        pass

    if up_key and down_key:

        if keys[up_key]:
            pass
        if keys[down_key]:
            pass

def use_input(keys, objects):
    
    for obj in objects:
        if hasattr(obj, 'input_group'):
            if obj.input_group == 1:
                handle_movement(keys, obj, pygame.K_LEFT, pygame.K_RIGHT, None, None)
