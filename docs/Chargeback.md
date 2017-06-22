# Chargeback

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | The user&#39;s account ID according to your systems. Note that user IDs are case sensitive. | [optional] 
**session_id** | **str** | The user&#39;s current session ID, used to tie a user&#39;s action before and after login or account creation. Required if no user_id values is provided. | [optional] 
**order_id** | **str** | The ID for the order that this chargeback is filed against. This field is not required if this chargeback was filed against a transaction with no _orderId. | [optional] 
**transaction_id** | **str** | The ID for the transaction that this chargeback is filed against. | [optional] 
**chargeback_state** | **str** | The current state of the chargeback. e.g. _received, _accepted, _disputed, _won, _lost | [optional] 
**chargeback_reason** | **str** | This field can be used to capture the reason given. e.g. _fraud, _duplicate, _product_not_received, _product_unacceptable, _other\&quot; | [optional] 
**custom_info** | [**CustomInfo**](CustomInfo.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


