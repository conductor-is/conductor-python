# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "Check",
    "Address",
    "BankAccount",
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
    "ItemGroupLineItemLine",
    "ItemGroupLineItemLineClass",
    "ItemGroupLineItemLineCustomer",
    "ItemGroupLineItemLineCustomField",
    "ItemGroupLineItemLineInventorySite",
    "ItemGroupLineItemLineInventorySiteLocation",
    "ItemGroupLineItemLineItem",
    "ItemGroupLineItemLineOverrideUnitOfMeasureSet",
    "ItemGroupLineItemLineSalesRepresentative",
    "ItemGroupLineItemLineSalesTaxCode",
    "ItemGroupLineOverrideUnitOfMeasureSet",
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
    "Payee",
    "SalesTaxCode",
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


class ExpenseLineAccount(BaseModel):
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


class ExpenseLineClass(BaseModel):
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


class ExpenseLineCustomField(BaseModel):
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


class ExpenseLinePayee(BaseModel):
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


class ExpenseLineSalesRepresentative(BaseModel):
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


class ExpenseLineSalesTaxCode(BaseModel):
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


class ExpenseLine(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks to this expense line.

    This ID is unique across all transaction line types.
    """

    account: Optional[ExpenseLineAccount] = None
    """The expense account being debited (increased).

    The corresponding account being credited is usually a liability account (e.g.,
    Accounts-Payable) or an asset account (e.g., Cash), depending on the transaction
    type.
    """

    amount: Optional[str] = None
    """The monetary amount of this expense line, represented as a decimal string."""

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
    The custom fields for the expense line object, added as user-defined data
    extensions, not included in the standard QuickBooks object.
    """

    memo: Optional[str] = None
    """A memo or note for this expense line."""

    object_type: Literal["qbd_expense_line"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_expense_line"`."""

    payee: Optional[ExpenseLinePayee] = None
    """
    If `account` refers to an Accounts-Payable (A/P) account, `payee` refers to the
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


class ItemGroupLineItemGroup(BaseModel):
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


class ItemGroupLineItemLineClass(BaseModel):
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


class ItemGroupLineItemLineCustomer(BaseModel):
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


class ItemGroupLineItemLineCustomField(BaseModel):
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


class ItemGroupLineItemLineInventorySite(BaseModel):
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


class ItemGroupLineItemLineInventorySiteLocation(BaseModel):
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


class ItemGroupLineItemLineItem(BaseModel):
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


class ItemGroupLineItemLineOverrideUnitOfMeasureSet(BaseModel):
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


class ItemGroupLineItemLineSalesRepresentative(BaseModel):
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


class ItemGroupLineItemLineSalesTaxCode(BaseModel):
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


class ItemGroupLineItemLine(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks to this item line.

    This ID is unique across all transaction line types.
    """

    amount: Optional[str] = None
    """The monetary amount of this item line, represented as a decimal string.

    If both `quantity` and `cost` are specified but not `amount`, QuickBooks will
    use them to calculate `amount`. If `amount`, `cost`, and `quantity` are all
    unspecified, then QuickBooks will calculate `amount` based on a `quantity` of
    `1` and the suggested `cost`.
    """

    billing_status: Optional[Literal["billable", "has_been_billed", "not_billable"]] = FieldInfo(
        alias="billingStatus", default=None
    )
    """The billing status of this item line."""

    class_: Optional[ItemGroupLineItemLineClass] = FieldInfo(alias="class", default=None)
    """The item line's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default. If a class is specified for the entire parent transaction, it is
    automatically applied to all item lines unless overridden here, at the
    transaction line level.
    """

    cost: Optional[str] = None
    """The cost of this item line, represented as a decimal string.

    If both `quantity` and `amount` are specified but not `cost`, QuickBooks will
    use them to calculate `cost`.
    """

    customer: Optional[ItemGroupLineItemLineCustomer] = None
    """The customer or customer-job associated with this item line."""

    custom_fields: List[ItemGroupLineItemLineCustomField] = FieldInfo(alias="customFields")
    """
    The custom fields for the item line object, added as user-defined data
    extensions, not included in the standard QuickBooks object.
    """

    description: Optional[str] = None
    """A description of this item line."""

    expiration_date: Optional[date] = FieldInfo(alias="expirationDate", default=None)
    """
    The expiration date for the serial number or lot number of the item associated
    with this item line, in ISO 8601 format (YYYY-MM-DD). This is particularly
    relevant for perishable or time-sensitive inventory items. Note that this field
    is only supported on QuickBooks Desktop 2023 or later.
    """

    inventory_site: Optional[ItemGroupLineItemLineInventorySite] = FieldInfo(alias="inventorySite", default=None)
    """
    The site location where inventory for the item associated with this item line is
    stored.
    """

    inventory_site_location: Optional[ItemGroupLineItemLineInventorySiteLocation] = FieldInfo(
        alias="inventorySiteLocation", default=None
    )
    """
    The specific location (e.g., bin or shelf) within the inventory site where the
    item associated with this item line is stored.
    """

    item: Optional[ItemGroupLineItemLineItem] = None
    """The item associated with this item line.

    This can refer to any good or service that the business buys or sells, including
    item types such as a service item, inventory item, or special calculation item
    like a discount item or sales-tax item.
    """

    lot_number: Optional[str] = FieldInfo(alias="lotNumber", default=None)
    """The lot number of the item associated with this item line.

    Used for tracking groups of inventory items that are purchased or manufactured
    together.
    """

    object_type: Literal["qbd_item_line"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_item_line"`."""

    override_unit_of_measure_set: Optional[ItemGroupLineItemLineOverrideUnitOfMeasureSet] = FieldInfo(
        alias="overrideUnitOfMeasureSet", default=None
    )
    """
    Specifies an alternative unit-of-measure set when updating this item line's
    `unitOfMeasure` field (e.g., "pound" or "kilogram"). This allows you to select
    units from a different set than the item's default unit-of-measure set, which
    remains unchanged on the item itself. The override applies only to this specific
    line. For example, you can sell an item typically measured in volume units using
    weight units in a specific transaction by specifying a different unit-of-measure
    set with this field.
    """

    quantity: Optional[float] = None
    """The quantity of the item associated with this item line."""

    sales_representative: Optional[ItemGroupLineItemLineSalesRepresentative] = FieldInfo(
        alias="salesRepresentative", default=None
    )
    """The item line's sales representative.

    Sales representatives can be employees, vendors, or other names in QuickBooks.
    """

    sales_tax_code: Optional[ItemGroupLineItemLineSalesTaxCode] = FieldInfo(alias="salesTaxCode", default=None)
    """
    The sales-tax code associated with this item line, determining whether it is
    taxable or non-taxable. It's used to assign a default tax status to all
    transactions for this item line. Default codes include "Non" (non-taxable) and
    "Tax" (taxable), but custom codes can also be created in QuickBooks. If
    QuickBooks is not set up to charge sales tax (via the "Do You Charge Sales Tax?"
    preference), it will assign the default non-taxable code to all sales.
    """

    serial_number: Optional[str] = FieldInfo(alias="serialNumber", default=None)
    """The serial number of the item associated with this item line.

    This is used for tracking individual units of serialized inventory items.
    """

    unit_of_measure: Optional[str] = FieldInfo(alias="unitOfMeasure", default=None)
    """The unit-of-measure used for the `quantity` in this item line.

    Must be a valid unit within the item's available units of measure.
    """


class ItemGroupLineOverrideUnitOfMeasureSet(BaseModel):
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


class ItemGroupLine(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks to this item group line.

    This ID is unique across all transaction line types.
    """

    custom_fields: List[ItemGroupLineCustomField] = FieldInfo(alias="customFields")
    """
    The custom fields for the item group line object, added as user-defined data
    extensions, not included in the standard QuickBooks object.
    """

    description: Optional[str] = None
    """A description of this item group line."""

    item_group: ItemGroupLineItemGroup = FieldInfo(alias="itemGroup")
    """
    The item group line's item group, representing a predefined set of items bundled
    because they are commonly purchased together or grouped for faster entry.
    """

    item_lines: List[ItemGroupLineItemLine] = FieldInfo(alias="itemLines")
    """
    The item group line's item lines, each representing the purchase of a specific
    item or service.
    """

    object_type: Literal["qbd_item_group_line"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_item_group_line"`."""

    override_unit_of_measure_set: Optional[ItemGroupLineOverrideUnitOfMeasureSet] = FieldInfo(
        alias="overrideUnitOfMeasureSet", default=None
    )
    """
    Specifies an alternative unit-of-measure set when updating this item group
    line's `unitOfMeasure` field (e.g., "pound" or "kilogram"). This allows you to
    select units from a different set than the item's default unit-of-measure set,
    which remains unchanged on the item itself. The override applies only to this
    specific line. For example, you can sell an item typically measured in volume
    units using weight units in a specific transaction by specifying a different
    unit-of-measure set with this field.
    """

    quantity: Optional[float] = None
    """The quantity of the item group associated with this item group line."""

    total_amount: str = FieldInfo(alias="totalAmount")
    """
    The total monetary amount of this item group line, represented as a decimal
    string.
    """

    unit_of_measure: Optional[str] = FieldInfo(alias="unitOfMeasure", default=None)
    """The unit-of-measure used for the `quantity` in this item group line.

    Must be a valid unit within the item's available units of measure.
    """


class ItemLineClass(BaseModel):
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


class ItemLineCustomer(BaseModel):
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


class ItemLineCustomField(BaseModel):
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


class ItemLineInventorySite(BaseModel):
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


class ItemLineInventorySiteLocation(BaseModel):
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


class ItemLineItem(BaseModel):
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


class ItemLineOverrideUnitOfMeasureSet(BaseModel):
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


class ItemLineSalesRepresentative(BaseModel):
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


class ItemLineSalesTaxCode(BaseModel):
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


class ItemLine(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks to this item line.

    This ID is unique across all transaction line types.
    """

    amount: Optional[str] = None
    """The monetary amount of this item line, represented as a decimal string.

    If both `quantity` and `cost` are specified but not `amount`, QuickBooks will
    use them to calculate `amount`. If `amount`, `cost`, and `quantity` are all
    unspecified, then QuickBooks will calculate `amount` based on a `quantity` of
    `1` and the suggested `cost`.
    """

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

    If both `quantity` and `amount` are specified but not `cost`, QuickBooks will
    use them to calculate `cost`.
    """

    customer: Optional[ItemLineCustomer] = None
    """The customer or customer-job associated with this item line."""

    custom_fields: List[ItemLineCustomField] = FieldInfo(alias="customFields")
    """
    The custom fields for the item line object, added as user-defined data
    extensions, not included in the standard QuickBooks object.
    """

    description: Optional[str] = None
    """A description of this item line."""

    expiration_date: Optional[date] = FieldInfo(alias="expirationDate", default=None)
    """
    The expiration date for the serial number or lot number of the item associated
    with this item line, in ISO 8601 format (YYYY-MM-DD). This is particularly
    relevant for perishable or time-sensitive inventory items. Note that this field
    is only supported on QuickBooks Desktop 2023 or later.
    """

    inventory_site: Optional[ItemLineInventorySite] = FieldInfo(alias="inventorySite", default=None)
    """
    The site location where inventory for the item associated with this item line is
    stored.
    """

    inventory_site_location: Optional[ItemLineInventorySiteLocation] = FieldInfo(
        alias="inventorySiteLocation", default=None
    )
    """
    The specific location (e.g., bin or shelf) within the inventory site where the
    item associated with this item line is stored.
    """

    item: Optional[ItemLineItem] = None
    """The item associated with this item line.

    This can refer to any good or service that the business buys or sells, including
    item types such as a service item, inventory item, or special calculation item
    like a discount item or sales-tax item.
    """

    lot_number: Optional[str] = FieldInfo(alias="lotNumber", default=None)
    """The lot number of the item associated with this item line.

    Used for tracking groups of inventory items that are purchased or manufactured
    together.
    """

    object_type: Literal["qbd_item_line"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_item_line"`."""

    override_unit_of_measure_set: Optional[ItemLineOverrideUnitOfMeasureSet] = FieldInfo(
        alias="overrideUnitOfMeasureSet", default=None
    )
    """
    Specifies an alternative unit-of-measure set when updating this item line's
    `unitOfMeasure` field (e.g., "pound" or "kilogram"). This allows you to select
    units from a different set than the item's default unit-of-measure set, which
    remains unchanged on the item itself. The override applies only to this specific
    line. For example, you can sell an item typically measured in volume units using
    weight units in a specific transaction by specifying a different unit-of-measure
    set with this field.
    """

    quantity: Optional[float] = None
    """The quantity of the item associated with this item line."""

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
    """The serial number of the item associated with this item line.

    This is used for tracking individual units of serialized inventory items.
    """

    unit_of_measure: Optional[str] = FieldInfo(alias="unitOfMeasure", default=None)
    """The unit-of-measure used for the `quantity` in this item line.

    Must be a valid unit within the item's available units of measure.
    """


class LinkedTransaction(BaseModel):
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
