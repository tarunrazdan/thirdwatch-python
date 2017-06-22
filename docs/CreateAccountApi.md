# thirdwatch_api.CreateAccountApi

All URIs are relative to *https://api.thirdwatch.ai/event*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_account**](CreateAccountApi.md#create_account) | **POST** /v1/create_account | Use create_account to pass user details at user registration.


# **create_account**
> EventResponse create_account(json)

Use create_account to pass user details at user registration.

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
api_instance = thirdwatch_api.CreateAccountApi()
json = thirdwatch_api.CreateAccount() # CreateAccount | Pass user details after registration. Only `_userID` is required field. But this should contain user info.

try: 
    # Use create_account to pass user details at user registration.
    api_response = api_instance.create_account(json)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateAccountApi->create_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json** | [**CreateAccount**](CreateAccount.md)| Pass user details after registration. Only &#x60;_userID&#x60; is required field. But this should contain user info. | 

### Return type

[**EventResponse**](EventResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

