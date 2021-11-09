import time
import board
import busio
import os

import adafruit_mpr121
import qwiic_led_stick

i2c = busio.I2C(board.SCL, board.SDA)

mpr121 = adafruit_mpr121.MPR121(i2c)
leds = qwiic_led_stick.QwiicLEDStick()


#could abstract to arbitrary drums by mapping
#inputs to sounds in ordered lists
drum_folder = "drumkit/"
drum_sounds = ["cymbal1.wav", "snare.wav", "tom.wav", "kick.wav", "cymbal2.wav"]
drum_press_history = [False] * 6

beat = 1
num_beats = 8
last_beat = 1
drum_colors = [[0,0,200], [0,0,0], [0,200,0], [0,0,0], [0,0,200], [0,200,0], [0,0,200], [0,0,0], [200,0,0]]
correct_drum = [2, -1, 2, -1, 2, 1, 2, -1]

leds.set_all_LED_brightness(5)
leds.set_all_LED_color(0,0,0)

while True:
    if (beat == num_beats):
        beat = 1
    leds.set_single_LED_color(beat, drum_colors[beat][0], drum_colors[beat][1], drum_colors[beat][2]) 
    for i in range(5):
        if mpr121[i].value and not drum_press_history[i]:
            #os.system('omxplayer ' + drum_folder +  drum_sounds[i] + " &")
            drum_press_history[i] = True
        else:
            drum_press_history[i] = False
        if drum_press_history[i] and (correct_drum[beat] == i):
            #leds.set_single_LED_color(10, 100,100,0)
            print("")
        else:
            print("")
            #leds.set_single_LED_color(10, 0,0,0)
    #time.sleep(1)
    last_beat = beat
    beat = beat + 1
    leds.set_single_LED_color(last_beat, 0, 0, 0)
    time.sleep(.8)
