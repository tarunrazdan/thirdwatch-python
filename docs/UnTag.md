# UnTag

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | The user&#39;s account ID according to your systems. Note that user IDs are case sensitive. | [optional] 
**abuse_type** | **str** | The type of abuse for which you want to untag user. It&#39;s important to send a untag specific to the type of abuse. You&#39;ll end up with more accurate results this way. e.g. _paymentAbuse, _contentAbuse, _promotionAbuse, _accountAbuse If you wants to untag from all type of abuses than don&#39;t send this parameter. | [optional] 
**analyst** | **str** | Unique identifier (e.g. email address) of the analyst who applied the label. Useful for tracking purposes after the fact. | [optional] 
**custom_info** | [**CustomInfo**](CustomInfo.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


