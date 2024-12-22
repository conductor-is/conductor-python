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

__all__ = ["Bill", "Currency", "PayablesAccount", "SalesTaxCode", "Terms", "Vendor"]


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


class Terms(BaseModel):
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


class Bill(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks to this bill.

    This ID is unique across all transaction types.
    """

    amount_due: str = FieldInfo(alias="amountDue")
    """The total monetary amount due for this bill, represented as a decimal string.

    This equals the sum of the amounts in the bill's expense lines, item lines, and
    item group lines. It also equals `openAmount` plus any credits or discounts.
    """

    amount_due_in_home_currency: Optional[str] = FieldInfo(alias="amountDueInHomeCurrency", default=None)
    """
    The total monetary amount due for this bill converted to the home currency of
    the QuickBooks company file. Represented as a decimal string.
    """

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when this bill was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """

    currency: Optional[Currency] = None
    """The bill's currency.

    For built-in currencies, the name and code are standard international values.
    For user-defined currencies, all values are editable.
    """

    custom_fields: List[CustomField] = FieldInfo(alias="customFields")
    """
    The custom fields for the bill object, added as user-defined data extensions,
    not included in the standard QuickBooks object.
    """

    due_date: Optional[date] = FieldInfo(alias="dueDate", default=None)
    """The date by which this bill must be paid, in ISO 8601 format (YYYY-MM-DD)."""

    exchange_rate: Optional[float] = FieldInfo(alias="exchangeRate", default=None)
    """
    The market exchange rate between this bill's currency and the home currency in
    QuickBooks at the time of this transaction. Represented as a decimal value
    (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).
    """

    expense_lines: List[ExpenseLine] = FieldInfo(alias="expenseLines")
    """The bill's expense lines, each representing one line in this expense."""

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """
    A globally unique identifier (GUID) you can provide for tracking this object in
    your external system.

    **IMPORTANT**: Must be formatted as a valid GUID; otherwise, QuickBooks will
    return an error. This field is immutable and can only be set during object
    creation.
    """

    is_paid: Optional[bool] = FieldInfo(alias="isPaid", default=None)
    """Indicates whether this bill has been paid in full.

    When `true`, `openAmount` will be 0.
    """

    is_pending: Optional[bool] = FieldInfo(alias="isPending", default=None)
    """Indicates whether this bill has not been completed or is in a draft version."""

    item_group_lines: List[ItemGroupLine] = FieldInfo(alias="itemGroupLines")
    """
    The bill's item group lines, each representing a predefined set of items bundled
    together because they are commonly purchased together or grouped for faster
    entry.
    """

    item_lines: List[ItemLine] = FieldInfo(alias="itemLines")
    """
    The bill's item lines, each representing the purchase of a specific item or
    service.
    """

    linked_transactions: List[LinkedTransaction] = FieldInfo(alias="linkedTransactions")
    """
    The bill's linked transactions, such as payments applied, credits used, or
    associated purchase orders.

    **IMPORTANT**: You must specify the parameter `includeLinkedTransactions` when
    fetching a list of bills to receive this field because it is not returned by
    default.
    """

    memo: Optional[str] = None
    """
    A memo or note for this bill that appears in the Accounts-Payable register and
    in reports that include this bill.
    """

    object_type: Literal["qbd_bill"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_bill"`."""

    open_amount: Optional[str] = FieldInfo(alias="openAmount", default=None)
    """
    The remaining amount owed on this bill after subtracting any credits or
    discounts from the `openAmount`. Represented as a decimal string.
    """

    payables_account: Optional[PayablesAccount] = FieldInfo(alias="payablesAccount", default=None)
    """
    The Accounts-Payable (A/P) account to which this bill is assigned, used to track
    the amount owed. If not specified, QuickBooks Desktop will use its default A/P
    account.

    **IMPORTANT**: If this bill is linked to other transactions, this A/P account
    must match the `payablesAccount` used in those other transactions.
    """

    ref_number: Optional[str] = FieldInfo(alias="refNumber", default=None)
    """
    The case-sensitive user-defined reference number for this bill, which can be
    used to identify the transaction in QuickBooks. This value is not required to be
    unique and can be arbitrarily changed by the QuickBooks user.
    """

    revision_number: str = FieldInfo(alias="revisionNumber")
    """
    The current revision number of this bill object, which changes each time the
    object is modified. When updating this object, you must provide the most recent
    `revisionNumber` to ensure you're working with the latest data; otherwise, the
    update will return an error.
    """

    sales_tax_code: Optional[SalesTaxCode] = FieldInfo(alias="salesTaxCode", default=None)
    """
    The sales-tax code associated with this bill, determining whether it is taxable
    or non-taxable. It's used to assign a default tax status to all transactions for
    this bill. Default codes include "Non" (non-taxable) and "Tax" (taxable), but
    custom codes can also be created in QuickBooks. If QuickBooks is not set up to
    charge sales tax (via the "Do You Charge Sales Tax?" preference), it will assign
    the default non-taxable code to all sales.
    """

    terms: Optional[Terms] = None
    """
    The bill's payment terms, defining when payment is due and any applicable
    discounts.
    """

    transaction_date: date = FieldInfo(alias="transactionDate")
    """The date of this bill, in ISO 8601 format (YYYY-MM-DD)."""

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when this bill was last updated, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """

    vendor: Vendor
    """The vendor who sent this bill for goods or services purchased."""

    vendor_address: Optional[Address] = FieldInfo(alias="vendorAddress", default=None)
    """The address of the vendor who sent this bill."""
