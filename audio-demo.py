from turtle import delay
import pygame.mixer as mixer

AUDIO_FILE_PATH = "audio-demo.wav"


# init and start playback
mixer.init(frequency=48000, size=-16, channels=2)
sound = mixer.Sound(AUDIO_FILE_PATH)
channel = sound.play(loops=-1,fade_ms=1000)

# change channel volume according to user input
while True:
    output = input("output channel: \n")

    if output == 'middle':
        channel.set_volume(1,1)

    elif output == 'left':
        channel.set_volume(1,0.2)

    elif output == 'right':
        channel.set_volume(0.2,1)
    
    elif output == 'stop':
        break

    delay(2)