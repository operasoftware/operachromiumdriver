# Step by step instructions for Python setup

## Python

* install Python
* install/upgrade [Python bindings](http://selenium-python.readthedocs.org/en/latest/installation.html) (no need to install the Selenium server)

## Desktop

* install Opera in the default location

## Android

* install Android DSK tools: <http://developer.android.com/sdk/index.html> → _View all downloads and sizes_ → _SDK Tools only_)
* run ` .../android-sdk/tools/android sdk`
    + check ‘Android SDK Platform-tools’
    + ‘Google USB Driver’ (for Windows)
    + click ‘install’
* add `.../android-sdk/platform-tools` to the `PATH` environment variable
* install drivers for the device
* run `adb devices` to make sure if your device is available
* download Opera apk (link)
* install Opera on the device (when using pure Selenium)

### Appium

* install Appium
* initialize Appium: `./reset.sh --selendroid --android`

## Driver

* download OperaDriver
* add location to `PATH`

## Run example

For Android use [pure Selenium](../examples/android.py) or [Appium](../examples/appium_simple.py).
Desktop example: [desktop.py](../examples/desktop.py).

## Troubleshooting

### Desktop

If you get the “cannot find Opera binary” error, use the `binary` option in `operaOptions` as shown in [`desktop.md`](desktop.md).
