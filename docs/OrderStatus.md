# OrderStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | The user&#39;s account ID according to your systems. Note that user IDs are case sensitive. | [optional] 
**session_id** | **str** | The user&#39;s current session ID, used to tie a user&#39;s action before and after login or account creation. Required if no user_id values is provided. | [optional] 
**order_id** | **str** | The ID for the order that this chargeback is filed against. This field is not required if this chargeback was filed against a transaction with no _orderId. | [optional] 
**order_status** | **str** | Indicates the high-level state of the order. e.g. _approved, _canceled, _held, _fulfilled, _returned | [optional] 
**reason** | **str** | The reason for a cancellation. e.g. _paymentRisk, _abuse, _policy, _other | [optional] 
**shipping_cost** | **str** | if _approved or _fulfilled than pass the shipping cost. e.g. \&quot;50\&quot; | [optional] 
**tracking_number** | **str** | if _approved or _fulfilled than pass the tracking number. e.g. \&quot;55327470\&quot; | [optional] 
**tracking_method** | **str** | if _approved or _fulfilled than pass the tracking url. e.g. \&quot;http://fedex.com/track?q&#x3D;abc123\&quot; | [optional] 
**source** | **str** | The source of a decision. e.g. _automated, _manualReview\&quot; | [optional] 
**analyst** | **str** | The analyst who made the decision, if manual. | [optional] 
**description** | **str** | Any additional information about this order status change. | [optional] 
**custom_info** | [**CustomInfo**](CustomInfo.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


