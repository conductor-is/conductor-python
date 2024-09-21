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
    "InvoiceLineGroupInvoiceLineSalesTaxCode",
    "InvoiceLineGroupItemGroup",
    "InvoiceLineGroupOverrideUnitOfMeasure",
    "InvoiceLine",
    "InvoiceLineClass",
    "InvoiceLineCustomField",
    "InvoiceLineInventorySite",
    "InvoiceLineInventorySiteLocation",
    "InvoiceLineItem",
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
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical, case-insensitive name of this object, including its full path
    in the QuickBooks list structure. Names are separated by colons (e.g.,
    "Parent:Child:Grandchild").
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
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical, case-insensitive name of this object, including its full path
    in the QuickBooks list structure. Names are separated by colons (e.g.,
    "Parent:Child:Grandchild").
    """


class Currency(BaseModel):
    id: Optional[str] = None
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical, case-insensitive name of this object, including its full path
    in the QuickBooks list structure. Names are separated by colons (e.g.,
    "Parent:Child:Grandchild").
    """


class Customer(BaseModel):
    id: Optional[str] = None
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical, case-insensitive name of this object, including its full path
    in the QuickBooks list structure. Names are separated by colons (e.g.,
    "Parent:Child:Grandchild").
    """


class CustomerMessage(BaseModel):
    id: Optional[str] = None
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical, case-insensitive name of this object, including its full path
    in the QuickBooks list structure. Names are separated by colons (e.g.,
    "Parent:Child:Grandchild").
    """


class CustomerSalesTaxCode(BaseModel):
    id: Optional[str] = None
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical, case-insensitive name of this object, including its full path
    in the QuickBooks list structure. Names are separated by colons (e.g.,
    "Parent:Child:Grandchild").
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
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical, case-insensitive name of this object, including its full path
    in the QuickBooks list structure. Names are separated by colons (e.g.,
    "Parent:Child:Grandchild").
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
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical, case-insensitive name of this object, including its full path
    in the QuickBooks list structure. Names are separated by colons (e.g.,
    "Parent:Child:Grandchild").
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
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical, case-insensitive name of this object, including its full path
    in the QuickBooks list structure. Names are separated by colons (e.g.,
    "Parent:Child:Grandchild").
    """


class InvoiceLineGroupInvoiceLineInventorySiteLocation(BaseModel):
    id: Optional[str] = None
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical, case-insensitive name of this object, including its full path
    in the QuickBooks list structure. Names are separated by colons (e.g.,
    "Parent:Child:Grandchild").
    """


class InvoiceLineGroupInvoiceLineItem(BaseModel):
    id: Optional[str] = None
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical, case-insensitive name of this object, including its full path
    in the QuickBooks list structure. Names are separated by colons (e.g.,
    "Parent:Child:Grandchild").
    """


class InvoiceLineGroupInvoiceLineSalesTaxCode(BaseModel):
    id: Optional[str] = None
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical, case-insensitive name of this object, including its full path
    in the QuickBooks list structure. Names are separated by colons (e.g.,
    "Parent:Child:Grandchild").
    """


class InvoiceLineGroupInvoiceLine(BaseModel):
    id: str
    """
    The QuickBooks-assigned identifier for this transaction line, unique across all
    transaction lines.
    """

    amount: Optional[str] = None

    class_: Optional[InvoiceLineGroupInvoiceLineClass] = FieldInfo(alias="class", default=None)
    """The class associated with this object.

    Classes can be used to categorize objects or transactions by department,
    location, or other meaningful segments.
    """

    custom_fields: List[InvoiceLineGroupInvoiceLineCustomField] = FieldInfo(alias="customFields")
    """The custom fields added by the user to QuickBooks object as a data extension.

    These fields are not part of the standard QuickBooks object.
    """

    description: Optional[str] = None

    expiration_date: Optional[str] = FieldInfo(alias="expirationDate", default=None)

    inventory_site: Optional[InvoiceLineGroupInvoiceLineInventorySite] = FieldInfo(alias="inventorySite", default=None)

    inventory_site_location: Optional[InvoiceLineGroupInvoiceLineInventorySiteLocation] = FieldInfo(
        alias="inventorySiteLocation", default=None
    )

    item: Optional[InvoiceLineGroupInvoiceLineItem] = None

    lot_number: Optional[str] = FieldInfo(alias="lotNumber", default=None)

    other_field1: Optional[str] = FieldInfo(alias="otherField1", default=None)

    other_field2: Optional[str] = FieldInfo(alias="otherField2", default=None)

    quantity: Optional[float] = None

    rate: Optional[str] = None

    rate_percent: Optional[str] = FieldInfo(alias="ratePercent", default=None)

    sales_tax_code: Optional[InvoiceLineGroupInvoiceLineSalesTaxCode] = FieldInfo(alias="salesTaxCode", default=None)
    """The sales tax code, indicating whether related items are taxable or non-taxable.

    Two default codes are 'Non' (non-taxable) and 'Tax' (taxable). If QuickBooks is
    not set up to charge sales tax, it will assign the default non-taxable code to
    all sales.
    """

    serial_number: Optional[str] = FieldInfo(alias="serialNumber", default=None)

    service_date: Optional[str] = FieldInfo(alias="serviceDate", default=None)

    unit_of_measure: Optional[str] = FieldInfo(alias="unitOfMeasure", default=None)


class InvoiceLineGroupItemGroup(BaseModel):
    id: Optional[str] = None
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical, case-insensitive name of this object, including its full path
    in the QuickBooks list structure. Names are separated by colons (e.g.,
    "Parent:Child:Grandchild").
    """


class InvoiceLineGroupOverrideUnitOfMeasure(BaseModel):
    id: Optional[str] = None
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical, case-insensitive name of this object, including its full path
    in the QuickBooks list structure. Names are separated by colons (e.g.,
    "Parent:Child:Grandchild").
    """


class InvoiceLineGroup(BaseModel):
    id: str
    """
    The QuickBooks-assigned identifier for this transaction line, unique across all
    transaction lines.
    """

    custom_fields: List[InvoiceLineGroupCustomField] = FieldInfo(alias="customFields")
    """The custom fields added by the user to QuickBooks object as a data extension.

    These fields are not part of the standard QuickBooks object.
    """

    description: Optional[str] = None

    invoice_lines: List[InvoiceLineGroupInvoiceLine] = FieldInfo(alias="invoiceLines")

    is_print_items_in_group: bool = FieldInfo(alias="isPrintItemsInGroup")

    item_group: InvoiceLineGroupItemGroup = FieldInfo(alias="itemGroup")

    override_unit_of_measure: Optional[InvoiceLineGroupOverrideUnitOfMeasure] = FieldInfo(
        alias="overrideUnitOfMeasure", default=None
    )

    quantity: Optional[float] = None

    total_amount: str = FieldInfo(alias="totalAmount")

    unit_of_measure: Optional[str] = FieldInfo(alias="unitOfMeasure", default=None)


class InvoiceLineClass(BaseModel):
    id: Optional[str] = None
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical, case-insensitive name of this object, including its full path
    in the QuickBooks list structure. Names are separated by colons (e.g.,
    "Parent:Child:Grandchild").
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
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical, case-insensitive name of this object, including its full path
    in the QuickBooks list structure. Names are separated by colons (e.g.,
    "Parent:Child:Grandchild").
    """


class InvoiceLineInventorySiteLocation(BaseModel):
    id: Optional[str] = None
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical, case-insensitive name of this object, including its full path
    in the QuickBooks list structure. Names are separated by colons (e.g.,
    "Parent:Child:Grandchild").
    """


class InvoiceLineItem(BaseModel):
    id: Optional[str] = None
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical, case-insensitive name of this object, including its full path
    in the QuickBooks list structure. Names are separated by colons (e.g.,
    "Parent:Child:Grandchild").
    """


class InvoiceLineSalesTaxCode(BaseModel):
    id: Optional[str] = None
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical, case-insensitive name of this object, including its full path
    in the QuickBooks list structure. Names are separated by colons (e.g.,
    "Parent:Child:Grandchild").
    """


class InvoiceLine(BaseModel):
    id: str
    """
    The QuickBooks-assigned identifier for this transaction line, unique across all
    transaction lines.
    """

    amount: Optional[str] = None

    class_: Optional[InvoiceLineClass] = FieldInfo(alias="class", default=None)
    """The class associated with this object.

    Classes can be used to categorize objects or transactions by department,
    location, or other meaningful segments.
    """

    custom_fields: List[InvoiceLineCustomField] = FieldInfo(alias="customFields")
    """The custom fields added by the user to QuickBooks object as a data extension.

    These fields are not part of the standard QuickBooks object.
    """

    description: Optional[str] = None

    expiration_date: Optional[str] = FieldInfo(alias="expirationDate", default=None)

    inventory_site: Optional[InvoiceLineInventorySite] = FieldInfo(alias="inventorySite", default=None)

    inventory_site_location: Optional[InvoiceLineInventorySiteLocation] = FieldInfo(
        alias="inventorySiteLocation", default=None
    )

    item: Optional[InvoiceLineItem] = None

    lot_number: Optional[str] = FieldInfo(alias="lotNumber", default=None)

    other_field1: Optional[str] = FieldInfo(alias="otherField1", default=None)

    other_field2: Optional[str] = FieldInfo(alias="otherField2", default=None)

    quantity: Optional[float] = None

    rate: Optional[str] = None

    rate_percent: Optional[str] = FieldInfo(alias="ratePercent", default=None)

    sales_tax_code: Optional[InvoiceLineSalesTaxCode] = FieldInfo(alias="salesTaxCode", default=None)
    """The sales tax code, indicating whether related items are taxable or non-taxable.

    Two default codes are 'Non' (non-taxable) and 'Tax' (taxable). If QuickBooks is
    not set up to charge sales tax, it will assign the default non-taxable code to
    all sales.
    """

    serial_number: Optional[str] = FieldInfo(alias="serialNumber", default=None)

    service_date: Optional[str] = FieldInfo(alias="serviceDate", default=None)

    unit_of_measure: Optional[str] = FieldInfo(alias="unitOfMeasure", default=None)


class ItemSalesTax(BaseModel):
    id: Optional[str] = None
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical, case-insensitive name of this object, including its full path
    in the QuickBooks list structure. Names are separated by colons (e.g.,
    "Parent:Child:Grandchild").
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
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical, case-insensitive name of this object, including its full path
    in the QuickBooks list structure. Names are separated by colons (e.g.,
    "Parent:Child:Grandchild").
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
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical, case-insensitive name of this object, including its full path
    in the QuickBooks list structure. Names are separated by colons (e.g.,
    "Parent:Child:Grandchild").
    """


class Terms(BaseModel):
    id: Optional[str] = None
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical, case-insensitive name of this object, including its full path
    in the QuickBooks list structure. Names are separated by colons (e.g.,
    "Parent:Child:Grandchild").
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
    """
    The invoice's class, used for categorization (e.g., by department, location, or
    type of work).
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
    """The customer or customer job that this invoice is for."""

    customer_message: Optional[CustomerMessage] = FieldInfo(alias="customerMessage", default=None)
    """The message to display to the customer on the invoice."""

    customer_sales_tax_code: Optional[CustomerSalesTaxCode] = FieldInfo(alias="customerSalesTaxCode", default=None)
    """
    The sales-tax code for items sold to the `customer` of this invoice, indicating
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
    in QuickBooks Desktop.
    """

    is_to_be_printed: Optional[bool] = FieldInfo(alias="isToBePrinted", default=None)
    """Indicates whether this invoice is queued for printing.

    If set to `true`, the invoice will appear in the list of documents to be printed
    in QuickBooks Desktop.
    """

    item_sales_tax: Optional[ItemSalesTax] = FieldInfo(alias="itemSalesTax", default=None)
    """The sales tax item for items associated with this invoice.

    A sales-tax item represents a single sales tax that is collected at a specified
    rate and paid to a single agency. For complex tax situations, a zero percent tax
    item named "Tax Calculated On Invoice" may be used, indicating that taxes are
    applied manually on the invoice.
    """

    linked_transactions: List[LinkedTransaction] = FieldInfo(alias="linkedTransactions")
    """
    The invoice's linked transactions, such as payments applied, credits used, or
    linked purchase orders.
    """

    memo: Optional[str] = None
    """A memo or note for this invoice, as entered by the user.

    This appears in reports, but not on the invoice.
    """

    object_type: Literal["qbd_invoice"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_invoice"`."""

    other_custom_field: Optional[str] = FieldInfo(alias="otherCustomField", default=None)
    """A custom field for additional information associated with this invoice.

    Developers often use this field for tracking information that is not part of the
    standard QuickBooks object model. The fields can be written to and modified, but
    its visibility to the user in the QuickBooks UI depends on the transaction
    template settings. Note that each of this invoice's line items have similar
    fields available, `otherCustomField1` and `otherCustomField2`, but this field
    specific to the invoice as a whole.
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
