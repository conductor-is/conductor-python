# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .credit_card_transaction_request import CreditCardTransactionRequest
from .credit_card_transaction_response import CreditCardTransactionResponse

__all__ = ["CreditCardTransaction"]


class CreditCardTransaction(BaseModel):
    request: Optional[CreditCardTransactionRequest] = None
    """
    The transaction request data originally supplied for this credit card
    transaction when using QuickBooks Merchant Services (QBMS).
    """

    response: Optional[CreditCardTransactionResponse] = None
    """
    The transaction response data for this credit card transaction when using
    QuickBooks Merchant Services (QBMS).
    """
