# thirdwatch_api

ThirdwatchApi - Python client for thirdwatch_api

The first version of the Thirdwatch API is an exciting step forward towards making it easier for developers to pass data to Thirdwatch.  

# Introduction 

Once you've [registered your website/app](https://thirdwatch.ai) it's easy to start sending data to Thirdwatch.  All endpoints are only accessible via https and are located at `api.thirdwatch.ai`. 
For instance: you can send event at the moment by ```HTTP POST``` Request to the following URL with your API key in ```Header``` and ```JSON``` data in request body. 

```   https://api.thirdwatch.ai/event/v1 ``` 

Every API request must contain ```API Key``` in header value ```X-THIRDWATCH-API-KEY```  Every event must contain your ```_userId``` (if this is not available, you can alternatively provide a ```_sessionId``` value also in ```_userId```). 

- API version: 0.0.1
- Package version: 0.0.2
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import thirdwatch_api 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import thirdwatch_api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import thirdwatch_api
from thirdwatch_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
thirdwatch_api.configuration.api_key['X-THIRDWATCH-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# thirdwatch_api.configuration.api_key_prefix['X-THIRDWATCH-API-KEY'] = 'Bearer'
# create an instance of the API class
api_instance = thirdwatch_api.AddPromotionApi()
json = thirdwatch_api.AddPromotion() # AddPromotion | Pass added promotion info to thirdwatch. Only `_userID` is required field. But this should contain promotion info.

try:
    # Use add_promotion to record when a user adds one or more promotions to their account.
    api_response = api_instance.add_promotion(json)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddPromotionApi->add_promotion: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.thirdwatch.ai/event*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AddPromotionApi* | [**add_promotion**](docs/AddPromotionApi.md#add_promotion) | **POST** /v1/add_promotion | Use add_promotion to record when a user adds one or more promotions to their account.
*AddToCartApi* | [**add_to_cart**](docs/AddToCartApi.md#add_to_cart) | **POST** /v1/add_to_cart | Use add_to_cart when a user adds an item to their shopping cart or list.
*ChargebackApi* | [**chargeback**](docs/ChargebackApi.md#chargeback) | **POST** /v1/chargeback | Use chargeback to capture a chargeback reported on a transaction. This event can be called multiple times to record changes to the chargeback state.
*CreateAccountApi* | [**create_account**](docs/CreateAccountApi.md#create_account) | **POST** /v1/create_account | Use create_account to pass user details at user registration.
*CreateOrderApi* | [**create_order**](docs/CreateOrderApi.md#create_order) | **POST** /v1/createOrder | Submit a new or existing order to Thirdwatch for review. This API should contain order item info, the payment info, and user identity info.
*CustomEventApi* | [**custom_event**](docs/CustomEventApi.md#custom_event) | **POST** /v1/custom_event | Use order_status to track the order processing workflow of a previously submitted order.
*ItemStatusApi* | [**item_status**](docs/ItemStatusApi.md#item_status) | **POST** /event/item_status | Use item_status to update the status of item that you’ve already pass to Thirdwatch.
*LinkSessionToUserApi* | [**link_session_to_user**](docs/LinkSessionToUserApi.md#link_session_to_user) | **POST** /v1/link_session_to_user | Use link_session_to_user to associate specific session to a user. Generally used only in anonymous checkout workflows.
*LoginApi* | [**login**](docs/LoginApi.md#login) | **POST** /v1/login | Use login to record when a user attempts to log in.
*LogoutApi* | [**logout**](docs/LogoutApi.md#logout) | **POST** /v1/logout | Use logout to record when a user logs out.
*OrderStatusApi* | [**order_status**](docs/OrderStatusApi.md#order_status) | **POST** /v1/order_status | Use order_status to track the order processing workflow of a previously submitted order.
*RemoveFromCartApi* | [**remove_from_cart**](docs/RemoveFromCartApi.md#remove_from_cart) | **POST** /v1/remove_from_cart | Use remove_from_cart when a user removes an item from their shopping cart or list.
*ReportItemApi* | [**report_item**](docs/ReportItemApi.md#report_item) | **POST** /v1/report_item | Use report_item to let us know when another user reports that this item may violate your company’s policies.
*SendMessageApi* | [**send_message**](docs/SendMessageApi.md#send_message) | **POST** /v1/send_message | Use send_message to record when a user sends a message to other i.e. seller, support.
*SubmitReviewApi* | [**submit_review**](docs/SubmitReviewApi.md#submit_review) | **POST** /v1/submit_review | Use submit_review when a user-submitted review of a product or seller.
*TagAPIApi* | [**tag_user**](docs/TagAPIApi.md#tag_user) | **POST** /v1/tag | The Tag API enables you to tell Thirdwatch which of your users are bad and which are good.
*TransactionApi* | [**transaction**](docs/TransactionApi.md#transaction) | **POST** /v1/transaction | Use transaction to record attempts results to Pay, Transfer money, Refund or other transactions.
*UntagAPIApi* | [**un_tag_user**](docs/UntagAPIApi.md#un_tag_user) | **POST** /v1/untag | If you are unsure whether a user is bad or good, you can always remove tag and leave the user in a neutral state.
*UpdateAccountApi* | [**update_account**](docs/UpdateAccountApi.md#update_account) | **POST** /v1/update_account | Use update_account to record changes to the user&#39;s account information.
*UpdateOrderApi* | [**update_order**](docs/UpdateOrderApi.md#update_order) | **POST** /v1/update_order | Update details of an existing order.


## Documentation For Models

 - [AddPromotion](docs/AddPromotion.md)
 - [AddToCart](docs/AddToCart.md)
 - [BillingAddress](docs/BillingAddress.md)
 - [Chargeback](docs/Chargeback.md)
 - [CreateAccount](docs/CreateAccount.md)
 - [CreateOrder](docs/CreateOrder.md)
 - [Custom](docs/Custom.md)
 - [CustomInfo](docs/CustomInfo.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [EventResponse](docs/EventResponse.md)
 - [Item](docs/Item.md)
 - [ItemStatus](docs/ItemStatus.md)
 - [LinkSessionToUser](docs/LinkSessionToUser.md)
 - [Login](docs/Login.md)
 - [Logout](docs/Logout.md)
 - [OrderStatus](docs/OrderStatus.md)
 - [PaymentMethod](docs/PaymentMethod.md)
 - [Promotion](docs/Promotion.md)
 - [RemoveFromCart](docs/RemoveFromCart.md)
 - [ReportItem](docs/ReportItem.md)
 - [Seller](docs/Seller.md)
 - [SendMessage](docs/SendMessage.md)
 - [ShippingAddress](docs/ShippingAddress.md)
 - [SubmitReview](docs/SubmitReview.md)
 - [Tag](docs/Tag.md)
 - [Transaction](docs/Transaction.md)
 - [UnTag](docs/UnTag.md)
 - [UpdateAccount](docs/UpdateAccount.md)
 - [UpdateOrder](docs/UpdateOrder.md)


## Documentation For Authorization


## api_key

- **Type**: API key
- **API key parameter name**: X-THIRDWATCH-API-KEY
- **Location**: HTTP header


## Author



