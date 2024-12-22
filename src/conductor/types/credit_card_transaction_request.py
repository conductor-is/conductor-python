# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CreditCardTransactionRequest"]


class CreditCardTransactionRequest(BaseModel):
    address: Optional[str] = None
    """The card's billing address."""

    commercial_card_code: Optional[str] = FieldInfo(alias="commercialCardCode", default=None)
    """
    The commercial card code identifies the type of business credit card being used
    (purchase, corporate, or business) for Visa and Mastercard transactions only.
    When provided, this code may qualify the transaction for lower processing fees
    compared to the standard rates that apply when no code is specified.
    """

    expiration_month: float = FieldInfo(alias="expirationMonth")
    """The month when the credit card expires."""

    expiration_year: float = FieldInfo(alias="expirationYear")
    """The year when the credit card expires."""

    name: str
    """The cardholder's name on the card."""

    number: str
    """The credit card number. Must be masked with lower case "x" and no dashes."""

    postal_code: Optional[str] = FieldInfo(alias="postalCode", default=None)
    """The card's billing address ZIP or postal code."""

    transaction_mode: Optional[Literal["card_not_present", "card_present"]] = FieldInfo(
        alias="transactionMode", default=None
    )
    """
    Indicates whether this credit card transaction came from a card swipe
    (`card_present`) or not (`card_not_present`).
    """

    transaction_type: Optional[Literal["authorization", "capture", "charge", "refund", "voice_authorization"]] = (
        FieldInfo(alias="transactionType", default=None)
    )
    """The QBMS transaction type from which the current transaction data originated."""
