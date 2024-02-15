# Computer Vision Automation Python for Nike SNKRS App

## Overview
This Python program utilizes computer vision to recognize mobile UI elements within the Nike SNKRS app to automate the checkout process. It is designed to work with real Android devices, leveraging libraries such as OpenCV for image processing and ADB for sending commands to devices. The program also uses Scrapy to capture frames from the Android screen and supports multiprocessing to automate tasks across multiple devices simultaneously.

## Requirements
- Operating System: Windows only
- Python 3.x
- Dependencies listed in `requirements.txt`

## Installation
1. Ensure Python 3.x is installed on your Windows machine.
2. Clone the repository or download the source code.
3. Navigate to the project directory and install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage
1. Connect your Android device(s) to your Windows computer via USB.
2. Enable USB debugging on your Android device(s). Follow the guide [here](https://www.fonepaw.com/tutorials/enable-usb-debugging-on-android.html) to enable USB debugging.
3. Run the program using the `main.py` file:
```python
python main.py
```


## Important Notes
- Do not modify the names or contents of any folders, except the settings folder where you can edit the `.txt` files.
- Ensure your Android device is connected to your computer before running the bot.
- Avoid moving your computer mouse when the Test or SNKRS Pass scripts are active, as this may interfere with the bot's functionality.

For detailed instructions on how to use the program, refer to the user guide provided in a separate markdown file.
