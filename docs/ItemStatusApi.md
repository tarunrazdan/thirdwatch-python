# thirdwatch_api.ItemStatusApi

All URIs are relative to *https://api.thirdwatch.ai/event*

Method | HTTP request | Description
------------- | ------------- | -------------
[**item_status**](ItemStatusApi.md#item_status) | **POST** /v1/item_status | Use item_status to update the status of item that you’ve already pass to Thirdwatch.


# **item_status**
> EventResponse item_status(json)

Use item_status to update the status of item that you’ve already pass to Thirdwatch.

If the status is the only thing that’s changing about the item, use this as a convenient way to send status of the item after order processing. 

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
api_instance = thirdwatch_api.ItemStatusApi()
json = thirdwatch_api.ItemStatus() # ItemStatus | Pass change item status to thirdwatch. Only `_userID` is required field. But this should contain item status.

try: 
    # Use item_status to update the status of item that you’ve already pass to Thirdwatch.
    api_response = api_instance.item_status(json)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemStatusApi->item_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json** | [**ItemStatus**](ItemStatus.md)| Pass change item status to thirdwatch. Only &#x60;_userID&#x60; is required field. But this should contain item status. | 

### Return type

[**EventResponse**](EventResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

