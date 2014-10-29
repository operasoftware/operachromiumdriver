#Step by step instructions for python setup

##Python
* install python
* install/upgrade [python bindings](http://selenium-python.readthedocs.org/en/latest/installation.html), (no need to install the Selenium server).

##Desktop
* install Opera in the default location


##Android
* install android sdk tools (go [here](http://developer.android.com/sdk/index.html) -> VIEW ALL DOWNLOADS AND SIZES -> Sdk Tools only)
* run  ` .../android-sdk/tools/android sdk`
    + check ‘Android SDK Platform-tools’
    + ‘Google USB Driver’ (for Windows)
    + click ‘install’
* add `.../android-sdk/platform-tools` to PATH environment variable
* install drivers for the device
* run adb devices to make sure if your device is available

* download Opera apk (link)
* install Opera on a device (when using pure selenium)

###Appium:
* install Appium
* initialize Appium (./reset.sh --selendroid --android)


##Driver
* download OperaDriver
* set execution permissions
* add location to PATH

##Run example
For Android use [pure selenium](../examples/android.py) or [Appium](../examples/appium_simple.py)  
Desktop example: [desktop.py](../examples/desktop.py)


##Troubleshooting

###Desktop
if you get the ‘cannot find Opera binary’ error, use the ‘binary’ option in operaOptions as shown in [desktop.md](desktop.md)

