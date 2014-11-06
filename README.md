# OperaChromiumDriver

## Intro

OperaChromiumDriver is a WebDriver implementation derived from [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) and adapted by [Opera](http://www.opera.com/) that enables programmatic automation of Chromium-based Opera products for desktop and Android platforms. It is a part of the [Selenium](http://code.google.com/p/selenium) project.

WebDriver is a general purpose library for automating web browsers. It can drive the browser, running various tests on your web pages, just as if a real user was navigating through them. It can emulate actions like clicking links, entering text and submitting forms, and reporting results back to you so you know that your website works as intended.

OperaChromiumDriver end-user emulation ensures that your entire stack (HTML, scripts, styling, embedded resources and backend setup) is functioning correctly without tedious manual testing routines.

OperaChromiumDriver can be used without extra setup on Chromium-based versions of Opera starting from version 26.

For driving Presto-based Opera browsers, refer to the [OperaPrestoDriver](https://github.com/operasoftware/operaprestodriver) project.

## Sources

OperaChromiumDriver is based on [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/). The plan is to extract Opera-specific code and to generalize those parts of the code that could handle any Chromium-embedding browser. This code is going to be upstreamed to Chromium soon.

Once that is done, the remaining OperaChromiumDriver source code (using ChromeDriver code as a module) will be posted to this repository.

## Binaries

Binaries are available under [the releases tab](https://github.com/operasoftware/operachromiumdriver/releases).

## Documentation

Documentation on how to use the OperaChromiumDriver is included in this repository. It can be used with Selenium bindings — there are instructions on how to use Python Selenium bindings for Opera browsers running on [desktop](docs/desktop.md) and [Android](docs/android.md).

OperaChromiumDriver also may be used with [Appium](http://appium.io/) which enables context switching between UI and the web. It is very helpful when you need to close the native dialog which blocks further test execution. For instructions on how to use OperaChromiumDriver with Appium see [appium.md](docs/appium.md).

Some [Python examples](./examples) are available as well. 