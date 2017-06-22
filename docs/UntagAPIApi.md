# thirdwatch_api.UntagAPIApi

All URIs are relative to *https://api.thirdwatch.ai/event*

Method | HTTP request | Description
------------- | ------------- | -------------
[**un_tag_user**](UntagAPIApi.md#un_tag_user) | **POST** /v1/untag | If you are unsure whether a user is bad or good, you can always remove tag and leave the user in a neutral state.


# **un_tag_user**
> EventResponse un_tag_user(json)

If you are unsure whether a user is bad or good, you can always remove tag and leave the user in a neutral state.

To untag a user for a particular abuse type, send the abuse_type key in json data. In the rare case that you want to remove all tags for all abuse types for a particular user, send without the abuse_type query parameter. 

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
api_instance = thirdwatch_api.UntagAPIApi()
json = thirdwatch_api.UnTag() # UnTag | Pass user and it's info to thirdwatch. Only `_userID` is required field. But this should contain untag info.

try: 
    # If you are unsure whether a user is bad or good, you can always remove tag and leave the user in a neutral state.
    api_response = api_instance.un_tag_user(json)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UntagAPIApi->un_tag_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json** | [**UnTag**](UnTag.md)| Pass user and it&#39;s info to thirdwatch. Only &#x60;_userID&#x60; is required field. But this should contain untag info. | 

### Return type

[**EventResponse**](EventResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

