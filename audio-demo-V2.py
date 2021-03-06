import time
import pygame.mixer as mixer

MIDDLE_FILE = "crowd-talking.wav"
LEFT_FILE = "left-person.wav"
RIGHT_FILE = "right-person.wav"

FADE_TIME = 1       #fade time in seconds
FADE_STEPS = 5      #fade steps


# fade from current volume to target volume, given as tuple [left, right]
def fade(sounds, current, target):
    '''
    Fading between different audio levels
    input:
        sounds: soundfiles
        current: current volume as tuple [left, right]
        target: target volume as [left, right]
    output:
        new volume level as tuple [left, right]
    '''
    print(f"fading from {current} to {target}")

    #calculate discrete volumesteps
    volumesteps = [[], []]
    delta = [current[0]-target[0], current[1]-target[1]]
    for channel in range(2):
        volumesteps[channel] = [current[channel] - i * (delta[channel] / FADE_STEPS) for i in range(FADE_STEPS+1)]
    
    # set volume according to calculated steps
    for vol in range(len(volumesteps[0])):
        sounds['left'].set_volume(volumesteps[0][vol])
        sounds['right'].set_volume(volumesteps[1][vol])
        time.sleep(FADE_TIME/FADE_STEPS)
    
    # return volume as tuple [left, right]
    return [sounds['left'].get_volume(), sounds['right'].get_volume()]


# load sounds
def loadsounds():
    '''
    Loading sounds from files
    input:
    output:
        dictionary with loaded sounds. Keys are 'left', 'middle', 'right'
    '''
    left_sound = mixer.Sound(LEFT_FILE)
    middle_sound = mixer.Sound(MIDDLE_FILE)
    right_sound = mixer.Sound(RIGHT_FILE)

    return {'left': left_sound, 'middle': middle_sound, 'right': right_sound}


def audio_demo():
    '''
    Adjusting audio levels according to eye position
    input:
        output of the heog classifier. Keywords are 'Left', 'Center', 'Right'
    output:
    '''
    #init and load sounds
    mixer.init(frequency=48000, size=-16, channels=3)
    volume = [1,1]
    sounds = loadsounds()

    #start playback
    for sound in sounds.values():
        sound.play(loops=-1, fade_ms=200)

    # change channel volume according to user input
    while volume != [0,0]:

        eye_position = input("channel: \n")

        if eye_position == 'stop':
            mixer.fadeout(2000)
            volume = [0,0]
        
        elif eye_position == 'Left':
            volume = fade(sounds=sounds, current=volume, target=[1, 0.2])

        elif eye_position == 'Right':
            volume = fade(sounds=sounds, current=volume, target=[0.2, 1])
        
        elif eye_position == 'Center':
            volume = fade(sounds=sounds, current=volume, target=[1, 1])

        else:
            continue

        time.sleep(1)

audio_demo()