# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .address import Address
from ..._models import BaseModel
from .custom_field import CustomField
from .linked_transaction import LinkedTransaction

__all__ = [
    "PurchaseOrder",
    "Class",
    "Currency",
    "DocumentTemplate",
    "InventorySite",
    "LineGroup",
    "LineGroupItemGroup",
    "LineGroupLine",
    "LineGroupLineClass",
    "LineGroupLineInventorySiteLocation",
    "LineGroupLineItem",
    "LineGroupLineOverrideUnitOfMeasureSet",
    "LineGroupLinePayee",
    "LineGroupLineSalesTaxCode",
    "LineGroupOverrideUnitOfMeasureSet",
    "Line",
    "LineClass",
    "LineInventorySiteLocation",
    "LineItem",
    "LineOverrideUnitOfMeasureSet",
    "LinePayee",
    "LineSalesTaxCode",
    "SalesTaxCode",
    "ShippingMethod",
    "ShipToEntity",
    "Terms",
    "Vendor",
]


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


class InventorySite(BaseModel):
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


class LineGroupLinePayee(BaseModel):
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
    """The unique identifier assigned by QuickBooks to this purchase order line.

    This ID is unique across all transaction line types.
    """

    amount: Optional[str] = None
    """The monetary amount of this purchase order line, represented as a decimal
    string.

    If both `quantity` and `rate` are specified but not `amount`, QuickBooks will
    use them to calculate `amount`. If `amount`, `rate`, and `quantity` are all
    unspecified, then QuickBooks will calculate `amount` based on a `quantity` of
    `1` and the suggested `rate`. This field cannot be cleared.
    """

    class_: Optional[LineGroupLineClass] = FieldInfo(alias="class", default=None)
    """The purchase order line's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default. If a class is specified for the entire parent transaction, it is
    automatically applied to all purchase order lines unless overridden here, at the
    transaction line level.
    """

    custom_fields: List[CustomField] = FieldInfo(alias="customFields")
    """
    The custom fields for the purchase order line object, added as user-defined data
    extensions, not included in the standard QuickBooks object.
    """

    description: Optional[str] = None
    """A description of this purchase order line."""

    inventory_site_location: Optional[LineGroupLineInventorySiteLocation] = FieldInfo(
        alias="inventorySiteLocation", default=None
    )
    """
    The specific location (e.g., bin or shelf) within the inventory site where the
    item associated with this purchase order line is stored.
    """

    is_billed: Optional[bool] = FieldInfo(alias="isBilled", default=None)
    """Indicates whether this purchase order line has been billed."""

    is_manually_closed: Optional[bool] = FieldInfo(alias="isManuallyClosed", default=None)
    """
    Indicates whether this purchase order line has been manually marked as closed,
    even if this item has not been received or its sale has not been cancelled. If
    all the purchase order lines are marked as closed, the purchase order itself is
    marked as closed as well. You cannot change `isManuallyClosed` to `false` after
    the purchase order line has been fully received.
    """

    item: Optional[LineGroupLineItem] = None
    """The item associated with this purchase order line.

    This can refer to any good or service that the business buys or sells, including
    item types such as a service item, inventory item, or special calculation item
    like a discount item or sales-tax item.
    """

    object_type: Literal["qbd_purchase_order_line"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_purchase_order_line"`."""

    other_custom_field1: Optional[str] = FieldInfo(alias="otherCustomField1", default=None)
    """
    A built-in custom field for additional information specific to this purchase
    order line. Unlike the user-defined fields in the `customFields` array, this is
    a standard QuickBooks field that exists for all purchase order lines for
    convenience. Developers often use this field for tracking information that
    doesn't fit into other standard QuickBooks fields. Hidden by default in the
    QuickBooks UI.
    """

    other_custom_field2: Optional[str] = FieldInfo(alias="otherCustomField2", default=None)
    """
    A second built-in custom field for additional information specific to this
    purchase order line. Unlike the user-defined fields in the `customFields` array,
    this is a standard QuickBooks field that exists for all purchase order lines for
    convenience. Like `otherCustomField1`, developers often use this field for
    tracking information that doesn't fit into other standard QuickBooks fields.
    Hidden by default in the QuickBooks UI.
    """

    override_unit_of_measure_set: Optional[LineGroupLineOverrideUnitOfMeasureSet] = FieldInfo(
        alias="overrideUnitOfMeasureSet", default=None
    )
    """
    Specifies an alternative unit-of-measure set when updating this purchase order
    line's `unitOfMeasure` field (e.g., "pound" or "kilogram"). This allows you to
    select units from a different set than the item's default unit-of-measure set,
    which remains unchanged on the item itself. The override applies only to this
    specific line. For example, you can sell an item typically measured in volume
    units using weight units in a specific transaction by specifying a different
    unit-of-measure set with this field.
    """

    payee: Optional[LineGroupLinePayee] = None
    """
    If `account` refers to an Accounts-Payable (A/P) account, `payee` refers to the
    expense's vendor (not the customer). If `account` refers to any other type of
    account, `payee` refers to the expense's customer (not the vendor).
    """

    quantity: Optional[float] = None
    """The quantity of the item associated with this purchase order line.

    This field cannot be cleared.
    """

    rate: Optional[str] = None
    """The price per unit for this purchase order line.

    If both `rate` and `amount` are specified, `rate` will be ignored. If both
    `quantity` and `amount` are specified but not `rate`, QuickBooks will use them
    to calculate `rate`. Represented as a decimal string. This field cannot be
    cleared.
    """

    received_quantity: Optional[float] = FieldInfo(alias="receivedQuantity", default=None)
    """The quantity that has been received against this purchase order line."""

    sales_tax_code: Optional[LineGroupLineSalesTaxCode] = FieldInfo(alias="salesTaxCode", default=None)
    """
    The sales-tax code associated with this purchase order line, determining whether
    items bought from this vendor are taxable or non-taxable. It's used to assign a
    default tax status to all transactions for this purchase order line. Default
    codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes can also
    be created in QuickBooks. If QuickBooks is not set up to charge sales tax (via
    the "Do You Charge Sales Tax?" preference), it will assign the default
    non-taxable code to all sales.
    """

    service_date: Optional[date] = FieldInfo(alias="serviceDate", default=None)
    """
    The date on which the service for this purchase order line was or will be
    performed, in ISO 8601 format (YYYY-MM-DD). This is particularly relevant for
    service items.
    """

    sku: Optional[str] = None
    """
    The purchase order line's stock keeping unit (SKU), which is sometimes the
    manufacturer's part number.
    """

    unbilled_quantity: Optional[float] = FieldInfo(alias="unbilledQuantity", default=None)
    """The quantity that has not been billed for this purchase order line."""

    unit_of_measure: Optional[str] = FieldInfo(alias="unitOfMeasure", default=None)
    """The unit-of-measure used for the `quantity` in this purchase order line.

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
    """The unique identifier assigned by QuickBooks to this purchase order line group.

    This ID is unique across all transaction line types.
    """

    custom_fields: List[CustomField] = FieldInfo(alias="customFields")
    """
    The custom fields for the purchase order line group object, added as
    user-defined data extensions, not included in the standard QuickBooks object.
    """

    description: Optional[str] = None
    """A description of this purchase order line group."""

    item_group: LineGroupItemGroup = FieldInfo(alias="itemGroup")
    """
    The purchase order line group's item group, representing a predefined set of
    items bundled because they are commonly purchased together or grouped for faster
    entry.
    """

    lines: List[LineGroupLine]
    """
    The purchase order line group's line items, each representing a single product
    or service ordered.
    """

    object_type: Literal["qbd_purchase_order_line_group"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_purchase_order_line_group"`."""

    override_unit_of_measure_set: Optional[LineGroupOverrideUnitOfMeasureSet] = FieldInfo(
        alias="overrideUnitOfMeasureSet", default=None
    )
    """
    Specifies an alternative unit-of-measure set when updating this purchase order
    line group's `unitOfMeasure` field (e.g., "pound" or "kilogram"). This allows
    you to select units from a different set than the item's default unit-of-measure
    set, which remains unchanged on the item itself. The override applies only to
    this specific line. For example, you can sell an item typically measured in
    volume units using weight units in a specific transaction by specifying a
    different unit-of-measure set with this field.
    """

    quantity: Optional[float] = None
    """The quantity of the item group associated with this purchase order line group.

    This field cannot be cleared.
    """

    should_print_items_in_group: bool = FieldInfo(alias="shouldPrintItemsInGroup")
    """
    Indicates whether the individual items in this purchase order line group and
    their separate amounts appear on printed forms.
    """

    total_amount: str = FieldInfo(alias="totalAmount")
    """
    The total monetary amount of this purchase order line group, represented as a
    decimal string.
    """

    unit_of_measure: Optional[str] = FieldInfo(alias="unitOfMeasure", default=None)
    """The unit-of-measure used for the `quantity` in this purchase order line group.

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


class LinePayee(BaseModel):
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
    """The unique identifier assigned by QuickBooks to this purchase order line.

    This ID is unique across all transaction line types.
    """

    amount: Optional[str] = None
    """The monetary amount of this purchase order line, represented as a decimal
    string.

    If both `quantity` and `rate` are specified but not `amount`, QuickBooks will
    use them to calculate `amount`. If `amount`, `rate`, and `quantity` are all
    unspecified, then QuickBooks will calculate `amount` based on a `quantity` of
    `1` and the suggested `rate`. This field cannot be cleared.
    """

    class_: Optional[LineClass] = FieldInfo(alias="class", default=None)
    """The purchase order line's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default. If a class is specified for the entire parent transaction, it is
    automatically applied to all purchase order lines unless overridden here, at the
    transaction line level.
    """

    custom_fields: List[CustomField] = FieldInfo(alias="customFields")
    """
    The custom fields for the purchase order line object, added as user-defined data
    extensions, not included in the standard QuickBooks object.
    """

    description: Optional[str] = None
    """A description of this purchase order line."""

    inventory_site_location: Optional[LineInventorySiteLocation] = FieldInfo(
        alias="inventorySiteLocation", default=None
    )
    """
    The specific location (e.g., bin or shelf) within the inventory site where the
    item associated with this purchase order line is stored.
    """

    is_billed: Optional[bool] = FieldInfo(alias="isBilled", default=None)
    """Indicates whether this purchase order line has been billed."""

    is_manually_closed: Optional[bool] = FieldInfo(alias="isManuallyClosed", default=None)
    """
    Indicates whether this purchase order line has been manually marked as closed,
    even if this item has not been received or its sale has not been cancelled. If
    all the purchase order lines are marked as closed, the purchase order itself is
    marked as closed as well. You cannot change `isManuallyClosed` to `false` after
    the purchase order line has been fully received.
    """

    item: Optional[LineItem] = None
    """The item associated with this purchase order line.

    This can refer to any good or service that the business buys or sells, including
    item types such as a service item, inventory item, or special calculation item
    like a discount item or sales-tax item.
    """

    object_type: Literal["qbd_purchase_order_line"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_purchase_order_line"`."""

    other_custom_field1: Optional[str] = FieldInfo(alias="otherCustomField1", default=None)
    """
    A built-in custom field for additional information specific to this purchase
    order line. Unlike the user-defined fields in the `customFields` array, this is
    a standard QuickBooks field that exists for all purchase order lines for
    convenience. Developers often use this field for tracking information that
    doesn't fit into other standard QuickBooks fields. Hidden by default in the
    QuickBooks UI.
    """

    other_custom_field2: Optional[str] = FieldInfo(alias="otherCustomField2", default=None)
    """
    A second built-in custom field for additional information specific to this
    purchase order line. Unlike the user-defined fields in the `customFields` array,
    this is a standard QuickBooks field that exists for all purchase order lines for
    convenience. Like `otherCustomField1`, developers often use this field for
    tracking information that doesn't fit into other standard QuickBooks fields.
    Hidden by default in the QuickBooks UI.
    """

    override_unit_of_measure_set: Optional[LineOverrideUnitOfMeasureSet] = FieldInfo(
        alias="overrideUnitOfMeasureSet", default=None
    )
    """
    Specifies an alternative unit-of-measure set when updating this purchase order
    line's `unitOfMeasure` field (e.g., "pound" or "kilogram"). This allows you to
    select units from a different set than the item's default unit-of-measure set,
    which remains unchanged on the item itself. The override applies only to this
    specific line. For example, you can sell an item typically measured in volume
    units using weight units in a specific transaction by specifying a different
    unit-of-measure set with this field.
    """

    payee: Optional[LinePayee] = None
    """
    If `account` refers to an Accounts-Payable (A/P) account, `payee` refers to the
    expense's vendor (not the customer). If `account` refers to any other type of
    account, `payee` refers to the expense's customer (not the vendor).
    """

    quantity: Optional[float] = None
    """The quantity of the item associated with this purchase order line.

    This field cannot be cleared.
    """

    rate: Optional[str] = None
    """The price per unit for this purchase order line.

    If both `rate` and `amount` are specified, `rate` will be ignored. If both
    `quantity` and `amount` are specified but not `rate`, QuickBooks will use them
    to calculate `rate`. Represented as a decimal string. This field cannot be
    cleared.
    """

    received_quantity: Optional[float] = FieldInfo(alias="receivedQuantity", default=None)
    """The quantity that has been received against this purchase order line."""

    sales_tax_code: Optional[LineSalesTaxCode] = FieldInfo(alias="salesTaxCode", default=None)
    """
    The sales-tax code associated with this purchase order line, determining whether
    items bought from this vendor are taxable or non-taxable. It's used to assign a
    default tax status to all transactions for this purchase order line. Default
    codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes can also
    be created in QuickBooks. If QuickBooks is not set up to charge sales tax (via
    the "Do You Charge Sales Tax?" preference), it will assign the default
    non-taxable code to all sales.
    """

    service_date: Optional[date] = FieldInfo(alias="serviceDate", default=None)
    """
    The date on which the service for this purchase order line was or will be
    performed, in ISO 8601 format (YYYY-MM-DD). This is particularly relevant for
    service items.
    """

    sku: Optional[str] = None
    """
    The purchase order line's stock keeping unit (SKU), which is sometimes the
    manufacturer's part number.
    """

    unbilled_quantity: Optional[float] = FieldInfo(alias="unbilledQuantity", default=None)
    """The quantity that has not been billed for this purchase order line."""

    unit_of_measure: Optional[str] = FieldInfo(alias="unitOfMeasure", default=None)
    """The unit-of-measure used for the `quantity` in this purchase order line.

    Must be a valid unit within the item's available units of measure.
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


class ShipToEntity(BaseModel):
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


class PurchaseOrder(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks to this purchase order.

    This ID is unique across all transaction types.
    """

    class_: Optional[Class] = FieldInfo(alias="class", default=None)
    """The purchase order's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default. A class defined here is automatically used in this purchase order's
    line items unless overridden at the line item level.
    """

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when this purchase order was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """

    currency: Optional[Currency] = None
    """The purchase order's currency.

    For built-in currencies, the name and code are standard international values.
    For user-defined currencies, all values are editable.
    """

    custom_fields: List[CustomField] = FieldInfo(alias="customFields")
    """
    The custom fields for the purchase order object, added as user-defined data
    extensions, not included in the standard QuickBooks object.
    """

    document_template: Optional[DocumentTemplate] = FieldInfo(alias="documentTemplate", default=None)
    """
    The predefined template in QuickBooks that determines the layout and formatting
    for this purchase order when printed or displayed.
    """

    due_date: Optional[date] = FieldInfo(alias="dueDate", default=None)
    """
    The date by which this purchase order must be paid, in ISO 8601 format
    (YYYY-MM-DD).
    """

    exchange_rate: Optional[float] = FieldInfo(alias="exchangeRate", default=None)
    """
    The market exchange rate between this purchase order's currency and the home
    currency in QuickBooks at the time of this transaction. Represented as a decimal
    value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).
    """

    expected_date: Optional[date] = FieldInfo(alias="expectedDate", default=None)
    """
    The date on which shipment of this purchase order is expected to be completed,
    in ISO 8601 format (YYYY-MM-DD).
    """

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """
    A globally unique identifier (GUID) you can provide for tracking this object in
    your external system.

    **IMPORTANT**: Must be formatted as a valid GUID; otherwise, QuickBooks will
    return an error. This field is immutable and can only be set during object
    creation.
    """

    inventory_site: Optional[InventorySite] = FieldInfo(alias="inventorySite", default=None)
    """
    The site location where inventory for the item associated with this purchase
    order is stored.
    """

    is_fully_received: Optional[bool] = FieldInfo(alias="isFullyReceived", default=None)
    """
    Indicates whether all items in this purchase order have been received and none
    of them were closed manually.
    """

    is_manually_closed: Optional[bool] = FieldInfo(alias="isManuallyClosed", default=None)
    """
    Indicates whether this purchase order has been manually marked as closed, even
    if all items have not been received or the sale has not been cancelled. Once the
    purchase order is marked as closed, all of its line items become closed as well.
    You cannot change `isManuallyClosed` to `false` after the purchase order has
    been fully received.
    """

    is_queued_for_email: Optional[bool] = FieldInfo(alias="isQueuedForEmail", default=None)
    """
    Indicates whether this purchase order is included in the queue of documents for
    QuickBooks to email to the customer.
    """

    is_queued_for_print: Optional[bool] = FieldInfo(alias="isQueuedForPrint", default=None)
    """
    Indicates whether this purchase order is included in the queue of documents for
    QuickBooks to print.
    """

    line_groups: List[LineGroup] = FieldInfo(alias="lineGroups")
    """
    The purchase order's line item groups, each representing a predefined set of
    related items.
    """

    lines: List[Line]
    """
    The purchase order's line items, each representing a single product or service
    ordered.
    """

    linked_transactions: List[LinkedTransaction] = FieldInfo(alias="linkedTransactions")
    """
    The purchase order's linked transactions, such as payments applied, credits
    used, or associated purchase orders.

    **IMPORTANT**: You must specify the parameter `includeLinkedTransactions` when
    fetching a list of purchase orders to receive this field because it is not
    returned by default.
    """

    memo: Optional[str] = None
    """
    A memo or note for this purchase order that appears in reports, but not on the
    purchase order.
    """

    object_type: Literal["qbd_purchase_order"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_purchase_order"`."""

    other_custom_field1: Optional[str] = FieldInfo(alias="otherCustomField1", default=None)
    """
    A built-in custom field for additional information specific to this purchase
    order. Unlike the user-defined fields in the `customFields` array, this is a
    standard QuickBooks field that exists for all purchase orders for convenience.
    Developers often use this field for tracking information that doesn't fit into
    other standard QuickBooks fields. Hidden by default in the QuickBooks UI.
    """

    other_custom_field2: Optional[str] = FieldInfo(alias="otherCustomField2", default=None)
    """
    A second built-in custom field for additional information specific to this
    purchase order. Unlike the user-defined fields in the `customFields` array, this
    is a standard QuickBooks field that exists for all purchase orders for
    convenience. Like `otherCustomField1`, developers often use this field for
    tracking information that doesn't fit into other standard QuickBooks fields.
    Hidden by default in the QuickBooks UI.
    """

    ref_number: Optional[str] = FieldInfo(alias="refNumber", default=None)
    """
    The case-sensitive user-defined reference number for this purchase order, which
    can be used to identify the transaction in QuickBooks. This value is not
    required to be unique and can be arbitrarily changed by the QuickBooks user.
    """

    revision_number: str = FieldInfo(alias="revisionNumber")
    """
    The current revision number of this purchase order object, which changes each
    time the object is modified. When updating this object, you must provide the
    most recent `revisionNumber` to ensure you're working with the latest data;
    otherwise, the update will return an error.
    """

    sales_tax_code: Optional[SalesTaxCode] = FieldInfo(alias="salesTaxCode", default=None)
    """
    The sales-tax code associated with this purchase order, determining whether
    items bought from this vendor are taxable or non-taxable. It's used to assign a
    default tax status to all transactions for this purchase order. Default codes
    include "Non" (non-taxable) and "Tax" (taxable), but custom codes can also be
    created in QuickBooks. If QuickBooks is not set up to charge sales tax (via the
    "Do You Charge Sales Tax?" preference), it will assign the default non-taxable
    code to all sales.
    """

    shipment_origin: Optional[str] = FieldInfo(alias="shipmentOrigin", default=None)
    """
    The origin location from where the product associated with this purchase order
    is shipped. This is the point at which ownership and liability for goods
    transfer from seller to buyer. Internally, QuickBooks uses the term "FOB" for
    this field, which stands for "freight on board". This field is informational and
    has no accounting implications.
    """

    shipping_address: Optional[Address] = FieldInfo(alias="shippingAddress", default=None)
    """The purchase order's shipping address."""

    shipping_method: Optional[ShippingMethod] = FieldInfo(alias="shippingMethod", default=None)
    """
    The shipping method used for this purchase order, such as standard mail or
    overnight delivery.
    """

    ship_to_entity: Optional[ShipToEntity] = FieldInfo(alias="shipToEntity", default=None)
    """
    The customer, vendor, employee, or other entity to whom this purchase order is
    to be shipped.
    """

    terms: Optional[Terms] = None
    """
    The purchase order's payment terms, defining when payment is due and any
    applicable discounts.
    """

    total_amount: Optional[str] = FieldInfo(alias="totalAmount", default=None)
    """
    The total monetary amount of this purchase order, represented as a decimal
    string.
    """

    total_amount_in_home_currency: Optional[str] = FieldInfo(alias="totalAmountInHomeCurrency", default=None)
    """
    The total monetary amount for this purchase order converted to the home currency
    of the QuickBooks company file. Represented as a decimal string.
    """

    transaction_date: date = FieldInfo(alias="transactionDate")
    """The date of this purchase order, in ISO 8601 format (YYYY-MM-DD)."""

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when this purchase order was last updated, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """

    vendor: Vendor
    """The vendor who sent this purchase order for goods or services purchased."""

    vendor_address: Optional[Address] = FieldInfo(alias="vendorAddress", default=None)
    """The address of the vendor who sent this purchase order."""

    vendor_message: Optional[str] = FieldInfo(alias="vendorMessage", default=None)
    """A message to be printed on this purchase order for the vendor to read."""
