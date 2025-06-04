import pygame
import time
import os

pygame.mixer.init()

def play_melody(notes):
    base_path = os.path.abspath("sounds")
    for i, (note, duration) in enumerate(notes, start=1):
        if note == "REST":
            print(f"(pauza {duration}ms)")
            time.sleep(duration / 1000)
            continue

        path = os.path.join(base_path, f"{note}.wav")
        if not os.path.exists(path):
            print(f"(brak dźwięku: {note})")
            continue

        try:
            print(f"Playing note {i}/{len(notes)}: {note} ({duration}ms)")
            sound = pygame.mixer.Sound(path)
            sound.play()
            time.sleep(duration / 1000)
        except Exception as e:
            print(f"Error playing note {note}: {e}")
