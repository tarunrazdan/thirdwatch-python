# thirdwatch_api.LogoutApi

All URIs are relative to *https://api.thirdwatch.ai/event*

Method | HTTP request | Description
------------- | ------------- | -------------
[**logout**](LogoutApi.md#logout) | **POST** /v1/logout | Use logout to record when a user logs out.


# **logout**
> EventResponse logout(json)

Use logout to record when a user logs out.

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
api_instance = thirdwatch_api.LogoutApi()
json = thirdwatch_api.Logout() # Logout | Pass logout status to thirdwatch. Only `_userID` is required field. But this should contain logout info.

try: 
    # Use logout to record when a user logs out.
    api_response = api_instance.logout(json)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogoutApi->logout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json** | [**Logout**](Logout.md)| Pass logout status to thirdwatch. Only &#x60;_userID&#x60; is required field. But this should contain logout info. | 

### Return type

[**EventResponse**](EventResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

