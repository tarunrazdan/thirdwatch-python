# thirdwatch_api.UpdateAccountApi

All URIs are relative to *https://api.thirdwatch.ai/event*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_account**](UpdateAccountApi.md#update_account) | **POST** /v1/update_account | Use update_account to record changes to the user&#39;s account information.


# **update_account**
> EventResponse update_account(json)

Use update_account to record changes to the user's account information.

For user accounts created before integration with Thirdwatch, there's no need to call `create_account` before `update_account`. Simply call `update_account` and we'll infer that account was created before integration. 

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
api_instance = thirdwatch_api.UpdateAccountApi()
json = thirdwatch_api.UpdateAccount() # UpdateAccount | Pass user details after update or change in user info. Only `_userID` is required field. But this should contain user info.

try: 
    # Use update_account to record changes to the user's account information.
    api_response = api_instance.update_account(json)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpdateAccountApi->update_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json** | [**UpdateAccount**](UpdateAccount.md)| Pass user details after update or change in user info. Only &#x60;_userID&#x60; is required field. But this should contain user info. | 

### Return type

[**EventResponse**](EventResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

