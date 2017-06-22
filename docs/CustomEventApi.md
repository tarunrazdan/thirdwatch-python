# thirdwatch_api.CustomEventApi

All URIs are relative to *https://api.thirdwatch.ai/event*

Method | HTTP request | Description
------------- | ------------- | -------------
[**custom_event**](CustomEventApi.md#custom_event) | **POST** /v1/custom_event | Use order_status to track the order processing workflow of a previously submitted order.


# **custom_event**
> EventResponse custom_event(json)

Use order_status to track the order processing workflow of a previously submitted order.

Custom events and fields capture user behavior and differences not covered by our reserved events and fields. For example, a location tracking business can create a custom event called trackLocation with custom fields that are relevant. 

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
api_instance = thirdwatch_api.CustomEventApi()
json = thirdwatch_api.Custom() # Custom | Pass order status to thirdwatch. Only `_userID` is required field. But this should contain custom info.

try: 
    # Use order_status to track the order processing workflow of a previously submitted order.
    api_response = api_instance.custom_event(json)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomEventApi->custom_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json** | [**Custom**](Custom.md)| Pass order status to thirdwatch. Only &#x60;_userID&#x60; is required field. But this should contain custom info. | 

### Return type

[**EventResponse**](EventResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

