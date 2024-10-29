# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["NonInventoryItemCreateParams", "Barcode", "SalesAndPurchaseDetails", "SalesOrPurchaseDetails"]


class NonInventoryItemCreateParams(TypedDict, total=False):
    name: Required[str]
    """The case-insensitive name of this non-inventory item.

    Not guaranteed to be unique because it does not include the names of its parent
    objects like `fullName` does. For example, two non-inventory items could both
    have the `name` "Printer Ink Cartridge", but they could have unique `fullName`
    values, such as "Office-Supplies:Printer Ink Cartridge" and
    "Miscellaneous:Printer Ink Cartridge".
    """

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    barcode: Barcode
    """The non-inventory item's barcode."""

    class_id: Annotated[str, PropertyInfo(alias="classId")]
    """The non-inventory item's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default.
    """

    external_id: Annotated[str, PropertyInfo(alias="externalId")]
    """
    A globally unique identifier (GUID) you can provide for tracking this object in
    your external system. Must be formatted as a valid GUID; otherwise, QuickBooks
    will return an error. This field is immutable and can only be set during object
    creation.
    """

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]
    """Indicates whether this non-inventory item is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    """

    manufacturer_part_number: Annotated[str, PropertyInfo(alias="manufacturerPartNumber")]
    """
    The manufacturer's part number for this non-inventory item, which is often the
    stock keeping unit (SKU).
    """

    parent_id: Annotated[str, PropertyInfo(alias="parentId")]
    """The parent non-inventory item one level above this one in the hierarchy.

    For example, if this non-inventory item has a `fullName` of
    "Office-Supplies:Printer Ink Cartridge", its parent has a `fullName` of
    "Office-Supplies". If this non-inventory item is at the top level, this field
    will be `null`.
    """

    sales_and_purchase_details: Annotated[SalesAndPurchaseDetails, PropertyInfo(alias="salesAndPurchaseDetails")]

    sales_or_purchase_details: Annotated[SalesOrPurchaseDetails, PropertyInfo(alias="salesOrPurchaseDetails")]

    sales_tax_code_id: Annotated[str, PropertyInfo(alias="salesTaxCodeId")]
    """
    The sales-tax code associated with this non-inventory item, determining whether
    it is taxable or non-taxable. It's used to assign a default tax status to all
    transactions for this non-inventory item. Default codes include "Non"
    (non-taxable) and "Tax" (taxable), but custom codes can also be created in
    QuickBooks. If QuickBooks is not set up to charge sales tax (via the "Do You
    Charge Sales Tax?" preference), it will assign the default non-taxable code to
    all sales.
    """

    unit_of_measure_set_id: Annotated[str, PropertyInfo(alias="unitOfMeasureSetId")]
    """
    The unit-of-measure set associated with this non-inventory item, which consists
    of a base unit and related units.
    """


class Barcode(TypedDict, total=False):
    allow_override: Annotated[bool, PropertyInfo(alias="allowOverride")]
    """Indicates whether to allow the barcode to be overridden."""

    assign_even_if_used: Annotated[bool, PropertyInfo(alias="assignEvenIfUsed")]
    """Indicates whether to assign the barcode even if it is already used."""

    value: str
    """The item's barcode value."""


class SalesAndPurchaseDetails(TypedDict, total=False):
    expense_account_id: Annotated[str, PropertyInfo(alias="expenseAccountId")]
    """The expense account used to track expenses from purchases of this item."""

    income_account_id: Annotated[str, PropertyInfo(alias="incomeAccountId")]
    """The income account used to track revenue from sales of this item."""

    preferred_vendor_id: Annotated[str, PropertyInfo(alias="preferredVendorId")]
    """The preferred vendor from whom this item is typically purchased."""

    purchase_cost: Annotated[str, PropertyInfo(alias="purchaseCost")]
    """
    The cost at which this item is purchased from vendors, represented as a decimal
    string.
    """

    purchase_description: Annotated[str, PropertyInfo(alias="purchaseDescription")]
    """
    The description of this item that appears on purchase forms (e.g., checks,
    bills, item receipts) when it is ordered or bought from vendors.
    """

    purchase_tax_code_id: Annotated[str, PropertyInfo(alias="purchaseTaxCodeId")]
    """The tax code applied to purchases of this item.

    Applicable in regions where purchase taxes are used, such as Canada or the UK.
    """

    sales_description: Annotated[str, PropertyInfo(alias="salesDescription")]
    """
    The description of this item that appears on sales forms (e.g., invoices, sales
    receipts) when sold to customers.
    """

    sales_price: Annotated[str, PropertyInfo(alias="salesPrice")]
    """
    The price at which this item is sold to customers, represented as a decimal
    string.
    """


class SalesOrPurchaseDetails(TypedDict, total=False):
    account_id: Annotated[str, PropertyInfo(alias="accountId")]
    """
    The account associated with this item, used when recording transactions
    involving this item. This could be an income account when selling or an expense
    account when purchasing.
    """

    description: str
    """A description of this item."""

    price: str
    """
    The price at which this item is purchased or sold, represented as a decimal
    string.
    """

    price_percentage: Annotated[str, PropertyInfo(alias="pricePercentage")]
    """
    The price of this item expressed as a percentage, used instead of `price` when
    the item's cost is calculated as a percentage of another amount. For example, a
    service item that costs a percentage of another item's price.
    """
