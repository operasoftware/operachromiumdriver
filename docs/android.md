# Android

## Enabling remote debugging

You need to create the command line file for Opera for Android and enable remote debugging:

```
adb shell "echo 'opera --enable-remote-debugging' &> /data/local/tmp/opera-browser-command-line"
```

## Creating an OperaDriver service

```python
# Create OperaDriver service:
from selenium.webdriver.chrome import service
webdriver_service = service.Service('path/to/operadriver')
```

## Creating a remote webdriver

```python
# Create remote webdriver:
from selenium import webdriver
remote = webdriver.Remote(webdriver_service, capabilities)
```

Depending on capabilites OperaDriver may be connected to the browser in two ways.

  1. Let OperaDriver start Opera.

  ```python
  capabilities = {
      'operaOptions': {
          'androidPackage': 'com.opera.browser'
      }
  }
  ```

  2. Attach to the existing Opera instance.

  ```python
  capabilities = {
      'operaOptions': {
          'androidPackage': 'com.opera.browser',
          'androidUseRunningPackage': true
      }
  }
  ```


## Browser options

The list of `operaOptions` for Android is similar to [the available desktop options](./desktop.md#browser-options).
