# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..custom_field import CustomField
from ..receivable_transaction import ReceivableTransaction
from ..credit_card_transaction import CreditCardTransaction

__all__ = ["ReceivePayment", "Currency", "Customer", "DepositToAccount", "PaymentMethod", "ReceivablesAccount"]


class Currency(BaseModel):
    id: Optional[str] = None
    """The unique identifier assigned by QuickBooks to this object.

    This ID is unique across all objects of the same type, but not across different
    QuickBooks object types.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The fully-qualified unique name for this object, formed by combining the names
    of its parent objects with its own `name`, separated by colons. Not
    case-sensitive.
    """


class Customer(BaseModel):
    id: Optional[str] = None
    """The unique identifier assigned by QuickBooks to this object.

    This ID is unique across all objects of the same type, but not across different
    QuickBooks object types.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The fully-qualified unique name for this object, formed by combining the names
    of its parent objects with its own `name`, separated by colons. Not
    case-sensitive.
    """


class DepositToAccount(BaseModel):
    id: Optional[str] = None
    """The unique identifier assigned by QuickBooks to this object.

    This ID is unique across all objects of the same type, but not across different
    QuickBooks object types.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The fully-qualified unique name for this object, formed by combining the names
    of its parent objects with its own `name`, separated by colons. Not
    case-sensitive.
    """


class PaymentMethod(BaseModel):
    id: Optional[str] = None
    """The unique identifier assigned by QuickBooks to this object.

    This ID is unique across all objects of the same type, but not across different
    QuickBooks object types.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The fully-qualified unique name for this object, formed by combining the names
    of its parent objects with its own `name`, separated by colons. Not
    case-sensitive.
    """


class ReceivablesAccount(BaseModel):
    id: Optional[str] = None
    """The unique identifier assigned by QuickBooks to this object.

    This ID is unique across all objects of the same type, but not across different
    QuickBooks object types.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The fully-qualified unique name for this object, formed by combining the names
    of its parent objects with its own `name`, separated by colons. Not
    case-sensitive.
    """


class ReceivePayment(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks to this receive-payment.

    This ID is unique across all transaction types.
    """

    applied_to_transactions: List[ReceivableTransaction] = FieldInfo(alias="appliedToTransactions")
    """The invoice(s) paid by this receive-payment."""

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when this receive-payment was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """

    credit_card_transaction: Optional[CreditCardTransaction] = FieldInfo(alias="creditCardTransaction", default=None)
    """
    The credit card transaction data for this receive-payment's payment when using
    QuickBooks Merchant Services (QBMS).
    """

    currency: Optional[Currency] = None
    """The receive-payment's currency.

    For built-in currencies, the name and code are standard international values.
    For user-defined currencies, all values are editable.
    """

    customer: Customer
    """
    The customer or customer-job to which the payment for this receive-payment is
    credited.
    """

    custom_fields: List[CustomField] = FieldInfo(alias="customFields")
    """
    The custom fields for the receive-payment object, added as user-defined data
    extensions, not included in the standard QuickBooks object.
    """

    deposit_to_account: Optional[DepositToAccount] = FieldInfo(alias="depositToAccount", default=None)
    """
    The account where the funds for this receive-payment will be or have been
    deposited.
    """

    exchange_rate: Optional[float] = FieldInfo(alias="exchangeRate", default=None)
    """
    The market exchange rate between this receive-payment's currency and the home
    currency in QuickBooks at the time of this transaction. Represented as a decimal
    value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).
    """

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """
    A globally unique identifier (GUID) you can provide for tracking this object in
    your external system.

    **IMPORTANT**: Must be formatted as a valid GUID; otherwise, QuickBooks will
    return an error. This field is immutable and can only be set during object
    creation.
    """

    memo: Optional[str] = None
    """
    A memo or note that appears in reports that show details of this
    receive-payment.
    """

    object_type: Literal["qbd_receive_payment"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_receive_payment"`."""

    payment_method: Optional[PaymentMethod] = FieldInfo(alias="paymentMethod", default=None)
    """The receive-payment's payment method (e.g., cash, check, credit card)."""

    receivables_account: Optional[ReceivablesAccount] = FieldInfo(alias="receivablesAccount", default=None)
    """
    The Accounts-Receivable (A/R) account to which this receive-payment is assigned,
    used to track the amount owed. If not specified, QuickBooks Desktop will use its
    default A/R account.

    **IMPORTANT**: If this receive-payment is linked to other transactions, this A/R
    account must match the `receivablesAccount` used in all linked transactions. For
    example, when refunding a credit card payment, the A/R account must match the
    one used in the original credit transactions being refunded.
    """

    ref_number: Optional[str] = FieldInfo(alias="refNumber", default=None)
    """
    The case-sensitive user-defined reference number for this receive-payment, which
    can be used to identify the transaction in QuickBooks. This value is not
    required to be unique and can be arbitrarily changed by the QuickBooks user.
    """

    revision_number: str = FieldInfo(alias="revisionNumber")
    """
    The current revision number of this receive-payment object, which changes each
    time the object is modified. When updating this object, you must provide the
    most recent `revisionNumber` to ensure you're working with the latest data;
    otherwise, the update will return an error.
    """

    total_amount: str = FieldInfo(alias="totalAmount")
    """
    The total monetary amount of this receive-payment, represented as a decimal
    string.

    **NOTE:** The sum of the `paymentAmount` amounts in the `applyToTransactions`
    array cannot exceed the `totalAmount`, or you will receive an error.
    """

    total_amount_in_home_currency: Optional[str] = FieldInfo(alias="totalAmountInHomeCurrency", default=None)
    """
    The total monetary amount for this receive-payment converted to the home
    currency of the QuickBooks company file. Represented as a decimal string.
    """

    transaction_date: date = FieldInfo(alias="transactionDate")
    """The date of this receive-payment, in ISO 8601 format (YYYY-MM-DD)."""

    unused_credits: Optional[str] = FieldInfo(alias="unusedCredits", default=None)
    """
    The amount of credit that remains unused after applying credits to this
    receive-payment. This occurs when the `applyCredit.appliedAmount` specified for
    a credit memo (`applyCredit.creditMemoId`) in the `applyToTransactions` array is
    less than the total available credit amount for that credit memo.
    """

    unused_payment: Optional[str] = FieldInfo(alias="unusedPayment", default=None)
    """The amount of this receive-payment that remains unapplied to any transactions.

    This occurs in two cases: (1) When the sum of `paymentAmount` amounts in
    `applyToTransactions` is less than `totalAmount`, leaving a portion of the
    payment unused, or (2) When a payment is received that equals the exact amount
    of an invoice, but credits or discounts are also applied, resulting in excess
    payment.
    """

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when this receive-payment was last updated, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """
