# thirdwatch_api.ChargebackApi

All URIs are relative to *https://api.thirdwatch.ai/event*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chargeback**](ChargebackApi.md#chargeback) | **POST** /v1/chargeback | Use chargeback to capture a chargeback reported on a transaction. This event can be called multiple times to record changes to the chargeback state.


# **chargeback**
> EventResponse chargeback(json)

Use chargeback to capture a chargeback reported on a transaction. This event can be called multiple times to record changes to the chargeback state.

Note - When you send a chargeback event you also need to send a label event if you want to prevent the user from making another purchase. 

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
api_instance = thirdwatch_api.ChargebackApi()
json = thirdwatch_api.Chargeback() # Chargeback | Pass chargeback to thirdwatch. Only `_userID` is required field. But this should contain chargeback info.

try: 
    # Use chargeback to capture a chargeback reported on a transaction. This event can be called multiple times to record changes to the chargeback state.
    api_response = api_instance.chargeback(json)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChargebackApi->chargeback: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json** | [**Chargeback**](Chargeback.md)| Pass chargeback to thirdwatch. Only &#x60;_userID&#x60; is required field. But this should contain chargeback info. | 

### Return type

[**EventResponse**](EventResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

