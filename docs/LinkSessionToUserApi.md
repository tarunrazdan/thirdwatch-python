# thirdwatch_api.LinkSessionToUserApi

All URIs are relative to *https://api.thirdwatch.ai/event*

Method | HTTP request | Description
------------- | ------------- | -------------
[**link_session_to_user**](LinkSessionToUserApi.md#link_session_to_user) | **POST** /v1/link_session_to_user | Use link_session_to_user to associate specific session to a user. Generally used only in anonymous checkout workflows.


# **link_session_to_user**
> EventResponse link_session_to_user(json)

Use link_session_to_user to associate specific session to a user. Generally used only in anonymous checkout workflows.

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
api_instance = thirdwatch_api.LinkSessionToUserApi()
json = thirdwatch_api.LinkSessionToUser() # LinkSessionToUser | Pass session and user to thirdwatch for link. Only `_userID` is required field. But this should contain session and user info.

try: 
    # Use link_session_to_user to associate specific session to a user. Generally used only in anonymous checkout workflows.
    api_response = api_instance.link_session_to_user(json)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinkSessionToUserApi->link_session_to_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json** | [**LinkSessionToUser**](LinkSessionToUser.md)| Pass session and user to thirdwatch for link. Only &#x60;_userID&#x60; is required field. But this should contain session and user info. | 

### Return type

[**EventResponse**](EventResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

