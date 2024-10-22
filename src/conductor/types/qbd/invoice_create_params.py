# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "InvoiceCreateParams",
    "BillingAddress",
    "InvoiceLineGroup",
    "InvoiceLineGroupCustomField",
    "InvoiceLine",
    "InvoiceLineCustomField",
    "InvoiceLineLinkToTransactionLine",
    "SetCredit",
    "ShippingAddress",
]


class InvoiceCreateParams(TypedDict, total=False):
    customer_id: Required[Annotated[str, PropertyInfo(alias="customerId")]]
    """The customer or customer-job associated with this invoice."""

    transaction_date: Required[Annotated[Union[str, date], PropertyInfo(alias="transactionDate", format="iso8601")]]
    """The date of this invoice, in ISO 8601 format (YYYY-MM-DD)."""

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

    external_id: Annotated[str, PropertyInfo(alias="externalId")]
    """
    A globally unique identifier (GUID) you can provide for tracking this object in
    your external system. Must be formatted as a valid GUID; otherwise, QuickBooks
    will return an error.
    """

    invoice_line_groups: Annotated[Iterable[InvoiceLineGroup], PropertyInfo(alias="invoiceLineGroups")]
    """The invoice's line item groups.

    Each group represents a predefined set of related items.
    """

    invoice_lines: Annotated[Iterable[InvoiceLine], PropertyInfo(alias="invoiceLines")]
    """
    The invoice's invoice lines, each representing a single product or service sold.
    """

    is_finance_charge: Annotated[bool, PropertyInfo(alias="isFinanceCharge")]
    """Whether this invoice includes a finance charge."""

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

    link_to_transaction_ids: Annotated[List[str], PropertyInfo(alias="linkToTransactionIds")]
    """
    IDs of existing transactions that you wish to link to this invoice, such as
    payments applied, credits used, or associated purchase orders. Note that this
    links entire transactions, not individual transaction lines. If you want to link
    individual lines in a transaction, instead use the field `linkToTransactionLine`
    on this invoice's lines, if available.

    You can use both `linkToTransactionIds` (on this invoice) and
    `linkToTransactionLine` (on its transaction lines) as long as they do NOT link
    to the same transaction (otherwise, QuickBooks will return an error). QuickBooks
    will also return an error if you attempt to link a transaction that is empty or
    already closed.

    Note that QuickBooks will not return any information about these links in this
    endpoint's response even though they are created. To see the transactions linked
    via this field, refetch the invoice and check the `linkedTransactions` field. If
    fetching a list of invoices, you must also specify the parameter
    `includeLinkedTransactions` to return the `linkedTransactions` field.
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
    """A note about the address for additional context."""

    postal_code: Annotated[str, PropertyInfo(alias="postalCode")]
    """The postal code or ZIP code of the address."""

    state: str
    """The state, county, province, or region name of the address."""


class InvoiceLineGroupCustomField(TypedDict, total=False):
    name: Required[str]
    """The name of the custom field, unique for the specified `ownerId`.

    For public custom fields, this name is visible as a label in the QuickBooks UI.
    """

    owner_id: Required[Annotated[str, PropertyInfo(alias="ownerId")]]
    """
    The identifier of the owner of the custom field, which QuickBooks internally
    calls a "data extension". For public custom fields visible in the UI, such as
    those added by the QuickBooks user, this is always "0". For private custom
    fields that are only visible to the application that created them, this is a
    valid GUID identifying the owning application. Internally, Conductor always
    fetches all public custom fields (those with an `ownerId` of "0") for all
    objects.
    """

    value: Required[str]
    """The value of the custom field.

    The maximum length depends on the field's data type.
    """


class InvoiceLineGroup(TypedDict, total=False):
    item_group_id: Required[Annotated[str, PropertyInfo(alias="itemGroupId")]]
    """
    The invoice line group's item group, representing a predefined set of items
    bundled because they are commonly purchased together or grouped for faster
    entry.
    """

    custom_fields: Annotated[Iterable[InvoiceLineGroupCustomField], PropertyInfo(alias="customFields")]
    """
    The custom fields for the invoice line group object, added as user-defined data
    extensions, not included in the standard QuickBooks object.
    """

    inventory_site_id: Annotated[str, PropertyInfo(alias="inventorySiteId")]
    """
    The site location where inventory for the item group associated with this
    invoice line group is stored.
    """

    inventory_site_location_id: Annotated[str, PropertyInfo(alias="inventorySiteLocationId")]
    """
    The specific location (e.g., bin or shelf) within the inventory site where the
    item group associated with this invoice line group is stored.
    """

    quantity: float
    """The quantity of the item group associated with this invoice line group."""

    unit_of_measure: Annotated[str, PropertyInfo(alias="unitOfMeasure")]
    """The unit of measure used for the `quantity` in this invoice line group.

    Must be a valid unit within the item's available units of measure.
    """


class InvoiceLineCustomField(TypedDict, total=False):
    name: Required[str]
    """The name of the custom field, unique for the specified `ownerId`.

    For public custom fields, this name is visible as a label in the QuickBooks UI.
    """

    owner_id: Required[Annotated[str, PropertyInfo(alias="ownerId")]]
    """
    The identifier of the owner of the custom field, which QuickBooks internally
    calls a "data extension". For public custom fields visible in the UI, such as
    those added by the QuickBooks user, this is always "0". For private custom
    fields that are only visible to the application that created them, this is a
    valid GUID identifying the owning application. Internally, Conductor always
    fetches all public custom fields (those with an `ownerId` of "0") for all
    objects.
    """

    value: Required[str]
    """The value of the custom field.

    The maximum length depends on the field's data type.
    """


class InvoiceLineLinkToTransactionLine(TypedDict, total=False):
    transaction_id: Required[Annotated[str, PropertyInfo(alias="transactionId")]]

    transaction_line_id: Required[Annotated[str, PropertyInfo(alias="transactionLineId")]]


class InvoiceLine(TypedDict, total=False):
    amount: str
    """The monetary amount for this invoice line, represented as a decimal string."""

    class_id: Annotated[str, PropertyInfo(alias="classId")]
    """The invoice line's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default. If a class is specified for the entire parent transaction, it is
    automatically applied to all invoice lines unless overridden here, at the
    transaction line level.
    """

    custom_fields: Annotated[Iterable[InvoiceLineCustomField], PropertyInfo(alias="customFields")]
    """
    The custom fields for the invoice line object, added as user-defined data
    extensions, not included in the standard QuickBooks object.
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

    link_to_transaction_line: Annotated[InvoiceLineLinkToTransactionLine, PropertyInfo(alias="linkToTransactionLine")]
    """An existing transaction line that you wish to link to this invoice line.

    Note that this only links to a single transaction line item, not an entire
    transaction. If you want to link an entire transaction and bring in all its
    lines, instead use the field `linkToTransactionIds` on the parent transaction,
    if available. For invoice lines, you can only link to sales orders; QuickBooks
    does not support linking invoice lines to other transaction types.

    If you use `linkToTransactionLine` on this invoice line, you cannot use the
    field `item` on this line (QuickBooks will return an error) because this field
    brings in all of the item information you need. You can, however, specify
    whatever `quantity` or `rate` that you want, or any other transaction line
    element other than `item`.

    If the parent transaction supports the `linkToTransactionIds` field, you can use
    both `linkToTransactionLine` (on this invoice line) and `linkToTransactionIds`
    (on its parent transaction) in the same request as long as they do NOT link to
    the same transaction (otherwise, QuickBooks will return an error). QuickBooks
    will also return an error if you attempt to link a transaction that is empty or
    already closed.

    Note that QuickBooks will not return any information about these links in this
    endpoint's response even though they are created. To see the transaction lines
    linked via this field, refetch the parent transaction and check the
    `linkedTransactions` field. If fetching a list of transactions, you must also
    specify the parameter `includeLinkedTransactions` to return the
    `linkedTransactions` field.
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
    """The unit of measure used for the `quantity` in this invoice line.

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
    """A note about the address for additional context."""

    postal_code: Annotated[str, PropertyInfo(alias="postalCode")]
    """The postal code or ZIP code of the address."""

    state: str
    """The state, county, province, or region name of the address."""
