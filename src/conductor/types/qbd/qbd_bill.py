# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "QbdBill",
    "AccountsPayableAccount",
    "Currency",
    "CustomField",
    "ExpenseLine",
    "ExpenseLineAccount",
    "ExpenseLineClass",
    "ExpenseLineCustomField",
    "ExpenseLinePayee",
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
    "ItemGroupLineItemOverrideUnitOfMeasureSet",
    "ItemGroupLineItemSalesRepresentative",
    "ItemGroupLineItemSalesTaxCode",
    "ItemLine",
    "ItemLineClass",
    "ItemLineCustomer",
    "ItemLineCustomField",
    "ItemLineInventorySite",
    "ItemLineInventorySiteLocation",
    "ItemLineItem",
    "ItemLineOverrideUnitOfMeasureSet",
    "ItemLineSalesRepresentative",
    "ItemLineSalesTaxCode",
    "LinkedTransaction",
    "SalesTaxCode",
    "Terms",
    "Vendor",
    "VendorAddress",
]


class AccountsPayableAccount(BaseModel):
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


class ExpenseLinePayee(BaseModel):
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

    billing_status: Optional[Literal["billable", "has_been_billed", "not_billable"]] = FieldInfo(
        alias="billingStatus", default=None
    )
    """The billing status of this expense line."""

    class_: Optional[ExpenseLineClass] = FieldInfo(alias="class", default=None)
    """The expense line's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default. If a class is specified for the entire parent transaction, it is
    automatically applied to all expense lines unless overridden here, at the
    transaction line level.
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

    payee: Optional[ExpenseLinePayee] = None
    """
    If `account` refers to an Accounts Payable (A/P) account, `payee` refers to the
    expense's vendor (not the customer). If `account` refers to any other type of
    account, `payee` refers to the expense's customer (not the vendor).
    """

    sales_representative: Optional[ExpenseLineSalesRepresentative] = FieldInfo(
        alias="salesRepresentative", default=None
    )
    """The expense line's sales representative.

    Sales representatives can be employees, vendors, or other names in QuickBooks.
    """

    sales_tax_code: Optional[ExpenseLineSalesTaxCode] = FieldInfo(alias="salesTaxCode", default=None)
    """
    The sales-tax code associated with this expense line, determining whether it is
    taxable or non-taxable. It's used to assign a default tax status to all
    transactions for this expense line. Default codes include "Non" (non-taxable)
    and "Tax" (taxable), but custom codes can also be created in QuickBooks. If
    QuickBooks is not set up to charge sales tax (via the "Do You Charge Sales Tax?"
    preference), it will assign the default non-taxable code to all sales.
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


class ItemGroupLineItemOverrideUnitOfMeasureSet(BaseModel):
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
    """The unique identifier assigned by QuickBooks for this item line.

    This ID is unique among all transaction line types.
    """

    amount: Optional[str] = None
    """The monetary amount for this item line, represented as a decimal string."""

    billing_status: Optional[Literal["billable", "has_been_billed", "not_billable"]] = FieldInfo(
        alias="billingStatus", default=None
    )
    """The billing status of this item line."""

    class_: Optional[ItemGroupLineItemClass] = FieldInfo(alias="class", default=None)
    """The item line's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default. If a class is specified for the entire parent transaction, it is
    automatically applied to all item lines unless overridden here, at the
    transaction line level.
    """

    cost: Optional[str] = None
    """The cost of this item line, represented as a decimal string.

    If both `quantity` and `amount` are specified, QuickBooks will use them to
    calculate `cost`. Likewise, if both `quantity` and `cost` are specified,
    QuickBooks will use them to calculate the `amount`.
    """

    customer: Optional[ItemGroupLineItemCustomer] = None
    """The customer or customer-job associated with this item line."""

    custom_fields: List[ItemGroupLineItemCustomField] = FieldInfo(alias="customFields")
    """The custom fields added by the user to this item line object as a data
    extension.

    These fields are not part of the standard QuickBooks object.
    """

    description: Optional[str] = None
    """A description of this item line."""

    expiration_date: Optional[date] = FieldInfo(alias="expirationDate", default=None)
    """
    The expiration date for the serial number or lot number of the item in this item
    line, in ISO 8601 format (YYYY-MM-DD). This is particularly relevant for
    perishable or time-sensitive inventory items. Note that this field is only
    supported on QuickBooks Desktop 2023 or later.
    """

    inventory_site: Optional[ItemGroupLineItemInventorySite] = FieldInfo(alias="inventorySite", default=None)
    """The site location where inventory for the item in this item line is stored."""

    inventory_site_location: Optional[ItemGroupLineItemInventorySiteLocation] = FieldInfo(
        alias="inventorySiteLocation", default=None
    )
    """
    The specific location within the inventory site where the item in this item line
    is stored, such as a bin or shelf.
    """

    item: Optional[ItemGroupLineItemItem] = None
    """The item associated with this item line.

    This can refer to any good or service that the business buys or sells, including
    item types such as a service item, inventory item, or special calculation item
    like a discount item or sales-tax item.
    """

    lot_number: Optional[str] = FieldInfo(alias="lotNumber", default=None)
    """The lot number of the item in this item line.

    Used for tracking groups of inventory items that are purchased or manufactured
    together.
    """

    object_type: Literal["qbd_item_line"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_item_line"`."""

    override_unit_of_measure_set: Optional[ItemGroupLineItemOverrideUnitOfMeasureSet] = FieldInfo(
        alias="overrideUnitOfMeasureSet", default=None
    )
    """Specifies an alternative unit of measure set for this specific item line.

    This does not change the item's default unit of measure set (which is set on the
    item itself rather than a transaction line), but allows selecting from a
    different set of units for this particular line. For example, an item typically
    measured in volume units could be sold using weight units in a specific
    transaction. The actual unit selection (e.g., "pound" or "kilogram") is made
    separately via the `unitOfMeasure` field.
    """

    quantity: Optional[float] = None
    """The quantity of the item in this item line.

    If both `quantity` and `amount` are specified but not `rate`, QuickBooks will
    calculate `rate`. If `quantity` and `rate` are specified but not `amount`,
    QuickBooks will calculate `amount`.
    """

    sales_representative: Optional[ItemGroupLineItemSalesRepresentative] = FieldInfo(
        alias="salesRepresentative", default=None
    )
    """The item line's sales representative.

    Sales representatives can be employees, vendors, or other names in QuickBooks.
    """

    sales_tax_code: Optional[ItemGroupLineItemSalesTaxCode] = FieldInfo(alias="salesTaxCode", default=None)
    """
    The sales-tax code associated with this item line, determining whether it is
    taxable or non-taxable. It's used to assign a default tax status to all
    transactions for this item line. Default codes include "Non" (non-taxable) and
    "Tax" (taxable), but custom codes can also be created in QuickBooks. If
    QuickBooks is not set up to charge sales tax (via the "Do You Charge Sales Tax?"
    preference), it will assign the default non-taxable code to all sales.
    """

    serial_number: Optional[str] = FieldInfo(alias="serialNumber", default=None)
    """The serial number of the item in this item line.

    This is used for tracking individual units of serialized inventory items.
    """

    unit_of_measure: Optional[str] = FieldInfo(alias="unitOfMeasure", default=None)
    """The unit of measure used for the `quantity` in this item line.

    Must be a valid unit within the item's available units of measure.
    """


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


class ItemLineOverrideUnitOfMeasureSet(BaseModel):
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
    """The unique identifier assigned by QuickBooks for this item line.

    This ID is unique among all transaction line types.
    """

    amount: Optional[str] = None
    """The monetary amount for this item line, represented as a decimal string."""

    billing_status: Optional[Literal["billable", "has_been_billed", "not_billable"]] = FieldInfo(
        alias="billingStatus", default=None
    )
    """The billing status of this item line."""

    class_: Optional[ItemLineClass] = FieldInfo(alias="class", default=None)
    """The item line's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default. If a class is specified for the entire parent transaction, it is
    automatically applied to all item lines unless overridden here, at the
    transaction line level.
    """

    cost: Optional[str] = None
    """The cost of this item line, represented as a decimal string.

    If both `quantity` and `amount` are specified, QuickBooks will use them to
    calculate `cost`. Likewise, if both `quantity` and `cost` are specified,
    QuickBooks will use them to calculate the `amount`.
    """

    customer: Optional[ItemLineCustomer] = None
    """The customer or customer-job associated with this item line."""

    custom_fields: List[ItemLineCustomField] = FieldInfo(alias="customFields")
    """The custom fields added by the user to this item line object as a data
    extension.

    These fields are not part of the standard QuickBooks object.
    """

    description: Optional[str] = None
    """A description of this item line."""

    expiration_date: Optional[date] = FieldInfo(alias="expirationDate", default=None)
    """
    The expiration date for the serial number or lot number of the item in this item
    line, in ISO 8601 format (YYYY-MM-DD). This is particularly relevant for
    perishable or time-sensitive inventory items. Note that this field is only
    supported on QuickBooks Desktop 2023 or later.
    """

    inventory_site: Optional[ItemLineInventorySite] = FieldInfo(alias="inventorySite", default=None)
    """The site location where inventory for the item in this item line is stored."""

    inventory_site_location: Optional[ItemLineInventorySiteLocation] = FieldInfo(
        alias="inventorySiteLocation", default=None
    )
    """
    The specific location within the inventory site where the item in this item line
    is stored, such as a bin or shelf.
    """

    item: Optional[ItemLineItem] = None
    """The item associated with this item line.

    This can refer to any good or service that the business buys or sells, including
    item types such as a service item, inventory item, or special calculation item
    like a discount item or sales-tax item.
    """

    lot_number: Optional[str] = FieldInfo(alias="lotNumber", default=None)
    """The lot number of the item in this item line.

    Used for tracking groups of inventory items that are purchased or manufactured
    together.
    """

    object_type: Literal["qbd_item_line"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_item_line"`."""

    override_unit_of_measure_set: Optional[ItemLineOverrideUnitOfMeasureSet] = FieldInfo(
        alias="overrideUnitOfMeasureSet", default=None
    )
    """Specifies an alternative unit of measure set for this specific item line.

    This does not change the item's default unit of measure set (which is set on the
    item itself rather than a transaction line), but allows selecting from a
    different set of units for this particular line. For example, an item typically
    measured in volume units could be sold using weight units in a specific
    transaction. The actual unit selection (e.g., "pound" or "kilogram") is made
    separately via the `unitOfMeasure` field.
    """

    quantity: Optional[float] = None
    """The quantity of the item in this item line.

    If both `quantity` and `amount` are specified but not `rate`, QuickBooks will
    calculate `rate`. If `quantity` and `rate` are specified but not `amount`,
    QuickBooks will calculate `amount`.
    """

    sales_representative: Optional[ItemLineSalesRepresentative] = FieldInfo(alias="salesRepresentative", default=None)
    """The item line's sales representative.

    Sales representatives can be employees, vendors, or other names in QuickBooks.
    """

    sales_tax_code: Optional[ItemLineSalesTaxCode] = FieldInfo(alias="salesTaxCode", default=None)
    """
    The sales-tax code associated with this item line, determining whether it is
    taxable or non-taxable. It's used to assign a default tax status to all
    transactions for this item line. Default codes include "Non" (non-taxable) and
    "Tax" (taxable), but custom codes can also be created in QuickBooks. If
    QuickBooks is not set up to charge sales tax (via the "Do You Charge Sales Tax?"
    preference), it will assign the default non-taxable code to all sales.
    """

    serial_number: Optional[str] = FieldInfo(alias="serialNumber", default=None)
    """The serial number of the item in this item line.

    This is used for tracking individual units of serialized inventory items.
    """

    unit_of_measure: Optional[str] = FieldInfo(alias="unitOfMeasure", default=None)
    """The unit of measure used for the `quantity` in this item line.

    Must be a valid unit within the item's available units of measure.
    """


class LinkedTransaction(BaseModel):
    id: str
    """
    The QuickBooks-assigned identifier for this transaction, unique across all
    transactions.
    """

    amount: str

    link_type: Optional[Literal["amount", "quantity"]] = FieldInfo(alias="linkType", default=None)
    """
    Indicates how transactions are linked: "amount" denotes an amount-based link
    (e.g., an invoice linked to a payment), and "quantity" denotes a quantity-based
    link (e.g., an invoice created from a sales order based on the quantity of items
    received).
    """

    ref_number: Optional[str] = FieldInfo(alias="refNumber", default=None)
    """The user-defined identifier for the transaction.

    It is not required to be unique and can be arbitrarily changed by the QuickBooks
    user. Case sensitive.
    """

    transaction_date: str = FieldInfo(alias="transactionDate")

    transaction_type: Literal[
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
    """The type of transaction."""


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


class Terms(BaseModel):
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


class Vendor(BaseModel):
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


class VendorAddress(BaseModel):
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
    """A note about the address for additional context."""

    postal_code: Optional[str] = FieldInfo(alias="postalCode", default=None)
    """The postal code or ZIP code of the address."""

    state: Optional[str] = None
    """The state, county, province, or region name of the address."""


class QbdBill(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks for this bill.

    This ID is unique among all transaction types.
    """

    accounts_payable_account: Optional[AccountsPayableAccount] = FieldInfo(alias="accountsPayableAccount", default=None)
    """
    The Accounts Payable account to which this bill is assigned, used to track the
    amount owed. If not specified, the default Accounts Payable account in
    QuickBooks is used.
    """

    amount_due: str = FieldInfo(alias="amountDue")
    """The total monetary amount due for this bill, represented as a decimal string.

    This equals the sum of the amounts in the bill's expense lines, item lines, and
    item group lines. It also equals `openAmount` plus any credits or discounts.
    """

    amount_due_in_home_currency: Optional[str] = FieldInfo(alias="amountDueInHomeCurrency", default=None)
    """
    The total amount due for this bill converted to the home currency of the
    QuickBooks company file. Represented as a decimal string.
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
    """The custom fields added by the user to this bill object as a data extension.

    These fields are not part of the standard QuickBooks object.
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
    your external system. Must be formatted as a valid GUID; otherwise, QuickBooks
    will return an error.
    """

    is_paid: Optional[bool] = FieldInfo(alias="isPaid", default=None)
    """Indicates whether this bill has been paid in full.

    If `true`, `openAmount` will be 0.
    """

    is_pending: Optional[bool] = FieldInfo(alias="isPending", default=None)
    """Indicates whether this bill is pending approval or completion.

    If `true`, the bill is in a draft state and has not been finalized.
    """

    item_group_lines: List[ItemGroupLine] = FieldInfo(alias="itemGroupLines")
    """
    The bill's item-group lines, each representing a predefined group of items
    purchased together.
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
    """

    memo: Optional[str] = None
    """A memo or note for this bill, as entered by the user.

    Appears in the Accounts Payable register and relevant reports.
    """

    object_type: Literal["qbd_bill"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_bill"`."""

    open_amount: Optional[str] = FieldInfo(alias="openAmount", default=None)
    """
    The remaining amount owed on this bill after subtracting any credits or
    discounts from the `openAmount`. Represented as a decimal string.
    """

    ref_number: Optional[str] = FieldInfo(alias="refNumber", default=None)
    """
    The case-sensitive user-defined reference number for this bill, which can be
    used to identify the transaction in QuickBooks. This value is not required to be
    unique and can be arbitrarily changed by the QuickBooks user.
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

    vendor_address: Optional[VendorAddress] = FieldInfo(alias="vendorAddress", default=None)
    """The address of the vendor who sent this bill."""

    version: str
    """
    The current version identifier for this bill, which changes each time the object
    is modified. When updating this object, you must provide the most recent
    `version` to ensure you're working with the latest data; otherwise, the update
    will fail. This value is opaque and should not be interpreted.
    """
