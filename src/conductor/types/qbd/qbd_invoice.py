# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "QbdInvoice",
    "AccountsReceivableAccount",
    "BillingAddress",
    "Class",
    "Currency",
    "Customer",
    "CustomerMessage",
    "CustomerSalesTaxCode",
    "CustomField",
    "DocumentTemplate",
    "InvoiceLineGroup",
    "InvoiceLineGroupCustomField",
    "InvoiceLineGroupInvoiceLine",
    "InvoiceLineGroupInvoiceLineClass",
    "InvoiceLineGroupInvoiceLineCustomField",
    "InvoiceLineGroupInvoiceLineInventorySite",
    "InvoiceLineGroupInvoiceLineInventorySiteLocation",
    "InvoiceLineGroupInvoiceLineItem",
    "InvoiceLineGroupInvoiceLineOverrideUnitOfMeasureSet",
    "InvoiceLineGroupInvoiceLineSalesTaxCode",
    "InvoiceLineGroupItemGroup",
    "InvoiceLineGroupOverrideUnitOfMeasureSet",
    "InvoiceLine",
    "InvoiceLineClass",
    "InvoiceLineCustomField",
    "InvoiceLineInventorySite",
    "InvoiceLineInventorySiteLocation",
    "InvoiceLineItem",
    "InvoiceLineOverrideUnitOfMeasureSet",
    "InvoiceLineSalesTaxCode",
    "ItemSalesTax",
    "LinkedTransaction",
    "SalesRepresentative",
    "ShippingAddress",
    "ShippingMethod",
    "Terms",
]


class AccountsReceivableAccount(BaseModel):
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
    """A note about the address for additional context."""

    postal_code: Optional[str] = FieldInfo(alias="postalCode", default=None)
    """The postal code or ZIP code of the address."""

    state: Optional[str] = None
    """The state, county, province, or region name of the address."""


class Class(BaseModel):
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


class Customer(BaseModel):
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


class CustomerMessage(BaseModel):
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


class CustomerSalesTaxCode(BaseModel):
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


class DocumentTemplate(BaseModel):
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


class InvoiceLineGroupCustomField(BaseModel):
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


class InvoiceLineGroupInvoiceLineClass(BaseModel):
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


class InvoiceLineGroupInvoiceLineCustomField(BaseModel):
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


class InvoiceLineGroupInvoiceLineInventorySite(BaseModel):
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


class InvoiceLineGroupInvoiceLineInventorySiteLocation(BaseModel):
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


class InvoiceLineGroupInvoiceLineItem(BaseModel):
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


class InvoiceLineGroupInvoiceLineOverrideUnitOfMeasureSet(BaseModel):
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


class InvoiceLineGroupInvoiceLineSalesTaxCode(BaseModel):
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


class InvoiceLineGroupInvoiceLine(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks for this invoice line.

    This ID is unique among all transaction line types.
    """

    amount: Optional[str] = None
    """The monetary amount for this invoice line, represented as a decimal string."""

    class_: Optional[InvoiceLineGroupInvoiceLineClass] = FieldInfo(alias="class", default=None)
    """The invoice line's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default. If a class is specified for the entire parent transaction, it is
    automatically applied to all invoice lines unless overridden here, at the
    transaction line level.
    """

    custom_fields: List[InvoiceLineGroupInvoiceLineCustomField] = FieldInfo(alias="customFields")
    """
    The custom fields added by the user to this invoice line object as a data
    extension. These fields are not part of the standard QuickBooks object.
    """

    description: Optional[str] = None
    """A description of this invoice line."""

    expiration_date: Optional[date] = FieldInfo(alias="expirationDate", default=None)
    """
    The expiration date for the serial number or lot number of the item in this
    invoice line, in ISO 8601 format (YYYY-MM-DD). This is particularly relevant for
    perishable or time-sensitive inventory items. Note that this field is only
    supported on QuickBooks Desktop 2023 or later.
    """

    inventory_site: Optional[InvoiceLineGroupInvoiceLineInventorySite] = FieldInfo(alias="inventorySite", default=None)
    """The site location where inventory for the item in this invoice line is stored."""

    inventory_site_location: Optional[InvoiceLineGroupInvoiceLineInventorySiteLocation] = FieldInfo(
        alias="inventorySiteLocation", default=None
    )
    """
    The specific location within the inventory site where the item in this invoice
    line is stored, such as a bin or shelf.
    """

    item: Optional[InvoiceLineGroupInvoiceLineItem] = None
    """The item associated with this invoice line.

    This can refer to any good or service that the business buys or sells, including
    item types such as a service item, inventory item, or special calculation item
    like a discount item or sales-tax item.
    """

    lot_number: Optional[str] = FieldInfo(alias="lotNumber", default=None)
    """The lot number of the item in this invoice line.

    Used for tracking groups of inventory items that are purchased or manufactured
    together.
    """

    object_type: Literal["qbd_invoice_line"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_invoice_line"`."""

    other_custom_field1: Optional[str] = FieldInfo(alias="otherCustomField1", default=None)
    """A built-in custom field for additional information specific to this invoice
    line.

    Unlike the user-defined fields in the `customFields` array, this is a standard
    QuickBooks field that exists for all invoice lines for convenience. Developers
    often use this field for tracking information that doesn't fit into other
    standard QuickBooks fields. Hidden by default in the QuickBooks UI.
    """

    other_custom_field2: Optional[str] = FieldInfo(alias="otherCustomField2", default=None)
    """
    A second built-in custom field for additional information specific to this
    invoice line. Unlike the user-defined fields in the `customFields` array, this
    is a standard QuickBooks field that exists for all invoice lines for
    convenience. Like `otherCustomField1`, developers often use this field for
    tracking information that doesn't fit into other standard QuickBooks fields.
    Hidden by default in the QuickBooks UI.
    """

    override_unit_of_measure_set: Optional[InvoiceLineGroupInvoiceLineOverrideUnitOfMeasureSet] = FieldInfo(
        alias="overrideUnitOfMeasureSet", default=None
    )
    """Specifies an alternative unit of measure set for this specific invoice line.

    This does not change the item's default unit of measure set (which is set on the
    item itself rather than a transaction line), but allows selecting from a
    different set of units for this particular line. For example, an item typically
    measured in volume units could be sold using weight units in a specific
    transaction. The actual unit selection (e.g., "pound" or "kilogram") is made
    separately via the `unitOfMeasure` field.
    """

    quantity: Optional[float] = None
    """The quantity of the item in this invoice line.

    If both `quantity` and `amount` are specified but not `rate`, QuickBooks will
    calculate `rate`. If `quantity` and `rate` are specified but not `amount`,
    QuickBooks will calculate `amount`.
    """

    rate: Optional[str] = None
    """The price per unit for this invoice line.

    If both `rate` and `amount` are specified, `rate` will be ignored and
    recalculated based on `quantity` and `amount`. Represented as a decimal string.
    """

    rate_percent: Optional[str] = FieldInfo(alias="ratePercent", default=None)
    """The price of this invoice line expressed as a percentage.

    Typically used for discount or markup items.
    """

    sales_tax_code: Optional[InvoiceLineGroupInvoiceLineSalesTaxCode] = FieldInfo(alias="salesTaxCode", default=None)
    """
    The sales-tax code associated with this invoice line, determining whether it is
    taxable or non-taxable. It's used to assign a default tax status to all
    transactions for this invoice line. Default codes include "Non" (non-taxable)
    and "Tax" (taxable), but custom codes can also be created in QuickBooks. If
    QuickBooks is not set up to charge sales tax (via the "Do You Charge Sales Tax?"
    preference), it will assign the default non-taxable code to all sales.
    """

    serial_number: Optional[str] = FieldInfo(alias="serialNumber", default=None)
    """The serial number of the item in this invoice line.

    This is used for tracking individual units of serialized inventory items.
    """

    service_date: Optional[date] = FieldInfo(alias="serviceDate", default=None)
    """
    The date on which the service for this invoice line was or will be performed, in
    ISO 8601 format (YYYY-MM-DD). This is particularly relevant for service items.
    """

    unit_of_measure: Optional[str] = FieldInfo(alias="unitOfMeasure", default=None)
    """The unit of measure used for the `quantity` in this invoice line.

    Must be a valid unit within the item's available units of measure.
    """


class InvoiceLineGroupItemGroup(BaseModel):
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


class InvoiceLineGroupOverrideUnitOfMeasureSet(BaseModel):
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


class InvoiceLineGroup(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks for this invoice line group.

    This ID is unique among all transaction line types.
    """

    custom_fields: List[InvoiceLineGroupCustomField] = FieldInfo(alias="customFields")
    """
    The custom fields added by the user to this invoice line group object as a data
    extension. These fields are not part of the standard QuickBooks object.
    """

    description: Optional[str] = None
    """A description of this invoice line group."""

    invoice_lines: List[InvoiceLineGroupInvoiceLine] = FieldInfo(alias="invoiceLines")
    """
    The invoice line group's line items, each representing a single product or
    service sold.
    """

    is_print_items_in_group: bool = FieldInfo(alias="isPrintItemsInGroup")
    """
    Indicates whether a list of this invoice line group's individual items their
    amounts will appear on printed forms.
    """

    item_group: InvoiceLineGroupItemGroup = FieldInfo(alias="itemGroup")
    """The item group associated with this invoice line group.

    Item groups represent items that are grouped together for fast entry.
    """

    object_type: Literal["qbd_invoice_line_group"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_invoice_line_group"`."""

    override_unit_of_measure_set: Optional[InvoiceLineGroupOverrideUnitOfMeasureSet] = FieldInfo(
        alias="overrideUnitOfMeasureSet", default=None
    )
    """
    Specifies an alternative unit of measure set for this specific invoice line
    group. This does not change the item's default unit of measure set (which is set
    on the item itself rather than a transaction line), but allows selecting from a
    different set of units for this particular line. For example, an item typically
    measured in volume units could be sold using weight units in a specific
    transaction. The actual unit selection (e.g., "pound" or "kilogram") is made
    separately via the `unitOfMeasure` field.
    """

    quantity: Optional[float] = None
    """The quantity of the item in this invoice line group.

    If both `quantity` and `amount` are specified but not `rate`, QuickBooks will
    calculate `rate`. If `quantity` and `rate` are specified but not `amount`,
    QuickBooks will calculate `amount`.
    """

    total_amount: str = FieldInfo(alias="totalAmount")
    """
    The total monetary amount for this invoice line group, represented as a decimal
    string.
    """

    unit_of_measure: Optional[str] = FieldInfo(alias="unitOfMeasure", default=None)
    """The unit of measure used for the `quantity` in this invoice line group.

    Must be a valid unit within the item's available units of measure.
    """


class InvoiceLineClass(BaseModel):
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


class InvoiceLineCustomField(BaseModel):
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


class InvoiceLineInventorySite(BaseModel):
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


class InvoiceLineInventorySiteLocation(BaseModel):
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


class InvoiceLineItem(BaseModel):
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


class InvoiceLineOverrideUnitOfMeasureSet(BaseModel):
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


class InvoiceLineSalesTaxCode(BaseModel):
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


class InvoiceLine(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks for this invoice line.

    This ID is unique among all transaction line types.
    """

    amount: Optional[str] = None
    """The monetary amount for this invoice line, represented as a decimal string."""

    class_: Optional[InvoiceLineClass] = FieldInfo(alias="class", default=None)
    """The invoice line's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default. If a class is specified for the entire parent transaction, it is
    automatically applied to all invoice lines unless overridden here, at the
    transaction line level.
    """

    custom_fields: List[InvoiceLineCustomField] = FieldInfo(alias="customFields")
    """
    The custom fields added by the user to this invoice line object as a data
    extension. These fields are not part of the standard QuickBooks object.
    """

    description: Optional[str] = None
    """A description of this invoice line."""

    expiration_date: Optional[date] = FieldInfo(alias="expirationDate", default=None)
    """
    The expiration date for the serial number or lot number of the item in this
    invoice line, in ISO 8601 format (YYYY-MM-DD). This is particularly relevant for
    perishable or time-sensitive inventory items. Note that this field is only
    supported on QuickBooks Desktop 2023 or later.
    """

    inventory_site: Optional[InvoiceLineInventorySite] = FieldInfo(alias="inventorySite", default=None)
    """The site location where inventory for the item in this invoice line is stored."""

    inventory_site_location: Optional[InvoiceLineInventorySiteLocation] = FieldInfo(
        alias="inventorySiteLocation", default=None
    )
    """
    The specific location within the inventory site where the item in this invoice
    line is stored, such as a bin or shelf.
    """

    item: Optional[InvoiceLineItem] = None
    """The item associated with this invoice line.

    This can refer to any good or service that the business buys or sells, including
    item types such as a service item, inventory item, or special calculation item
    like a discount item or sales-tax item.
    """

    lot_number: Optional[str] = FieldInfo(alias="lotNumber", default=None)
    """The lot number of the item in this invoice line.

    Used for tracking groups of inventory items that are purchased or manufactured
    together.
    """

    object_type: Literal["qbd_invoice_line"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_invoice_line"`."""

    other_custom_field1: Optional[str] = FieldInfo(alias="otherCustomField1", default=None)
    """A built-in custom field for additional information specific to this invoice
    line.

    Unlike the user-defined fields in the `customFields` array, this is a standard
    QuickBooks field that exists for all invoice lines for convenience. Developers
    often use this field for tracking information that doesn't fit into other
    standard QuickBooks fields. Hidden by default in the QuickBooks UI.
    """

    other_custom_field2: Optional[str] = FieldInfo(alias="otherCustomField2", default=None)
    """
    A second built-in custom field for additional information specific to this
    invoice line. Unlike the user-defined fields in the `customFields` array, this
    is a standard QuickBooks field that exists for all invoice lines for
    convenience. Like `otherCustomField1`, developers often use this field for
    tracking information that doesn't fit into other standard QuickBooks fields.
    Hidden by default in the QuickBooks UI.
    """

    override_unit_of_measure_set: Optional[InvoiceLineOverrideUnitOfMeasureSet] = FieldInfo(
        alias="overrideUnitOfMeasureSet", default=None
    )
    """Specifies an alternative unit of measure set for this specific invoice line.

    This does not change the item's default unit of measure set (which is set on the
    item itself rather than a transaction line), but allows selecting from a
    different set of units for this particular line. For example, an item typically
    measured in volume units could be sold using weight units in a specific
    transaction. The actual unit selection (e.g., "pound" or "kilogram") is made
    separately via the `unitOfMeasure` field.
    """

    quantity: Optional[float] = None
    """The quantity of the item in this invoice line.

    If both `quantity` and `amount` are specified but not `rate`, QuickBooks will
    calculate `rate`. If `quantity` and `rate` are specified but not `amount`,
    QuickBooks will calculate `amount`.
    """

    rate: Optional[str] = None
    """The price per unit for this invoice line.

    If both `rate` and `amount` are specified, `rate` will be ignored and
    recalculated based on `quantity` and `amount`. Represented as a decimal string.
    """

    rate_percent: Optional[str] = FieldInfo(alias="ratePercent", default=None)
    """The price of this invoice line expressed as a percentage.

    Typically used for discount or markup items.
    """

    sales_tax_code: Optional[InvoiceLineSalesTaxCode] = FieldInfo(alias="salesTaxCode", default=None)
    """
    The sales-tax code associated with this invoice line, determining whether it is
    taxable or non-taxable. It's used to assign a default tax status to all
    transactions for this invoice line. Default codes include "Non" (non-taxable)
    and "Tax" (taxable), but custom codes can also be created in QuickBooks. If
    QuickBooks is not set up to charge sales tax (via the "Do You Charge Sales Tax?"
    preference), it will assign the default non-taxable code to all sales.
    """

    serial_number: Optional[str] = FieldInfo(alias="serialNumber", default=None)
    """The serial number of the item in this invoice line.

    This is used for tracking individual units of serialized inventory items.
    """

    service_date: Optional[date] = FieldInfo(alias="serviceDate", default=None)
    """
    The date on which the service for this invoice line was or will be performed, in
    ISO 8601 format (YYYY-MM-DD). This is particularly relevant for service items.
    """

    unit_of_measure: Optional[str] = FieldInfo(alias="unitOfMeasure", default=None)
    """The unit of measure used for the `quantity` in this invoice line.

    Must be a valid unit within the item's available units of measure.
    """


class ItemSalesTax(BaseModel):
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


class SalesRepresentative(BaseModel):
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
    """A note about the address for additional context."""

    postal_code: Optional[str] = FieldInfo(alias="postalCode", default=None)
    """The postal code or ZIP code of the address."""

    state: Optional[str] = None
    """The state, county, province, or region name of the address."""


class ShippingMethod(BaseModel):
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


class QbdInvoice(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks for this invoice.

    This ID is unique among all transaction types.
    """

    accounts_receivable_account: Optional[AccountsReceivableAccount] = FieldInfo(
        alias="accountsReceivableAccount", default=None
    )
    """
    The Accounts Receivable account to which this invoice is assigned, used to track
    the amount owed. If not specified, the default Accounts Receivable account in
    QuickBooks is used. If this invoice is linked to other transactions, make sure
    this `accountsReceivableAccount` matches the `accountsReceivableAccount` used in
    the other transactions.
    """

    applied_amount: Optional[str] = FieldInfo(alias="appliedAmount", default=None)
    """The amount of credit or payment already applied to this invoice.

    This could include customer deposits, payments, or credits. Represented as a
    decimal string.
    """

    balance_remaining: Optional[str] = FieldInfo(alias="balanceRemaining", default=None)
    """The outstanding balance on this invoice after applying any credits or payments.

    Calculated as (`subtotal` + `salesTaxTotal`) - `appliedAmount`. Represented as a
    decimal string.
    """

    balance_remaining_in_home_currency: Optional[str] = FieldInfo(alias="balanceRemainingInHomeCurrency", default=None)
    """
    The outstanding balance of this invoice converted to the home currency of the
    QuickBooks company file. Represented as a decimal string.
    """

    billing_address: Optional[BillingAddress] = FieldInfo(alias="billingAddress", default=None)
    """The invoice's billing address."""

    class_: Optional[Class] = FieldInfo(alias="class", default=None)
    """The invoice's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default.
    """

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when this invoice was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """

    currency: Optional[Currency] = None
    """The invoice's currency.

    For built-in currencies, the name and code are standard international values.
    For user-defined currencies, all values are editable.
    """

    customer: Customer
    """The customer or customer-job associated with this invoice."""

    customer_message: Optional[CustomerMessage] = FieldInfo(alias="customerMessage", default=None)
    """The message to display to the customer on the invoice."""

    customer_sales_tax_code: Optional[CustomerSalesTaxCode] = FieldInfo(alias="customerSalesTaxCode", default=None)
    """
    The sales-tax code for items sold to the `customer` of this invoice, determining
    whether items sold to this customer are taxable or non-taxable.
    """

    custom_fields: List[CustomField] = FieldInfo(alias="customFields")
    """The custom fields added by the user to this invoice object as a data extension.

    These fields are not part of the standard QuickBooks object.
    """

    document_template: Optional[DocumentTemplate] = FieldInfo(alias="documentTemplate", default=None)
    """
    The predefined template in QuickBooks that determines the layout and formatting
    for this invoice when printed or displayed.
    """

    due_date: Optional[date] = FieldInfo(alias="dueDate", default=None)
    """The date by which this invoice must be paid, in ISO 8601 format (YYYY-MM-DD)."""

    exchange_rate: Optional[float] = FieldInfo(alias="exchangeRate", default=None)
    """
    The market exchange rate between this invoice's currency and the home currency
    in QuickBooks at the time of this transaction. Represented as a decimal value
    (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).
    """

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """
    A developer-assigned globally unique identifier (GUID) for tracking this object
    in external systems. Must be formatted as a valid GUID; otherwise, QuickBooks
    will return an error.
    """

    invoice_line_groups: List[InvoiceLineGroup] = FieldInfo(alias="invoiceLineGroups")
    """The invoice's line item groups.

    Each group represents a predefined set of related items, enabling organized
    presentation of multiple items within the invoice.
    """

    invoice_lines: List[InvoiceLine] = FieldInfo(alias="invoiceLines")
    """The invoice's line items, each representing a single product or service sold."""

    is_finance_charge: Optional[bool] = FieldInfo(alias="isFinanceCharge", default=None)
    """Whether this invoice includes a finance charge."""

    is_paid: Optional[bool] = FieldInfo(alias="isPaid", default=None)
    """Indicates whether this invoice has been paid in full.

    If `true`, `openAmount` will be 0.
    """

    is_pending: Optional[bool] = FieldInfo(alias="isPending", default=None)
    """Indicates whether this invoice is pending approval or completion.

    If `true`, the invoice is in a draft state and has not been finalized.
    """

    is_to_be_emailed: Optional[bool] = FieldInfo(alias="isToBeEmailed", default=None)
    """Indicates whether this invoice is queued to be emailed to the customer.

    If set to `true`, the invoice will appear in the list of documents to be emailed
    in QuickBooks.
    """

    is_to_be_printed: Optional[bool] = FieldInfo(alias="isToBePrinted", default=None)
    """Indicates whether this invoice is queued for printing.

    If set to `true`, the invoice will appear in the list of documents to be printed
    in QuickBooks.
    """

    item_sales_tax: Optional[ItemSalesTax] = FieldInfo(alias="itemSalesTax", default=None)
    """
    The sales-tax item used to calculate the actual tax amount for this invoice's
    transactions by applying a specific tax rate collected for a single tax agency.
    Unlike `salesTaxCode`, which only indicates general taxability, this field
    drives the actual tax calculation and reporting.
    """

    linked_transactions: List[LinkedTransaction] = FieldInfo(alias="linkedTransactions")
    """
    The invoice's linked transactions, such as payments applied, credits used, or
    associated purchase orders.
    """

    memo: Optional[str] = None
    """A memo or note for this invoice, as entered by the user.

    This appears in reports, but not on the invoice.
    """

    object_type: Literal["qbd_invoice"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_invoice"`."""

    other_custom_field: Optional[str] = FieldInfo(alias="otherCustomField", default=None)
    """A built-in custom field for additional information specific to this invoice.

    Unlike the user-defined fields in the `customFields` array, this is a standard
    QuickBooks field that exists for all invoices for convenience. Developers often
    use this field for tracking information that doesn't fit into other standard
    QuickBooks fields. Unlike `otherCustomField1` and `otherCustomField2`, which are
    line item fields, this exists at the transaction level. Hidden by default in the
    QuickBooks UI.
    """

    purchase_order_number: Optional[str] = FieldInfo(alias="purchaseOrderNumber", default=None)
    """The customer's Purchase Order (PO) number associated with this invoice.

    This field is often used to cross-reference the invoice with the customer's
    purchasing system.
    """

    ref_number: Optional[str] = FieldInfo(alias="refNumber", default=None)
    """
    The user-defined reference number for this invoice, which can be used to
    identify the transaction in QuickBooks. This value is not required to be unique
    and can be arbitrarily changed by the QuickBooks user.
    """

    sales_representative: Optional[SalesRepresentative] = FieldInfo(alias="salesRepresentative", default=None)
    """The invoice's sales representative.

    Sales representatives can be employees, vendors, or other names in QuickBooks.
    """

    sales_tax_percentage: Optional[str] = FieldInfo(alias="salesTaxPercentage", default=None)
    """
    The sales tax percentage applied to this invoice, represented as a decimal
    string.
    """

    sales_tax_total: Optional[str] = FieldInfo(alias="salesTaxTotal", default=None)
    """
    The total amount of sales tax charged for this invoice, represented as a decimal
    string.
    """

    shipping_address: Optional[ShippingAddress] = FieldInfo(alias="shippingAddress", default=None)
    """The invoice's shipping address."""

    shipping_date: Optional[date] = FieldInfo(alias="shippingDate", default=None)
    """
    The date when the products or services for this invoice were shipped or are
    expected to be shipped, in ISO 8601 format (YYYY-MM-DD).
    """

    shipping_method: Optional[ShippingMethod] = FieldInfo(alias="shippingMethod", default=None)
    """
    The shipping method used for this invoice, such as standard mail or overnight
    delivery.
    """

    shipping_origin: Optional[str] = FieldInfo(alias="shippingOrigin", default=None)
    """
    The point of origin from where the product associated with this invoice is
    shipped. This is the point at which ownership and liability for goods transfer
    from seller to buyer. Internally, QuickBooks uses the term "FOB" for this field,
    which stands for "freight on board." This field is informational and has no
    accounting implications.
    """

    subtotal: Optional[str] = None
    """
    The subtotal of this invoice, which is the sum of all line items before taxes
    and discounts are applied, represented as a decimal string.
    """

    suggested_discount_amount: Optional[str] = FieldInfo(alias="suggestedDiscountAmount", default=None)
    """
    The suggested discount amount for this invoice, represented as a decimal string.
    """

    suggested_discount_date: Optional[date] = FieldInfo(alias="suggestedDiscountDate", default=None)
    """
    The date when the `suggestedDiscountAmount` for this invoice would apply, in ISO
    8601 format (YYYY-MM-DD).
    """

    terms: Optional[Terms] = None
    """
    The invoice's payment terms, defining when payment is due and any applicable
    discounts.
    """

    transaction_date: date = FieldInfo(alias="transactionDate")
    """The date of this invoice, in ISO 8601 format (YYYY-MM-DD)."""

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when this invoice was last updated, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """

    version: str
    """
    The current version identifier for this invoice, which changes each time the
    object is modified. When updating this object, you must provide the most recent
    `version` to ensure you're working with the latest data; otherwise, the update
    will fail. This value is opaque and should not be interpreted.
    """
