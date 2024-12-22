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
    "Estimate",
    "Class",
    "Currency",
    "Customer",
    "CustomerMessage",
    "DocumentTemplate",
    "LineGroup",
    "LineGroupItemGroup",
    "LineGroupLine",
    "LineGroupLineClass",
    "LineGroupLineInventorySite",
    "LineGroupLineInventorySiteLocation",
    "LineGroupLineItem",
    "LineGroupLineOverrideUnitOfMeasureSet",
    "LineGroupLineSalesTaxCode",
    "LineGroupOverrideUnitOfMeasureSet",
    "Line",
    "LineClass",
    "LineInventorySite",
    "LineInventorySiteLocation",
    "LineItem",
    "LineOverrideUnitOfMeasureSet",
    "LineSalesTaxCode",
    "SalesRepresentative",
    "SalesTaxCode",
    "SalesTaxItem",
    "Terms",
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
    """The unique identifier assigned by QuickBooks to this estimate line.

    This ID is unique across all transaction line types.
    """

    amount: Optional[str] = None
    """The monetary amount of this estimate line, represented as a decimal string.

    If both `quantity` and `rate` are specified but not `amount`, QuickBooks will
    use them to calculate `amount`. If `amount`, `rate`, and `quantity` are all
    unspecified, then QuickBooks will calculate `amount` based on a `quantity` of
    `1` and the suggested `rate`. This field cannot be cleared.
    """

    class_: Optional[LineGroupLineClass] = FieldInfo(alias="class", default=None)
    """The estimate line's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default. If a class is specified for the entire parent transaction, it is
    automatically applied to all estimate lines unless overridden here, at the
    transaction line level.
    """

    custom_fields: List[CustomField] = FieldInfo(alias="customFields")
    """
    The custom fields for the estimate line object, added as user-defined data
    extensions, not included in the standard QuickBooks object.
    """

    description: Optional[str] = None
    """A description of this estimate line."""

    inventory_site: Optional[LineGroupLineInventorySite] = FieldInfo(alias="inventorySite", default=None)
    """
    The site location where inventory for the item associated with this estimate
    line is stored.
    """

    inventory_site_location: Optional[LineGroupLineInventorySiteLocation] = FieldInfo(
        alias="inventorySiteLocation", default=None
    )
    """
    The specific location (e.g., bin or shelf) within the inventory site where the
    item associated with this estimate line is stored.
    """

    item: Optional[LineGroupLineItem] = None
    """The item associated with this estimate line.

    This can refer to any good or service that the business buys or sells, including
    item types such as a service item, inventory item, or special calculation item
    like a discount item or sales-tax item.
    """

    markup_rate: Optional[str] = FieldInfo(alias="markupRate", default=None)
    """
    The markup that will be passed on to the customer for this item on this estimate
    line. `amount = (quantity * rate) * (1 + markupRate)`
    """

    markup_rate_percent: Optional[str] = FieldInfo(alias="markupRatePercent", default=None)
    """
    The markup, expressed as a percentage, that will be passed on to the customer
    for this item on this estimate line.
    `amount = (quantity * rate) * (1 + markupRatePercent/100)`
    """

    object_type: Literal["qbd_estimate_line"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_estimate_line"`."""

    other_custom_field1: Optional[str] = FieldInfo(alias="otherCustomField1", default=None)
    """
    A built-in custom field for additional information specific to this estimate
    line. Unlike the user-defined fields in the `customFields` array, this is a
    standard QuickBooks field that exists for all estimate lines for convenience.
    Developers often use this field for tracking information that doesn't fit into
    other standard QuickBooks fields. Hidden by default in the QuickBooks UI.
    """

    other_custom_field2: Optional[str] = FieldInfo(alias="otherCustomField2", default=None)
    """
    A second built-in custom field for additional information specific to this
    estimate line. Unlike the user-defined fields in the `customFields` array, this
    is a standard QuickBooks field that exists for all estimate lines for
    convenience. Like `otherCustomField1`, developers often use this field for
    tracking information that doesn't fit into other standard QuickBooks fields.
    Hidden by default in the QuickBooks UI.
    """

    override_unit_of_measure_set: Optional[LineGroupLineOverrideUnitOfMeasureSet] = FieldInfo(
        alias="overrideUnitOfMeasureSet", default=None
    )
    """
    Specifies an alternative unit-of-measure set when updating this estimate line's
    `unitOfMeasure` field (e.g., "pound" or "kilogram"). This allows you to select
    units from a different set than the item's default unit-of-measure set, which
    remains unchanged on the item itself. The override applies only to this specific
    line. For example, you can sell an item typically measured in volume units using
    weight units in a specific transaction by specifying a different unit-of-measure
    set with this field.
    """

    quantity: Optional[float] = None
    """The quantity of the item associated with this estimate line.

    This field cannot be cleared.
    """

    rate: Optional[str] = None
    """The price per unit for this estimate line.

    If both `rate` and `amount` are specified, `rate` will be ignored. If both
    `quantity` and `amount` are specified but not `rate`, QuickBooks will use them
    to calculate `rate`. Represented as a decimal string. This field cannot be
    cleared.
    """

    rate_percent: Optional[str] = FieldInfo(alias="ratePercent", default=None)
    """The price of this estimate line expressed as a percentage.

    Typically used for discount or markup items.
    """

    sales_tax_code: Optional[LineGroupLineSalesTaxCode] = FieldInfo(alias="salesTaxCode", default=None)
    """
    The sales-tax code associated with this estimate line, determining whether items
    sold to this customer are taxable or non-taxable. It's used to assign a default
    tax status to all transactions for this estimate line. Default codes include
    "Non" (non-taxable) and "Tax" (taxable), but custom codes can also be created in
    QuickBooks. If QuickBooks is not set up to charge sales tax (via the "Do You
    Charge Sales Tax?" preference), it will assign the default non-taxable code to
    all sales.
    """

    unit_of_measure: Optional[str] = FieldInfo(alias="unitOfMeasure", default=None)
    """The unit-of-measure used for the `quantity` in this estimate line.

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
    """The unique identifier assigned by QuickBooks to this estimate line group.

    This ID is unique across all transaction line types.
    """

    custom_fields: List[CustomField] = FieldInfo(alias="customFields")
    """
    The custom fields for the estimate line group object, added as user-defined data
    extensions, not included in the standard QuickBooks object.
    """

    description: Optional[str] = None
    """A description of this estimate line group."""

    item_group: LineGroupItemGroup = FieldInfo(alias="itemGroup")
    """
    The estimate line group's item group, representing a predefined set of items
    bundled because they are commonly purchased together or grouped for faster
    entry.
    """

    lines: List[LineGroupLine]
    """
    The estimate line group's line items, each representing a single product or
    service quoted.
    """

    object_type: Literal["qbd_estimate_line_group"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_estimate_line_group"`."""

    override_unit_of_measure_set: Optional[LineGroupOverrideUnitOfMeasureSet] = FieldInfo(
        alias="overrideUnitOfMeasureSet", default=None
    )
    """
    Specifies an alternative unit-of-measure set when updating this estimate line
    group's `unitOfMeasure` field (e.g., "pound" or "kilogram"). This allows you to
    select units from a different set than the item's default unit-of-measure set,
    which remains unchanged on the item itself. The override applies only to this
    specific line. For example, you can sell an item typically measured in volume
    units using weight units in a specific transaction by specifying a different
    unit-of-measure set with this field.
    """

    quantity: Optional[float] = None
    """The quantity of the item group associated with this estimate line group.

    This field cannot be cleared.
    """

    should_print_items_in_group: bool = FieldInfo(alias="shouldPrintItemsInGroup")
    """
    Indicates whether the individual items in this estimate line group and their
    separate amounts appear on printed forms.
    """

    total_amount: str = FieldInfo(alias="totalAmount")
    """
    The total monetary amount of this estimate line group, represented as a decimal
    string.
    """

    unit_of_measure: Optional[str] = FieldInfo(alias="unitOfMeasure", default=None)
    """The unit-of-measure used for the `quantity` in this estimate line group.

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
    """The unique identifier assigned by QuickBooks to this estimate line.

    This ID is unique across all transaction line types.
    """

    amount: Optional[str] = None
    """The monetary amount of this estimate line, represented as a decimal string.

    If both `quantity` and `rate` are specified but not `amount`, QuickBooks will
    use them to calculate `amount`. If `amount`, `rate`, and `quantity` are all
    unspecified, then QuickBooks will calculate `amount` based on a `quantity` of
    `1` and the suggested `rate`. This field cannot be cleared.
    """

    class_: Optional[LineClass] = FieldInfo(alias="class", default=None)
    """The estimate line's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default. If a class is specified for the entire parent transaction, it is
    automatically applied to all estimate lines unless overridden here, at the
    transaction line level.
    """

    custom_fields: List[CustomField] = FieldInfo(alias="customFields")
    """
    The custom fields for the estimate line object, added as user-defined data
    extensions, not included in the standard QuickBooks object.
    """

    description: Optional[str] = None
    """A description of this estimate line."""

    inventory_site: Optional[LineInventorySite] = FieldInfo(alias="inventorySite", default=None)
    """
    The site location where inventory for the item associated with this estimate
    line is stored.
    """

    inventory_site_location: Optional[LineInventorySiteLocation] = FieldInfo(
        alias="inventorySiteLocation", default=None
    )
    """
    The specific location (e.g., bin or shelf) within the inventory site where the
    item associated with this estimate line is stored.
    """

    item: Optional[LineItem] = None
    """The item associated with this estimate line.

    This can refer to any good or service that the business buys or sells, including
    item types such as a service item, inventory item, or special calculation item
    like a discount item or sales-tax item.
    """

    markup_rate: Optional[str] = FieldInfo(alias="markupRate", default=None)
    """
    The markup that will be passed on to the customer for this item on this estimate
    line. `amount = (quantity * rate) * (1 + markupRate)`
    """

    markup_rate_percent: Optional[str] = FieldInfo(alias="markupRatePercent", default=None)
    """
    The markup, expressed as a percentage, that will be passed on to the customer
    for this item on this estimate line.
    `amount = (quantity * rate) * (1 + markupRatePercent/100)`
    """

    object_type: Literal["qbd_estimate_line"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_estimate_line"`."""

    other_custom_field1: Optional[str] = FieldInfo(alias="otherCustomField1", default=None)
    """
    A built-in custom field for additional information specific to this estimate
    line. Unlike the user-defined fields in the `customFields` array, this is a
    standard QuickBooks field that exists for all estimate lines for convenience.
    Developers often use this field for tracking information that doesn't fit into
    other standard QuickBooks fields. Hidden by default in the QuickBooks UI.
    """

    other_custom_field2: Optional[str] = FieldInfo(alias="otherCustomField2", default=None)
    """
    A second built-in custom field for additional information specific to this
    estimate line. Unlike the user-defined fields in the `customFields` array, this
    is a standard QuickBooks field that exists for all estimate lines for
    convenience. Like `otherCustomField1`, developers often use this field for
    tracking information that doesn't fit into other standard QuickBooks fields.
    Hidden by default in the QuickBooks UI.
    """

    override_unit_of_measure_set: Optional[LineOverrideUnitOfMeasureSet] = FieldInfo(
        alias="overrideUnitOfMeasureSet", default=None
    )
    """
    Specifies an alternative unit-of-measure set when updating this estimate line's
    `unitOfMeasure` field (e.g., "pound" or "kilogram"). This allows you to select
    units from a different set than the item's default unit-of-measure set, which
    remains unchanged on the item itself. The override applies only to this specific
    line. For example, you can sell an item typically measured in volume units using
    weight units in a specific transaction by specifying a different unit-of-measure
    set with this field.
    """

    quantity: Optional[float] = None
    """The quantity of the item associated with this estimate line.

    This field cannot be cleared.
    """

    rate: Optional[str] = None
    """The price per unit for this estimate line.

    If both `rate` and `amount` are specified, `rate` will be ignored. If both
    `quantity` and `amount` are specified but not `rate`, QuickBooks will use them
    to calculate `rate`. Represented as a decimal string. This field cannot be
    cleared.
    """

    rate_percent: Optional[str] = FieldInfo(alias="ratePercent", default=None)
    """The price of this estimate line expressed as a percentage.

    Typically used for discount or markup items.
    """

    sales_tax_code: Optional[LineSalesTaxCode] = FieldInfo(alias="salesTaxCode", default=None)
    """
    The sales-tax code associated with this estimate line, determining whether items
    sold to this customer are taxable or non-taxable. It's used to assign a default
    tax status to all transactions for this estimate line. Default codes include
    "Non" (non-taxable) and "Tax" (taxable), but custom codes can also be created in
    QuickBooks. If QuickBooks is not set up to charge sales tax (via the "Do You
    Charge Sales Tax?" preference), it will assign the default non-taxable code to
    all sales.
    """

    unit_of_measure: Optional[str] = FieldInfo(alias="unitOfMeasure", default=None)
    """The unit-of-measure used for the `quantity` in this estimate line.

    Must be a valid unit within the item's available units of measure.
    """


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


class Estimate(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks to this estimate.

    This ID is unique across all transaction types.
    """

    billing_address: Optional[Address] = FieldInfo(alias="billingAddress", default=None)
    """The estimate's billing address."""

    class_: Optional[Class] = FieldInfo(alias="class", default=None)
    """The estimate's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default. A class defined here is automatically used in this estimate's line
    items unless overridden at the line item level.
    """

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when this estimate was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """

    currency: Optional[Currency] = None
    """The estimate's currency.

    For built-in currencies, the name and code are standard international values.
    For user-defined currencies, all values are editable.
    """

    customer: Customer
    """The customer or customer-job associated with this estimate."""

    customer_message: Optional[CustomerMessage] = FieldInfo(alias="customerMessage", default=None)
    """The message to display to the customer on the estimate."""

    custom_fields: List[CustomField] = FieldInfo(alias="customFields")
    """
    The custom fields for the estimate object, added as user-defined data
    extensions, not included in the standard QuickBooks object.
    """

    document_template: Optional[DocumentTemplate] = FieldInfo(alias="documentTemplate", default=None)
    """
    The predefined template in QuickBooks that determines the layout and formatting
    for this estimate when printed or displayed.
    """

    due_date: Optional[date] = FieldInfo(alias="dueDate", default=None)
    """The date by which this estimate must be paid, in ISO 8601 format (YYYY-MM-DD)."""

    exchange_rate: Optional[float] = FieldInfo(alias="exchangeRate", default=None)
    """
    The market exchange rate between this estimate's currency and the home currency
    in QuickBooks at the time of this transaction. Represented as a decimal value
    (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).
    """

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """
    A globally unique identifier (GUID) you can provide for tracking this object in
    your external system.

    **IMPORTANT**: Must be formatted as a valid GUID; otherwise, QuickBooks will
    return an error. This field is immutable and can only be set during object
    creation.
    """

    is_active: bool = FieldInfo(alias="isActive")
    """Indicates whether this estimate is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    """

    is_queued_for_email: Optional[bool] = FieldInfo(alias="isQueuedForEmail", default=None)
    """
    Indicates whether this estimate is included in the queue of documents for
    QuickBooks to email to the customer.
    """

    line_groups: List[LineGroup] = FieldInfo(alias="lineGroups")
    """
    The estimate's line item groups, each representing a predefined set of related
    items.
    """

    lines: List[Line]
    """
    The estimate's line items, each representing a single product or service quoted.
    """

    linked_transactions: List[LinkedTransaction] = FieldInfo(alias="linkedTransactions")
    """
    The estimate's linked transactions, such as payments applied, credits used, or
    associated purchase orders.

    **IMPORTANT**: You must specify the parameter `includeLinkedTransactions` when
    fetching a list of estimates to receive this field because it is not returned by
    default.
    """

    memo: Optional[str] = None
    """
    A memo or note for this estimate that appears in reports, but not on the
    estimate. Use `customerMessage` to add a note to this estimate.
    """

    object_type: Literal["qbd_estimate"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_estimate"`."""

    other_custom_field: Optional[str] = FieldInfo(alias="otherCustomField", default=None)
    """A built-in custom field for additional information specific to this estimate.

    Unlike the user-defined fields in the `customFields` array, this is a standard
    QuickBooks field that exists for all estimates for convenience. Developers often
    use this field for tracking information that doesn't fit into other standard
    QuickBooks fields. Unlike `otherCustomField1` and `otherCustomField2`, which are
    line item fields, this exists at the transaction level. Hidden by default in the
    QuickBooks UI.
    """

    purchase_order_number: Optional[str] = FieldInfo(alias="purchaseOrderNumber", default=None)
    """The customer's Purchase Order (PO) number associated with this estimate.

    This field is often used to cross-reference the estimate with the customer's
    purchasing system.
    """

    ref_number: Optional[str] = FieldInfo(alias="refNumber", default=None)
    """
    The case-sensitive user-defined reference number for this estimate, which can be
    used to identify the transaction in QuickBooks. This value is not required to be
    unique and can be arbitrarily changed by the QuickBooks user.
    """

    revision_number: str = FieldInfo(alias="revisionNumber")
    """
    The current revision number of this estimate object, which changes each time the
    object is modified. When updating this object, you must provide the most recent
    `revisionNumber` to ensure you're working with the latest data; otherwise, the
    update will return an error.
    """

    sales_representative: Optional[SalesRepresentative] = FieldInfo(alias="salesRepresentative", default=None)
    """The estimate's sales representative.

    Sales representatives can be employees, vendors, or other names in QuickBooks.
    """

    sales_tax_code: Optional[SalesTaxCode] = FieldInfo(alias="salesTaxCode", default=None)
    """
    The sales-tax code for items sold to the `customer` of this estimate,
    determining whether items sold to this customer are taxable or non-taxable.
    Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
    can also be created in QuickBooks. If QuickBooks is not set up to charge sales
    tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
    non-taxable code to all sales.
    """

    sales_tax_item: Optional[SalesTaxItem] = FieldInfo(alias="salesTaxItem", default=None)
    """
    The sales-tax item used to calculate the actual tax amount for this estimate's
    transactions by applying a specific tax rate collected for a single tax agency.
    Unlike `salesTaxCode`, which only indicates general taxability, this field
    drives the actual tax calculation and reporting.
    """

    sales_tax_percentage: Optional[str] = FieldInfo(alias="salesTaxPercentage", default=None)
    """
    The sales tax percentage applied to this estimate, represented as a decimal
    string.
    """

    sales_tax_total: Optional[str] = FieldInfo(alias="salesTaxTotal", default=None)
    """
    The total amount of sales tax charged for this estimate, represented as a
    decimal string.
    """

    shipment_origin: Optional[str] = FieldInfo(alias="shipmentOrigin", default=None)
    """
    The origin location from where the product associated with this estimate is
    shipped. This is the point at which ownership and liability for goods transfer
    from seller to buyer. Internally, QuickBooks uses the term "FOB" for this field,
    which stands for "freight on board". This field is informational and has no
    accounting implications.
    """

    shipping_address: Optional[Address] = FieldInfo(alias="shippingAddress", default=None)
    """The estimate's shipping address."""

    subtotal: Optional[str] = None
    """
    The subtotal of this estimate, which is the sum of all estimate lines before
    taxes and discounts are applied, represented as a decimal string.
    """

    terms: Optional[Terms] = None
    """
    The estimate's payment terms, defining when payment is due and any applicable
    discounts.
    """

    total_amount: Optional[str] = FieldInfo(alias="totalAmount", default=None)
    """The total monetary amount of this estimate, represented as a decimal string."""

    total_amount_in_home_currency: Optional[str] = FieldInfo(alias="totalAmountInHomeCurrency", default=None)
    """
    The total monetary amount for this estimate converted to the home currency of
    the QuickBooks company file. Represented as a decimal string.
    """

    transaction_date: date = FieldInfo(alias="transactionDate")
    """The date of this estimate, in ISO 8601 format (YYYY-MM-DD)."""

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when this estimate was last updated, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """
