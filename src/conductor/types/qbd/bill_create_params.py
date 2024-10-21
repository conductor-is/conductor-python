# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "BillCreateParams",
    "ExpenseLine",
    "ExpenseLineCustomField",
    "ItemGroupLine",
    "ItemGroupLineCustomField",
    "ItemLine",
    "ItemLineCustomField",
    "ItemLineLinkToTransactionLineItem",
    "VendorAddress",
]


class BillCreateParams(TypedDict, total=False):
    transaction_date: Required[Annotated[Union[str, date], PropertyInfo(alias="transactionDate", format="iso8601")]]
    """The date of this bill, in ISO 8601 format (YYYY-MM-DD)."""

    vendor_id: Required[Annotated[str, PropertyInfo(alias="vendorId")]]
    """The vendor who sent this bill for goods or services purchased."""

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    accounts_payable_account_id: Annotated[str, PropertyInfo(alias="accountsPayableAccountId")]
    """
    The Accounts Payable account to which this bill is assigned, used to track the
    amount owed. If not specified, the default Accounts Payable account in
    QuickBooks is used.
    """

    due_date: Annotated[Union[str, date], PropertyInfo(alias="dueDate", format="iso8601")]
    """The date by which this bill must be paid, in ISO 8601 format (YYYY-MM-DD)."""

    exchange_rate: Annotated[float, PropertyInfo(alias="exchangeRate")]
    """
    The market exchange rate between this bill's currency and the home currency in
    QuickBooks at the time of this transaction. Represented as a decimal value
    (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).
    """

    expense_lines: Annotated[Iterable[ExpenseLine], PropertyInfo(alias="expenseLines")]
    """The bill's expense lines, each representing one line in this expense."""

    external_id: Annotated[str, PropertyInfo(alias="externalId")]
    """
    A globally unique identifier (GUID) you can provide for tracking this object in
    your external system. Must be formatted as a valid GUID; otherwise, QuickBooks
    will return an error.
    """

    item_group_lines: Annotated[Iterable[ItemGroupLine], PropertyInfo(alias="itemGroupLines")]
    """
    The bill's item group lines, each representing a predefined set of items bundled
    because they are commonly purchased together or grouped for faster entry.
    """

    item_lines: Annotated[Iterable[ItemLine], PropertyInfo(alias="itemLines")]
    """
    The bill's item lines, each representing the purchase of a specific item or
    service.
    """

    link_to_transaction_ids: Annotated[List[str], PropertyInfo(alias="linkToTransactionIds")]
    """
    IDs of existing transactions that you wish to link to this bill, such as
    payments applied, credits used, or associated purchase orders. Note that this
    links entire transactions, not individual transaction lines. If you want to link
    individual lines in a transaction, instead use the field `linkToTransactionLine`
    on this bill's lines, if available.

    You can use both `linkToTransactionIds` (on this bill) and
    `linkToTransactionLine` (on its transaction lines) as long as they do NOT link
    to the same transaction (otherwise, QuickBooks will return an error). QuickBooks
    will also return an error if you attempt to link a transaction that is empty or
    already closed.

    Note that QuickBooks will not return any information about these links in this
    endpoint's response even though they are created. To see the transactions linked
    via this field, refetch the bill and check the `linkedTransactions` field. If
    fetching a list of bills, you must also specify the parameter
    `includeLinkedTransactions` to return the `linkedTransactions` field.
    """

    memo: str
    """A memo or note for this bill, as entered by the user.

    Appears in the Accounts Payable register and relevant reports.
    """

    ref_number: Annotated[str, PropertyInfo(alias="refNumber")]
    """
    The case-sensitive user-defined reference number for this bill, which can be
    used to identify the transaction in QuickBooks. This value is not required to be
    unique and can be arbitrarily changed by the QuickBooks user.
    """

    sales_tax_code_id: Annotated[str, PropertyInfo(alias="salesTaxCodeId")]
    """
    The sales-tax code associated with this bill, determining whether it is taxable
    or non-taxable. It's used to assign a default tax status to all transactions for
    this bill. Default codes include "Non" (non-taxable) and "Tax" (taxable), but
    custom codes can also be created in QuickBooks. If QuickBooks is not set up to
    charge sales tax (via the "Do You Charge Sales Tax?" preference), it will assign
    the default non-taxable code to all sales.
    """

    terms_id: Annotated[str, PropertyInfo(alias="termsId")]
    """
    The bill's payment terms, defining when payment is due and any applicable
    discounts.
    """

    vendor_address: Annotated[VendorAddress, PropertyInfo(alias="vendorAddress")]
    """The address of the vendor who sent this bill."""


class ExpenseLineCustomField(TypedDict, total=False):
    name: Required[str]
    """The name of the custom field, unique for the specified `ownerId`.

    For public custom fields, this name is visible as a label in the QuickBooks UI.
    """

    owner_id: Required[Annotated[str, PropertyInfo(alias="ownerId")]]
    """
    The identifier of the owner of the custom field, which QuickBooks internally
    calls a "data extension". For public custom fields visible in the UI, such as
    those added by the QuickBooks user, this is always "0". For private custom
    fields that are only visible to the application that created them, this is a
    valid GUID identifying the owning application. Internally, Conductor always
    fetches all public custom fields (those with an `ownerId` of "0") for all
    objects.
    """

    value: Required[str]
    """The value of the custom field.

    The maximum length depends on the field's data type.
    """


class ExpenseLine(TypedDict, total=False):
    account_id: Annotated[str, PropertyInfo(alias="accountId")]
    """The expense account being debited (increased).

    The corresponding account being credited is usually a liability account (e.g.,
    Accounts Payable) or an asset account (e.g., Cash), depending on the transaction
    type.
    """

    amount: str
    """The monetary amount for this expense line, represented as a decimal string."""

    billing_status: Annotated[
        Literal["billable", "has_been_billed", "not_billable"], PropertyInfo(alias="billingStatus")
    ]
    """The billing status of this expense line."""

    class_id: Annotated[str, PropertyInfo(alias="classId")]
    """The expense line's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default. If a class is specified for the entire parent transaction, it is
    automatically applied to all expense lines unless overridden here, at the
    transaction line level.
    """

    custom_fields: Annotated[Iterable[ExpenseLineCustomField], PropertyInfo(alias="customFields")]
    """
    The custom fields for the expense line object, added as user-defined data
    extensions, not included in the standard QuickBooks object.
    """

    memo: str
    """A memo or note for this expense line, as entered by the user."""

    payee_id: Annotated[str, PropertyInfo(alias="payeeId")]
    """
    If `account` refers to an Accounts Payable (A/P) account, `payee` refers to the
    expense's vendor (not the customer). If `account` refers to any other type of
    account, `payee` refers to the expense's customer (not the vendor).
    """

    sales_representative_id: Annotated[str, PropertyInfo(alias="salesRepresentativeId")]
    """The expense line's sales representative.

    Sales representatives can be employees, vendors, or other names in QuickBooks.
    """

    sales_tax_code_id: Annotated[str, PropertyInfo(alias="salesTaxCodeId")]
    """
    The sales-tax code associated with this expense line, determining whether it is
    taxable or non-taxable. It's used to assign a default tax status to all
    transactions for this expense line. Default codes include "Non" (non-taxable)
    and "Tax" (taxable), but custom codes can also be created in QuickBooks. If
    QuickBooks is not set up to charge sales tax (via the "Do You Charge Sales Tax?"
    preference), it will assign the default non-taxable code to all sales.
    """


class ItemGroupLineCustomField(TypedDict, total=False):
    name: Required[str]
    """The name of the custom field, unique for the specified `ownerId`.

    For public custom fields, this name is visible as a label in the QuickBooks UI.
    """

    owner_id: Required[Annotated[str, PropertyInfo(alias="ownerId")]]
    """
    The identifier of the owner of the custom field, which QuickBooks internally
    calls a "data extension". For public custom fields visible in the UI, such as
    those added by the QuickBooks user, this is always "0". For private custom
    fields that are only visible to the application that created them, this is a
    valid GUID identifying the owning application. Internally, Conductor always
    fetches all public custom fields (those with an `ownerId` of "0") for all
    objects.
    """

    value: Required[str]
    """The value of the custom field.

    The maximum length depends on the field's data type.
    """


class ItemGroupLine(TypedDict, total=False):
    item_group_id: Required[Annotated[str, PropertyInfo(alias="itemGroupId")]]
    """
    The item group line's item group, representing a predefined set of items bundled
    because they are commonly purchased together or grouped for faster entry.
    """

    custom_fields: Annotated[Iterable[ItemGroupLineCustomField], PropertyInfo(alias="customFields")]
    """
    The custom fields for the item group line object, added as user-defined data
    extensions, not included in the standard QuickBooks object.
    """

    inventory_site_id: Annotated[str, PropertyInfo(alias="inventorySiteId")]
    """
    The site location where inventory for the item group in this item group line is
    stored.
    """

    inventory_site_location_id: Annotated[str, PropertyInfo(alias="inventorySiteLocationId")]
    """
    The specific location within the inventory site where the item group in this
    item group line is stored, such as a bin or shelf.
    """

    quantity: float
    """The quantity of the item in this item group line.

    If both `quantity` and `amount` are specified but not `rate`, QuickBooks will
    calculate `rate`. If `quantity` and `rate` are specified but not `amount`,
    QuickBooks will calculate `amount`.
    """

    unit_of_measure: Annotated[str, PropertyInfo(alias="unitOfMeasure")]
    """The unit of measure used for the `quantity` in this item group line.

    Must be a valid unit within the item's available units of measure.
    """


class ItemLineCustomField(TypedDict, total=False):
    name: Required[str]
    """The name of the custom field, unique for the specified `ownerId`.

    For public custom fields, this name is visible as a label in the QuickBooks UI.
    """

    owner_id: Required[Annotated[str, PropertyInfo(alias="ownerId")]]
    """
    The identifier of the owner of the custom field, which QuickBooks internally
    calls a "data extension". For public custom fields visible in the UI, such as
    those added by the QuickBooks user, this is always "0". For private custom
    fields that are only visible to the application that created them, this is a
    valid GUID identifying the owning application. Internally, Conductor always
    fetches all public custom fields (those with an `ownerId` of "0") for all
    objects.
    """

    value: Required[str]
    """The value of the custom field.

    The maximum length depends on the field's data type.
    """


class ItemLineLinkToTransactionLineItem(TypedDict, total=False):
    transaction_id: Required[Annotated[str, PropertyInfo(alias="transactionId")]]

    transaction_line_id: Required[Annotated[str, PropertyInfo(alias="transactionLineId")]]


class ItemLine(TypedDict, total=False):
    amount: str

    billable_status: Annotated[
        Literal["billable", "has_been_billed", "not_billable"], PropertyInfo(alias="billableStatus")
    ]
    """The billing status of this line item."""

    class_id: Annotated[str, PropertyInfo(alias="classId")]

    cost: str

    customer_id: Annotated[str, PropertyInfo(alias="customerId")]

    custom_fields: Annotated[Iterable[ItemLineCustomField], PropertyInfo(alias="customFields")]

    description: str

    expiration_date: Annotated[str, PropertyInfo(alias="expirationDate")]

    inventory_site_id: Annotated[str, PropertyInfo(alias="inventorySiteId")]
    """The ID of the inventory site where the item is stored."""

    inventory_site_location_id: Annotated[str, PropertyInfo(alias="inventorySiteLocationId")]
    """The ID of the inventory site location where the item is stored."""

    item_id: Annotated[str, PropertyInfo(alias="itemId")]

    link_to_transaction_line_item: Annotated[
        ItemLineLinkToTransactionLineItem, PropertyInfo(alias="linkToTransactionLineItem")
    ]

    lot_number: Annotated[str, PropertyInfo(alias="lotNumber")]

    override_item_account_id: Annotated[str, PropertyInfo(alias="overrideItemAccountId")]

    quantity: float

    sales_representative_id: Annotated[str, PropertyInfo(alias="salesRepresentativeId")]

    sales_tax_code_id: Annotated[str, PropertyInfo(alias="salesTaxCodeId")]

    serial_number: Annotated[str, PropertyInfo(alias="serialNumber")]
    """The serial number of the item."""

    unit_of_measure: Annotated[str, PropertyInfo(alias="unitOfMeasure")]


class VendorAddress(TypedDict, total=False):
    city: str
    """The city, district, suburb, town, or village name of the address."""

    country: str
    """The country name of the address."""

    line1: str
    """The first line of the address (e.g., street, PO Box, or company name)."""

    line2: str
    """
    The second line of the address, if needed (e.g., apartment, suite, unit, or
    building).
    """

    line3: str
    """The third line of the address, if needed."""

    line4: str
    """The fourth line of the address, if needed."""

    line5: str
    """The fifth line of the address, if needed."""

    note: str
    """A note about the address for additional context."""

    postal_code: Annotated[str, PropertyInfo(alias="postalCode")]
    """The postal code or ZIP code of the address."""

    state: str
    """The state, county, province, or region name of the address."""
