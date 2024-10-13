# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["InventoryItemCreateParams", "Barcode"]


class InventoryItemCreateParams(TypedDict, total=False):
    name: Required[str]
    """The case-insensitive name of this inventory item.

    Not guaranteed to be unique because it does not include the names of its parent
    objects like `fullName` does. For example, two inventory items could both have
    the `name` "Widget", but they could have unique `fullName` values, such as
    "Products:Widget" and "Inventory:Widget".
    """

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    asset_account_id: Annotated[str, PropertyInfo(alias="assetAccountId")]
    """
    The asset account used to track the current value of this inventory item in
    inventory.
    """

    barcode: Barcode
    """The inventory item's barcode."""

    class_id: Annotated[str, PropertyInfo(alias="classId")]
    """The inventory item's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default.
    """

    cogs_account_id: Annotated[str, PropertyInfo(alias="cogsAccountId")]
    """
    The Cost of Goods Sold (COGS) account for this inventory item, tracking the
    original direct costs of producing goods sold.
    """

    external_id: Annotated[str, PropertyInfo(alias="externalId")]
    """
    A globally unique identifier (GUID) you can provide for tracking this object in
    your external system. Must be formatted as a valid GUID; otherwise, QuickBooks
    will return an error.
    """

    income_account_id: Annotated[str, PropertyInfo(alias="incomeAccountId")]
    """The inventory item's income account, used to track revenue from sales."""

    inventory_date: Annotated[Union[str, date], PropertyInfo(alias="inventoryDate", format="iso8601")]
    """
    The date when this inventory item was converted into an inventory item from some
    other type of item, in ISO 8601 format (YYYY-MM-DD).
    """

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]
    """Indicates whether this inventory item is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    """

    manufacturer_part_number: Annotated[str, PropertyInfo(alias="manufacturerPartNumber")]
    """The manufacturer's part number for this inventory item."""

    maximum_on_hand_quantity: Annotated[float, PropertyInfo(alias="maximumOnHandQuantity")]
    """The maximum quantity of this inventory item desired in inventory."""

    parent_id: Annotated[str, PropertyInfo(alias="parentId")]
    """The parent inventory item one level above this one in the hierarchy.

    For example, if this inventory item has a `fullName` of
    "Products:Electronics:Widgets", its parent has a `fullName` of
    "Products:Electronics". If this inventory item is at the top level, `parent`
    will be `null`.
    """

    preferred_vendor_id: Annotated[str, PropertyInfo(alias="preferredVendorId")]
    """The preferred vendor from whom this inventory item is typically purchased."""

    purchase_cost: Annotated[str, PropertyInfo(alias="purchaseCost")]
    """
    The cost at which this inventory item is purchased from vendors, represented as
    a decimal string.
    """

    purchase_description: Annotated[str, PropertyInfo(alias="purchaseDescription")]
    """
    The description of this inventory item that appears on purchase forms (e.g.,
    checks, bills, item receipts) when ordered or bought from vendors.
    """

    purchase_tax_code_id: Annotated[str, PropertyInfo(alias="purchaseTaxCodeId")]
    """The tax code applied to purchases of this inventory item.

    Applicable in regions where purchase taxes are used, such as Canada or the UK.
    """

    quantity_on_hand: Annotated[float, PropertyInfo(alias="quantityOnHand")]
    """The current quantity of this inventory item available in inventory.

    To change the `quantityOnHand` for an inventory item, you must create an
    inventory-adjustment instead of updating this inventory item directly.
    """

    reorder_point: Annotated[float, PropertyInfo(alias="reorderPoint")]
    """
    The minimum quantity of this inventory item at which QuickBooks prompts for
    reordering.
    """

    sales_description: Annotated[str, PropertyInfo(alias="salesDescription")]
    """
    The description of this inventory item that appears on sales forms (e.g.,
    invoices, sales receipts) when sold to customers. For fixed assets, it details
    the sale of the asset for accounting purposes.
    """

    sales_price: Annotated[str, PropertyInfo(alias="salesPrice")]
    """
    The price at which this inventory item is sold to customers, represented as a
    decimal string.
    """

    sales_tax_code_id: Annotated[str, PropertyInfo(alias="salesTaxCodeId")]
    """
    The sales-tax code associated with this inventory item, determining whether it
    is taxable or non-taxable. It's used to assign a default tax status to all
    transactions for this inventory item. Default codes include "Non" (non-taxable)
    and "Tax" (taxable), but custom codes can also be created in QuickBooks. If
    QuickBooks is not set up to charge sales tax (via the "Do You Charge Sales Tax?"
    preference), it will assign the default non-taxable code to all sales.
    """

    total_value: Annotated[str, PropertyInfo(alias="totalValue")]
    """The total value of this inventory item.

    If `totalValue` is provided, `quantityOnHand` must also be provided and must be
    greater than zero. If both `quantityOnHand` and `purchaseCost` are provided,
    then `totalValue` will be set to `quantityOnHand` times `purchaseCost`,
    regardless of what `totalValue` is explicitly set to.
    """

    unit_of_measure_set_id: Annotated[str, PropertyInfo(alias="unitOfMeasureSetId")]
    """
    The unit of measure set associated with this inventory item, which consists of a
    base unit and related units.
    """


class Barcode(TypedDict, total=False):
    allow_override: Annotated[bool, PropertyInfo(alias="allowOverride")]
    """Whether to allow the barcode to be overridden."""

    assign_even_if_used: Annotated[bool, PropertyInfo(alias="assignEvenIfUsed")]
    """Whether to assign the barcode even if it is already used."""

    bar_code_value: Annotated[str, PropertyInfo(alias="barCodeValue")]
    """The item's barcode value."""
