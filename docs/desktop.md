For now to drive the Chromium based Opera you’ll need to use the RemoteWebDriver. Python examples are provided belov. For other languages please refer to the [Selenium docs](http://docs.seleniumhq.org/docs/04_webdriver_advanced.jsp#remotewebdriver).

### Creating an OperaDriver service

```python
# Create OperaDriver service:
from selenium.webdriver.chrome import service
webdriver_service = service.Service(opera_driver_exe_path,
                                        port_on_which_service_will_be_running)
```


### Creating a remote webdriver

```python
# Create remote webdriver:
from selenium import webdriver
remote = webdriver.Remote(webdriver_service, capabilities)
```

Depending on capabilites OperaDriver may be connected to the browser in several ways.

  1. Let the driver start a given Opera executable.

  ```python
  capabilities = {
      'operaOptions': {
          'binary': opera_exe_path
      }
  }
  ```

  2. Let the driver auto-detect the Opera executable’s location and start it.

  ```python
  capabilities = { }
  ```

  3. Attach to the existing Opera instance. This requires running Opera with `--remote-debugging-port=port`.

  ```python
  capabilities = {
      'operaOptions': {
          'debuggerAddress': port # Same port as passed to the Opera.
      }
  }
  ```

### Browser options

As OperaDriver is based on ChromeDriver, it has similar [supported options](https://sites.google.com/a/chromium.org/chromedriver/capabilities#TOC-List-of-recognized-capabilities).
You can also set the path where browser logs will be stored using the `logPath` option.
