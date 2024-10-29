# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "InvoiceUpdateParams",
    "BillingAddress",
    "InvoiceLineGroup",
    "InvoiceLineGroupInvoiceLine",
    "InvoiceLine",
    "SetCredit",
    "ShippingAddress",
]


class InvoiceUpdateParams(TypedDict, total=False):
    version: Required[str]
    """
    The current version identifier of the invoice you are updating, which you can
    get by fetching the object first. Provide the most recent `version` to ensure
    you're working with the latest data; otherwise, the update will fail.
    """

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    accounts_receivable_account_id: Annotated[str, PropertyInfo(alias="accountsReceivableAccountId")]
    """
    The Accounts Receivable account to which this invoice is assigned, used to track
    the amount owed. If not specified, the default Accounts Receivable account in
    QuickBooks is used. If this invoice is linked to other transactions, make sure
    this `accountsReceivableAccount` matches the `accountsReceivableAccount` used in
    the other transactions.
    """

    billing_address: Annotated[BillingAddress, PropertyInfo(alias="billingAddress")]
    """The invoice's billing address."""

    class_id: Annotated[str, PropertyInfo(alias="classId")]
    """The invoice's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default. A class defined here is automatically used in this invoice's line items
    unless overridden at the line item level.
    """

    customer_id: Annotated[str, PropertyInfo(alias="customerId")]
    """The customer or customer-job associated with this invoice."""

    customer_message_id: Annotated[str, PropertyInfo(alias="customerMessageId")]
    """The message to display to the customer on the invoice."""

    document_template_id: Annotated[str, PropertyInfo(alias="documentTemplateId")]
    """
    The predefined template in QuickBooks that determines the layout and formatting
    for this invoice when printed or displayed.
    """

    due_date: Annotated[Union[str, date], PropertyInfo(alias="dueDate", format="iso8601")]
    """The date by which this invoice must be paid, in ISO 8601 format (YYYY-MM-DD)."""

    exchange_rate: Annotated[float, PropertyInfo(alias="exchangeRate")]
    """
    The market exchange rate between this invoice's currency and the home currency
    in QuickBooks at the time of this transaction. Represented as a decimal value
    (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).
    """

    invoice_line_groups: Annotated[Iterable[InvoiceLineGroup], PropertyInfo(alias="invoiceLineGroups")]
    """
    The invoice's line item groups, each representing a predefined set of related
    items.

    IMPORTANT: When updating an invoice's line item groups, this array completely
    REPLACES all existing line item groups for that invoice. To retain any current
    line item groups, include them in this array, even if they have not changed. Any
    line item groups not included will be removed. To add a new line item group,
    include it with its `id` set to `-1`. If you do not wish to modify the line item
    groups, you can omit this field entirely to keep them unchanged.
    """

    invoice_lines: Annotated[Iterable[InvoiceLine], PropertyInfo(alias="invoiceLines")]
    """The invoice's line items, each representing a single product or service sold.

    IMPORTANT: When updating an invoice's line items, this array completely REPLACES
    all existing line items for that invoice. To retain any current line items,
    include them in this array, even if they have not changed. Any line items not
    included will be removed. To add a new line item, include it with its `id` set
    to `-1`. If you do not wish to modify the line items, you can omit this field
    entirely to keep them unchanged.
    """

    is_pending: Annotated[bool, PropertyInfo(alias="isPending")]
    """Indicates whether this invoice is pending approval or completion.

    If `true`, the invoice is in a draft state and has not been finalized.
    """

    is_to_be_emailed: Annotated[bool, PropertyInfo(alias="isToBeEmailed")]
    """Indicates whether this invoice is queued to be emailed to the customer.

    If set to `true`, the invoice will appear in the list of documents to be emailed
    in QuickBooks.
    """

    is_to_be_printed: Annotated[bool, PropertyInfo(alias="isToBePrinted")]
    """Indicates whether this invoice is queued for printing.

    If set to `true`, the invoice will appear in the list of documents to be printed
    in QuickBooks.
    """

    item_sales_tax_id: Annotated[str, PropertyInfo(alias="itemSalesTaxId")]
    """
    The sales-tax item used to calculate the actual tax amount for this invoice's
    transactions by applying a specific tax rate collected for a single tax agency.
    Unlike `salesTaxCode`, which only indicates general taxability, this field
    drives the actual tax calculation and reporting.
    """

    memo: str
    """A memo or note for this invoice, as entered by the user.

    This appears in reports, but not on the invoice. Use `customerMessage` to add a
    note to the invoice.
    """

    other_custom_field: Annotated[str, PropertyInfo(alias="otherCustomField")]
    """A built-in custom field for additional information specific to this invoice.

    Unlike the user-defined fields in the `customFields` array, this is a standard
    QuickBooks field that exists for all invoices for convenience. Developers often
    use this field for tracking information that doesn't fit into other standard
    QuickBooks fields. Unlike `otherCustomField1` and `otherCustomField2`, which are
    line item fields, this exists at the transaction level. Hidden by default in the
    QuickBooks UI.
    """

    purchase_order_number: Annotated[str, PropertyInfo(alias="purchaseOrderNumber")]
    """The customer's Purchase Order (PO) number associated with this invoice.

    This field is often used to cross-reference the invoice with the customer's
    purchasing system.
    """

    ref_number: Annotated[str, PropertyInfo(alias="refNumber")]
    """
    The case-sensitive user-defined reference number for this invoice, which can be
    used to identify the transaction in QuickBooks. This value is not required to be
    unique and can be arbitrarily changed by the QuickBooks user.
    """

    sales_representative_id: Annotated[str, PropertyInfo(alias="salesRepresentativeId")]
    """The invoice's sales representative.

    Sales representatives can be employees, vendors, or other names in QuickBooks.
    """

    sales_tax_code_id: Annotated[str, PropertyInfo(alias="salesTaxCodeId")]
    """
    The sales-tax code for items sold to the `customer` of this invoice, determining
    whether items sold to this customer are taxable or non-taxable. Default codes
    include "Non" (non-taxable) and "Tax" (taxable), but custom codes can also be
    created in QuickBooks. If QuickBooks is not set up to charge sales tax (via the
    "Do You Charge Sales Tax?" preference), it will assign the default non-taxable
    code to all sales.
    """

    set_credits: Annotated[Iterable[SetCredit], PropertyInfo(alias="setCredits")]
    """Credits to apply to this invoice.

    Applying a credit uses an available credit to reduce the balance of this
    invoice. This creates a link between this invoice and the corresponding existing
    credit memo.

    Note that QuickBooks will not return any information about these links in this
    endpoint's response even though they are created. To see the transactions linked
    via this field, refetch the invoice and check the `linkedTransactions` field. If
    fetching a list of invoices, you must also specify the parameter
    `includeLinkedTransactions` to see the `linkedTransactions` field.
    """

    shipping_address: Annotated[ShippingAddress, PropertyInfo(alias="shippingAddress")]
    """The invoice's shipping address."""

    shipping_date: Annotated[Union[str, date], PropertyInfo(alias="shippingDate", format="iso8601")]
    """
    The date when the products or services for this invoice were shipped or are
    expected to be shipped, in ISO 8601 format (YYYY-MM-DD).
    """

    shipping_method_id: Annotated[str, PropertyInfo(alias="shippingMethodId")]
    """
    The shipping method used for this invoice, such as standard mail or overnight
    delivery.
    """

    shipping_origin: Annotated[str, PropertyInfo(alias="shippingOrigin")]
    """
    The point of origin from where the product associated with this invoice is
    shipped. This is the point at which ownership and liability for goods transfer
    from seller to buyer. Internally, QuickBooks uses the term "FOB" for this field,
    which stands for "freight on board". This field is informational and has no
    accounting implications.
    """

    terms_id: Annotated[str, PropertyInfo(alias="termsId")]
    """
    The invoice's payment terms, defining when payment is due and any applicable
    discounts.
    """

    transaction_date: Annotated[Union[str, date], PropertyInfo(alias="transactionDate", format="iso8601")]
    """The date of this invoice, in ISO 8601 format (YYYY-MM-DD)."""


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


class InvoiceLineGroupInvoiceLine(TypedDict, total=False):
    id: Required[str]
    """
    The QuickBooks-assigned unique identifier of an existing invoice line you wish
    to retain or update. Set this field to `-1` for new invoice lines you wish to
    add.
    """

    amount: str
    """The monetary amount of this invoice line, represented as a decimal string."""

    class_id: Annotated[str, PropertyInfo(alias="classId")]
    """The invoice line's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default. If a class is specified for the entire parent transaction, it is
    automatically applied to all invoice lines unless overridden here, at the
    transaction line level.
    """

    description: str
    """A description of this invoice line."""

    inventory_site_id: Annotated[str, PropertyInfo(alias="inventorySiteId")]
    """
    The site location where inventory for the item associated with this invoice line
    is stored.
    """

    inventory_site_location_id: Annotated[str, PropertyInfo(alias="inventorySiteLocationId")]
    """
    The specific location (e.g., bin or shelf) within the inventory site where the
    item associated with this invoice line is stored.
    """

    item_id: Annotated[str, PropertyInfo(alias="itemId")]
    """The item associated with this invoice line.

    This can refer to any good or service that the business buys or sells, including
    item types such as a service item, inventory item, or special calculation item
    like a discount item or sales-tax item.
    """

    lot_number: Annotated[str, PropertyInfo(alias="lotNumber")]
    """The lot number of the item associated with this invoice line.

    Used for tracking groups of inventory items that are purchased or manufactured
    together.
    """

    other_custom_field1: Annotated[str, PropertyInfo(alias="otherCustomField1")]
    """A built-in custom field for additional information specific to this invoice
    line.

    Unlike the user-defined fields in the `customFields` array, this is a standard
    QuickBooks field that exists for all invoice lines for convenience. Developers
    often use this field for tracking information that doesn't fit into other
    standard QuickBooks fields. Hidden by default in the QuickBooks UI.
    """

    other_custom_field2: Annotated[str, PropertyInfo(alias="otherCustomField2")]
    """
    A second built-in custom field for additional information specific to this
    invoice line. Unlike the user-defined fields in the `customFields` array, this
    is a standard QuickBooks field that exists for all invoice lines for
    convenience. Like `otherCustomField1`, developers often use this field for
    tracking information that doesn't fit into other standard QuickBooks fields.
    Hidden by default in the QuickBooks UI.
    """

    override_item_account_id: Annotated[str, PropertyInfo(alias="overrideItemAccountId")]
    """
    The account to use for this invoice line, overriding the default account
    associated with the item.
    """

    override_unit_of_measure_set_id: Annotated[str, PropertyInfo(alias="overrideUnitOfMeasureSetId")]
    """
    Specifies an alternative unit-of-measure set when updating this invoice line's
    `unitOfMeasure` field (e.g., "pound" or "kilogram"). This allows you to select
    units from a different set than the item's default unit-of-measure set, which
    remains unchanged on the item itself. The override applies only to this specific
    line. For example, you can sell an item typically measured in volume units using
    weight units in a specific transaction by specifying a different unit-of-measure
    set with this field.
    """

    price_level_id: Annotated[str, PropertyInfo(alias="priceLevelId")]
    """
    The custom price level assigned to this invoice line, used to apply custom
    pricing in invoices, sales receipts, sales orders, or credit memos for that
    invoice line. You can override this automatic feature, however, when you create
    the invoices, sales receipts, etc. Notice that the affected sales transactions
    do not list the price level, but instead list the rate for the item, which was
    set using the price level.
    """

    price_rule_conflict_behavior: Annotated[
        Literal["base_price", "zero"], PropertyInfo(alias="priceRuleConflictBehavior")
    ]
    """
    Specifies how to resolve price rule conflicts when adding or modifying this
    invoice line.
    """

    quantity: float
    """The quantity of the item associated with this invoice line."""

    rate: str
    """The price per unit for this invoice line.

    If both `rate` and `amount` are specified, `rate` will be ignored and
    recalculated based on `quantity` and `amount`. If `rate` is not specified,
    QuickBooks will calculate it based on `quantity` and `amount`. Represented as a
    decimal string.
    """

    rate_percent: Annotated[str, PropertyInfo(alias="ratePercent")]
    """The price of this invoice line expressed as a percentage.

    Typically used for discount or markup items.
    """

    sales_tax_code_id: Annotated[str, PropertyInfo(alias="salesTaxCodeId")]
    """
    The sales-tax code associated with this invoice line, determining whether it is
    taxable or non-taxable. It's used to assign a default tax status to all
    transactions for this invoice line. Default codes include "Non" (non-taxable)
    and "Tax" (taxable), but custom codes can also be created in QuickBooks. If
    QuickBooks is not set up to charge sales tax (via the "Do You Charge Sales Tax?"
    preference), it will assign the default non-taxable code to all sales.
    """

    serial_number: Annotated[str, PropertyInfo(alias="serialNumber")]
    """The serial number of the item associated with this invoice line.

    This is used for tracking individual units of serialized inventory items.
    """

    service_date: Annotated[Union[str, date], PropertyInfo(alias="serviceDate", format="iso8601")]
    """
    The date on which the service for this invoice line was or will be performed, in
    ISO 8601 format (YYYY-MM-DD). This is particularly relevant for service items.
    """

    unit_of_measure: Annotated[str, PropertyInfo(alias="unitOfMeasure")]
    """The unit-of-measure used for the `quantity` in this invoice line.

    Must be a valid unit within the item's available units of measure.
    """


class InvoiceLineGroup(TypedDict, total=False):
    id: Required[str]
    """
    The QuickBooks-assigned unique identifier of an existing invoice line group you
    wish to retain or update. Set this field to `-1` for new invoice line groups you
    wish to add.
    """

    invoice_lines: Annotated[Iterable[InvoiceLineGroupInvoiceLine], PropertyInfo(alias="invoiceLines")]
    """
    The invoice line group's line items, each representing a single product or
    service sold.

    IMPORTANT: When updating an invoice line group's line items, this array
    completely REPLACES all existing line items for that invoice line group. To
    retain any current line items, include them in this array, even if they have not
    changed. Any line items not included will be removed. To add a new line item,
    include it with its `id` set to `-1`. If you do not wish to modify the line
    items, you can omit this field entirely to keep them unchanged.
    """

    item_group_id: Annotated[str, PropertyInfo(alias="itemGroupId")]
    """
    The invoice line group's item group, representing a predefined set of items
    bundled because they are commonly purchased together or grouped for faster
    entry.
    """

    override_unit_of_measure_set_id: Annotated[str, PropertyInfo(alias="overrideUnitOfMeasureSetId")]
    """
    Specifies an alternative unit-of-measure set when updating this invoice line
    group's `unitOfMeasure` field (e.g., "pound" or "kilogram"). This allows you to
    select units from a different set than the item's default unit-of-measure set,
    which remains unchanged on the item itself. The override applies only to this
    specific line. For example, you can sell an item typically measured in volume
    units using weight units in a specific transaction by specifying a different
    unit-of-measure set with this field.
    """

    quantity: float
    """The quantity of the item group associated with this invoice line group."""

    unit_of_measure: Annotated[str, PropertyInfo(alias="unitOfMeasure")]
    """The unit-of-measure used for the `quantity` in this invoice line group.

    Must be a valid unit within the item's available units of measure.
    """


class InvoiceLine(TypedDict, total=False):
    id: Required[str]
    """
    The QuickBooks-assigned unique identifier of an existing invoice line you wish
    to retain or update. Set this field to `-1` for new invoice lines you wish to
    add.
    """

    amount: str
    """The monetary amount of this invoice line, represented as a decimal string."""

    class_id: Annotated[str, PropertyInfo(alias="classId")]
    """The invoice line's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default. If a class is specified for the entire parent transaction, it is
    automatically applied to all invoice lines unless overridden here, at the
    transaction line level.
    """

    description: str
    """A description of this invoice line."""

    inventory_site_id: Annotated[str, PropertyInfo(alias="inventorySiteId")]
    """
    The site location where inventory for the item associated with this invoice line
    is stored.
    """

    inventory_site_location_id: Annotated[str, PropertyInfo(alias="inventorySiteLocationId")]
    """
    The specific location (e.g., bin or shelf) within the inventory site where the
    item associated with this invoice line is stored.
    """

    item_id: Annotated[str, PropertyInfo(alias="itemId")]
    """The item associated with this invoice line.

    This can refer to any good or service that the business buys or sells, including
    item types such as a service item, inventory item, or special calculation item
    like a discount item or sales-tax item.
    """

    lot_number: Annotated[str, PropertyInfo(alias="lotNumber")]
    """The lot number of the item associated with this invoice line.

    Used for tracking groups of inventory items that are purchased or manufactured
    together.
    """

    other_custom_field1: Annotated[str, PropertyInfo(alias="otherCustomField1")]
    """A built-in custom field for additional information specific to this invoice
    line.

    Unlike the user-defined fields in the `customFields` array, this is a standard
    QuickBooks field that exists for all invoice lines for convenience. Developers
    often use this field for tracking information that doesn't fit into other
    standard QuickBooks fields. Hidden by default in the QuickBooks UI.
    """

    other_custom_field2: Annotated[str, PropertyInfo(alias="otherCustomField2")]
    """
    A second built-in custom field for additional information specific to this
    invoice line. Unlike the user-defined fields in the `customFields` array, this
    is a standard QuickBooks field that exists for all invoice lines for
    convenience. Like `otherCustomField1`, developers often use this field for
    tracking information that doesn't fit into other standard QuickBooks fields.
    Hidden by default in the QuickBooks UI.
    """

    override_item_account_id: Annotated[str, PropertyInfo(alias="overrideItemAccountId")]
    """
    The account to use for this invoice line, overriding the default account
    associated with the item.
    """

    override_unit_of_measure_set_id: Annotated[str, PropertyInfo(alias="overrideUnitOfMeasureSetId")]
    """
    Specifies an alternative unit-of-measure set when updating this invoice line's
    `unitOfMeasure` field (e.g., "pound" or "kilogram"). This allows you to select
    units from a different set than the item's default unit-of-measure set, which
    remains unchanged on the item itself. The override applies only to this specific
    line. For example, you can sell an item typically measured in volume units using
    weight units in a specific transaction by specifying a different unit-of-measure
    set with this field.
    """

    price_level_id: Annotated[str, PropertyInfo(alias="priceLevelId")]
    """
    The custom price level assigned to this invoice line, used to apply custom
    pricing in invoices, sales receipts, sales orders, or credit memos for that
    invoice line. You can override this automatic feature, however, when you create
    the invoices, sales receipts, etc. Notice that the affected sales transactions
    do not list the price level, but instead list the rate for the item, which was
    set using the price level.
    """

    price_rule_conflict_behavior: Annotated[
        Literal["base_price", "zero"], PropertyInfo(alias="priceRuleConflictBehavior")
    ]
    """
    Specifies how to resolve price rule conflicts when adding or modifying this
    invoice line.
    """

    quantity: float
    """The quantity of the item associated with this invoice line."""

    rate: str
    """The price per unit for this invoice line.

    If both `rate` and `amount` are specified, `rate` will be ignored and
    recalculated based on `quantity` and `amount`. If `rate` is not specified,
    QuickBooks will calculate it based on `quantity` and `amount`. Represented as a
    decimal string.
    """

    rate_percent: Annotated[str, PropertyInfo(alias="ratePercent")]
    """The price of this invoice line expressed as a percentage.

    Typically used for discount or markup items.
    """

    sales_tax_code_id: Annotated[str, PropertyInfo(alias="salesTaxCodeId")]
    """
    The sales-tax code associated with this invoice line, determining whether it is
    taxable or non-taxable. It's used to assign a default tax status to all
    transactions for this invoice line. Default codes include "Non" (non-taxable)
    and "Tax" (taxable), but custom codes can also be created in QuickBooks. If
    QuickBooks is not set up to charge sales tax (via the "Do You Charge Sales Tax?"
    preference), it will assign the default non-taxable code to all sales.
    """

    serial_number: Annotated[str, PropertyInfo(alias="serialNumber")]
    """The serial number of the item associated with this invoice line.

    This is used for tracking individual units of serialized inventory items.
    """

    service_date: Annotated[Union[str, date], PropertyInfo(alias="serviceDate", format="iso8601")]
    """
    The date on which the service for this invoice line was or will be performed, in
    ISO 8601 format (YYYY-MM-DD). This is particularly relevant for service items.
    """

    unit_of_measure: Annotated[str, PropertyInfo(alias="unitOfMeasure")]
    """The unit-of-measure used for the `quantity` in this invoice line.

    Must be a valid unit within the item's available units of measure.
    """


class SetCredit(TypedDict, total=False):
    applied_amount: Required[Annotated[str, PropertyInfo(alias="appliedAmount")]]
    """The amount of credit applied to this transaction.

    This could include customer deposits, payments, or credits. Represented as a
    decimal string.
    """

    credit_id: Required[Annotated[str, PropertyInfo(alias="creditId")]]
    """The unique identifier of the credit memo to apply to this transaction."""

    override: bool
    """Indicates whether to override the credit."""


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