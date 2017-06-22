# UpdateAccount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | The user&#39;s account ID according to your systems. Note that user IDs are case sensitive. | [optional] 
**session_id** | **str** | The user&#39;s current session ID, used to tie a user&#39;s action before and after login or account creation. Required if no user_id values is provided. | [optional] 
**device_ip** | **str** | IP address of the request made by the user. Recommended for historical backfills and customers with mobile apps. | [optional] 
**origin_timestamp** | **str** | Represents the time the event occured in your system. Send as a UNIX timestamp in milliseconds in string. | [optional] 
**user_email** | **str** | Email of the user creating this order. Note - If the user&#39;s email is also their account ID in your system, set both the userId and userEmail fields to their email address. | [optional] 
**first_name** | **str** | Provide the first name associated with the user here. | [optional] 
**last_name** | **str** | Provide the last name associated with the user here. | [optional] 
**phone** | **str** | The primary phone number of the user associated with this account. Provide the phone number as a string. | [optional] 
**age** | **str** | Age of the user e.g. \&quot;25\&quot; | [optional] 
**gender** | **str** | Gender of the user e.g. \&quot;_male\&quot;, \&quot;_female\&quot; or \&quot;_trans\&quot; | [optional] 
**referral_code** | **str** | Code or promotion used by the user while creating account. | [optional] 
**referrer_user_id** | **str** | The ID of the user that referred the current user to your business. This field is required for detecting referral fraud. | [optional] 
**billing_address** | [**BillingAddress**](BillingAddress.md) |  | [optional] 
**shipping_address** | [**ShippingAddress**](ShippingAddress.md) |  | [optional] 
**payment_methods** | [**list[PaymentMethod]**](PaymentMethod.md) | The payment information associated with this account. Represented as an array of nested payment_method objects containing payment type, payment gateway, credit card bin, etc. | [optional] 
**promotions** | [**list[Promotion]**](Promotion.md) | The list of promotions that apply to this account. You can add one or more promotions when creating or updating an order. Represented as a JSON array of promotion objects. You can also separately add promotions to the account via the addPromotion event. | [optional] 
**social_sign_on_type** | **str** | If the user logged in with a social identify provider, give the name here. e.g. _google, _facebook, _twitter, _linkedin, _other | [optional] 
**email_confirmed_status** | **str** | Status of email verification. e.g. _success, _failure, _pending | [optional] 
**phone_confirmed_status** | **str** | Status of phone verification. e.g. _success, _failure, _pending | [optional] 
**is_newsletter_subscribed** | **bool** | Is user subscribed for newsletter. e.g. true, false | [optional] 
**account_status** | **str** | Current status of account, e.g. _active, _inactive | [optional] 
**facebook_id** | **str** | Facebook user id or token of the user. This can help to varify his social identity. | [optional] 
**google_id** | **str** | Google user id or token of the user. This can help to varify his social identity. | [optional] 
**twitter_id** | **str** | Twitter handle or token of the user. This can help to varify his social identity. | [optional] 
**custom_info** | [**CustomInfo**](CustomInfo.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


