### Creating OperaDriver service:

```python
# Create OperaDriver service:
from selenium.webdriver.chrome import service
webdriver_service = service.Service(opera_driver_exe_path)
```


### Create remote webdriver.

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

1. Attach to the existing Opera instance.
```python
capabilities = {
    'operaOptions': {
        'androidPackage': 'com.opera.browser'
        'androidUseRunningPackage' : true,
        }
}
```


### Browser options:

The list of operaOptions for Android is similar to [desktop options](./desktop.md#options) with some additional options described in [android-products.md](./android-products.md)
