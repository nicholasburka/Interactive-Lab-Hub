import time
import calendar
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0
time_x = 24
time_y = 32

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
bigfont = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 40)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

#buttons
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

#logic
stopped_clock = False
was_stopped = False
stopped_time = 0

while True:
    if not buttonA.value:
        stopped_clock = True
        if not was_stopped:
            was_stopped = True
            stopped_time = calendar.timegm(time.localtime())
    elif not buttonB.value:
        stopped_clock = False
    if (not stopped_clock) and was_stopped:
        current_time = calendar.timegm(time.localtime())
        if (current_time != stopped_time):
            stopped_clock = False
            was_stopped = True
            draw.rectangle((0,0,width,height), outline=0, fill=0)
            draw.text((0,0), time.strftime("%m/%d/%Y"), font=font, fill="#0000FF")
            diff = current_time - stopped_time
            #hex_str_R = str(hex(int(256 - (diff))))[2:]
            #draw.text((time_x, time_y), time.strftime("%H:%M:%S", time.gmtime(stopped_time)), font=bigfont, fill="#"+hex_str_R+"00"+hex_str_R)
            draw.text((time_x, time_y), time.strftime("%H:%M:%S", time.gmtime(stopped_time)), font=bigfont, fill="#FF0AFF")
            disp.image(image, rotation)
            time.sleep(1/(diff + 1))
            stopped_time = stopped_time + 1
        else:
            was_stopped = False
    elif (not stopped_clock):
        # Draw a black filled box to clear the image.
        draw.rectangle((0, 0, width, height), outline=0, fill=0)

        #TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py 
        draw.text((0,0), time.strftime("%m/%d/%Y"), font=font, fill="#0000FF")
        draw.text((time_x, time_y), time.strftime("%H:%M:%S"), font=bigfont, fill="#FF00FF")


        # Display image.
        disp.image(image, rotation)
        time.sleep(1)
