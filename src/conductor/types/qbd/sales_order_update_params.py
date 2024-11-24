# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SalesOrderUpdateParams", "BillingAddress", "LineGroup", "LineGroupLine", "Line", "ShippingAddress"]


class SalesOrderUpdateParams(TypedDict, total=False):
    revision_number: Required[Annotated[str, PropertyInfo(alias="revisionNumber")]]
    """
    The current revision number of the sales order object you are updating, which
    you can get by fetching the object first. Provide the most recent
    `revisionNumber` to ensure you're working with the latest data; otherwise, the
    update will return an error.
    """

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    billing_address: Annotated[BillingAddress, PropertyInfo(alias="billingAddress")]
    """The sales order's billing address."""

    class_id: Annotated[str, PropertyInfo(alias="classId")]
    """The sales order's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default. A class defined here is automatically used in this sales order's line
    items unless overridden at the line item level.
    """

    customer_id: Annotated[str, PropertyInfo(alias="customerId")]
    """The customer or customer-job associated with this sales order."""

    customer_message_id: Annotated[str, PropertyInfo(alias="customerMessageId")]
    """The message to display to the customer on the sales order."""

    document_template_id: Annotated[str, PropertyInfo(alias="documentTemplateId")]
    """
    The predefined template in QuickBooks that determines the layout and formatting
    for this sales order when printed or displayed.
    """

    due_date: Annotated[Union[str, date], PropertyInfo(alias="dueDate", format="iso8601")]
    """
    The date by which this sales order must be paid, in ISO 8601 format
    (YYYY-MM-DD).
    """

    exchange_rate: Annotated[float, PropertyInfo(alias="exchangeRate")]
    """
    The market exchange rate between this sales order's currency and the home
    currency in QuickBooks at the time of this transaction. Represented as a decimal
    value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).
    """

    is_manually_closed: Annotated[bool, PropertyInfo(alias="isManuallyClosed")]
    """
    Indicates whether this sales order has been manually marked as closed, even if
    it has not been invoiced.
    """

    is_queued_for_email: Annotated[bool, PropertyInfo(alias="isQueuedForEmail")]
    """
    Indicates whether this sales order is included in the queue of documents for
    QuickBooks to email to the customer.
    """

    is_queued_for_print: Annotated[bool, PropertyInfo(alias="isQueuedForPrint")]
    """
    Indicates whether this sales order is included in the queue of documents for
    QuickBooks to print.
    """

    line_groups: Annotated[Iterable[LineGroup], PropertyInfo(alias="lineGroups")]
    """
    The sales order's line item groups, each representing a predefined set of
    related items.

    **IMPORTANT**: When updating a sales order's line item groups, this array
    completely REPLACES all existing line item groups for that sales order. To
    retain any current line item groups, include them in this array, even if they
    have not changed. Any line item groups not included will be removed. To add a
    new line item group, include it with its `id` set to `-1`. If you do not wish to
    modify the line item groups, you can omit this field entirely to keep them
    unchanged.
    """

    lines: Iterable[Line]
    """
    The sales order's line items, each representing a single product or service
    ordered.

    **IMPORTANT**: When updating a sales order's line items, this array completely
    REPLACES all existing line items for that sales order. To retain any current
    line items, include them in this array, even if they have not changed. Any line
    items not included will be removed. To add a new line item, include it with its
    `id` set to `-1`. If you do not wish to modify the line items, you can omit this
    field entirely to keep them unchanged.
    """

    memo: str
    """A memo or note for this sales order, as entered by the user."""

    other_custom_field: Annotated[str, PropertyInfo(alias="otherCustomField")]
    """A built-in custom field for additional information specific to this sales order.

    Unlike the user-defined fields in the `customFields` array, this is a standard
    QuickBooks field that exists for all sales orders for convenience. Developers
    often use this field for tracking information that doesn't fit into other
    standard QuickBooks fields. Unlike `otherCustomField1` and `otherCustomField2`,
    which are line item fields, this exists at the transaction level. Hidden by
    default in the QuickBooks UI.
    """

    purchase_order_number: Annotated[str, PropertyInfo(alias="purchaseOrderNumber")]
    """The customer's Purchase Order (PO) number associated with this sales order.

    This field is often used to cross-reference the sales order with the customer's
    purchasing system.
    """

    ref_number: Annotated[str, PropertyInfo(alias="refNumber")]
    """
    The case-sensitive user-defined reference number for this sales order, which can
    be used to identify the transaction in QuickBooks. This value is not required to
    be unique and can be arbitrarily changed by the QuickBooks user.
    """

    sales_channel_name: Annotated[Literal["blank", "ecommerce"], PropertyInfo(alias="salesChannelName")]
    """The type of the sales channel for this sales order."""

    sales_representative_id: Annotated[str, PropertyInfo(alias="salesRepresentativeId")]
    """The sales order's sales representative.

    Sales representatives can be employees, vendors, or other names in QuickBooks.
    """

    sales_store_name: Annotated[str, PropertyInfo(alias="salesStoreName")]
    """The name of the sales store for this sales order."""

    sales_store_type: Annotated[str, PropertyInfo(alias="salesStoreType")]
    """The type of the sales store for this sales order."""

    sales_tax_code_id: Annotated[str, PropertyInfo(alias="salesTaxCodeId")]
    """
    The sales-tax code for items sold to the `customer` of this sales order,
    determining whether items sold to this customer are taxable or non-taxable.
    Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
    can also be created in QuickBooks. If QuickBooks is not set up to charge sales
    tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
    non-taxable code to all sales.
    """

    sales_tax_item_id: Annotated[str, PropertyInfo(alias="salesTaxItemId")]
    """
    The sales-tax item used to calculate the actual tax amount for this sales
    order's transactions by applying a specific tax rate collected for a single tax
    agency. Unlike `salesTaxCode`, which only indicates general taxability, this
    field drives the actual tax calculation and reporting.
    """

    shipment_origin: Annotated[str, PropertyInfo(alias="shipmentOrigin")]
    """
    The origin location from where the product associated with this sales order is
    shipped. This is the point at which ownership and liability for goods transfer
    from seller to buyer. Internally, QuickBooks uses the term "FOB" for this field,
    which stands for "freight on board". This field is informational and has no
    accounting implications.
    """

    shipping_address: Annotated[ShippingAddress, PropertyInfo(alias="shippingAddress")]
    """The sales order's shipping address."""

    shipping_date: Annotated[Union[str, date], PropertyInfo(alias="shippingDate", format="iso8601")]
    """
    The date when the products or services for this sales order were shipped or are
    expected to be shipped, in ISO 8601 format (YYYY-MM-DD).
    """

    shipping_method_id: Annotated[str, PropertyInfo(alias="shippingMethodId")]
    """
    The shipping method used for this sales order, such as standard mail or
    overnight delivery.
    """

    terms_id: Annotated[str, PropertyInfo(alias="termsId")]
    """
    The sales order's payment terms, defining when payment is due and any applicable
    discounts.
    """

    transaction_date: Annotated[Union[str, date], PropertyInfo(alias="transactionDate", format="iso8601")]
    """The date of this sales order, in ISO 8601 format (YYYY-MM-DD)."""


class BillingAddress(TypedDict, total=False):
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
    """
    A note written at the bottom of the address in the form in which it appears,
    such as the invoice form.
    """

    postal_code: Annotated[str, PropertyInfo(alias="postalCode")]
    """The postal code or ZIP code of the address."""

    state: str
    """The state, county, province, or region name of the address."""


class LineGroupLine(TypedDict, total=False):
    id: Required[str]
    """
    The QuickBooks-assigned unique identifier of an existing sales order line you
    wish to retain or update. Set this field to `-1` for new sales order lines you
    wish to add.
    """

    amount: str
    """The monetary amount of this sales order line, represented as a decimal string.

    If both `quantity` and `rate` are specified but not `amount`, QuickBooks will
    use them to calculate `amount`. If `amount`, `rate`, and `quantity` are all
    unspecified, then QuickBooks will calculate `amount` based on a `quantity` of
    `1` and the suggested `rate`.
    """

    class_id: Annotated[str, PropertyInfo(alias="classId")]
    """The sales order line's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default. If a class is specified for the entire parent transaction, it is
    automatically applied to all sales order lines unless overridden here, at the
    transaction line level.
    """

    description: str
    """A description of this sales order line."""

    inventory_site_id: Annotated[str, PropertyInfo(alias="inventorySiteId")]
    """
    The site location where inventory for the item associated with this sales order
    line is stored.
    """

    inventory_site_location_id: Annotated[str, PropertyInfo(alias="inventorySiteLocationId")]
    """
    The specific location (e.g., bin or shelf) within the inventory site where the
    item associated with this sales order line is stored.
    """

    is_manually_closed: Annotated[bool, PropertyInfo(alias="isManuallyClosed")]
    """
    Indicates whether this sales order line has been manually marked as closed, even
    if it has not been invoiced.
    """

    item_id: Annotated[str, PropertyInfo(alias="itemId")]
    """The item associated with this sales order line.

    This can refer to any good or service that the business buys or sells, including
    item types such as a service item, inventory item, or special calculation item
    like a discount item or sales-tax item.
    """

    lot_number: Annotated[str, PropertyInfo(alias="lotNumber")]
    """The lot number of the item associated with this sales order line.

    Used for tracking groups of inventory items that are purchased or manufactured
    together.
    """

    other_custom_field1: Annotated[str, PropertyInfo(alias="otherCustomField1")]
    """
    A built-in custom field for additional information specific to this sales order
    line. Unlike the user-defined fields in the `customFields` array, this is a
    standard QuickBooks field that exists for all sales order lines for convenience.
    Developers often use this field for tracking information that doesn't fit into
    other standard QuickBooks fields. Hidden by default in the QuickBooks UI.
    """

    other_custom_field2: Annotated[str, PropertyInfo(alias="otherCustomField2")]
    """
    A second built-in custom field for additional information specific to this sales
    order line. Unlike the user-defined fields in the `customFields` array, this is
    a standard QuickBooks field that exists for all sales order lines for
    convenience. Like `otherCustomField1`, developers often use this field for
    tracking information that doesn't fit into other standard QuickBooks fields.
    Hidden by default in the QuickBooks UI.
    """

    override_unit_of_measure_set_id: Annotated[str, PropertyInfo(alias="overrideUnitOfMeasureSetId")]
    """
    Specifies an alternative unit-of-measure set when updating this sales order
    line's `unitOfMeasure` field (e.g., "pound" or "kilogram"). This allows you to
    select units from a different set than the item's default unit-of-measure set,
    which remains unchanged on the item itself. The override applies only to this
    specific line. For example, you can sell an item typically measured in volume
    units using weight units in a specific transaction by specifying a different
    unit-of-measure set with this field.
    """

    price_level_id: Annotated[str, PropertyInfo(alias="priceLevelId")]
    """The price level applied to this sales order line.

    This overrides any price level set on the corresponding customer. The resulting
    sales order line will not show this price level, only the final `rate`
    calculated from it.
    """

    price_rule_conflict_strategy: Annotated[
        Literal["base_price", "zero"], PropertyInfo(alias="priceRuleConflictStrategy")
    ]
    """
    Specifies how to resolve price rule conflicts when adding or modifying this
    sales order line.
    """

    quantity: float
    """The quantity of the item associated with this sales order line."""

    rate: str
    """The price per unit for this sales order line.

    If both `rate` and `amount` are specified, `rate` will be ignored. If both
    `quantity` and `amount` are specified but not `rate`, QuickBooks will use them
    to calculate `rate`. Represented as a decimal string.
    """

    rate_percent: Annotated[str, PropertyInfo(alias="ratePercent")]
    """The price of this sales order line expressed as a percentage.

    Typically used for discount or markup items.
    """

    sales_tax_code_id: Annotated[str, PropertyInfo(alias="salesTaxCodeId")]
    """
    The sales-tax code associated with this sales order line, determining whether
    items sold to this customer are taxable or non-taxable. It's used to assign a
    default tax status to all transactions for this sales order line. Default codes
    include "Non" (non-taxable) and "Tax" (taxable), but custom codes can also be
    created in QuickBooks. If QuickBooks is not set up to charge sales tax (via the
    "Do You Charge Sales Tax?" preference), it will assign the default non-taxable
    code to all sales.
    """

    serial_number: Annotated[str, PropertyInfo(alias="serialNumber")]
    """The serial number of the item associated with this sales order line.

    This is used for tracking individual units of serialized inventory items.
    """

    unit_of_measure: Annotated[str, PropertyInfo(alias="unitOfMeasure")]
    """The unit-of-measure used for the `quantity` in this sales order line.

    Must be a valid unit within the item's available units of measure.
    """


class LineGroup(TypedDict, total=False):
    id: Required[str]
    """
    The QuickBooks-assigned unique identifier of an existing sales order line group
    you wish to retain or update. Set this field to `-1` for new sales order line
    groups you wish to add.
    """

    item_group_id: Annotated[str, PropertyInfo(alias="itemGroupId")]
    """
    The sales order line group's item group, representing a predefined set of items
    bundled because they are commonly purchased together or grouped for faster
    entry.
    """

    lines: Iterable[LineGroupLine]
    """
    The sales order line group's line items, each representing a single product or
    service ordered.

    **IMPORTANT**: When updating a sales order line group's line items, this array
    completely REPLACES all existing line items for that sales order line group. To
    retain any current line items, include them in this array, even if they have not
    changed. Any line items not included will be removed. To add a new line item,
    include it with its `id` set to `-1`. If you do not wish to modify the line
    items, you can omit this field entirely to keep them unchanged.
    """

    override_unit_of_measure_set_id: Annotated[str, PropertyInfo(alias="overrideUnitOfMeasureSetId")]
    """
    Specifies an alternative unit-of-measure set when updating this sales order line
    group's `unitOfMeasure` field (e.g., "pound" or "kilogram"). This allows you to
    select units from a different set than the item's default unit-of-measure set,
    which remains unchanged on the item itself. The override applies only to this
    specific line. For example, you can sell an item typically measured in volume
    units using weight units in a specific transaction by specifying a different
    unit-of-measure set with this field.
    """

    quantity: float
    """The quantity of the item group associated with this sales order line group."""

    unit_of_measure: Annotated[str, PropertyInfo(alias="unitOfMeasure")]
    """The unit-of-measure used for the `quantity` in this sales order line group.

    Must be a valid unit within the item's available units of measure.
    """


class Line(TypedDict, total=False):
    id: Required[str]
    """
    The QuickBooks-assigned unique identifier of an existing sales order line you
    wish to retain or update. Set this field to `-1` for new sales order lines you
    wish to add.
    """

    amount: str
    """The monetary amount of this sales order line, represented as a decimal string.

    If both `quantity` and `rate` are specified but not `amount`, QuickBooks will
    use them to calculate `amount`. If `amount`, `rate`, and `quantity` are all
    unspecified, then QuickBooks will calculate `amount` based on a `quantity` of
    `1` and the suggested `rate`.
    """

    class_id: Annotated[str, PropertyInfo(alias="classId")]
    """The sales order line's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default. If a class is specified for the entire parent transaction, it is
    automatically applied to all sales order lines unless overridden here, at the
    transaction line level.
    """

    description: str
    """A description of this sales order line."""

    inventory_site_id: Annotated[str, PropertyInfo(alias="inventorySiteId")]
    """
    The site location where inventory for the item associated with this sales order
    line is stored.
    """

    inventory_site_location_id: Annotated[str, PropertyInfo(alias="inventorySiteLocationId")]
    """
    The specific location (e.g., bin or shelf) within the inventory site where the
    item associated with this sales order line is stored.
    """

    is_manually_closed: Annotated[bool, PropertyInfo(alias="isManuallyClosed")]
    """
    Indicates whether this sales order line has been manually marked as closed, even
    if it has not been invoiced.
    """

    item_id: Annotated[str, PropertyInfo(alias="itemId")]
    """The item associated with this sales order line.

    This can refer to any good or service that the business buys or sells, including
    item types such as a service item, inventory item, or special calculation item
    like a discount item or sales-tax item.
    """

    lot_number: Annotated[str, PropertyInfo(alias="lotNumber")]
    """The lot number of the item associated with this sales order line.

    Used for tracking groups of inventory items that are purchased or manufactured
    together.
    """

    other_custom_field1: Annotated[str, PropertyInfo(alias="otherCustomField1")]
    """
    A built-in custom field for additional information specific to this sales order
    line. Unlike the user-defined fields in the `customFields` array, this is a
    standard QuickBooks field that exists for all sales order lines for convenience.
    Developers often use this field for tracking information that doesn't fit into
    other standard QuickBooks fields. Hidden by default in the QuickBooks UI.
    """

    other_custom_field2: Annotated[str, PropertyInfo(alias="otherCustomField2")]
    """
    A second built-in custom field for additional information specific to this sales
    order line. Unlike the user-defined fields in the `customFields` array, this is
    a standard QuickBooks field that exists for all sales order lines for
    convenience. Like `otherCustomField1`, developers often use this field for
    tracking information that doesn't fit into other standard QuickBooks fields.
    Hidden by default in the QuickBooks UI.
    """

    override_unit_of_measure_set_id: Annotated[str, PropertyInfo(alias="overrideUnitOfMeasureSetId")]
    """
    Specifies an alternative unit-of-measure set when updating this sales order
    line's `unitOfMeasure` field (e.g., "pound" or "kilogram"). This allows you to
    select units from a different set than the item's default unit-of-measure set,
    which remains unchanged on the item itself. The override applies only to this
    specific line. For example, you can sell an item typically measured in volume
    units using weight units in a specific transaction by specifying a different
    unit-of-measure set with this field.
    """

    price_level_id: Annotated[str, PropertyInfo(alias="priceLevelId")]
    """The price level applied to this sales order line.

    This overrides any price level set on the corresponding customer. The resulting
    sales order line will not show this price level, only the final `rate`
    calculated from it.
    """

    price_rule_conflict_strategy: Annotated[
        Literal["base_price", "zero"], PropertyInfo(alias="priceRuleConflictStrategy")
    ]
    """
    Specifies how to resolve price rule conflicts when adding or modifying this
    sales order line.
    """

    quantity: float
    """The quantity of the item associated with this sales order line."""

    rate: str
    """The price per unit for this sales order line.

    If both `rate` and `amount` are specified, `rate` will be ignored. If both
    `quantity` and `amount` are specified but not `rate`, QuickBooks will use them
    to calculate `rate`. Represented as a decimal string.
    """

    rate_percent: Annotated[str, PropertyInfo(alias="ratePercent")]
    """The price of this sales order line expressed as a percentage.

    Typically used for discount or markup items.
    """

    sales_tax_code_id: Annotated[str, PropertyInfo(alias="salesTaxCodeId")]
    """
    The sales-tax code associated with this sales order line, determining whether
    items sold to this customer are taxable or non-taxable. It's used to assign a
    default tax status to all transactions for this sales order line. Default codes
    include "Non" (non-taxable) and "Tax" (taxable), but custom codes can also be
    created in QuickBooks. If QuickBooks is not set up to charge sales tax (via the
    "Do You Charge Sales Tax?" preference), it will assign the default non-taxable
    code to all sales.
    """

    serial_number: Annotated[str, PropertyInfo(alias="serialNumber")]
    """The serial number of the item associated with this sales order line.

    This is used for tracking individual units of serialized inventory items.
    """

    unit_of_measure: Annotated[str, PropertyInfo(alias="unitOfMeasure")]
    """The unit-of-measure used for the `quantity` in this sales order line.

    Must be a valid unit within the item's available units of measure.
    """


class ShippingAddress(TypedDict, total=False):
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
    """
    A note written at the bottom of the address in the form in which it appears,
    such as the invoice form.
    """

    postal_code: Annotated[str, PropertyInfo(alias="postalCode")]
    """The postal code or ZIP code of the address."""

    state: str
    """The state, county, province, or region name of the address."""
