import time
import signal
from gfxhat import touch, lcd, backlight, fonts
from PIL import Image, ImageFont, ImageDraw

# Function to display option on LCD
def display_option(option):
    lcd.clear()
    lcd.show()
    draw.text((10, 10), option, 1, font)
    lcd.show()

# Function for option 1
def option1():
    display_option("Option 1 Selected")
    # Your logic for option 1 goes here
    time.sleep(2)

# Function for option 2
def option2():
    display_option("Option 2 Selected")
    # Your logic for option 2 goes here
    time.sleep(2)

# Function for option 3
def option3():
    display_option("Option 3 Selected")
    # Your logic for option 3 goes here
    time.sleep(2)

# Initialize GFX HAT
led_states = [False for _ in range(6)]
width, height = lcd.dimensions()
image = Image.new('P', (width, height))
draw = ImageDraw.Draw(image)
font = ImageFont.truetype(fonts.AmaticSCBold, 20)

# Define menu options and corresponding functions
menu_options = {
    "Option 1": option1,
    "Option 2": option2,
    "Option 3": option3,
}

# Display menu on LCD
selected_option = list(menu_options.keys())[0]
lcd.clear()
lcd.show()
draw.text((10, 10), "Select an option:", 1, font)
for idx, option_name in enumerate(menu_options.keys()):
    draw.text((10, 30 + idx * 20), f"{idx + 1}. {option_name}", 1, font)
lcd.show()

# Function to handle button presses
def button_handler(ch, event):
    global selected_option

    if event == 'press':
        if ch == 3:  # Button channel 3 (Move selection up)
            selected_option = list(menu_options.keys())[(list(menu_options.keys()).index(selected_option) - 1) % len(menu_options)]
        elif ch == 5:  # Button channel 5 (Move selection down)
            selected_option = list(menu_options.keys())[(list(menu_options.keys()).index(selected_option) + 1) % len(menu_options)]
        elif ch == 4:  # Button channel 4 (Select option)
            menu_options[selected_option]()

        # Update the display to highlight the selected option
        lcd.clear()
        lcd.show()
        draw.text((10, 10), "Select an option:", 1, font)
        for idx, option_name in enumerate(menu_options.keys()):
            draw.text((10, 30 + idx * 20), f"{idx + 1}. {option_name}", 1, font)

        # Highlight the selected option
        draw.text((10, 30 + list(menu_options.keys()).index(selected_option) * 20), f"{list(menu_options.keys()).index(selected_option) + 1}. {selected_option}", 1, font)
        lcd.show()

# Set up buttons
for ch in range(6):
    touch.on(ch, button_handler)

try:
    signal.pause()
except KeyboardInterrupt:
    lcd.clear()
    lcd.show()
    for x in range(6):
        backlight.set_pixel(x, 0, 0, 0)
        touch.set_led(x, 0)
    backlight.show()
