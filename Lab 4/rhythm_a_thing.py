import time
import board
import busio
import os

import adafruit_mpr121

i2c = busio.I2C(board.SCL, board.SDA)

mpr121 = adafruit_mpr121.MPR121(i2c)

#could abstract to arbitrary drums by mapping
#inputs to sounds in ordered lists
drum_folder = "drumkit/"
drum_sounds = ["cymbal1.wav", "snare.wav", "tom.wav", "kick.wav", "cymbal2.wav"]
drum_press_history = [False] * 6

while True:
    for i in range(5):
        if mpr121[i].value and not drum_press_history[i]:
            os.system('omxplayer ' + drum_folder +  drum_sounds[i] + " &")
            drum_press_history[i] = True
        else:
            drum_press_history[i] = False
    time.sleep(.3)
