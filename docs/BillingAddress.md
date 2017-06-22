# BillingAddress

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Provide the full name associated with the address here. Concatenate first name and last name together if you collect them separately in your system. | [optional] 
**phone** | **str** | The phone number associated with this address. Provide the phone number as a string starting with the country code. Use E.164 format or send in the standard national format of number&#39;s origin. | [optional] 
**address1** | **str** | Address first line, e.g., \&quot;C802 Nirvana Courtyard\&quot;. | [optional] 
**address2** | **str** | Address second line, e.g., \&quot;Nirvana Country, Sector 50\&quot;. | [optional] 
**city** | **str** | The city or town name, e.g., \&quot;Gurgaon\&quot; . | [optional] 
**region** | **str** | The region portion of the address. In the India, this corresponds to the state. | [optional] 
**country** | **str** | The [ISO-3166](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code for the billing address, e.g., \&quot;IN\&quot; in case of India. | [optional] 
**zipcode** | **str** | The postal code associated with the address, e.g., \&quot;122002\&quot;. | [optional] 
**is_office_address** | **bool** | Is user chosen this address as office address. | [optional] 
**is_home_address** | **bool** | Is user chosen this address as home address. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


