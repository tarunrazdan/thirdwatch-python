# thirdwatch_api.AddPromotionApi

All URIs are relative to *https://api.thirdwatch.ai/event*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_promotion**](AddPromotionApi.md#add_promotion) | **POST** /v1/add_promotion | Use add_promotion to record when a user adds one or more promotions to their account.


# **add_promotion**
> EventResponse add_promotion(json)

Use add_promotion to record when a user adds one or more promotions to their account.

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
api_instance = thirdwatch_api.AddPromotionApi()
json = thirdwatch_api.AddPromotion() # AddPromotion | Pass added promotion info to thirdwatch. Only `_userID` is required field. But this should contain promotion info.

try: 
    # Use add_promotion to record when a user adds one or more promotions to their account.
    api_response = api_instance.add_promotion(json)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddPromotionApi->add_promotion: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json** | [**AddPromotion**](AddPromotion.md)| Pass added promotion info to thirdwatch. Only &#x60;_userID&#x60; is required field. But this should contain promotion info. | 

### Return type

[**EventResponse**](EventResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

