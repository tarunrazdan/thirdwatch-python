# thirdwatch_api.CreateOrderApi

All URIs are relative to *https://api.thirdwatch.ai/event*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_order**](CreateOrderApi.md#create_order) | **POST** /v1/createOrder | Submit a new or existing order to Thirdwatch for review. This API should contain order item info, the payment info, and user identity info.


# **create_order**
> EventResponse create_order(body)

Submit a new or existing order to Thirdwatch for review. This API should contain order item info, the payment info, and user identity info.

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
api_instance = thirdwatch_api.CreateOrderApi()
body = thirdwatch_api.CreateOrder() # CreateOrder | An order to submit for review. Only `_userID` is required field. But this should contain order info.

try: 
    # Submit a new or existing order to Thirdwatch for review. This API should contain order item info, the payment info, and user identity info.
    api_response = api_instance.create_order(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateOrderApi->create_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateOrder**](CreateOrder.md)| An order to submit for review. Only &#x60;_userID&#x60; is required field. But this should contain order info. | 

### Return type

[**EventResponse**](EventResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

