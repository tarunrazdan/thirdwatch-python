# coding: utf-8

"""
    Thirdwatch API

    The first version of the Thirdwatch API is an exciting step forward towards making it easier for developers to pass data to Thirdwatch.   # Introduction Once you've [registered your website/app](https://thirdwatch.ai) it's easy to start sending data to Thirdwatch.  All endpoints are only accessible via https and are located at `api.thirdwatch.ai`. For instance: you can send event at the moment by ```HTTP POST``` Request to the following URL with your API key in ```Header``` and ```JSON``` data in request body. ```   https://api.thirdwatch.ai/event/v1 ``` Every API request must contain ```API Key``` in header value ```X-THIRDWATCH-API-KEY```  Every event must contain your ```_userId``` (if this is not available, you can alternatively provide a ```_sessionId``` value also in ```_userId```).  # Score API The Score API is use to get an up to date cutomer trust score after you have sent transaction event and order successful. This API will provide the riskiness score of the order with reasons. Some examples of when you may want to check the score are before:    - Before Shippement of a package   - Finalizing a money transfer   - Giving access to a prearranged vacation rental   - Sending voucher on mail    ```   https://api.thirdwatch.ai/neo/v1/score?api_key=<your api key>&order_id=<Order id> ```  According to Score you can decide to take action Approve or Reject. Orders with score more than 70 will consider as Riskey orders. We'll provide some reasons also in rules section.  ## Response score API  ``` {   \"order_id\": \"OCT45671\",   \"user_id\": \"ajay_245\",   \"order_timestamp\": \"2017-05-09T09:40:45.717Z\",   \"score\": 82,   \"flag\": \"red\",     -\"reasons\": [     {         \"name\": \"_numOfFailedTransactions\",         \"display_name\": \"Number of failed transactions\",         \"flag\": \"green\",         \"value\": \"0\",         \"is_display\": true       },       {         \"name\": \"_accountAge\",         \"display_name\": \"Account age\",         \"flag\": \"red\",         \"value\": \"0\",         \"is_display\": true       },        {         \"name\": \"_numOfOrderSameIp\",         \"display_name\": \"Number of orders from same IP\",         \"flag\": \"red\",         \"value\": \"11\",         \"is_display\": true       }     ] } ``` 

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Promotion(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, promotion_id=None, status=None, description=None, amount=None, min_purchase_amount=None, referrer_user_id=None, failure_reason=None, percentage_off=None, currency_code=None, type=None):
        """
        Promotion - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'promotion_id': 'str',
            'status': 'str',
            'description': 'str',
            'amount': 'str',
            'min_purchase_amount': 'str',
            'referrer_user_id': 'str',
            'failure_reason': 'str',
            'percentage_off': 'str',
            'currency_code': 'str',
            'type': 'str'
        }

        self.attribute_map = {
            'promotion_id': '_promotionId',
            'status': '_status',
            'description': '_description',
            'amount': '_amount',
            'min_purchase_amount': '_minPurchaseAmount',
            'referrer_user_id': '_referrerUserId',
            'failure_reason': '_failureReason',
            'percentage_off': '_percentageOff',
            'currency_code': '_currencyCode',
            'type': '_type'
        }

        self._promotion_id = promotion_id
        self._status = status
        self._description = description
        self._amount = amount
        self._min_purchase_amount = min_purchase_amount
        self._referrer_user_id = referrer_user_id
        self._failure_reason = failure_reason
        self._percentage_off = percentage_off
        self._currency_code = currency_code
        self._type = type

    @property
    def promotion_id(self):
        """
        Gets the promotion_id of this Promotion.
        The ID/Coupon Code within your system that you use to represent this promotion. This ID is ideally unique to the promotion across users (e.g. \"Welcome\").

        :return: The promotion_id of this Promotion.
        :rtype: str
        """
        return self._promotion_id

    @promotion_id.setter
    def promotion_id(self, promotion_id):
        """
        Sets the promotion_id of this Promotion.
        The ID/Coupon Code within your system that you use to represent this promotion. This ID is ideally unique to the promotion across users (e.g. \"Welcome\").

        :param promotion_id: The promotion_id of this Promotion.
        :type: str
        """

        self._promotion_id = promotion_id

    @property
    def status(self):
        """
        Gets the status of this Promotion.
        The status of the addition of promotion to an account. Best used with the add_promotion event. This way you can pass to Thirdwatch both successful and failed attempts when using a promotion. May be useful in spotting potential abuse. e.g. _success, _Failed

        :return: The status of this Promotion.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Promotion.
        The status of the addition of promotion to an account. Best used with the add_promotion event. This way you can pass to Thirdwatch both successful and failed attempts when using a promotion. May be useful in spotting potential abuse. e.g. _success, _Failed

        :param status: The status of this Promotion.
        :type: str
        """

        self._status = status

    @property
    def description(self):
        """
        Gets the description of this Promotion.
        Describe promotion here.

        :return: The description of this Promotion.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Promotion.
        Describe promotion here.

        :param description: The description of this Promotion.
        :type: str
        """

        self._description = description

    @property
    def amount(self):
        """
        Gets the amount of this Promotion.
        The amount or credits the promotion is worth.

        :return: The amount of this Promotion.
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        Sets the amount of this Promotion.
        The amount or credits the promotion is worth.

        :param amount: The amount of this Promotion.
        :type: str
        """

        self._amount = amount

    @property
    def min_purchase_amount(self):
        """
        Gets the min_purchase_amount of this Promotion.
        The minimum amount someone must spend in order for the promotion to be applied.

        :return: The min_purchase_amount of this Promotion.
        :rtype: str
        """
        return self._min_purchase_amount

    @min_purchase_amount.setter
    def min_purchase_amount(self, min_purchase_amount):
        """
        Sets the min_purchase_amount of this Promotion.
        The minimum amount someone must spend in order for the promotion to be applied.

        :param min_purchase_amount: The min_purchase_amount of this Promotion.
        :type: str
        """

        self._min_purchase_amount = min_purchase_amount

    @property
    def referrer_user_id(self):
        """
        Gets the referrer_user_id of this Promotion.
        The unique user ID of the user who referred the user to this promotion.

        :return: The referrer_user_id of this Promotion.
        :rtype: str
        """
        return self._referrer_user_id

    @referrer_user_id.setter
    def referrer_user_id(self, referrer_user_id):
        """
        Sets the referrer_user_id of this Promotion.
        The unique user ID of the user who referred the user to this promotion.

        :param referrer_user_id: The referrer_user_id of this Promotion.
        :type: str
        """

        self._referrer_user_id = referrer_user_id

    @property
    def failure_reason(self):
        """
        Gets the failure_reason of this Promotion.
        When adding a promotion fails, use this to describe why it failed.e.g. _alreadyUsed, _invalidCode, _notApplicable, _expired

        :return: The failure_reason of this Promotion.
        :rtype: str
        """
        return self._failure_reason

    @failure_reason.setter
    def failure_reason(self, failure_reason):
        """
        Sets the failure_reason of this Promotion.
        When adding a promotion fails, use this to describe why it failed.e.g. _alreadyUsed, _invalidCode, _notApplicable, _expired

        :param failure_reason: The failure_reason of this Promotion.
        :type: str
        """

        self._failure_reason = failure_reason

    @property
    def percentage_off(self):
        """
        Gets the percentage_off of this Promotion.
        The percentage discount. If the discount is 10% off, you would send \"10\".

        :return: The percentage_off of this Promotion.
        :rtype: str
        """
        return self._percentage_off

    @percentage_off.setter
    def percentage_off(self, percentage_off):
        """
        Sets the percentage_off of this Promotion.
        The percentage discount. If the discount is 10% off, you would send \"10\".

        :param percentage_off: The percentage_off of this Promotion.
        :type: str
        """

        self._percentage_off = percentage_off

    @property
    def currency_code(self):
        """
        Gets the currency_code of this Promotion.
        The [ISO-4217](http://en.wikipedia.org/wiki/ISO_4217) currency code for the amount. e.g., USD, INR alternative currencies, like bitcoin or points systems.

        :return: The currency_code of this Promotion.
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """
        Sets the currency_code of this Promotion.
        The [ISO-4217](http://en.wikipedia.org/wiki/ISO_4217) currency code for the amount. e.g., USD, INR alternative currencies, like bitcoin or points systems.

        :param currency_code: The currency_code of this Promotion.
        :type: str
        """

        self._currency_code = currency_code

    @property
    def type(self):
        """
        Gets the type of this Promotion.
        Type of the promotion e.g., First Time, Refer, Diwali

        :return: The type of this Promotion.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Promotion.
        Type of the promotion e.g., First Time, Refer, Diwali

        :param type: The type of this Promotion.
        :type: str
        """

        self._type = type

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Promotion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
