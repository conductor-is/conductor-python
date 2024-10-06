# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "QbdCreditCardCharge",
    "Account",
    "Currency",
    "CustomField",
    "ExpenseLine",
    "ExpenseLineAccount",
    "ExpenseLineClass",
    "ExpenseLineCustomer",
    "ExpenseLineCustomField",
    "ExpenseLineSalesRepresentative",
    "ExpenseLineSalesTaxCode",
    "ItemGroupLine",
    "ItemGroupLineCustomField",
    "ItemGroupLineItemGroup",
    "ItemGroupLineItem",
    "ItemGroupLineItemClass",
    "ItemGroupLineItemCustomer",
    "ItemGroupLineItemCustomField",
    "ItemGroupLineItemInventorySite",
    "ItemGroupLineItemInventorySiteLocation",
    "ItemGroupLineItemItem",
    "ItemGroupLineItemOverrideUnitOfMeasure",
    "ItemGroupLineItemSalesRepresentative",
    "ItemGroupLineItemSalesTaxCode",
    "ItemLine",
    "ItemLineClass",
    "ItemLineCustomer",
    "ItemLineCustomField",
    "ItemLineInventorySite",
    "ItemLineInventorySiteLocation",
    "ItemLineItem",
    "ItemLineOverrideUnitOfMeasure",
    "ItemLineSalesRepresentative",
    "ItemLineSalesTaxCode",
    "Payee",
    "SalesTaxCode",
]


class Account(BaseModel):
    id: Optional[str] = None
    """The unique identifier assigned by QuickBooks for this object.

    This ID is unique among all objects of the same type, but not across different
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
    """The unique identifier assigned by QuickBooks for this object.

    This ID is unique among all objects of the same type, but not across different
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

    owner_id: Optional[str] = FieldInfo(alias="ownerId", default=None)

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
    """The custom field's data type, which corresponds to a QuickBooks data type."""

    value: str


class ExpenseLineAccount(BaseModel):
    id: Optional[str] = None
    """The unique identifier assigned by QuickBooks for this object.

    This ID is unique among all objects of the same type, but not across different
    QuickBooks object types.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The fully-qualified unique name for this object, formed by combining the names
    of its parent objects with its own `name`, separated by colons. Not
    case-sensitive.
    """


class ExpenseLineClass(BaseModel):
    id: Optional[str] = None
    """The unique identifier assigned by QuickBooks for this object.

    This ID is unique among all objects of the same type, but not across different
    QuickBooks object types.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The fully-qualified unique name for this object, formed by combining the names
    of its parent objects with its own `name`, separated by colons. Not
    case-sensitive.
    """


class ExpenseLineCustomer(BaseModel):
    id: Optional[str] = None
    """The unique identifier assigned by QuickBooks for this object.

    This ID is unique among all objects of the same type, but not across different
    QuickBooks object types.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The fully-qualified unique name for this object, formed by combining the names
    of its parent objects with its own `name`, separated by colons. Not
    case-sensitive.
    """


class ExpenseLineCustomField(BaseModel):
    name: str

    owner_id: Optional[str] = FieldInfo(alias="ownerId", default=None)

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
    """The custom field's data type, which corresponds to a QuickBooks data type."""

    value: str


class ExpenseLineSalesRepresentative(BaseModel):
    id: Optional[str] = None
    """The unique identifier assigned by QuickBooks for this object.

    This ID is unique among all objects of the same type, but not across different
    QuickBooks object types.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The fully-qualified unique name for this object, formed by combining the names
    of its parent objects with its own `name`, separated by colons. Not
    case-sensitive.
    """


class ExpenseLineSalesTaxCode(BaseModel):
    id: Optional[str] = None
    """The unique identifier assigned by QuickBooks for this object.

    This ID is unique among all objects of the same type, but not across different
    QuickBooks object types.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The fully-qualified unique name for this object, formed by combining the names
    of its parent objects with its own `name`, separated by colons. Not
    case-sensitive.
    """


class ExpenseLine(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks for this expense line.

    This ID is unique among all transaction line types.
    """

    account: Optional[ExpenseLineAccount] = None
    """
    For expense lines, this typically refers to the expense account being debited
    (increased). The corresponding credit would usually be to a liability account
    (e.g., Accounts Payable) or an asset account (e.g., Cash), depending on the
    transaction type.
    """

    amount: Optional[str] = None
    """The monetary amount for this expense line, represented as a decimal string."""

    billable_status: Optional[Literal["billable", "has_been_billed", "not_billable"]] = FieldInfo(
        alias="billableStatus", default=None
    )
    """The billing status of this expense line."""

    class_: Optional[ExpenseLineClass] = FieldInfo(alias="class", default=None)
    """
    The expense line's class, used for categorization (e.g., by department,
    location, or type of work).
    """

    customer: Optional[ExpenseLineCustomer] = None
    """
    For expense lines, if `account` refers to an Accounts Payable (A/P) account,
    `customer` refers to the expense's vendor (not the customer). If `account`
    refers to any other type of account, `customer` refers to the expense's customer
    (not the vendor).
    """

    custom_fields: List[ExpenseLineCustomField] = FieldInfo(alias="customFields")
    """
    The custom fields added by the user to this expense line object as a data
    extension. These fields are not part of the standard QuickBooks object.
    """

    memo: Optional[str] = None
    """A memo or note for this expense line, as entered by the user."""

    object_type: Literal["qbd_expense_line"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_expense_line"`."""

    sales_representative: Optional[ExpenseLineSalesRepresentative] = FieldInfo(
        alias="salesRepresentative", default=None
    )
    """The expense line's sales representative.

    Sales representatives can be employees, vendors, or other names in QuickBooks.
    """

    sales_tax_code: Optional[ExpenseLineSalesTaxCode] = FieldInfo(alias="salesTaxCode", default=None)
    """
    The sales tax code associated with this expense line, determining whether it is
    taxable or non-taxable. It's used to assign a default tax status to all
    transactions for this expense line. Default codes include 'NON' (non-taxable)
    and 'TAX' (taxable), but custom codes can also be created in QuickBooks. If
    QuickBooks is not set up to charge sales tax, it will assign the default
    non-taxable code to all sales.
    """


class ItemGroupLineCustomField(BaseModel):
    name: str

    owner_id: Optional[str] = FieldInfo(alias="ownerId", default=None)

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
    """The custom field's data type, which corresponds to a QuickBooks data type."""

    value: str


class ItemGroupLineItemGroup(BaseModel):
    id: Optional[str] = None
    """The unique identifier assigned by QuickBooks for this object.

    This ID is unique among all objects of the same type, but not across different
    QuickBooks object types.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The fully-qualified unique name for this object, formed by combining the names
    of its parent objects with its own `name`, separated by colons. Not
    case-sensitive.
    """


class ItemGroupLineItemClass(BaseModel):
    id: Optional[str] = None
    """The unique identifier assigned by QuickBooks for this object.

    This ID is unique among all objects of the same type, but not across different
    QuickBooks object types.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The fully-qualified unique name for this object, formed by combining the names
    of its parent objects with its own `name`, separated by colons. Not
    case-sensitive.
    """


class ItemGroupLineItemCustomer(BaseModel):
    id: Optional[str] = None
    """The unique identifier assigned by QuickBooks for this object.

    This ID is unique among all objects of the same type, but not across different
    QuickBooks object types.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The fully-qualified unique name for this object, formed by combining the names
    of its parent objects with its own `name`, separated by colons. Not
    case-sensitive.
    """


class ItemGroupLineItemCustomField(BaseModel):
    name: str

    owner_id: Optional[str] = FieldInfo(alias="ownerId", default=None)

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
    """The custom field's data type, which corresponds to a QuickBooks data type."""

    value: str


class ItemGroupLineItemInventorySite(BaseModel):
    id: Optional[str] = None
    """The unique identifier assigned by QuickBooks for this object.

    This ID is unique among all objects of the same type, but not across different
    QuickBooks object types.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The fully-qualified unique name for this object, formed by combining the names
    of its parent objects with its own `name`, separated by colons. Not
    case-sensitive.
    """


class ItemGroupLineItemInventorySiteLocation(BaseModel):
    id: Optional[str] = None
    """The unique identifier assigned by QuickBooks for this object.

    This ID is unique among all objects of the same type, but not across different
    QuickBooks object types.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The fully-qualified unique name for this object, formed by combining the names
    of its parent objects with its own `name`, separated by colons. Not
    case-sensitive.
    """


class ItemGroupLineItemItem(BaseModel):
    id: Optional[str] = None
    """The unique identifier assigned by QuickBooks for this object.

    This ID is unique among all objects of the same type, but not across different
    QuickBooks object types.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The fully-qualified unique name for this object, formed by combining the names
    of its parent objects with its own `name`, separated by colons. Not
    case-sensitive.
    """


class ItemGroupLineItemOverrideUnitOfMeasure(BaseModel):
    id: Optional[str] = None
    """The unique identifier assigned by QuickBooks for this object.

    This ID is unique among all objects of the same type, but not across different
    QuickBooks object types.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The fully-qualified unique name for this object, formed by combining the names
    of its parent objects with its own `name`, separated by colons. Not
    case-sensitive.
    """


class ItemGroupLineItemSalesRepresentative(BaseModel):
    id: Optional[str] = None
    """The unique identifier assigned by QuickBooks for this object.

    This ID is unique among all objects of the same type, but not across different
    QuickBooks object types.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The fully-qualified unique name for this object, formed by combining the names
    of its parent objects with its own `name`, separated by colons. Not
    case-sensitive.
    """


class ItemGroupLineItemSalesTaxCode(BaseModel):
    id: Optional[str] = None
    """The unique identifier assigned by QuickBooks for this object.

    This ID is unique among all objects of the same type, but not across different
    QuickBooks object types.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The fully-qualified unique name for this object, formed by combining the names
    of its parent objects with its own `name`, separated by colons. Not
    case-sensitive.
    """


class ItemGroupLineItem(BaseModel):
    id: str
    """
    The QuickBooks-assigned identifier for this transaction line, unique across all
    transaction lines.
    """

    amount: Optional[str] = None

    billable_status: Optional[Literal["billable", "has_been_billed", "not_billable"]] = FieldInfo(
        alias="billableStatus", default=None
    )
    """The billable status of this line item."""

    class_: Optional[ItemGroupLineItemClass] = FieldInfo(alias="class", default=None)
    """The class associated with this object.

    Classes can be used to categorize objects or transactions by department,
    location, or other meaningful segments.
    """

    cost: Optional[str] = None

    customer: Optional[ItemGroupLineItemCustomer] = None

    custom_fields: List[ItemGroupLineItemCustomField] = FieldInfo(alias="customFields")
    """The custom fields added by the user to QuickBooks object as a data extension.

    These fields are not part of the standard QuickBooks object.
    """

    description: Optional[str] = None

    inventory_site: Optional[ItemGroupLineItemInventorySite] = FieldInfo(alias="inventorySite", default=None)
    """The inventory site location where the item is stored."""

    inventory_site_location: Optional[ItemGroupLineItemInventorySiteLocation] = FieldInfo(
        alias="inventorySiteLocation", default=None
    )
    """The location within the inventory site where the item is stored."""

    item: Optional[ItemGroupLineItemItem] = None

    lot_number: Optional[str] = FieldInfo(alias="lotNumber", default=None)

    override_unit_of_measure: Optional[ItemGroupLineItemOverrideUnitOfMeasure] = FieldInfo(
        alias="overrideUnitOfMeasure", default=None
    )

    quantity: Optional[float] = None

    sales_representative: Optional[ItemGroupLineItemSalesRepresentative] = FieldInfo(
        alias="salesRepresentative", default=None
    )
    """The item's sales representative."""

    sales_tax_code: Optional[ItemGroupLineItemSalesTaxCode] = FieldInfo(alias="salesTaxCode", default=None)
    """The sales tax code, indicating whether related items are taxable or non-taxable.

    Two default codes are 'Non' (non-taxable) and 'Tax' (taxable). If QuickBooks is
    not set up to charge sales tax, it will assign the default non-taxable code to
    all sales.
    """

    serial_number: Optional[str] = FieldInfo(alias="serialNumber", default=None)
    """The serial number of the item."""

    unit_of_measure: Optional[str] = FieldInfo(alias="unitOfMeasure", default=None)


class ItemGroupLine(BaseModel):
    id: str
    """
    The QuickBooks-assigned identifier for this transaction line, unique across all
    transaction lines.
    """

    custom_fields: List[ItemGroupLineCustomField] = FieldInfo(alias="customFields")
    """The custom fields added by the user to QuickBooks object as a data extension.

    These fields are not part of the standard QuickBooks object.
    """

    description: Optional[str] = None

    item_group: ItemGroupLineItemGroup = FieldInfo(alias="itemGroup")

    items: List[ItemGroupLineItem]

    quantity: Optional[float] = None

    total_amount: str = FieldInfo(alias="totalAmount")

    unit_of_measure: Optional[str] = FieldInfo(alias="unitOfMeasure", default=None)


class ItemLineClass(BaseModel):
    id: Optional[str] = None
    """The unique identifier assigned by QuickBooks for this object.

    This ID is unique among all objects of the same type, but not across different
    QuickBooks object types.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The fully-qualified unique name for this object, formed by combining the names
    of its parent objects with its own `name`, separated by colons. Not
    case-sensitive.
    """


class ItemLineCustomer(BaseModel):
    id: Optional[str] = None
    """The unique identifier assigned by QuickBooks for this object.

    This ID is unique among all objects of the same type, but not across different
    QuickBooks object types.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The fully-qualified unique name for this object, formed by combining the names
    of its parent objects with its own `name`, separated by colons. Not
    case-sensitive.
    """


class ItemLineCustomField(BaseModel):
    name: str

    owner_id: Optional[str] = FieldInfo(alias="ownerId", default=None)

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
    """The custom field's data type, which corresponds to a QuickBooks data type."""

    value: str


class ItemLineInventorySite(BaseModel):
    id: Optional[str] = None
    """The unique identifier assigned by QuickBooks for this object.

    This ID is unique among all objects of the same type, but not across different
    QuickBooks object types.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The fully-qualified unique name for this object, formed by combining the names
    of its parent objects with its own `name`, separated by colons. Not
    case-sensitive.
    """


class ItemLineInventorySiteLocation(BaseModel):
    id: Optional[str] = None
    """The unique identifier assigned by QuickBooks for this object.

    This ID is unique among all objects of the same type, but not across different
    QuickBooks object types.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The fully-qualified unique name for this object, formed by combining the names
    of its parent objects with its own `name`, separated by colons. Not
    case-sensitive.
    """


class ItemLineItem(BaseModel):
    id: Optional[str] = None
    """The unique identifier assigned by QuickBooks for this object.

    This ID is unique among all objects of the same type, but not across different
    QuickBooks object types.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The fully-qualified unique name for this object, formed by combining the names
    of its parent objects with its own `name`, separated by colons. Not
    case-sensitive.
    """


class ItemLineOverrideUnitOfMeasure(BaseModel):
    id: Optional[str] = None
    """The unique identifier assigned by QuickBooks for this object.

    This ID is unique among all objects of the same type, but not across different
    QuickBooks object types.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The fully-qualified unique name for this object, formed by combining the names
    of its parent objects with its own `name`, separated by colons. Not
    case-sensitive.
    """


class ItemLineSalesRepresentative(BaseModel):
    id: Optional[str] = None
    """The unique identifier assigned by QuickBooks for this object.

    This ID is unique among all objects of the same type, but not across different
    QuickBooks object types.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The fully-qualified unique name for this object, formed by combining the names
    of its parent objects with its own `name`, separated by colons. Not
    case-sensitive.
    """


class ItemLineSalesTaxCode(BaseModel):
    id: Optional[str] = None
    """The unique identifier assigned by QuickBooks for this object.

    This ID is unique among all objects of the same type, but not across different
    QuickBooks object types.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The fully-qualified unique name for this object, formed by combining the names
    of its parent objects with its own `name`, separated by colons. Not
    case-sensitive.
    """


class ItemLine(BaseModel):
    id: str
    """
    The QuickBooks-assigned identifier for this transaction line, unique across all
    transaction lines.
    """

    amount: Optional[str] = None

    billable_status: Optional[Literal["billable", "has_been_billed", "not_billable"]] = FieldInfo(
        alias="billableStatus", default=None
    )
    """The billable status of this line item."""

    class_: Optional[ItemLineClass] = FieldInfo(alias="class", default=None)
    """The class associated with this object.

    Classes can be used to categorize objects or transactions by department,
    location, or other meaningful segments.
    """

    cost: Optional[str] = None

    customer: Optional[ItemLineCustomer] = None

    custom_fields: List[ItemLineCustomField] = FieldInfo(alias="customFields")
    """The custom fields added by the user to QuickBooks object as a data extension.

    These fields are not part of the standard QuickBooks object.
    """

    description: Optional[str] = None

    inventory_site: Optional[ItemLineInventorySite] = FieldInfo(alias="inventorySite", default=None)
    """The inventory site location where the item is stored."""

    inventory_site_location: Optional[ItemLineInventorySiteLocation] = FieldInfo(
        alias="inventorySiteLocation", default=None
    )
    """The location within the inventory site where the item is stored."""

    item: Optional[ItemLineItem] = None

    lot_number: Optional[str] = FieldInfo(alias="lotNumber", default=None)

    override_unit_of_measure: Optional[ItemLineOverrideUnitOfMeasure] = FieldInfo(
        alias="overrideUnitOfMeasure", default=None
    )

    quantity: Optional[float] = None

    sales_representative: Optional[ItemLineSalesRepresentative] = FieldInfo(alias="salesRepresentative", default=None)
    """The item's sales representative."""

    sales_tax_code: Optional[ItemLineSalesTaxCode] = FieldInfo(alias="salesTaxCode", default=None)
    """The sales tax code, indicating whether related items are taxable or non-taxable.

    Two default codes are 'Non' (non-taxable) and 'Tax' (taxable). If QuickBooks is
    not set up to charge sales tax, it will assign the default non-taxable code to
    all sales.
    """

    serial_number: Optional[str] = FieldInfo(alias="serialNumber", default=None)
    """The serial number of the item."""

    unit_of_measure: Optional[str] = FieldInfo(alias="unitOfMeasure", default=None)


class Payee(BaseModel):
    id: Optional[str] = None
    """The unique identifier assigned by QuickBooks for this object.

    This ID is unique among all objects of the same type, but not across different
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
    """The unique identifier assigned by QuickBooks for this object.

    This ID is unique among all objects of the same type, but not across different
    QuickBooks object types.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The fully-qualified unique name for this object, formed by combining the names
    of its parent objects with its own `name`, separated by colons. Not
    case-sensitive.
    """


class QbdCreditCardCharge(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks for this credit card charge.

    This ID is unique among all transaction types.
    """

    account: Account
    """
    The bank account or credit card company to whom money is owed for this credit
    card charge.
    """

    amount: str
    """
    The total monetary amount for this credit card charge, represented as a decimal
    string. This equals the sum of the amounts in the credit card charge's expense
    lines, item lines, and item group lines.
    """

    amount_in_home_currency: Optional[str] = FieldInfo(alias="amountInHomeCurrency", default=None)
    """
    The total amount for this credit card charge converted to the home currency of
    the QuickBooks company file. Represented as a decimal string.
    """

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when this credit card charge was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """

    currency: Optional[Currency] = None
    """The credit card charge's currency.

    For built-in currencies, the name and code are standard international values.
    For user-defined currencies, all values are editable.
    """

    custom_fields: List[CustomField] = FieldInfo(alias="customFields")
    """
    The custom fields added by the user to this credit card charge object as a data
    extension. These fields are not part of the standard QuickBooks object.
    """

    exchange_rate: Optional[float] = FieldInfo(alias="exchangeRate", default=None)
    """
    The market exchange rate between this credit card charge's currency and the home
    currency in QuickBooks at the time of this transaction. Represented as a decimal
    value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).
    """

    expense_lines: List[ExpenseLine] = FieldInfo(alias="expenseLines")
    """
    The credit card charge's expense lines, each representing an expense item or
    account affected by this transaction.
    """

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """
    A developer-assigned globally unique identifier (GUID) for tracking this object
    in external systems. Must be formatted as a valid GUID; otherwise, QuickBooks
    will return an error.
    """

    item_group_lines: List[ItemGroupLine] = FieldInfo(alias="itemGroupLines")
    """
    The credit card charge's item-group lines, each representing a predefined group
    of items purchased together.
    """

    item_lines: List[ItemLine] = FieldInfo(alias="itemLines")
    """
    The credit card charge's item lines, each representing the purchase of a
    specific item or service.
    """

    memo: Optional[str] = None
    """A memo or note for this credit card charge, as entered by the user."""

    object_type: Literal["qbd_credit_card_charge"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_credit_card_charge"`."""

    payee: Optional[Payee] = None
    """
    The vendor or company from whom merchandise or services were purchased for this
    credit card charge.
    """

    ref_number: Optional[str] = FieldInfo(alias="refNumber", default=None)
    """
    The user-defined reference number for this credit card charge, which can be used
    to identify the transaction in QuickBooks. This value is not required to be
    unique and can be arbitrarily changed by the QuickBooks user.
    """

    sales_tax_code: Optional[SalesTaxCode] = FieldInfo(alias="salesTaxCode", default=None)
    """
    The sales tax code associated with this credit card charge, determining whether
    it is taxable or non-taxable. It's used to assign a default tax status to all
    transactions for this credit card charge. Default codes include 'NON'
    (non-taxable) and 'TAX' (taxable), but custom codes can also be created in
    QuickBooks. If QuickBooks is not set up to charge sales tax, it will assign the
    default non-taxable code to all sales.
    """

    transaction_date: date = FieldInfo(alias="transactionDate")
    """The date of this credit card charge, in ISO 8601 format (YYYY-MM-DD)."""

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when this credit card charge was last updated, in ISO 8601
    format (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time
    zone in QuickBooks.
    """

    version: str
    """
    The current version identifier for this credit card charge, which changes each
    time the object is modified. When updating this object, you must provide the
    most recent `version` to ensure you're working with the latest data; otherwise,
    the update will fail. This value is opaque and should not be interpreted.
    """
