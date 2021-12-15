# Observant Systems


For lab this week, we focus on creating interactive systems that can detect and respond to events or stimuli in the environment of the Pi, like the Boat Detector we mentioned in lecture. 
Your **observant device** could, for example, count items, find objects, recognize an event or continuously monitor a room.

This lab will help you think through the design of observant systems, particularly corner cases that the algorithms needs to be aware of.

## Prep

1.  Pull the new Github Repo.
2.  Install VNC on your laptop if you have not yet done so. This lab will actually require you to run script on your Pi through VNC so that you can see the video stream. Please refer to the [prep for Lab 2](https://github.com/FAR-Lab/Interactive-Lab-Hub/blob/Fall2021/Lab%202/prep.md), we offered the instruction at the bottom.
3.  Read about [OpenCV](https://opencv.org/about/), [MediaPipe](https://mediapipe.dev/), and [TeachableMachines](https://teachablemachine.withgoogle.com/).
4.  Read Belloti, et al.'s [Making Sense of Sensing Systems: Five Questions for Designers and Researchers](https://www.cc.gatech.edu/~keith/pubs/chi2002-sensing.pdf).

### For the lab, you will need:

1. Raspberry Pi
1. Webcam 
1. Microphone (if you want to have speech or sound input for your design)

### Deliverables for this lab are:
1. Show pictures, videos of the "sense-making" algorithms you tried.
1. Show a video of how you embed one of these algorithms into your observant system.
1. Test, characterize your interactive device. Show faults in the detection and how the system handled it.

## Overview
Building upon the paper-airplane metaphor (we're understanding the material of machine learning for design), here are the four sections of the lab activity:

A) [Play](#part-a)

B) [Fold](#part-b)

C) [Flight test](#part-c)

D) [Reflect](#part-d)

---

### Part A
### Play with different sense-making algorithms.

#### OpenCV
A more traditional method to extract information out of images is provided with OpenCV. The RPI image provided to you comes with an optimized installation that can be accessed through python. We included 4 standard OpenCV examples: contour(blob) detection, face detection with the ``Haarcascade``, flow detection (a type of keypoint tracking), and standard object detection with the [Yolo](https://pjreddie.com/darknet/yolo/) darknet.

Most examples can be run with a screen (e.g. VNC or ssh -X or with an HDMI monitor), or with just the terminal. The examples are separated out into different folders. Each folder contains a ```HowToUse.md``` file, which explains how to run the python example. 

Following is a nicer way you can run and see the flow of the `openCV-examples` we have included in your Pi. Instead of `ls`, the command we will be using here is `tree`. [Tree](http://mama.indstate.edu/users/ice/tree/) is a recursive directory colored listing command that produces a depth indented listing of files. Install `tree` first and `cd` to the `openCV-examples` folder and run the command:

```shell
pi@ixe00:~ $ sudo apt install tree
...
pi@ixe00:~ $ cd openCV-examples
pi@ixe00:~/openCV-examples $ tree -l
.
├── contours-detection
│   ├── contours.py
│   └── HowToUse.md
├── data
│   ├── slow_traffic_small.mp4
│   └── test.jpg
├── face-detection
│   ├── face-detection.py
│   ├── faces_detected.jpg
│   ├── haarcascade_eye_tree_eyeglasses.xml
│   ├── haarcascade_eye.xml
│   ├── haarcascade_frontalface_alt.xml
│   ├── haarcascade_frontalface_default.xml
│   └── HowToUse.md
├── flow-detection
│   ├── flow.png
│   ├── HowToUse.md
│   └── optical_flow.py
└── object-detection
    ├── detected_out.jpg
    ├── detect.py
    ├── frozen_inference_graph.pb
    ├── HowToUse.md
    └── ssd_mobilenet_v2_coco_2018_03_29.pbtxt
```

The flow detection might seem random, but consider [this recent research](https://cseweb.ucsd.edu/~lriek/papers/taylor-icra-2021.pdf) that uses optical flow to determine busy-ness in hospital settings to facilitate robot navigation. Note the velocity parameter on page 3 and the mentions of optical flow.

Now, connect your webcam to your Pi and use **VNC to access to your Pi** and open the terminal. Use the following command lines to try each of the examples we provided:
(***it will not work if you use ssh from your laptop***)

```
pi@ixe00:~$ cd ~/openCV-examples/contours-detection
pi@ixe00:~/openCV-examples/contours-detection $ python contours.py
...
pi@ixe00:~$ cd ~/openCV-examples/face-detection
pi@ixe00:~/openCV-examples/face-detection $ python face-detection.py
...
pi@ixe00:~$ cd ~/openCV-examples/flow-detection
pi@ixe00:~/openCV-examples/flow-detection $ python optical_flow.py 0 window
...
pi@ixe00:~$ cd ~/openCV-examples/object-detection
pi@ixe00:~/openCV-examples/object-detection $ python detect.py
```

**\*\*\*Try each of the following four examples in the `openCV-examples`, include screenshots of your use and write about one design for each example that might work based on the individual benefits to each algorithm.\*\*\***

![contour](https://github.com/nicholasburka/Interactive-Lab-Hub/blob/Fall2021/Lab%205/contour.png)
![face](https://github.com/nicholasburka/Interactive-Lab-Hub/blob/Fall2021/Lab%205/face.png)
![flow](https://github.com/nicholasburka/Interactive-Lab-Hub/blob/Fall2021/Lab%205/flow.png)
![object](https://github.com/nicholasburka/Interactive-Lab-Hub/blob/Fall2021/Lab%205/object.png)
![design ideas](https://github.com/nicholasburka/Interactive-Lab-Hub/blob/Fall2021/Lab%205/design-ideas.png)

#### MediaPipe

A more recent open source and efficient method of extracting information from video streams comes out of Google's [MediaPipe](https://mediapipe.dev/), which offers state of the art face, face mesh, hand pose, and body pose detection.

![Alt Text](mp.gif)

To get started, create a new virtual environment with special indication this time:

```
pi@ixe00:~ $ virtualenv mpipe --system-site-packages
pi@ixe00:~ $ source mpipe/bin/activate
(mpipe) pi@ixe00:~ $ 
```

and install the following.

```
...
(mpipe) pi@ixe00:~ $ sudo apt install ffmpeg python3-opencv
(mpipe) pi@ixe00:~ $ sudo apt install libxcb-shm0 libcdio-paranoia-dev libsdl2-2.0-0 libxv1  libtheora0 libva-drm2 libva-x11-2 libvdpau1 libharfbuzz0b libbluray2 libatlas-base-dev libhdf5-103 libgtk-3-0 libdc1394-22 libopenexr23
(mpipe) pi@ixe00:~ $ pip3 install mediapipe-rpi4 pyalsaaudio
```

Each of the installs will take a while, please be patient. After successfully installing mediapipe, connect your webcam to your Pi and use **VNC to access to your Pi**, open the terminal, and go to Lab 5 folder and run the hand pose detection script we provide:
(***it will not work if you use ssh from your laptop***)


```
(mpipe) pi@ixe00:~ $ cd Interactive-Lab-Hub/Lab\ 5
(mpipe) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ python hand_pose.py
```

Try the two main features of this script: 1) pinching for percentage control, and 2) "[Quiet Coyote](https://www.youtube.com/watch?v=qsKlNVpY7zg)" for instant percentage setting. Notice how this example uses hardcoded positions and relates those positions with a desired set of events, in `hand_pose.py` lines 48-53. 

**\*\*\*Consider how you might use this position based approach to create an interaction, and write how you might use it on either face, hand or body pose tracking.\*\*\***
- 'Dance Dance Recognition' - a dance move recognizer. Could be generalized to many kinds of movement trainers (martial arts, physical therapy). Could have a robot that demonstrates a pose, and when the person matches that pose, the robot demonstrates the next move in the sequence (e.g. ballet sequences). 
- Conversely, wizarding robots.

(You might also consider how this notion of percentage control with hand tracking might be used in some of the physical UI you may have experimented with in the last lab, for instance in controlling a servo or rotary encoder.)


#### Teachable Machines
Google's [TeachableMachines](https://teachablemachine.withgoogle.com/train) might look very simple. However, its simplicity is very useful for experimenting with the capabilities of this technology.

![Alt Text](tm.gif)

To get started, create and activate a new virtual environment for this exercise with special indication:

```
pi@ixe00:~ $ virtualenv tmachine --system-site-packages
pi@ixe00:~ $ source tmachine/bin/activate
(tmachine) pi@ixe00:~ $ 
```

After activating the virtual environment, install the requisite TensorFlow libraries by running the following lines:
```
(tmachine) pi@ixe00:~ $ cd Interactive-Lab-Hub/Lab\ 5
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ sudo chmod +x ./teachable_machines.sh
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ ./teachable_machines.sh
``` 

This might take a while to get fully installed. After installation, connect your webcam to your Pi and use **VNC to access to your Pi**, open the terminal, and go to Lab 5 folder and run the example script:
(***it will not work if you use ssh from your laptop***)

```
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ python tm_ppe_detection.py
```


(**Optionally**: You can train your own model, too. First, visit [TeachableMachines](https://teachablemachine.withgoogle.com/train), select Image Project and Standard model. Second, use the webcam on your computer to train a model. For each class try to have over 50 samples, and consider adding a background class where you have nothing in view so the model is trained to know that this is the background. Then create classes based on what you want the model to classify. Lastly, preview and iterate, or export your model as a 'Tensorflow' model, and select 'Keras'. You will find an '.h5' file and a 'labels.txt' file. These are included in this labs 'teachable_machines' folder, to make the PPE model you used earlier. You can make your own folder or replace these to make your own classifier.)

**\*\*\*Whether you make your own model or not, include screenshots of your use of Teachable Machines, and write how you might use this to create your own classifier. Include what different affordances this method brings, compared to the OpenCV or MediaPipe options.\*\*\***
![teachable machines](https://github.com/nicholasburka/Interactive-Lab-Hub/blob/Fall2021/Lab%205/teachable_machines.png)
Teachable Machines affords developers a simple way to access the semantic-linguistic content of a video stream, not just its shape data (OpenCV or MediaPipe). In other words, TM determines the names of objects in video. Google might use TM to make a classifier to optimize a video chat algorithm by noting when two people or more are in the frame and altering the video chat audio processing algorithm. I could use TM to create fun presentation effects during a new product reveal - once the product appears on screen, apply a filter to dim the screen around the product and add particle/aura effects. Or, to cue special effects during improvised theater productions when an actor reveals one of their objects (live DnD etc).

*Don't forget to run ```deactivate``` to end the Teachable Machines demo, and to reactivate with ```source tmachine/bin/activate``` when you want to use it again.*


#### Filtering, FFTs, and Time Series data. (optional)
Additional filtering and analysis can be done on the sensors that were provided in the kit. For example, running a Fast Fourier Transform over the IMU data stream could create a simple activity classifier between walking, running, and standing.

Using the accelerometer, try the following:

**1. Set up threshold detection** Can you identify when a signal goes above certain fixed values?

**2. Set up averaging** Can you average your signal in N-sample blocks? N-sample running average?

**3. Set up peak detection** Can you identify when your signal reaches a peak and then goes down?

**\*\*\*Include links to your code here, and put the code for these in your repo--they will come in handy later.\*\*\***


### Part B
### Construct a simple interaction.

Pick one of the models you have tried, pick a class of objects, and experiment with prototyping an interaction.
This can be as simple as the boat detector earlier.
Try out different interaction outputs and inputs.

I tried to make a Teachable Machines models that could be used to practice the letters of the American Sign Language alphabet.
Ideally, a model would learn ASL words, but these require time-series analysis combined with image recognition, and while that 
would be cool, I didn't have enough time for that. 

Unfortunately, as you'll see below, using Teachable Machines to train 26 classes of different hand positions didn't work very well,
even though I tried to normalize the images by including different head placements in each class dataset and different hands/handsizes.

![ASL 1](https://github.com/nicholasburka/Interactive-Lab-Hub/blob/Fall2021/Lab%205/ASL-full-alpha-1.png)
![ASL 2](https://github.com/nicholasburka/Interactive-Lab-Hub/blob/Fall2021/Lab%205/ASL-full-alpha-2.png)

### Part C
### Test the interaction prototype

Now flight test your interactive prototype and **note down your observations**:
For example:
1. When does it what it is supposed to do?
1. When does it fail?
1. When it fails, why does it fail?
1. Based on the behavior you have seen, what other scenarios could cause problems?

In the first iteration, the model fails entirely. It simply responds too erratically and noisily to input images to accurately detect any ASL letters. It fails in some particular ways: the model produces false A's with certain other letters, and my head's position also influences certain errors, representing a failure to normalize the datasets with different backgrounds (such that each class dataset can reflect the hand position independently of any background features, and in balance with other classes).

I built a 2nd iteration, to distinguish an A and B in American Sign Language.

![ASL AB 1](https://github.com/nicholasburka/Interactive-Lab-Hub/blob/Fall2021/Lab%205/ASL-AB-1.png)
![ASL AB 2](https://github.com/nicholasburka/Interactive-Lab-Hub/blob/Fall2021/Lab%205/ASL-AB-2.png)
![ASL AB 3](https://github.com/nicholasburka/Interactive-Lab-Hub/blob/Fall2021/Lab%205/ASL-AB-3.png)
![ASL AB 4](https://github.com/nicholasburka/Interactive-Lab-Hub/blob/Fall2021/Lab%205/ASL-AB-4.png)

In the 2nd iteration, the model works robustly. Given this binary model, a misclassification would ruin the performance. This model could be expanded to something like a rock paper scissors game - maybe with A/B/C in ASL, if not simply rock/paper/scissors. In the current iteration, I don't think the model would fail but it doesn't provide interesting interactions - learning only A/B in ASL, while marginally useful, may be trivial for the user and not nearly as useful as the full alphabet, let alone a sophistocated vocabulary. Rock-paper-scissors would at least be fun.

**\*\*\*Think about someone using the system. Describe how you think this will work.\*\*\***
1. Are they aware of the uncertainties in the system?
1. How bad would they be impacted by a miss classification?
1. How could change your interactive system to address this?
1. Are there optimizations you can try to do on your sense-making algorithm.

### Part D
### Characterize your own Observant system

![ASL AB 1](https://github.com/nicholasburka/Interactive-Lab-Hub/blob/Fall2021/Lab%205/ASL-AB-1.png)
![ASL AB 2](https://github.com/nicholasburka/Interactive-Lab-Hub/blob/Fall2021/Lab%205/ASL-AB-2.png)
![ASL AB 3](https://github.com/nicholasburka/Interactive-Lab-Hub/blob/Fall2021/Lab%205/ASL-AB-3.png)
![ASL AB 4](https://github.com/nicholasburka/Interactive-Lab-Hub/blob/Fall2021/Lab%205/ASL-AB-4.png)

Briefly repeating from the above section, this model could be expanded to something like a rock paper scissors game - maybe with A/B/C in ASL, if not simply rock/paper/scissors. In the current iteration, I don't think the model would fail but it doesn't provide interesting interactions - learning only A/B in ASL, while marginally useful, may be trivial for the user and not nearly as useful as the full alphabet, let alone a sophistocated vocabulary. Rock-paper-scissors would at least be fun.

Rather than recording a video, I'll save interactivity with auditory feedback & a physical representation separate from the computer and camera for my next iteration involving RPS, and refer to the photos of my second iteration above in part C. To expand on the questions here, since the Teachable Machines model has been robust against differences in background given two classes and a variety of background and size conditions in each class' training set, this model can be used without much concern for good and bad environments. That said, an environment with multiple hands in the picture may break the model. Also, for expansion to the real world, image sets may better include diverse hands (size, race, gender, shape). When the model doesn't work, then the user would have a potentially frustrating experience - the system would misidentify the user's hand pose and therefore either misrepresent the sign languge letter depicted (removing any learning outcome) or give the player the wrong hand in RPS (changing the game outcome). For now, X feels simple. I like the feedback of having my hand poses recognized.

Now that you have experimented with one or more of these sense-making systems **characterize their behavior**.
During the lecture, we mentioned questions to help characterize a material:
* What can you use X for?
* What is a good environment for X?
* What is a bad environment for X?
* When will X break?
* When it breaks how will X break?
* What are other properties/behaviors of X?
* How does X feel?

**\*\*\*Include a short video demonstrating the answers to these questions.\*\*\***
[Teachable Machines Test](https://www.youtube.com/watch?v=ZXRyPOKyqPs)

### Part 2.

Following exploration and reflection from Part 1, finish building your interactive system, and demonstrate it in use with a video.

**\*\*\*Include a short video demonstrating the finished result.\*\*\***
[Proto RPS Teachable Machines System Demo](https://www.youtube.com/watch?v=r0HloEvlmro)
I made a simple matching game called agree, where the goal is to match the gesture (either ASL A or B) of your partner - if you do
you both get a point. It's meant to use text-to-speech to prompt interaction with a user, and uses the 
Teachable Machines model and webcam, but has the most sophistocated code, in agree.py. My Raspberry Pi speaker
wasn't working, so for full effect in the video I recorded my own voice and overdubbed instead of using my code system,
but my code works on my Raspberry Pi.
