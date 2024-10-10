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
    A developer-assigned globally unique identifier (GUID) for tracking this object
    in external systems. Must be formatted as a valid GUID; otherwise, QuickBooks
    will return an error.
    """

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]
    """Indicates whether this non-inventory item is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    """

    is_tax_included: Annotated[bool, PropertyInfo(alias="isTaxIncluded")]
    """Indicates whether the price of this non-inventory item includes tax.

    This is primarily used in international versions of QuickBooks.
    """

    manufacturer_part_number: Annotated[str, PropertyInfo(alias="manufacturerPartNumber")]
    """The manufacturer's part number for this non-inventory item."""

    parent_id: Annotated[str, PropertyInfo(alias="parentId")]
    """The parent non-inventory item one level above this one in the hierarchy.

    For example, if this non-inventory item has a `fullName` of
    "Office-Supplies:Printer Ink Cartridge", its parent has a `fullName` of
    "Office-Supplies". If this non-inventory item is at the top level, `parent` will
    be `null`.
    """

    sales_and_purchase_details: Annotated[SalesAndPurchaseDetails, PropertyInfo(alias="salesAndPurchaseDetails")]

    sales_or_purchase_details: Annotated[SalesOrPurchaseDetails, PropertyInfo(alias="salesOrPurchaseDetails")]

    sales_tax_code_id: Annotated[str, PropertyInfo(alias="salesTaxCodeId")]
    """
    The sales tax code associated with this non-inventory item, determining whether
    it is taxable or non-taxable. It's used to assign a default tax status to all
    transactions for this non-inventory item. Default codes include "NON"
    (non-taxable) and "TAX" (taxable), but custom codes can also be created in
    QuickBooks. If QuickBooks is not set up to charge sales tax, it will assign the
    default non-taxable code to all sales.
    """

    unit_of_measure_set_id: Annotated[str, PropertyInfo(alias="unitOfMeasureSetId")]
    """
    The unit of measure set associated with this non-inventory item, which consists
    of a base unit and related units.
    """


class Barcode(TypedDict, total=False):
    allow_override: Annotated[bool, PropertyInfo(alias="allowOverride")]
    """Whether to allow the barcode to be overridden."""

    assign_even_if_used: Annotated[bool, PropertyInfo(alias="assignEvenIfUsed")]
    """Whether to assign the barcode even if it is already used."""

    bar_code_value: Annotated[str, PropertyInfo(alias="barCodeValue")]
    """The item's barcode value."""


class SalesAndPurchaseDetails(TypedDict, total=False):
    expense_account_id: Annotated[str, PropertyInfo(alias="expenseAccountId")]
    """The expense account to use when purchasing this item."""

    income_account_id: Annotated[str, PropertyInfo(alias="incomeAccountId")]
    """The income account to use when selling this item."""

    preferred_vendor_id: Annotated[str, PropertyInfo(alias="preferredVendorId")]
    """The preferred vendor for this item."""

    purchase_cost: Annotated[str, PropertyInfo(alias="purchaseCost")]
    """The cost of this item when purchased, represented as a decimal string.

    This is the amount the business expects to pay when ordering or buying this
    item, or the amount that was actually paid.
    """

    purchase_description: Annotated[str, PropertyInfo(alias="purchaseDescription")]
    """
    The description that appears on purchase forms (e.g., checks, bills, item
    receipts) when this item is bought. For fixed assets, this describes the item as
    it was when purchased.
    """

    purchase_tax_code_id: Annotated[str, PropertyInfo(alias="purchaseTaxCodeId")]
    """The tax code to use when purchasing this item.

    Applicable in regions where purchase taxes are used, such as Canada or the UK.
    """

    sales_description: Annotated[str, PropertyInfo(alias="salesDescription")]
    """
    The description that appears on sales forms (e.g., invoices, sales receipts)
    when selling this item. For fixed assets, this describes the sale of the asset
    for accounting purposes.
    """

    sales_price: Annotated[str, PropertyInfo(alias="salesPrice")]
    """The price to charge for this item, represented as a decimal string."""


class SalesOrPurchaseDetails(TypedDict, total=False):
    account_id: Annotated[str, PropertyInfo(alias="accountId")]
    """
    The account associated with this item, used when recording transactions
    involving this item. This could be an income account when selling or an expense
    account when purchasing.
    """

    description: str
    """
    A description of the item that appears on sales or purchase forms, depending on
    whether the item is being sold or purchased.
    """

    price: str
    """
    The purchase price or sales price of this item, represented as a decimal string.
    """

    price_percentage: Annotated[str, PropertyInfo(alias="pricePercentage")]
    """
    The price expressed as a percentage, used instead of `price` when the item's
    cost is calculated as a percentage of another amount. For example, a service
    item that costs a percentage of another item's price.
    """
