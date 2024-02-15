# LoopIO User Guide

## Disclaimer
- Do not modify any of the folder names or contents, except for the settings folder where you can edit the `.txt` files.
- Always connect your Android phone to your computer before running the bot.
- When the Test or SNKRS Pass scripts are running and clicking, do not move your computer mouse as it may cause the bot to malfunction.

## Connecting the Android Phone
To connect your phone to your PC, you need to enable USB debugging. This is a one-time setup. Follow the guide [here](https://www.fonepaw.com/tutorials/enable-usb-debugging-on-android.html) to enable USB debugging.

## Installation Setup
1. Download the LoopIO installer from [this link](https://drive.google.com/file/d/1UgjJrS_QeqHN43KsZP-mrGMlWQLGrsKV/view?usp=sharing).
2. Open the installer and run it.
3. The LoopIO folder will be installed in the `C:\Desktop\LoopIO` directory. Note that this is not your main desktop, so you will not find the folder there.

## Settings
In the settings folder, you will find two `.txt` files: `licensekey` and `serial`.
- In `licensekey.txt`, enter your license key on the first line. Do not add anything other than the license key.
- In the `serial` file, add one device ID number. The method to find your device ID is covered in the "Running the bot" section.

## Running the Bot
1. Open the `LoopIO.exe` file.
2. If the bot indicates that your license key is invalid, close and reopen the bot. If the issue persists, contact our support team on Discord.
3. Once your license key is verified, you will see a menu with options to Get Device ID, Test Script, SNKRS Pass, and Exit.
   - Selecting "1" gives you the device ID for your Android Phone. Enter this ID in your `serial.txt` file.
   - Selecting "2" runs a test script to click on a specific product in the Instock Page of the SNKRS App and select a size. Set a delay in seconds before running.
   - Selecting "3" runs the SNKRS Pass script. Ensure you are on the SNKRS app page with the "reservation coming soon" button visible before the pass goes live.
   - Selecting "4" closes the bot.

## Preparing for the SNKRS Pass
- Test the bot with the Test Script before attempting the SNKRS Pass.
- Set your preferred size and gender in the SNKRS App preferences before the pass goes live.
- Fully close and reopen the SNKRS App a few minutes before the Pass goes live, ensuring the "reservations coming soon" button is visible.
- Launch the bot 2-3 minutes before the Pass goes live and select the SNKRS Pass Option, then simply wait until the SNKRS Pass goes live and LoopIO will automate the process. 
