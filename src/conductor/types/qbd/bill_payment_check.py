# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "BillPaymentCheck",
    "Address",
    "AppliedToTransaction",
    "AppliedToTransactionDiscountAccount",
    "AppliedToTransactionDiscountClass",
    "AppliedToTransactionLinkedTransaction",
    "BankAccount",
    "Currency",
    "CustomField",
    "PayablesAccount",
    "Vendor",
]


class Address(BaseModel):
    city: Optional[str] = None
    """The city, district, suburb, town, or village name of the address."""

    country: Optional[str] = None
    """The country name of the address."""

    line1: Optional[str] = None
    """The first line of the address (e.g., street, PO Box, or company name)."""

    line2: Optional[str] = None
    """
    The second line of the address, if needed (e.g., apartment, suite, unit, or
    building).
    """

    line3: Optional[str] = None
    """The third line of the address, if needed."""

    line4: Optional[str] = None
    """The fourth line of the address, if needed."""

    line5: Optional[str] = None
    """The fifth line of the address, if needed."""

    note: Optional[str] = None
    """
    A note written at the bottom of the address in the form in which it appears,
    such as the invoice form.
    """

    postal_code: Optional[str] = FieldInfo(alias="postalCode", default=None)
    """The postal code or ZIP code of the address."""

    state: Optional[str] = None
    """The state, county, province, or region name of the address."""


class AppliedToTransactionDiscountAccount(BaseModel):
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


class AppliedToTransactionDiscountClass(BaseModel):
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


class AppliedToTransactionLinkedTransaction(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks to this linked transaction.

    This ID is unique across all transaction types.
    """

    amount: str
    """
    The monetary amount of this linked transaction, represented as a decimal string.
    """

    link_type: Optional[Literal["amount", "quantity"]] = FieldInfo(alias="linkType", default=None)
    """
    Indicates the nature of the link between the transactions: `amount` denotes an
    amount-based link (e.g., an invoice linked to a payment), and `quantity` denotes
    a quantity-based link (e.g., an invoice created from a sales order based on the
    quantity of items received).
    """

    object_type: Literal["qbd_linked_transaction"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_linked_transaction"`."""

    ref_number: Optional[str] = FieldInfo(alias="refNumber", default=None)
    """
    The case-sensitive user-defined reference number for this linked transaction,
    which can be used to identify the transaction in QuickBooks. This value is not
    required to be unique and can be arbitrarily changed by the QuickBooks user.
    """

    transaction_date: date = FieldInfo(alias="transactionDate")
    """The date of this linked transaction, in ISO 8601 format (YYYY-MM-DD)."""

    transaction_type: Literal[
        "ar_refund_credit_card",
        "bill",
        "bill_payment_check",
        "bill_payment_credit_card",
        "build_assembly",
        "charge",
        "check",
        "credit_card_charge",
        "credit_card_credit",
        "credit_memo",
        "deposit",
        "estimate",
        "inventory_adjustment",
        "invoice",
        "item_receipt",
        "journal_entry",
        "liability_adjustment",
        "paycheck",
        "payroll_liability_check",
        "purchase_order",
        "receive_payment",
        "sales_order",
        "sales_receipt",
        "sales_tax_payment_check",
        "transfer",
        "vendor_credit",
        "ytd_adjustment",
    ] = FieldInfo(alias="transactionType")
    """The type of transaction for this linked transaction."""


class AppliedToTransaction(BaseModel):
    amount: Optional[str] = None
    """
    The monetary amount of this receivable transaction, represented as a decimal
    string.
    """

    balance_remaining: Optional[str] = FieldInfo(alias="balanceRemaining", default=None)
    """
    The outstanding balance of this receivable transaction after applying any
    credits or payments. Represented as a decimal string.
    """

    discount_account: Optional[AppliedToTransactionDiscountAccount] = FieldInfo(alias="discountAccount", default=None)
    """The financial account used to track this receivable transaction's discount."""

    discount_amount: Optional[str] = FieldInfo(alias="discountAmount", default=None)
    """
    The monetary amount by which to reduce the receivable transaction's receivable
    amount, represented as a decimal string.
    """

    discount_class: Optional[AppliedToTransactionDiscountClass] = FieldInfo(alias="discountClass", default=None)
    """The class used to track this receivable transaction's discount."""

    linked_transactions: List[AppliedToTransactionLinkedTransaction] = FieldInfo(alias="linkedTransactions")
    """
    The receivable transaction's linked transactions, such as payments applied,
    credits used, or associated purchase orders.

    **IMPORTANT**: You must specify the parameter `includeLinkedTransactions` when
    fetching a list of receivable transactions to receive this field because it is
    not returned by default.
    """

    ref_number: Optional[str] = FieldInfo(alias="refNumber", default=None)
    """
    The case-sensitive user-defined reference number for this receivable
    transaction, which can be used to identify the transaction in QuickBooks. This
    value is not required to be unique and can be arbitrarily changed by the
    QuickBooks user.
    """

    transaction_date: date = FieldInfo(alias="transactionDate")
    """The date of this receivable transaction, in ISO 8601 format (YYYY-MM-DD)."""

    transaction_id: str = FieldInfo(alias="transactionId")
    """The ID of the receivable transaction to which this payment is applied."""

    transaction_type: Literal[
        "ar_refund_credit_card",
        "bill",
        "bill_payment_check",
        "bill_payment_credit_card",
        "build_assembly",
        "charge",
        "check",
        "credit_card_charge",
        "credit_card_credit",
        "credit_memo",
        "deposit",
        "estimate",
        "inventory_adjustment",
        "invoice",
        "item_receipt",
        "journal_entry",
        "liability_adjustment",
        "paycheck",
        "payroll_liability_check",
        "purchase_order",
        "receive_payment",
        "sales_order",
        "sales_receipt",
        "sales_tax_payment_check",
        "transfer",
        "vendor_credit",
        "ytd_adjustment",
    ] = FieldInfo(alias="transactionType")
    """The type of transaction for this receivable transaction."""


class BankAccount(BaseModel):
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


class CustomField(BaseModel):
    name: str
    """The name of the custom field, unique for the specified `ownerId`.

    For public custom fields, this name is visible as a label in the QuickBooks UI.
    """

    owner_id: Optional[str] = FieldInfo(alias="ownerId", default=None)
    """
    The identifier of the owner of the custom field, which QuickBooks internally
    calls a "data extension". For public custom fields visible in the UI, such as
    those added by the QuickBooks user, this is always "0". For private custom
    fields that are only visible to the application that created them, this is a
    valid GUID identifying the owning application. Internally, Conductor always
    fetches all public custom fields (those with an `ownerId` of "0") for all
    objects.
    """

    type: Literal[
        "amount_type",
        "date_time_type",
        "integer_type",
        "percent_type",
        "price_type",
        "quantity_type",
        "string_1024_type",
        "string_255_type",
    ]
    """The data type of this custom field."""

    value: str
    """The value of this custom field.

    The maximum length depends on the field's data type.
    """


class PayablesAccount(BaseModel):
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


class Vendor(BaseModel):
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


class BillPaymentCheck(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks to this bill payment check.

    This ID is unique across all transaction types.
    """

    address: Optional[Address] = None
    """The address that is printed on the bill payment check."""

    amount: Optional[str] = None
    """
    The monetary amount of this bill payment check, represented as a decimal string.
    """

    amount_in_home_currency: Optional[str] = FieldInfo(alias="amountInHomeCurrency", default=None)
    """
    The total monetary amount for this bill payment check converted to the home
    currency of the QuickBooks company file. Represented as a decimal string.
    """

    applied_to_transactions: List[AppliedToTransaction] = FieldInfo(alias="appliedToTransactions")
    """The bill(s) paid by this bill payment check."""

    bank_account: BankAccount = FieldInfo(alias="bankAccount")
    """
    The bank account from which the funds are being drawn for this bill payment
    check; e.g., Checking or Savings. This bill payment check will decrease the
    balance of this account.
    """

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when this bill payment check was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """

    currency: Optional[Currency] = None
    """The bill payment check's currency.

    For built-in currencies, the name and code are standard international values.
    For user-defined currencies, all values are editable.
    """

    custom_fields: List[CustomField] = FieldInfo(alias="customFields")
    """
    The custom fields for the bill payment check object, added as user-defined data
    extensions, not included in the standard QuickBooks object.
    """

    exchange_rate: Optional[float] = FieldInfo(alias="exchangeRate", default=None)
    """
    The market exchange rate between this bill payment check's currency and the home
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

    is_queued_for_print: Optional[bool] = FieldInfo(alias="isQueuedForPrint", default=None)
    """
    Indicates whether this bill payment check is included in the queue of documents
    for QuickBooks to print.
    """

    memo: Optional[str] = None
    """A memo or note for this bill payment check."""

    object_type: Literal["qbd_bill_payment_check"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_bill_payment_check"`."""

    payables_account: Optional[PayablesAccount] = FieldInfo(alias="payablesAccount", default=None)
    """
    The Accounts-Payable (A/P) account to which this bill payment check is assigned,
    used to track the amount owed. If not specified, QuickBooks Desktop will use its
    default Accounts-Payable account.

    **IMPORTANT**: If this bill payment check is linked to other transactions, this
    A/P account must match the `payablesAccount` used in those other transactions.
    """

    ref_number: Optional[str] = FieldInfo(alias="refNumber", default=None)
    """
    The case-sensitive user-defined reference number for this bill payment check,
    which can be used to identify the transaction in QuickBooks. This value is not
    required to be unique and can be arbitrarily changed by the QuickBooks user.

    **IMPORTANT**: For checks, this field is the check number.
    """

    revision_number: str = FieldInfo(alias="revisionNumber")
    """
    The current revision number of this bill payment check object, which changes
    each time the object is modified. When updating this object, you must provide
    the most recent `revisionNumber` to ensure you're working with the latest data;
    otherwise, the update will return an error.
    """

    transaction_date: date = FieldInfo(alias="transactionDate")
    """The date of this bill payment check, in ISO 8601 format (YYYY-MM-DD)."""

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when this bill payment check was last updated, in ISO 8601
    format (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time
    zone in QuickBooks.
    """

    vendor: Optional[Vendor] = None
    """
    The vendor who sent the bill(s) that this check is paying and who will receive
    this payment.

    **IMPORTANT**: This vendor must match the `vendor` on the bill(s) specified in
    `applyToTransactions`.
    """
