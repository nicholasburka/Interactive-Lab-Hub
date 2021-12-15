#This example is directly copied from the Tensorflow examples provided from the Teachable Machine.

import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import cv2
import sys
import random
import time
import os


# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

img = None
webCam = False
if(len(sys.argv)>1 and not sys.argv[-1]== "noWindow"):
   try:
      print("I'll try to read your image");
      img = cv2.imread(sys.argv[1])
      if img is None:
         print("Failed to load image file:", sys.argv[1])
   except:
      print("Failed to load the image are you sure that:", sys.argv[1],"is a path to an image?")
else:
   try:
      print("Trying to open the Webcam.")
      cap = cv2.VideoCapture(0)
      if cap is None or not cap.isOpened():
         raise("No camera")
      webCam = True
   except:
      print("Unable to access webcam.")


# Load the model
model = tensorflow.keras.models.load_model('agree.h5')
# Load Labels:
labels=[]
f = open("agree-labels.txt", "r")
for line in f.readlines():
    if(len(line)<1):
        continue
    labels.append(line.split(' ')[1].strip())

game_stage = "prep"

#unused
stage_text = {
"move": "choose a hand",
"recognizing": "checking hand",
"unrecognized": "unrecognized",
"recognized": "recognized",
"announce": "opponent chose"
}

def randomHand():
	return ["rock", "paper", "scissors"][random.randint(0,2)]

player_move = "A"
last_player_move = "A"
comp_move = "A"
last_comp_move = "A"

#the copycat game
def next_comp_move(style="copycat"):
    if (style == "copycat"):
        return last_player_move
    elif (style == "flipper"):
        if (last_comp_move == "A"):
            return "B"
        else:
            return "A"
    #contrarian
    else:
        if (last_player_move == "A"):
            return "B"
        else:
            return "A"

points = 0

def say(text):
    os.system('echo ' + text + ' | festival --tts &')
    time.sleep(1)

def print_and_say(text):
    print(text)
    say(text)

while(True):
    if (game_stage == "prep"):
        print_and_say("choose your move and hold")
        game_stage = "move"
        time.sleep(3)
    if (game_stage == "move"):
        print_and_say("reading your move")
        if webCam:
            ret, img = cap.read()

        rows, cols, channels = img.shape
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        size = (224, 224)
        img =  cv2.resize(img, size, interpolation = cv2.INTER_AREA)
        #turn the image into a numpy array
        image_array = np.asarray(img)

        # Normalize the image
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        # Load the image into the array
        data[0] = normalized_image_array

        # run the inference
        prediction = model.predict(data)
        last_player_move = player_move
        player_move = labels[np.argmax(prediction)]
        print("I think its a:",player_move)
        print(prediction)
        if webCam:
            if sys.argv[-1] == "noWindow":
               cv2.imwrite('detected_out.jpg',img)
               continue
            cv2.imshow('detected (press q to quit)',img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cap.release()
                break
        else:
            break
        game_stage = "announce"
    if (game_stage == "announce"):
        last_comp_move = comp_move
        comp_move = next_comp_move()
        print_and_say("you chose: " + player_move)
        print_and_say("comp chose: " + comp_move)
        if (comp_move == player_move):
            print("match! +1")
            points += 1
        else:
            print("no match")
        print_and_say("score: " + str(points))
        game_stage = "prep"

cv2.imwrite('detected_out.jpg',img)
cv2.destroyAllWindows()
