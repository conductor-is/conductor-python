# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["NonInventoryItemCreateParams", "Barcode", "SalesAndPurchaseDetails", "SalesOrPurchaseDetails"]


class NonInventoryItemCreateParams(TypedDict, total=False):
    name: Required[str]

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    barcode: Barcode

    class_id: Annotated[str, PropertyInfo(alias="classId")]
    """The class associated with this object.

    Classes can be used to categorize objects or transactions by department,
    location, or other meaningful segments.
    """

    external_id: Annotated[str, PropertyInfo(alias="externalId")]
    """
    An arbitrary globally unique identifier (GUID) the developer can provide to
    track this object in their own system. This value must be formatted as a GUID;
    otherwise, QuickBooks will return an error.
    """

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]

    is_tax_included: Annotated[bool, PropertyInfo(alias="isTaxIncluded")]

    manufacturer_part_number: Annotated[str, PropertyInfo(alias="manufacturerPartNumber")]

    parent_id: Annotated[str, PropertyInfo(alias="parentId")]

    sales_and_purchase_details: Annotated[SalesAndPurchaseDetails, PropertyInfo(alias="salesAndPurchaseDetails")]

    sales_or_purchase_details: Annotated[SalesOrPurchaseDetails, PropertyInfo(alias="salesOrPurchaseDetails")]

    sales_tax_code_id: Annotated[str, PropertyInfo(alias="salesTaxCodeId")]

    unit_of_measure_set_id: Annotated[str, PropertyInfo(alias="unitOfMeasureSetId")]


class Barcode(TypedDict, total=False):
    allow_override: Annotated[bool, PropertyInfo(alias="AllowOverride")]

    assign_even_if_used: Annotated[bool, PropertyInfo(alias="AssignEvenIfUsed")]

    bar_code_value: Annotated[str, PropertyInfo(alias="BarCodeValue")]


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
