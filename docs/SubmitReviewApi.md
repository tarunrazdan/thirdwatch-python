# thirdwatch_api.SubmitReviewApi

All URIs are relative to *https://api.thirdwatch.ai/event*

Method | HTTP request | Description
------------- | ------------- | -------------
[**submit_review**](SubmitReviewApi.md#submit_review) | **POST** /v1/submit_review | Use submit_review when a user-submitted review of a product or seller.


# **submit_review**
> EventResponse submit_review(json)

Use submit_review when a user-submitted review of a product or seller.

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
api_instance = thirdwatch_api.SubmitReviewApi()
json = thirdwatch_api.SubmitReview() # SubmitReview | Pass review to thirdwatch. Only `_userID` is required field. But this should contain review info.

try: 
    # Use submit_review when a user-submitted review of a product or seller.
    api_response = api_instance.submit_review(json)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmitReviewApi->submit_review: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json** | [**SubmitReview**](SubmitReview.md)| Pass review to thirdwatch. Only &#x60;_userID&#x60; is required field. But this should contain review info. | 

### Return type

[**EventResponse**](EventResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

