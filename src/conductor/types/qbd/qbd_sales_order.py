# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "QbdSalesOrder",
    "BillingAddress",
    "Class",
    "Currency",
    "Customer",
    "CustomerMessage",
    "CustomField",
    "DocumentTemplate",
    "LineGroup",
    "LineGroupCustomField",
    "LineGroupItemGroup",
    "LineGroupLine",
    "LineGroupLineClass",
    "LineGroupLineCustomField",
    "LineGroupLineInventorySite",
    "LineGroupLineInventorySiteLocation",
    "LineGroupLineItem",
    "LineGroupLineOverrideUnitOfMeasureSet",
    "LineGroupLineSalesTaxCode",
    "LineGroupOverrideUnitOfMeasureSet",
    "Line",
    "LineClass",
    "LineCustomField",
    "LineInventorySite",
    "LineInventorySiteLocation",
    "LineItem",
    "LineOverrideUnitOfMeasureSet",
    "LineSalesTaxCode",
    "LinkedTransaction",
    "SalesRepresentative",
    "SalesTaxCode",
    "SalesTaxItem",
    "ShippingAddress",
    "ShippingMethod",
    "Terms",
]


class BillingAddress(BaseModel):
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


class Class(BaseModel):
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


class CustomerMessage(BaseModel):
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


class DocumentTemplate(BaseModel):
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


class LineGroupCustomField(BaseModel):
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


class LineGroupItemGroup(BaseModel):
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


class LineGroupLineClass(BaseModel):
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


class LineGroupLineCustomField(BaseModel):
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


class LineGroupLineInventorySite(BaseModel):
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


class LineGroupLineInventorySiteLocation(BaseModel):
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


class LineGroupLineItem(BaseModel):
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


class LineGroupLineOverrideUnitOfMeasureSet(BaseModel):
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


class LineGroupLineSalesTaxCode(BaseModel):
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


class LineGroupLine(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks to this sales order line.

    This ID is unique across all transaction line types.
    """

    amount: Optional[str] = None
    """The monetary amount of this sales order line, represented as a decimal string.

    If both `quantity` and `rate` are specified but not `amount`, QuickBooks will
    use them to calculate `amount`. If `amount`, `rate`, and `quantity` are all
    unspecified, then QuickBooks will calculate `amount` based on a `quantity` of
    `1` and the suggested `rate`.
    """

    class_: Optional[LineGroupLineClass] = FieldInfo(alias="class", default=None)
    """The sales order line's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default. If a class is specified for the entire parent transaction, it is
    automatically applied to all sales order lines unless overridden here, at the
    transaction line level.
    """

    custom_fields: List[LineGroupLineCustomField] = FieldInfo(alias="customFields")
    """
    The custom fields for the sales order line object, added as user-defined data
    extensions, not included in the standard QuickBooks object.
    """

    description: Optional[str] = None
    """A description of this sales order line."""

    expiration_date: Optional[date] = FieldInfo(alias="expirationDate", default=None)
    """
    The expiration date for the serial number or lot number of the item associated
    with this sales order line, in ISO 8601 format (YYYY-MM-DD). This is
    particularly relevant for perishable or time-sensitive inventory items. Note
    that this field is only supported on QuickBooks Desktop 2023 or later.
    """

    inventory_site: Optional[LineGroupLineInventorySite] = FieldInfo(alias="inventorySite", default=None)
    """
    The site location where inventory for the item associated with this sales order
    line is stored.
    """

    inventory_site_location: Optional[LineGroupLineInventorySiteLocation] = FieldInfo(
        alias="inventorySiteLocation", default=None
    )
    """
    The specific location (e.g., bin or shelf) within the inventory site where the
    item associated with this sales order line is stored.
    """

    is_manually_closed: Optional[bool] = FieldInfo(alias="isManuallyClosed", default=None)
    """
    Indicates whether this sales order line has been manually marked as closed, even
    if it has not been invoiced.
    """

    item: Optional[LineGroupLineItem] = None
    """The item associated with this sales order line.

    This can refer to any good or service that the business buys or sells, including
    item types such as a service item, inventory item, or special calculation item
    like a discount item or sales-tax item.
    """

    lot_number: Optional[str] = FieldInfo(alias="lotNumber", default=None)
    """The lot number of the item associated with this sales order line.

    Used for tracking groups of inventory items that are purchased or manufactured
    together.
    """

    object_type: Literal["qbd_sales_order_line"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_sales_order_line"`."""

    other_custom_field1: Optional[str] = FieldInfo(alias="otherCustomField1", default=None)
    """
    A built-in custom field for additional information specific to this sales order
    line. Unlike the user-defined fields in the `customFields` array, this is a
    standard QuickBooks field that exists for all sales order lines for convenience.
    Developers often use this field for tracking information that doesn't fit into
    other standard QuickBooks fields. Hidden by default in the QuickBooks UI.
    """

    other_custom_field2: Optional[str] = FieldInfo(alias="otherCustomField2", default=None)
    """
    A second built-in custom field for additional information specific to this sales
    order line. Unlike the user-defined fields in the `customFields` array, this is
    a standard QuickBooks field that exists for all sales order lines for
    convenience. Like `otherCustomField1`, developers often use this field for
    tracking information that doesn't fit into other standard QuickBooks fields.
    Hidden by default in the QuickBooks UI.
    """

    override_unit_of_measure_set: Optional[LineGroupLineOverrideUnitOfMeasureSet] = FieldInfo(
        alias="overrideUnitOfMeasureSet", default=None
    )
    """
    Specifies an alternative unit-of-measure set when updating this sales order
    line's `unitOfMeasure` field (e.g., "pound" or "kilogram"). This allows you to
    select units from a different set than the item's default unit-of-measure set,
    which remains unchanged on the item itself. The override applies only to this
    specific line. For example, you can sell an item typically measured in volume
    units using weight units in a specific transaction by specifying a different
    unit-of-measure set with this field.
    """

    quantity: Optional[float] = None
    """The quantity of the item associated with this sales order line."""

    quantity_invoiced: Optional[float] = FieldInfo(alias="quantityInvoiced", default=None)
    """
    The number of units of this sales order line's `quantity` that have been
    invoiced.
    """

    rate: Optional[str] = None
    """The price per unit for this sales order line.

    If both `rate` and `amount` are specified, `rate` will be ignored. If both
    `quantity` and `amount` are specified but not `rate`, QuickBooks will use them
    to calculate `rate`. Represented as a decimal string.
    """

    rate_percent: Optional[str] = FieldInfo(alias="ratePercent", default=None)
    """The price of this sales order line expressed as a percentage.

    Typically used for discount or markup items.
    """

    sales_tax_code: Optional[LineGroupLineSalesTaxCode] = FieldInfo(alias="salesTaxCode", default=None)
    """
    The sales-tax code associated with this sales order line, determining whether
    items sold to this customer are taxable or non-taxable. It's used to assign a
    default tax status to all transactions for this sales order line. Default codes
    include "Non" (non-taxable) and "Tax" (taxable), but custom codes can also be
    created in QuickBooks. If QuickBooks is not set up to charge sales tax (via the
    "Do You Charge Sales Tax?" preference), it will assign the default non-taxable
    code to all sales.
    """

    serial_number: Optional[str] = FieldInfo(alias="serialNumber", default=None)
    """The serial number of the item associated with this sales order line.

    This is used for tracking individual units of serialized inventory items.
    """

    unit_of_measure: Optional[str] = FieldInfo(alias="unitOfMeasure", default=None)
    """The unit-of-measure used for the `quantity` in this sales order line.

    Must be a valid unit within the item's available units of measure.
    """


class LineGroupOverrideUnitOfMeasureSet(BaseModel):
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


class LineGroup(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks to this sales order line group.

    This ID is unique across all transaction line types.
    """

    custom_fields: List[LineGroupCustomField] = FieldInfo(alias="customFields")
    """
    The custom fields for the sales order line group object, added as user-defined
    data extensions, not included in the standard QuickBooks object.
    """

    description: Optional[str] = None
    """A description of this sales order line group."""

    item_group: LineGroupItemGroup = FieldInfo(alias="itemGroup")
    """
    The sales order line group's item group, representing a predefined set of items
    bundled because they are commonly purchased together or grouped for faster
    entry.
    """

    lines: List[LineGroupLine]
    """
    The sales order line group's line items, each representing a single product or
    service ordered.
    """

    object_type: Literal["qbd_sales_order_line_group"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_sales_order_line_group"`."""

    override_unit_of_measure_set: Optional[LineGroupOverrideUnitOfMeasureSet] = FieldInfo(
        alias="overrideUnitOfMeasureSet", default=None
    )
    """
    Specifies an alternative unit-of-measure set when updating this sales order line
    group's `unitOfMeasure` field (e.g., "pound" or "kilogram"). This allows you to
    select units from a different set than the item's default unit-of-measure set,
    which remains unchanged on the item itself. The override applies only to this
    specific line. For example, you can sell an item typically measured in volume
    units using weight units in a specific transaction by specifying a different
    unit-of-measure set with this field.
    """

    quantity: Optional[float] = None
    """The quantity of the item group associated with this sales order line group."""

    should_print_items_in_group: bool = FieldInfo(alias="shouldPrintItemsInGroup")
    """
    Indicates whether the individual items in this sales order line group and their
    separate amounts appear on printed forms.
    """

    total_amount: str = FieldInfo(alias="totalAmount")
    """
    The total monetary amount of this sales order line group, represented as a
    decimal string.
    """

    unit_of_measure: Optional[str] = FieldInfo(alias="unitOfMeasure", default=None)
    """The unit-of-measure used for the `quantity` in this sales order line group.

    Must be a valid unit within the item's available units of measure.
    """


class LineClass(BaseModel):
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


class LineCustomField(BaseModel):
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


class LineInventorySite(BaseModel):
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


class LineInventorySiteLocation(BaseModel):
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


class LineItem(BaseModel):
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


class LineOverrideUnitOfMeasureSet(BaseModel):
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


class LineSalesTaxCode(BaseModel):
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


class Line(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks to this sales order line.

    This ID is unique across all transaction line types.
    """

    amount: Optional[str] = None
    """The monetary amount of this sales order line, represented as a decimal string.

    If both `quantity` and `rate` are specified but not `amount`, QuickBooks will
    use them to calculate `amount`. If `amount`, `rate`, and `quantity` are all
    unspecified, then QuickBooks will calculate `amount` based on a `quantity` of
    `1` and the suggested `rate`.
    """

    class_: Optional[LineClass] = FieldInfo(alias="class", default=None)
    """The sales order line's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default. If a class is specified for the entire parent transaction, it is
    automatically applied to all sales order lines unless overridden here, at the
    transaction line level.
    """

    custom_fields: List[LineCustomField] = FieldInfo(alias="customFields")
    """
    The custom fields for the sales order line object, added as user-defined data
    extensions, not included in the standard QuickBooks object.
    """

    description: Optional[str] = None
    """A description of this sales order line."""

    expiration_date: Optional[date] = FieldInfo(alias="expirationDate", default=None)
    """
    The expiration date for the serial number or lot number of the item associated
    with this sales order line, in ISO 8601 format (YYYY-MM-DD). This is
    particularly relevant for perishable or time-sensitive inventory items. Note
    that this field is only supported on QuickBooks Desktop 2023 or later.
    """

    inventory_site: Optional[LineInventorySite] = FieldInfo(alias="inventorySite", default=None)
    """
    The site location where inventory for the item associated with this sales order
    line is stored.
    """

    inventory_site_location: Optional[LineInventorySiteLocation] = FieldInfo(
        alias="inventorySiteLocation", default=None
    )
    """
    The specific location (e.g., bin or shelf) within the inventory site where the
    item associated with this sales order line is stored.
    """

    is_manually_closed: Optional[bool] = FieldInfo(alias="isManuallyClosed", default=None)
    """
    Indicates whether this sales order line has been manually marked as closed, even
    if it has not been invoiced.
    """

    item: Optional[LineItem] = None
    """The item associated with this sales order line.

    This can refer to any good or service that the business buys or sells, including
    item types such as a service item, inventory item, or special calculation item
    like a discount item or sales-tax item.
    """

    lot_number: Optional[str] = FieldInfo(alias="lotNumber", default=None)
    """The lot number of the item associated with this sales order line.

    Used for tracking groups of inventory items that are purchased or manufactured
    together.
    """

    object_type: Literal["qbd_sales_order_line"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_sales_order_line"`."""

    other_custom_field1: Optional[str] = FieldInfo(alias="otherCustomField1", default=None)
    """
    A built-in custom field for additional information specific to this sales order
    line. Unlike the user-defined fields in the `customFields` array, this is a
    standard QuickBooks field that exists for all sales order lines for convenience.
    Developers often use this field for tracking information that doesn't fit into
    other standard QuickBooks fields. Hidden by default in the QuickBooks UI.
    """

    other_custom_field2: Optional[str] = FieldInfo(alias="otherCustomField2", default=None)
    """
    A second built-in custom field for additional information specific to this sales
    order line. Unlike the user-defined fields in the `customFields` array, this is
    a standard QuickBooks field that exists for all sales order lines for
    convenience. Like `otherCustomField1`, developers often use this field for
    tracking information that doesn't fit into other standard QuickBooks fields.
    Hidden by default in the QuickBooks UI.
    """

    override_unit_of_measure_set: Optional[LineOverrideUnitOfMeasureSet] = FieldInfo(
        alias="overrideUnitOfMeasureSet", default=None
    )
    """
    Specifies an alternative unit-of-measure set when updating this sales order
    line's `unitOfMeasure` field (e.g., "pound" or "kilogram"). This allows you to
    select units from a different set than the item's default unit-of-measure set,
    which remains unchanged on the item itself. The override applies only to this
    specific line. For example, you can sell an item typically measured in volume
    units using weight units in a specific transaction by specifying a different
    unit-of-measure set with this field.
    """

    quantity: Optional[float] = None
    """The quantity of the item associated with this sales order line."""

    quantity_invoiced: Optional[float] = FieldInfo(alias="quantityInvoiced", default=None)
    """
    The number of units of this sales order line's `quantity` that have been
    invoiced.
    """

    rate: Optional[str] = None
    """The price per unit for this sales order line.

    If both `rate` and `amount` are specified, `rate` will be ignored. If both
    `quantity` and `amount` are specified but not `rate`, QuickBooks will use them
    to calculate `rate`. Represented as a decimal string.
    """

    rate_percent: Optional[str] = FieldInfo(alias="ratePercent", default=None)
    """The price of this sales order line expressed as a percentage.

    Typically used for discount or markup items.
    """

    sales_tax_code: Optional[LineSalesTaxCode] = FieldInfo(alias="salesTaxCode", default=None)
    """
    The sales-tax code associated with this sales order line, determining whether
    items sold to this customer are taxable or non-taxable. It's used to assign a
    default tax status to all transactions for this sales order line. Default codes
    include "Non" (non-taxable) and "Tax" (taxable), but custom codes can also be
    created in QuickBooks. If QuickBooks is not set up to charge sales tax (via the
    "Do You Charge Sales Tax?" preference), it will assign the default non-taxable
    code to all sales.
    """

    serial_number: Optional[str] = FieldInfo(alias="serialNumber", default=None)
    """The serial number of the item associated with this sales order line.

    This is used for tracking individual units of serialized inventory items.
    """

    unit_of_measure: Optional[str] = FieldInfo(alias="unitOfMeasure", default=None)
    """The unit-of-measure used for the `quantity` in this sales order line.

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


class SalesRepresentative(BaseModel):
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


class SalesTaxItem(BaseModel):
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


class ShippingAddress(BaseModel):
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


class ShippingMethod(BaseModel):
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


class QbdSalesOrder(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks to this sales order.

    This ID is unique across all transaction types.
    """

    billing_address: Optional[BillingAddress] = FieldInfo(alias="billingAddress", default=None)
    """The sales order's billing address."""

    class_: Optional[Class] = FieldInfo(alias="class", default=None)
    """The sales order's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default. A class defined here is automatically used in this sales order's line
    items unless overridden at the line item level.
    """

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when this sales order was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """

    currency: Optional[Currency] = None
    """The sales order's currency.

    For built-in currencies, the name and code are standard international values.
    For user-defined currencies, all values are editable.
    """

    customer: Customer
    """The customer or customer-job associated with this sales order."""

    customer_message: Optional[CustomerMessage] = FieldInfo(alias="customerMessage", default=None)
    """The message to display to the customer on the sales order."""

    custom_fields: List[CustomField] = FieldInfo(alias="customFields")
    """
    The custom fields for the sales order object, added as user-defined data
    extensions, not included in the standard QuickBooks object.
    """

    document_template: Optional[DocumentTemplate] = FieldInfo(alias="documentTemplate", default=None)
    """
    The predefined template in QuickBooks that determines the layout and formatting
    for this sales order when printed or displayed.
    """

    due_date: Optional[date] = FieldInfo(alias="dueDate", default=None)
    """
    The date by which this sales order must be paid, in ISO 8601 format
    (YYYY-MM-DD).
    """

    exchange_rate: Optional[float] = FieldInfo(alias="exchangeRate", default=None)
    """
    The market exchange rate between this sales order's currency and the home
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

    is_fully_invoiced: Optional[bool] = FieldInfo(alias="isFullyInvoiced", default=None)
    """Indicates whether all items in this sales order have been invoiced."""

    is_manually_closed: Optional[bool] = FieldInfo(alias="isManuallyClosed", default=None)
    """
    Indicates whether this sales order has been manually marked as closed, even if
    it has not been invoiced.
    """

    is_queued_for_email: Optional[bool] = FieldInfo(alias="isQueuedForEmail", default=None)
    """
    Indicates whether this sales order is included in the queue of documents for
    QuickBooks to email to the customer.
    """

    is_queued_for_print: Optional[bool] = FieldInfo(alias="isQueuedForPrint", default=None)
    """
    Indicates whether this sales order is included in the queue of documents for
    QuickBooks to print.
    """

    line_groups: List[LineGroup] = FieldInfo(alias="lineGroups")
    """
    The sales order's line item groups, each representing a predefined set of
    related items.
    """

    lines: List[Line]
    """
    The sales order's line items, each representing a single product or service
    ordered.
    """

    linked_transactions: List[LinkedTransaction] = FieldInfo(alias="linkedTransactions")
    """
    The sales order's linked transactions, such as payments applied, credits used,
    or associated purchase orders.

    **IMPORTANT**: You must specify the parameter `includeLinkedTransactions` when
    fetching a list of sales orders to receive this field because it is not returned
    by default.
    """

    memo: Optional[str] = None
    """A memo or note for this sales order."""

    object_type: Literal["qbd_sales_order"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_sales_order"`."""

    other_custom_field: Optional[str] = FieldInfo(alias="otherCustomField", default=None)
    """A built-in custom field for additional information specific to this sales order.

    Unlike the user-defined fields in the `customFields` array, this is a standard
    QuickBooks field that exists for all sales orders for convenience. Developers
    often use this field for tracking information that doesn't fit into other
    standard QuickBooks fields. Unlike `otherCustomField1` and `otherCustomField2`,
    which are line item fields, this exists at the transaction level. Hidden by
    default in the QuickBooks UI.
    """

    purchase_order_number: Optional[str] = FieldInfo(alias="purchaseOrderNumber", default=None)
    """The customer's Purchase Order (PO) number associated with this sales order.

    This field is often used to cross-reference the sales order with the customer's
    purchasing system.
    """

    ref_number: Optional[str] = FieldInfo(alias="refNumber", default=None)
    """
    The case-sensitive user-defined reference number for this sales order, which can
    be used to identify the transaction in QuickBooks. This value is not required to
    be unique and can be arbitrarily changed by the QuickBooks user.
    """

    revision_number: str = FieldInfo(alias="revisionNumber")
    """
    The current revision number of this sales order object, which changes each time
    the object is modified. When updating this object, you must provide the most
    recent `revisionNumber` to ensure you're working with the latest data;
    otherwise, the update will return an error.
    """

    sales_channel_name: Optional[Literal["blank", "ecommerce"]] = FieldInfo(alias="salesChannelName", default=None)
    """The type of the sales channel for this sales order."""

    sales_representative: Optional[SalesRepresentative] = FieldInfo(alias="salesRepresentative", default=None)
    """The sales order's sales representative.

    Sales representatives can be employees, vendors, or other names in QuickBooks.
    """

    sales_store_name: Optional[str] = FieldInfo(alias="salesStoreName", default=None)
    """The name of the sales store for this sales order."""

    sales_store_type: Optional[str] = FieldInfo(alias="salesStoreType", default=None)
    """The type of the sales store for this sales order."""

    sales_tax_code: Optional[SalesTaxCode] = FieldInfo(alias="salesTaxCode", default=None)
    """
    The sales-tax code for items sold to the `customer` of this sales order,
    determining whether items sold to this customer are taxable or non-taxable.
    Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
    can also be created in QuickBooks. If QuickBooks is not set up to charge sales
    tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
    non-taxable code to all sales.
    """

    sales_tax_item: Optional[SalesTaxItem] = FieldInfo(alias="salesTaxItem", default=None)
    """
    The sales-tax item used to calculate the actual tax amount for this sales
    order's transactions by applying a specific tax rate collected for a single tax
    agency. Unlike `salesTaxCode`, which only indicates general taxability, this
    field drives the actual tax calculation and reporting.
    """

    sales_tax_percentage: Optional[str] = FieldInfo(alias="salesTaxPercentage", default=None)
    """
    The sales tax percentage applied to this sales order, represented as a decimal
    string.
    """

    sales_tax_total: Optional[str] = FieldInfo(alias="salesTaxTotal", default=None)
    """
    The total amount of sales tax charged for this sales order, represented as a
    decimal string.
    """

    shipment_origin: Optional[str] = FieldInfo(alias="shipmentOrigin", default=None)
    """
    The origin location from where the product associated with this sales order is
    shipped. This is the point at which ownership and liability for goods transfer
    from seller to buyer. Internally, QuickBooks uses the term "FOB" for this field,
    which stands for "freight on board". This field is informational and has no
    accounting implications.
    """

    shipping_address: Optional[ShippingAddress] = FieldInfo(alias="shippingAddress", default=None)
    """The sales order's shipping address."""

    shipping_date: Optional[date] = FieldInfo(alias="shippingDate", default=None)
    """
    The date when the products or services for this sales order were shipped or are
    expected to be shipped, in ISO 8601 format (YYYY-MM-DD).
    """

    shipping_method: Optional[ShippingMethod] = FieldInfo(alias="shippingMethod", default=None)
    """
    The shipping method used for this sales order, such as standard mail or
    overnight delivery.
    """

    subtotal: Optional[str] = None
    """
    The subtotal of this sales order, which is the sum of all line items before
    taxes and discounts are applied, represented as a decimal string.
    """

    terms: Optional[Terms] = None
    """
    The sales order's payment terms, defining when payment is due and any applicable
    discounts.
    """

    total_amount: Optional[str] = FieldInfo(alias="totalAmount", default=None)
    """The total monetary amount of this sales order, represented as a decimal string."""

    total_amount_in_home_currency: Optional[str] = FieldInfo(alias="totalAmountInHomeCurrency", default=None)
    """
    The total monetary amount for this sales order converted to the home currency of
    the QuickBooks company file. Represented as a decimal string.
    """

    transaction_date: date = FieldInfo(alias="transactionDate")
    """The date of this sales order, in ISO 8601 format (YYYY-MM-DD)."""

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when this sales order was last updated, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """
