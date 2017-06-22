# thirdwatch_api.OrderStatusApi

All URIs are relative to *https://api.thirdwatch.ai/event*

Method | HTTP request | Description
------------- | ------------- | -------------
[**order_status**](OrderStatusApi.md#order_status) | **POST** /v1/order_status | Use order_status to track the order processing workflow of a previously submitted order.


# **order_status**
> EventResponse order_status(json)

Use order_status to track the order processing workflow of a previously submitted order.

For example, order_status can be used to indicate that an order has been held for review, canceled due to suspected fraud, or fulfilled. This event can be called multiple times to record changes an order's status. 

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
api_instance = thirdwatch_api.OrderStatusApi()
json = thirdwatch_api.OrderStatus() # OrderStatus | Pass order status to thirdwatch. Only `_userID` is required field. But this should contain order info.

try: 
    # Use order_status to track the order processing workflow of a previously submitted order.
    api_response = api_instance.order_status(json)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderStatusApi->order_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json** | [**OrderStatus**](OrderStatus.md)| Pass order status to thirdwatch. Only &#x60;_userID&#x60; is required field. But this should contain order info. | 

### Return type

[**EventResponse**](EventResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

