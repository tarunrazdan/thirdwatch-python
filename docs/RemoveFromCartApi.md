# thirdwatch_api.RemoveFromCartApi

All URIs are relative to *https://api.thirdwatch.ai/event*

Method | HTTP request | Description
------------- | ------------- | -------------
[**remove_from_cart**](RemoveFromCartApi.md#remove_from_cart) | **POST** /v1/remove_from_cart | Use remove_from_cart when a user removes an item from their shopping cart or list.


# **remove_from_cart**
> EventResponse remove_from_cart(json)

Use remove_from_cart when a user removes an item from their shopping cart or list.

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
api_instance = thirdwatch_api.RemoveFromCartApi()
json = thirdwatch_api.RemoveFromCart() # RemoveFromCart | Pass removed item info to thirdwatch. Only `_userID` is required field. But this should contain item info.

try: 
    # Use remove_from_cart when a user removes an item from their shopping cart or list.
    api_response = api_instance.remove_from_cart(json)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RemoveFromCartApi->remove_from_cart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json** | [**RemoveFromCart**](RemoveFromCart.md)| Pass removed item info to thirdwatch. Only &#x60;_userID&#x60; is required field. But this should contain item info. | 

### Return type

[**EventResponse**](EventResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

