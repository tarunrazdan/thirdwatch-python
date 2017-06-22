# UpdateOrder

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | The user&#39;s account ID according to your systems. Note that user IDs are case sensitive. | [optional] 
**session_id** | **str** | The user&#39;s current session ID, used to tie a user&#39;s action before and after login or account creation. Required if no user_id values is provided. | [optional] 
**order_id** | **str** | The ID for tracking this order in your system. | 
**device_ip** | **str** | IP address of the request made by the user. Recommended for historical backfills and customers with mobile apps. | [optional] 
**origin_timestamp** | **str** | Represents the time the event occured in your system. Send as a UNIX timestamp in milliseconds in string. | [optional] 
**user_email** | **str** | Email of the user creating this order. Note - If the user&#39;s email is also their account ID in your system, set both the userId and userEmail fields to their email address. | [optional] 
**amount** | **str** | The item unit price in numbers, in the base unit of the currency_code.e.g. \&quot;2500\&quot; | [optional] 
**currency_code** | **str** | The [ISO-4217](http://en.wikipedia.org/wiki/ISO_4217) currency code for the amount. e.g., USD, INR alternative currencies, like bitcoin or points systems. | [optional] 
**has_expedited_shipping** | **bool** | Whether the user requested priority/expedited shipping on their order. | [optional] 
**shipping_method** | **str** | Indicates the method of delivery to the user. e.g. _electronic, _physical | [optional] 
**order_referrer** | **str** | Referer website or user name. | [optional] 
**is_pre_paid** | **bool** | is order is prepaid. | [optional] 
**is_gift** | **bool** | Is user chosen gift pack. | [optional] 
**is_return** | **bool** | Is this return order. | [optional] 
**is_first_time_buyer** | **bool** | Is user first time buyer. | [optional] 
**billing_address** | [**BillingAddress**](BillingAddress.md) |  | [optional] 
**shipping_address** | [**ShippingAddress**](ShippingAddress.md) |  | [optional] 
**payment_methods** | [**list[PaymentMethod]**](PaymentMethod.md) | The payment information associated with this order. Represented as an array of nested payment_method objects containing payment type, payment gateway, credit card bin, etc. | [optional] 
**promotions** | [**list[Promotion]**](Promotion.md) | The list of promotions that apply to this order. You can add one or more promotions when creating or updating an order. Represented as a JSON array of promotion objects. You can also separately add promotions to the account via the addPromotion event. | [optional] 
**items** | [**list[Item]**](Item.md) | The list of items ordered. Represented as a JSON array of item | [optional] 
**custom_info** | [**CustomInfo**](CustomInfo.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


