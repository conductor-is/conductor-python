# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CreditCardTransactionResponse"]


class CreditCardTransactionResponse(BaseModel):
    authorization_code: Optional[str] = FieldInfo(alias="authorizationCode", default=None)
    """
    The authorization code returned from the credit card processor to indicate that
    this charge will be paid by the card issuer.
    """

    avs_street_status: Optional[Literal["fail", "not_available", "pass"]] = FieldInfo(
        alias="avsStreetStatus", default=None
    )
    """
    Indicates whether the street address supplied in the transaction request matches
    the customer's address on file at the card issuer.
    """

    avs_zip_status: Optional[Literal["fail", "not_available", "pass"]] = FieldInfo(alias="avsZipStatus", default=None)
    """
    Indicates whether the customer postal ZIP code supplied in the transaction
    request matches the customer's postal code recognized at the card issuer.
    """

    card_security_code_match: Optional[Literal["fail", "not_available", "pass"]] = FieldInfo(
        alias="cardSecurityCodeMatch", default=None
    )
    """
    Indicates whether the card security code supplied in the transaction request
    matches the card security code recognized for that credit card number at the
    card issuer.
    """

    client_transaction_id: Optional[str] = FieldInfo(alias="clientTransactionId", default=None)
    """
    A value returned from QBMS transactions for future use by the QuickBooks
    Reconciliation feature.
    """

    credit_card_transaction_id: str = FieldInfo(alias="creditCardTransactionId")
    """
    The ID returned from the credit card processor for this credit card transaction.
    """

    merchant_account_number: str = FieldInfo(alias="merchantAccountNumber")
    """
    The QBMS account number of the merchant who is running this transaction using
    the customer's credit card.
    """

    payment_grouping_code: Optional[float] = FieldInfo(alias="paymentGroupingCode", default=None)
    """
    An internal code returned by QuickBooks Merchant Services (QBMS) from the
    transaction request, needed for the QuickBooks reconciliation feature.
    """

    payment_status: Literal["completed", "unknown"] = FieldInfo(alias="paymentStatus")
    """
    Indicates whether this credit card transaction is known to have been
    successfully processed by the card issuer.
    """

    recon_batch_id: Optional[str] = FieldInfo(alias="reconBatchId", default=None)
    """
    An internal ID returned by QuickBooks Merchant Services (QBMS) from the
    transaction request, needed for the QuickBooks reconciliation feature.
    """

    status_code: float = FieldInfo(alias="statusCode")
    """
    The status code returned in the original QBMS transaction response for this
    credit card transaction.
    """

    status_message: str = FieldInfo(alias="statusMessage")
    """
    The status message returned in the original QBMS transaction response for this
    credit card transaction.
    """

    transaction_authorization_stamp: Optional[float] = FieldInfo(alias="transactionAuthorizationStamp", default=None)
    """
    An internal value for this credit card transaction, needed for the QuickBooks
    reconciliation feature.
    """

    transaction_authorized_at: str = FieldInfo(alias="transactionAuthorizedAt")
    """
    The date and time when the credit card processor authorized this credit card
    transaction.
    """
