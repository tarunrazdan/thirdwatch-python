# thirdwatch_api.UpdateOrderApi

All URIs are relative to *https://api.thirdwatch.ai/event*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_order**](UpdateOrderApi.md#update_order) | **POST** /v1/update_order | Update details of an existing order.


# **update_order**
> EventResponse update_order(json)

Update details of an existing order.

* This event contains the same fields as ```create_order```. * The existing order will be completely replaced by the values sent in `update_order`. Be sure to specify all values for the order, not just those that changed. * If no matching `_orderId` found, a new order will be created. 

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
api_instance = thirdwatch_api.UpdateOrderApi()
json = thirdwatch_api.UpdateOrder() # UpdateOrder | Update details of an existing order. Only `_userID` is required field. But this should contain existing order info.

try: 
    # Update details of an existing order.
    api_response = api_instance.update_order(json)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpdateOrderApi->update_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json** | [**UpdateOrder**](UpdateOrder.md)| Update details of an existing order. Only &#x60;_userID&#x60; is required field. But this should contain existing order info. | 

### Return type

[**EventResponse**](EventResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

