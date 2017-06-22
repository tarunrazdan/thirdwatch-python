# ReportItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | The user&#39;s account ID according to your systems. Note that user IDs are case sensitive. | [optional] 
**session_id** | **str** | The user&#39;s current session ID, used to tie a user&#39;s action before and after login or account creation. Required if no user_id values is provided. | [optional] 
**item_id** | **str** | The unique ID for the item that is being reported. Note - item IDs are case sensitive. | [optional] 
**device_ip** | **str** | IP address of the request made by the user. Recommended for historical backfills and customers with mobile apps. | [optional] 
**origin_timestamp** | **str** | Represents the time the event occured in your system. Send as a UNIX timestamp in milliseconds in string. | [optional] 
**user_email** | **str** | Email of the user creating this order. Note - If the user&#39;s email is also their account ID in your system, set both the userId and userEmail fields to their email address. | [optional] 
**custom_info** | [**CustomInfo**](CustomInfo.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


