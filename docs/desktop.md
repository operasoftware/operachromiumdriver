# Desktop

For now to drive the Chromium-based Opera you’ll need to use the `RemoteWebDriver`. Python examples are provided below. For other languages please refer to the [Selenium docs](http://docs.seleniumhq.org/docs/04_webdriver_advanced.jsp#remotewebdriver).

## Creating an OperaDriver service

```python
# Create and start OperaDriver service:
from selenium.webdriver.chrome import service
webdriver_service = service.Service(opera_driver_exe_path,
                                        port_on_which_service_will_be_running)
webdriver_service.start()
```
### Creating a remote webdriver for selenium 4

```python
# Create OperaDriver options:
from selenium import webdriver
options = webdriver.ChromeOptions()
options.binary_location = opera_exe_path
options.add_experimental_option('w3c', True)
```

```python
# Create remote webdriver
remote = webdriver.Remote(webdriver_service.service_url, options=options)
```

### Creating a remote webdriver for selenium 2, 3

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
