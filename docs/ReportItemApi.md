# thirdwatch_api.ReportItemApi

All URIs are relative to *https://api.thirdwatch.ai/event*

Method | HTTP request | Description
------------- | ------------- | -------------
[**report_item**](ReportItemApi.md#report_item) | **POST** /v1/report_item | Use report_item to let us know when another user reports that this item may violate your company’s policies.


# **report_item**
> EventResponse report_item(json)

Use report_item to let us know when another user reports that this item may violate your company’s policies.

If you have a feature like \"Report Item\" or \"Flag this Item\", send that event to us using this. 

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
api_instance = thirdwatch_api.ReportItemApi()
json = thirdwatch_api.ReportItem() # ReportItem | Pass report item info to thirdwatch. Only `_userID` is required field. But this should contain item id.

try: 
    # Use report_item to let us know when another user reports that this item may violate your company’s policies.
    api_response = api_instance.report_item(json)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportItemApi->report_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json** | [**ReportItem**](ReportItem.md)| Pass report item info to thirdwatch. Only &#x60;_userID&#x60; is required field. But this should contain item id. | 

### Return type

[**EventResponse**](EventResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

