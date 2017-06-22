# Promotion

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**promotion_id** | **str** | The ID/Coupon Code within your system that you use to represent this promotion. This ID is ideally unique to the promotion across users (e.g. \&quot;Welcome\&quot;). | [optional] 
**status** | **str** | The status of the addition of promotion to an account. Best used with the add_promotion event. This way you can pass to Thirdwatch both successful and failed attempts when using a promotion. May be useful in spotting potential abuse. e.g. _success, _Failed | [optional] 
**description** | **str** | Describe promotion here. | [optional] 
**amount** | **str** | The amount or credits the promotion is worth. | [optional] 
**min_purchase_amount** | **str** | The minimum amount someone must spend in order for the promotion to be applied. | [optional] 
**referrer_user_id** | **str** | The unique user ID of the user who referred the user to this promotion. | [optional] 
**failure_reason** | **str** | When adding a promotion fails, use this to describe why it failed.e.g. _alreadyUsed, _invalidCode, _notApplicable, _expired | [optional] 
**percentage_off** | **str** | The percentage discount. If the discount is 10% off, you would send \&quot;10\&quot;. | [optional] 
**currency_code** | **str** | The [ISO-4217](http://en.wikipedia.org/wiki/ISO_4217) currency code for the amount. e.g., USD, INR alternative currencies, like bitcoin or points systems. | [optional] 
**type** | **str** | Type of the promotion e.g., First Time, Refer, Diwali | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


