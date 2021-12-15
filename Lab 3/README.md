# Chatterboxes
[![Watch the video](https://user-images.githubusercontent.com/1128669/135009222-111fe522-e6ba-46ad-b6dc-d1633d21129c.png)](https://www.youtube.com/embed/Q8FWzLMobx0?start=19)

In this lab, we want you to design interaction with a speech-enabled device--something that listens and talks to you. This device can do anything *but* control lights (since we already did that in Lab 1).  First, we want you first to storyboard what you imagine the conversational interaction to be like. Then, you will use wizarding techniques to elicit examples of what people might say, ask, or respond.  We then want you to use the examples collected from at least two other people to inform the redesign of the device.

We will focus on **audio** as the main modality for interaction to start; these general techniques can be extended to **video**, **haptics** or other interactive mechanisms in the second part of the Lab.

## Prep for Part 1: Get the Latest Content and Pick up Additional Parts 

### Pick up Additional Parts

As mentioned during the class, we ordered additional mini microphone for Lab 3. Also, a new part that has finally arrived is encoder! Please remember to pick them up from the TA.

### Get the Latest Content

As always, pull updates from the class Interactive-Lab-Hub to both your Pi and your own GitHub repo. As we discussed in the class, there are 2 ways you can do so:

**\[recommended\]**Option 1: On the Pi, `cd` to your `Interactive-Lab-Hub`, pull the updates from upstream (class lab-hub) and push the updates back to your own GitHub repo. You will need the *personal access token* for this.

```
pi@ixe00:~$ cd Interactive-Lab-Hub
pi@ixe00:~/Interactive-Lab-Hub $ git pull upstream Fall2021
pi@ixe00:~/Interactive-Lab-Hub $ git add .
pi@ixe00:~/Interactive-Lab-Hub $ git commit -m "get lab3 updates"
pi@ixe00:~/Interactive-Lab-Hub $ git push
```

Option 2: On your your own GitHub repo, [create pull request](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2021Fall/readings/Submitting%20Labs.md) to get updates from the class Interactive-Lab-Hub. After you have latest updates online, go on your Pi, `cd` to your `Interactive-Lab-Hub` and use `git pull` to get updates from your own GitHub repo.

## Part 1.
### Text to Speech 

In this part of lab, we are going to start peeking into the world of audio on your Pi! 

We will be using a USB microphone, and the speaker on your webcamera. (Originally we intended to use the microphone on the web camera, but it does not seem to work on Linux.) In the home directory of your Pi, there is a folder called `text2speech` containing several shell scripts. `cd` to the folder and list out all the files by `ls`:

```
pi@ixe00:~/text2speech $ ls
Download        festival_demo.sh  GoogleTTS_demo.sh  pico2text_demo.sh
espeak_demo.sh  flite_demo.sh     lookdave.wav
```

You can run these shell files by typing `./filename`, for example, typing `./espeak_demo.sh` and see what happens. Take some time to look at each script and see how it works. You can see a script by typing `cat filename`. For instance:

```
pi@ixe00:~/text2speech $ cat festival_demo.sh 
#from: https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)#Festival_Text_to_Speech

echo "Just what do you think you're doing, Dave?" | festival --tts
```

Now, you might wonder what exactly is a `.sh` file? Typically, a `.sh` file is a shell script which you can execute in a terminal. The example files we offer here are for you to figure out the ways to play with audio on your Pi!

You can also play audio files directly with `aplay filename`. Try typing `aplay lookdave.wav`.

\*\***Write your own shell file to use your favorite of these TTS engines to have your Pi greet you by name.**\*\*
(This shell file should be saved to your own repo for this lab.)

Bonus: If this topic is very exciting to you, you can try out this new TTS system we recently learned about: https://github.com/rhasspy/larynx

### Speech to Text

Now examine the `speech2text` folder. We are using a speech recognition engine, [Vosk](https://alphacephei.com/vosk/), which is made by researchers at Carnegie Mellon University. Vosk is amazing because it is an offline speech recognition engine; that is, all the processing for the speech recognition is happening onboard the Raspberry Pi. 

In particular, look at `test_words.py` and make sure you understand how the vocab is defined. Then try `./vosk_demo_mic.sh`

One thing you might need to pay attention to is the audio input setting of Pi. Since you are plugging the USB cable of your webcam to your Pi at the same time to act as speaker, the default input might be set to the webcam microphone, which will not be working for recording.

\*\***Write your own shell file that verbally asks for a numerical based input (such as a phone number, zipcode, number of pets, etc) and records the answer the respondent provides.**\*\*

Bonus Activity:

If you are really excited about Speech to Text, you can try out [Mozilla DeepSpeech](https://github.com/mozilla/DeepSpeech) and [voice2json](http://voice2json.org/install.html)
There is an included [dspeech](./dspeech) demo  on the Pi. If you're interested in trying it out, we suggest you create a seperarate virutal environment for it . Create a new Python virtual environment by typing the following commands.

```
pi@ixe00:~ $ virtualenv dspeechexercise
pi@ixe00:~ $ source dspeechexercise/bin/activate
(dspeechexercise) pi@ixe00:~ $ 
```

### Serving Pages

In Lab 1, we served a webpage with flask. In this lab, you may find it useful to serve a webpage for the controller on a remote device. Here is a simple example of a webserver.

```
pi@ixe00:~/Interactive-Lab-Hub/Lab 3 $ python server.py
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 162-573-883
```
From a remote browser on the same network, check to make sure your webserver is working by going to `http://<YourPiIPAddress>:5000`. You should be able to see "Hello World" on the webpage.

### Storyboard

Storyboard and/or use a Verplank diagram to design a speech-enabled device. (Stuck? Make a device that talks for dogs. If that is too stupid, find an application that is better than that.) 


\*\***Post your storyboard and diagram here.**\*\*
![Brainstorming](https://github.com/nicholasburka/Interactive-Lab-Hub/blob/Fall2021/Lab%203/lab3-brainstorm.png)
![Verplank diagram](https://github.com/nicholasburka/Interactive-Lab-Hub/blob/Fall2021/Lab%203/lab3-verplank-diagram.png)

Write out what you imagine the dialogue to be. Use cards, post-its, or whatever method helps you develop alternatives or group responses. 
(Process described at top of dialogue imagination)
![Imagined dialogue](https://github.com/nicholasburka/Interactive-Lab-Hub/blob/Fall2021/Lab%203/example-dialogue.png)


### Acting out the dialogue

Find a partner, and *without sharing the script with your partner* try out the dialogue you've designed, where you (as the device designer) act as the device you are designing.  Please record this interaction (for example, using Zoom's record feature).

My partner for the interaction didn't realize the recording would be shared with a class (he's a friend from home) and declined to have the recording shared. The dialogue went completely differently than I expected. I expected thoughts to be paced, slowly and deliberately, relying on the device to provide repetition/reflection that prompted new thoughts. However, when I explained the hypothetical scenario to my friend - that he would be a real estate broker, offered to trade three potentially lucrative houses for an apartment complex - he launched directly into a long train of thought, pausing only momentarily, and not long enough to prompt my device to repeat any of his thoughts. 

This interaction suggested that the device may be better suited for users as an organizational thought playback and transcription tool rather than a strictly in-the-moment feedback system.

### Wizarding with the Pi (optional)
In the [demo directory](./demo), you will find an example Wizard of Oz project. In that project, you can see how audio and sensor data is streamed from the Pi to a wizard controller that runs in the browser.  You may use this demo code as a template. By running the `app.py` script, you can see how audio and sensor data (Adafruit MPU-6050 6-DoF Accel and Gyro Sensor) is streamed from the Pi to a wizard controller that runs in the browser `http://<YouPiIPAddress>:5000`. You can control what the system says from the controller as well!

\*\***Describe if the dialogue seemed different than what you imagined, or when acted out, when it was wizarded, and how.**\*\*

# Lab 3 Part 2

For Part 2, you will redesign the interaction with the speech-enabled device using the data collected, as well as feedback from part 1.

## Prep for Part 2

1. What are concrete things that could use improvement in the design of your device? For example: wording, timing, anticipation of misunderstandings...

- the device's timing only works for slow/confused/other trains of thought in which the repetition of thought after a moment of silence is useful
- by allowing users to pace, save, and organize their thoughts, users can still find value in the device regardless of the speed or continuity of their thoughts
- furthermore, storing and organizing all user-saved thoughts opens up a variety of possible uses: organizational notes, visualizations, analytics (necessarily this device would be encrypted and private)
- since thoughts would be organized (and colored), users could playback thoughts not immediately preceding their current thought, switch train of thoughts, and generally have a more flexible user experience 

3. What are other modes of interaction _beyond speech_ that you might also use to clarify how to interact?
- by modeling an organizational tool like a Novation Launchpad (used for making music with Ableton Live), could open up other modes of interaction: playback by pushing colored cell-buttons, organizing or deleting cells, re-coloring cells to show relatedness
- tactile feedback would be nice
5. Make a new storyboard, diagram and/or script based on these reflections.
![Brainstorming](https://github.com/nicholasburka/Interactive-Lab-Hub/blob/Fall2021/Lab%203/lab3-2-brainstorm.png)
![Verplank diagram](https://github.com/nicholasburka/Interactive-Lab-Hub/blob/Fall2021/Lab%203/lab3-2-verplank-diagram.png)
## Prototype your system

The system should:
* use the Raspberry Pi 
* use one or more sensors
* require participants to speak to it. 

The system works simply - press a button on the numpad to record an audio snippet of a predefined length, and then press that same button again to playback,
or press a different button to record a new snippet. Future iterations would allow overwriting and have visual feedback indicating when
the system is recording, playing back, or overwriting, and which buttons/cells have already recorded audio.

[Video demo/test](https://www.youtube.com/watch?v=_1z5ocWpiQY)

## Test the system

### What worked well about the system and what didn't?
The system performed core functionality well. However, it didn't feel fluid, and the inability to record audio of different lengths limits
possibilities.

### What worked well about the controller and what didn't?
The buttons aren't satisfying to push and don't have clear tactile feedback when depressed. There's no indication of when the system is recording
or playing back audio, which could cause issues. Also, having no clear feedback about which cells have been recorded to relies on user memory.

### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?
It's important that the system be well-suited and versatile to different user needs, as "thought processes" are highly personal. Therefore,
the system should be highly fluid, responsive, able to record audio of different lengths and quickly, and imply an organization of recorded
material regardless of (and in addition to) user organization.

### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?
Monitoring how users relate to the button, various timings could provide more insight. Also how quickly after pushing a button users
begin to speak, and how quickly after recording one thought users record another. Recording users continuously to see if they use the 
system as a real-time recorder or post-hoc - do they speak "off the air"?
