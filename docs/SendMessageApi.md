# thirdwatch_api.SendMessageApi

All URIs are relative to *https://api.thirdwatch.ai/event*

Method | HTTP request | Description
------------- | ------------- | -------------
[**send_message**](SendMessageApi.md#send_message) | **POST** /v1/send_message | Use send_message to record when a user sends a message to other i.e. seller, support.


# **send_message**
> EventResponse send_message(json)

Use send_message to record when a user sends a message to other i.e. seller, support.

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
api_instance = thirdwatch_api.SendMessageApi()
json = thirdwatch_api.SendMessage() # SendMessage | Pass message to thirdwatch. Only `_userID` is required field. But this should contain message info.

try: 
    # Use send_message to record when a user sends a message to other i.e. seller, support.
    api_response = api_instance.send_message(json)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SendMessageApi->send_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json** | [**SendMessage**](SendMessage.md)| Pass message to thirdwatch. Only &#x60;_userID&#x60; is required field. But this should contain message info. | 

### Return type

[**EventResponse**](EventResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

