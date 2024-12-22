# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .address import Address
from ..._models import BaseModel
from .item_line import ItemLine
from .custom_field import CustomField
from .expense_line import ExpenseLine
from .item_group_line import ItemGroupLine
from .linked_transaction import LinkedTransaction

__all__ = ["Check", "BankAccount", "Currency", "Payee", "SalesTaxCode"]


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


class Payee(BaseModel):
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


class SalesTaxCode(BaseModel):
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


class Check(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks to this check.

    This ID is unique across all transaction types.
    """

    address: Optional[Address] = None
    """The address that is printed on the check."""

    amount: str
    """The total monetary amount of this check, represented as a decimal string.

    This equals the sum of the amounts in the check's expense lines, item lines, and
    item group lines.
    """

    amount_in_home_currency: Optional[str] = FieldInfo(alias="amountInHomeCurrency", default=None)
    """
    The total monetary amount for this check converted to the home currency of the
    QuickBooks company file. Represented as a decimal string.
    """

    bank_account: BankAccount = FieldInfo(alias="bankAccount")
    """
    The bank account from which the funds are being drawn for this check; e.g.,
    Checking or Savings. This check will decrease the balance of this account.
    """

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when this check was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """

    currency: Optional[Currency] = None
    """The check's currency.

    For built-in currencies, the name and code are standard international values.
    For user-defined currencies, all values are editable.
    """

    custom_fields: List[CustomField] = FieldInfo(alias="customFields")
    """
    The custom fields for the check object, added as user-defined data extensions,
    not included in the standard QuickBooks object.
    """

    exchange_rate: Optional[float] = FieldInfo(alias="exchangeRate", default=None)
    """
    The market exchange rate between this check's currency and the home currency in
    QuickBooks at the time of this transaction. Represented as a decimal value
    (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).
    """

    expense_lines: List[ExpenseLine] = FieldInfo(alias="expenseLines")
    """The check's expense lines, each representing one line in this expense."""

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """
    A globally unique identifier (GUID) you can provide for tracking this object in
    your external system.

    **IMPORTANT**: Must be formatted as a valid GUID; otherwise, QuickBooks will
    return an error. This field is immutable and can only be set during object
    creation.
    """

    is_pending: Optional[bool] = FieldInfo(alias="isPending", default=None)
    """Indicates whether this check has not been completed."""

    is_queued_for_print: Optional[bool] = FieldInfo(alias="isQueuedForPrint", default=None)
    """
    Indicates whether this check is included in the queue of documents for
    QuickBooks to print.
    """

    item_group_lines: List[ItemGroupLine] = FieldInfo(alias="itemGroupLines")
    """
    The check's item group lines, each representing a predefined set of items
    bundled together because they are commonly purchased together or grouped for
    faster entry.
    """

    item_lines: List[ItemLine] = FieldInfo(alias="itemLines")
    """
    The check's item lines, each representing the purchase of a specific item or
    service.
    """

    linked_transactions: List[LinkedTransaction] = FieldInfo(alias="linkedTransactions")
    """
    The check's linked transactions, such as payments applied, credits used, or
    associated purchase orders.

    **IMPORTANT**: You must specify the parameter `includeLinkedTransactions` when
    fetching a list of checks to receive this field because it is not returned by
    default.
    """

    memo: Optional[str] = None
    """The memo that is printed on this check."""

    object_type: Literal["qbd_check"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_check"`."""

    payee: Optional[Payee] = None
    """The person or company who will receive this check."""

    ref_number: Optional[str] = FieldInfo(alias="refNumber", default=None)
    """
    The case-sensitive user-defined reference number for this check, which can be
    used to identify the transaction in QuickBooks. This value is not required to be
    unique and can be arbitrarily changed by the QuickBooks user.

    **IMPORTANT**: For checks, this field is the check number.
    """

    revision_number: str = FieldInfo(alias="revisionNumber")
    """
    The current revision number of this check object, which changes each time the
    object is modified. When updating this object, you must provide the most recent
    `revisionNumber` to ensure you're working with the latest data; otherwise, the
    update will return an error.
    """

    sales_tax_code: Optional[SalesTaxCode] = FieldInfo(alias="salesTaxCode", default=None)
    """
    The sales-tax code associated with this check, determining whether transactions
    in this account are taxable or non-taxable. It's used to assign a default tax
    status to all transactions for this check. Default codes include "Non"
    (non-taxable) and "Tax" (taxable), but custom codes can also be created in
    QuickBooks. If QuickBooks is not set up to charge sales tax (via the "Do You
    Charge Sales Tax?" preference), it will assign the default non-taxable code to
    all sales.
    """

    transaction_date: date = FieldInfo(alias="transactionDate")
    """The date written on this check, in ISO 8601 format (YYYY-MM-DD)."""

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when this check was last updated, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """
