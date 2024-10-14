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
    "InvoiceLineLinkToTransactionLineItem",
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

    Each group represents a predefined set of related items, enabling organized
    presentation of multiple items within the invoice.
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
    links entire transactions, not individual lines. If you want to link individual
    lines in a transaction, use the field `linkToTransaction` on the transaction
    line instead. You can link both at the transaction level and at the transaction
    line level in the same request so long as they do _not_ link to the same
    transaction. Note that QuickBooks will not return any information about these
    links in this endpoint's response even though they are created. If you need to
    retrieve which transactions were linked via this field, refetch the invoice and
    check the `linkedTransactions` field. If fetching a list of invoices, you must
    also specify the parameter `includeLinkedTransactions` to see the
    `linkedTransactions` field.
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
    credit memo. Note that QuickBooks will not return any information about these
    links in this endpoint's response even though they are created. If you need to
    retrieve which transactions were linked via this field, refetch the invoice and
    check the `linkedTransactions` field. If fetching a list of invoices, you must
    also specify the parameter `includeLinkedTransactions` to see the
    `linkedTransactions` field.
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

    owner_id: Required[Annotated[str, PropertyInfo(alias="ownerId")]]

    value: Required[str]


class InvoiceLineGroup(TypedDict, total=False):
    item_group_id: Required[Annotated[str, PropertyInfo(alias="itemGroupId")]]

    custom_fields: Annotated[Iterable[InvoiceLineGroupCustomField], PropertyInfo(alias="customFields")]

    inventory_site_id: Annotated[str, PropertyInfo(alias="inventorySiteId")]

    inventory_site_location_id: Annotated[str, PropertyInfo(alias="inventorySiteLocationId")]

    quantity: float

    unit_of_measure: Annotated[str, PropertyInfo(alias="unitOfMeasure")]


class InvoiceLineCustomField(TypedDict, total=False):
    name: Required[str]

    owner_id: Required[Annotated[str, PropertyInfo(alias="ownerId")]]

    value: Required[str]


class InvoiceLineLinkToTransactionLineItem(TypedDict, total=False):
    transaction_id: Required[Annotated[str, PropertyInfo(alias="transactionId")]]

    transaction_line_id: Required[Annotated[str, PropertyInfo(alias="transactionLineId")]]


class InvoiceLine(TypedDict, total=False):
    amount: str

    class_id: Annotated[str, PropertyInfo(alias="classId")]

    custom_fields: Annotated[Iterable[InvoiceLineCustomField], PropertyInfo(alias="customFields")]

    description: str

    inventory_site_id: Annotated[str, PropertyInfo(alias="inventorySiteId")]

    inventory_site_location_id: Annotated[str, PropertyInfo(alias="inventorySiteLocationId")]

    item_id: Annotated[str, PropertyInfo(alias="itemId")]

    link_to_transaction_line_item: Annotated[
        InvoiceLineLinkToTransactionLineItem, PropertyInfo(alias="linkToTransactionLineItem")
    ]

    lot_number: Annotated[str, PropertyInfo(alias="lotNumber")]

    other_field1: Annotated[str, PropertyInfo(alias="otherField1")]

    other_field2: Annotated[str, PropertyInfo(alias="otherField2")]

    override_item_account_id: Annotated[str, PropertyInfo(alias="overrideItemAccountId")]

    price_level_id: Annotated[str, PropertyInfo(alias="priceLevelId")]

    price_rule_conflict_behavior: Annotated[
        Literal["base_price", "zero"], PropertyInfo(alias="priceRuleConflictBehavior")
    ]
    """Specify how to handle price rule conflicts."""

    quantity: float

    rate: str

    rate_percent: Annotated[str, PropertyInfo(alias="ratePercent")]

    sales_tax_code_id: Annotated[str, PropertyInfo(alias="salesTaxCodeId")]

    serial_number: Annotated[str, PropertyInfo(alias="serialNumber")]

    service_date: Annotated[str, PropertyInfo(alias="serviceDate")]

    unit_of_measure: Annotated[str, PropertyInfo(alias="unitOfMeasure")]


class SetCredit(TypedDict, total=False):
    applied_amount: Required[Annotated[str, PropertyInfo(alias="appliedAmount")]]
    """The amount of credit applied to the transaction.

    For invoices, this is the amount applied to the customer's invoice. For bills,
    this is the amount applied to the vendor bill or credit.
    """

    credit_id: Required[Annotated[str, PropertyInfo(alias="creditId")]]
    """The unique identifier of the credit memo to apply to this transaction."""

    override: bool
    """Whether to override the credit."""


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
