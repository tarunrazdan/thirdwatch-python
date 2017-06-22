# Item

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **str** | The item&#39;s unique identifier according to your systems. Use the same ID that you would use to look up items on your website&#39;s database. | [optional] 
**product_title** | **str** | The item&#39;s name, e.g., \&quot;WD 2 TB External Hard Drive\&quot;. | [optional] 
**price** | **str** | The item unit price in numbers, in the base unit of the currency_code.e.g. \&quot;2500\&quot; | [optional] 
**currency_code** | **str** | The [ISO-4217](http://en.wikipedia.org/wiki/ISO_4217) currency code for the amount. e.g., USD, INR alternative currencies, like bitcoin or points systems. | [optional] 
**upc** | **str** | If the item has a Universal Product Code (UPC), provide it here. | [optional] 
**sku** | **str** | If the item has a Stock-keeping Unit ID (SKU), provide it here. | [optional] 
**isbn** | **str** | If the item is a book with an International Standard Book Number (ISBN), provide it here. | [optional] 
**brand** | **str** | The brand name of the item. | [optional] 
**manufacturer** | **str** | Name of the item&#39;s manufacturer. | [optional] 
**category** | **str** | The category this item is listed under in your business. e.g., \&quot;travel\&quot;, \&quot;man &gt; bags\&quot;. | [optional] 
**tags** | **str** | The tags used to describe this item in your business. e.g., \&quot;man\&quot;, \&quot;summer\&quot;. | [optional] 
**color** | **str** | The color of the item. | [optional] 
**quantity** | **int** | The quantity of the item. | [optional] 
**is_on_sale** | **bool** | Is item on sale or running offers on this item . | [optional] 
**max_quantity** | **int** | The max quantity per user for this item. | [optional] 
**discount_price** | **str** | Price of the product after discount. | [optional] 
**product_weight** | **str** | Weight of the product in Kilo Gram, e.g. \&quot;3\&quot; , \&quot;0.5\&quot; | [optional] 
**country** | **str** | The [ISO-3166](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the item, e.g., \&quot;IN\&quot; in case of India. | [optional] 
**description_short** | **str** | Short description of the item. | [optional] 
**description** | **str** | Detail description of the item. | [optional] 
**seller** | [**Seller**](Seller.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


