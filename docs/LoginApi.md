# thirdwatch_api.LoginApi

All URIs are relative to *https://api.thirdwatch.ai/event*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login**](LoginApi.md#login) | **POST** /v1/login | Use login to record when a user attempts to log in.


# **login**
> EventResponse login(json)

Use login to record when a user attempts to log in.

### Example 
```python
from __future__ import print_statement
import time
import thirdwatch_api
from thirdwatch_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
thirdwatch_api.configuration.api_key['X-THIRDWATCH-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# thirdwatch_api.configuration.api_key_prefix['X-THIRDWATCH-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = thirdwatch_api.LoginApi()
json = thirdwatch_api.Login() # Login | Pass login status to thirdwatch. Only `_userID` is required field. But this should contain login info.

try: 
    # Use login to record when a user attempts to log in.
    api_response = api_instance.login(json)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoginApi->login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json** | [**Login**](Login.md)| Pass login status to thirdwatch. Only &#x60;_userID&#x60; is required field. But this should contain login info. | 

### Return type

[**EventResponse**](EventResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

