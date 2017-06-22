# thirdwatch_api.TagAPIApi

All URIs are relative to *https://api.thirdwatch.ai/event*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tag_user**](TagAPIApi.md#tag_user) | **POST** /v1/tag | The Tag API enables you to tell Thirdwatch which of your users are bad and which are good.


# **tag_user**
> EventResponse tag_user(json)

The Tag API enables you to tell Thirdwatch which of your users are bad and which are good.

By telling us who is bad and who is good, we can identify patterns that are unique to your business. Once you give this feedback, the platform instantly analyzes it and learns to identify good and bad behavior of other users more accurately. If you want to change an existing label for a user - for example, from bad to good - all you need to do is send a new label and we'll overwrite the existing value. 

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
api_instance = thirdwatch_api.TagAPIApi()
json = thirdwatch_api.Tag() # Tag | Pass user and it's info to thirdwatch. Only `_userID` is required field. But this should contain tag info.

try: 
    # The Tag API enables you to tell Thirdwatch which of your users are bad and which are good.
    api_response = api_instance.tag_user(json)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagAPIApi->tag_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json** | [**Tag**](Tag.md)| Pass user and it&#39;s info to thirdwatch. Only &#x60;_userID&#x60; is required field. But this should contain tag info. | 

### Return type

[**EventResponse**](EventResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

