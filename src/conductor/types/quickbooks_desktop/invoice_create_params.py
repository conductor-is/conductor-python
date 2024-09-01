# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
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

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    accounts_receivable_account_id: Annotated[str, PropertyInfo(alias="accountsReceivableAccountId")]

    billing_address: Annotated[BillingAddress, PropertyInfo(alias="billingAddress")]

    class_id: Annotated[str, PropertyInfo(alias="classId")]
    """The class associated with this object.

    Classes can be used to categorize objects or transactions by department,
    location, or other meaningful segments.
    """

    customer_message_id: Annotated[str, PropertyInfo(alias="customerMessageId")]

    customer_sales_tax_code_id: Annotated[str, PropertyInfo(alias="customerSalesTaxCodeId")]

    due_date: Annotated[str, PropertyInfo(alias="dueDate")]

    exchange_rate: Annotated[float, PropertyInfo(alias="exchangeRate")]

    external_id: Annotated[str, PropertyInfo(alias="externalId")]
    """
    An arbitrary globally unique identifier (GUID) the developer can provide to
    track this object in their own system. This value must be formatted as a GUID;
    otherwise, QuickBooks will return an error.
    """

    invoice_line_groups: Annotated[Iterable[InvoiceLineGroup], PropertyInfo(alias="invoiceLineGroups")]

    invoice_lines: Annotated[Iterable[InvoiceLine], PropertyInfo(alias="invoiceLines")]

    is_finance_charge: Annotated[bool, PropertyInfo(alias="isFinanceCharge")]

    is_pending: Annotated[bool, PropertyInfo(alias="isPending")]

    is_tax_included: Annotated[bool, PropertyInfo(alias="isTaxIncluded")]

    is_to_be_emailed: Annotated[bool, PropertyInfo(alias="isToBeEmailed")]

    is_to_be_printed: Annotated[bool, PropertyInfo(alias="isToBePrinted")]

    item_sales_tax_id: Annotated[str, PropertyInfo(alias="itemSalesTaxId")]

    link_to_transaction_ids: Annotated[List[str], PropertyInfo(alias="linkToTransactionIds")]

    memo: str

    other_field: Annotated[str, PropertyInfo(alias="otherField")]

    purchase_order_number: Annotated[str, PropertyInfo(alias="purchaseOrderNumber")]

    ref_number: Annotated[str, PropertyInfo(alias="refNumber")]
    """The user-defined identifier for the transaction.

    It is not required to be unique and can be arbitrarily changed by the QuickBooks
    user. Case sensitive.
    """

    sales_representative_id: Annotated[str, PropertyInfo(alias="salesRepresentativeId")]

    set_credit: Annotated[Iterable[SetCredit], PropertyInfo(alias="setCredit")]

    shipping_address: Annotated[ShippingAddress, PropertyInfo(alias="shippingAddress")]

    shipping_date: Annotated[str, PropertyInfo(alias="shippingDate")]

    shipping_method_id: Annotated[str, PropertyInfo(alias="shippingMethodId")]

    shipping_origin: Annotated[str, PropertyInfo(alias="shippingOrigin")]

    template_id: Annotated[str, PropertyInfo(alias="templateId")]

    terms_id: Annotated[str, PropertyInfo(alias="termsId")]

    transaction_date: Annotated[str, PropertyInfo(alias="transactionDate")]


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
