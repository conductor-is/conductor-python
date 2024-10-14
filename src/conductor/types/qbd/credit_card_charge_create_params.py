# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "CreditCardChargeCreateParams",
    "ExpenseLine",
    "ExpenseLineCustomField",
    "ItemGroupLine",
    "ItemGroupLineCustomField",
    "ItemLine",
    "ItemLineCustomField",
    "ItemLineLinkToTransactionLineItem",
]


class CreditCardChargeCreateParams(TypedDict, total=False):
    account_id: Required[Annotated[str, PropertyInfo(alias="accountId")]]
    """
    The bank account or credit card company to whom money is owed for this credit
    card charge.
    """

    transaction_date: Required[Annotated[Union[str, date], PropertyInfo(alias="transactionDate", format="iso8601")]]
    """The date of this credit card charge, in ISO 8601 format (YYYY-MM-DD)."""

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    exchange_rate: Annotated[float, PropertyInfo(alias="exchangeRate")]
    """
    The market exchange rate between this credit card charge's currency and the home
    currency in QuickBooks at the time of this transaction. Represented as a decimal
    value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).
    """

    expense_lines: Annotated[Iterable[ExpenseLine], PropertyInfo(alias="expenseLines")]
    """
    The credit card charge's expense lines, each representing one line in this
    expense.
    """

    external_id: Annotated[str, PropertyInfo(alias="externalId")]
    """
    A globally unique identifier (GUID) you can provide for tracking this object in
    your external system. Must be formatted as a valid GUID; otherwise, QuickBooks
    will return an error.
    """

    item_group_lines: Annotated[Iterable[ItemGroupLine], PropertyInfo(alias="itemGroupLines")]
    """
    The credit card charge's item-group lines, each representing a predefined group
    of items purchased together.
    """

    item_lines: Annotated[Iterable[ItemLine], PropertyInfo(alias="itemLines")]
    """
    The credit card charge's item lines, each representing the purchase of a
    specific item or service.
    """

    memo: str
    """A memo or note for this credit card charge, as entered by the user."""

    payee_id: Annotated[str, PropertyInfo(alias="payeeId")]
    """
    The vendor or company from whom merchandise or services were purchased for this
    credit card charge.
    """

    ref_number: Annotated[str, PropertyInfo(alias="refNumber")]
    """
    The case-sensitive user-defined reference number for this credit card charge,
    which can be used to identify the transaction in QuickBooks. This value is not
    required to be unique and can be arbitrarily changed by the QuickBooks user.
    """

    sales_tax_code_id: Annotated[str, PropertyInfo(alias="salesTaxCodeId")]
    """
    The sales-tax code associated with this credit card charge, determining whether
    it is taxable or non-taxable. It's used to assign a default tax status to all
    transactions for this credit card charge. Default codes include "Non"
    (non-taxable) and "Tax" (taxable), but custom codes can also be created in
    QuickBooks. If QuickBooks is not set up to charge sales tax (via the "Do You
    Charge Sales Tax?" preference), it will assign the default non-taxable code to
    all sales.
    """


class ExpenseLineCustomField(TypedDict, total=False):
    name: Required[str]

    owner_id: Required[Annotated[str, PropertyInfo(alias="ownerId")]]

    value: Required[str]


class ExpenseLine(TypedDict, total=False):
    account_id: Annotated[str, PropertyInfo(alias="accountId")]

    amount: str

    billable_status: Annotated[
        Literal["billable", "has_been_billed", "not_billable"], PropertyInfo(alias="billableStatus")
    ]
    """The billing status of this line item."""

    class_id: Annotated[str, PropertyInfo(alias="classId")]
    """The class associated with this object.

    Classes can be used to categorize objects or transactions by department,
    location, or other meaningful segments.
    """

    customer_id: Annotated[str, PropertyInfo(alias="customerId")]

    custom_fields: Annotated[Iterable[ExpenseLineCustomField], PropertyInfo(alias="customFields")]

    memo: str

    sales_representative_id: Annotated[str, PropertyInfo(alias="salesRepresentativeId")]

    sales_tax_code_id: Annotated[str, PropertyInfo(alias="salesTaxCodeId")]


class ItemGroupLineCustomField(TypedDict, total=False):
    name: Required[str]

    owner_id: Required[Annotated[str, PropertyInfo(alias="ownerId")]]

    value: Required[str]


class ItemGroupLine(TypedDict, total=False):
    item_group_id: Required[Annotated[str, PropertyInfo(alias="itemGroupId")]]

    custom_fields: Annotated[Iterable[ItemGroupLineCustomField], PropertyInfo(alias="customFields")]

    inventory_site_id: Annotated[str, PropertyInfo(alias="inventorySiteId")]

    inventory_site_location_id: Annotated[str, PropertyInfo(alias="inventorySiteLocationId")]

    quantity: float

    unit_of_measure: Annotated[str, PropertyInfo(alias="unitOfMeasure")]


class ItemLineCustomField(TypedDict, total=False):
    name: Required[str]

    owner_id: Required[Annotated[str, PropertyInfo(alias="ownerId")]]

    value: Required[str]


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
    """The class associated with this object.

    Classes can be used to categorize objects or transactions by department,
    location, or other meaningful segments.
    """

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
