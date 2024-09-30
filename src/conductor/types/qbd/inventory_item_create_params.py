# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["InventoryItemCreateParams", "Barcode"]


class InventoryItemCreateParams(TypedDict, total=False):
    name: Required[str]

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    asset_account_id: Annotated[str, PropertyInfo(alias="assetAccountId")]

    barcode: Barcode

    class_id: Annotated[str, PropertyInfo(alias="classId")]
    """The class associated with this object.

    Classes can be used to categorize objects or transactions by department,
    location, or other meaningful segments.
    """

    cogs_account_id: Annotated[str, PropertyInfo(alias="cogsAccountId")]

    external_id: Annotated[str, PropertyInfo(alias="externalId")]
    """
    An arbitrary globally unique identifier (GUID) the developer can provide to
    track this object in their own system. This value must be formatted as a GUID;
    otherwise, QuickBooks will return an error.
    """

    income_account_id: Annotated[str, PropertyInfo(alias="incomeAccountId")]

    inventory_date: Annotated[str, PropertyInfo(alias="inventoryDate")]

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]

    is_tax_included: Annotated[bool, PropertyInfo(alias="isTaxIncluded")]

    manufacturer_part_number: Annotated[str, PropertyInfo(alias="manufacturerPartNumber")]

    maximum_on_hand_quantity: Annotated[float, PropertyInfo(alias="maximumOnHandQuantity")]

    parent_id: Annotated[str, PropertyInfo(alias="parentId")]

    preferred_vendor_id: Annotated[str, PropertyInfo(alias="preferredVendorId")]

    purchase_cost: Annotated[str, PropertyInfo(alias="purchaseCost")]

    purchase_description: Annotated[str, PropertyInfo(alias="purchaseDescription")]

    purchase_tax_code_id: Annotated[str, PropertyInfo(alias="purchaseTaxCodeId")]

    quantity_on_hand: Annotated[float, PropertyInfo(alias="quantityOnHand")]

    reorder_point: Annotated[float, PropertyInfo(alias="reorderPoint")]

    sales_description: Annotated[str, PropertyInfo(alias="salesDescription")]

    sales_price: Annotated[str, PropertyInfo(alias="salesPrice")]

    sales_tax_code_id: Annotated[str, PropertyInfo(alias="salesTaxCodeId")]

    total_value: Annotated[str, PropertyInfo(alias="totalValue")]

    unit_of_measure_set_id: Annotated[str, PropertyInfo(alias="unitOfMeasureSetId")]


class Barcode(TypedDict, total=False):
    allow_override: Annotated[bool, PropertyInfo(alias="AllowOverride")]

    assign_even_if_used: Annotated[bool, PropertyInfo(alias="AssignEvenIfUsed")]

    bar_code_value: Annotated[str, PropertyInfo(alias="BarCodeValue")]
