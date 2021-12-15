import qwiic_keypad
import time
import sys


import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

#play wav & record code from geeksforgeeks.org
import simpleaudio
import simpleaudio.functionchecks as fc
#fc.run_all()

freq = 44100
duration = 5

keypad = qwiic_keypad.QwiicKeypad()

if keypad.is_connected() == False:
	print("not connected")

sound_dict = {
	0: [],
	1: [],
	2: [],
	3: [],
	4: [],
	5: [],
	6: [],
	7: [],
	8: [],
	9: []
}
recd = []
while True:
	keypad.update_fifo()
	button = keypad.get_button()

	if button == -1:
		print("no key")
		time.sleep(1)

	elif button != 0:
		keychar = chr(button)
		print(keychar)
		if keychar in recd:
			print('playback')
			wave_obj = simpleaudio.WaveObject.from_wave_file(sound_dict[keychar])
			play = wave_obj.play()
			play.wait_done()
			play.stop()
		else: 
			print('recording')
			recording = sd.rec(int(duration*freq), samplerate=freq, channels=2)
			sd.wait()
			write(keychar + "raw.wav", freq, recording)
			wv.write(keychar + ".wav", recording, freq, sampwidth=2)
			sound_dict[keychar] = keychar+".wav"
			recd.append(keychar)
		sys.stdout.flush()

	time.sleep(.25)