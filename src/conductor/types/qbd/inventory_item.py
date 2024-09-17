# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "InventoryItem",
    "AssetAccount",
    "Class",
    "CogsAccount",
    "CustomField",
    "IncomeAccount",
    "Parent",
    "PreferredVendor",
    "PurchaseTaxCode",
    "SalesTaxCode",
    "UnitOfMeasureSet",
]


class AssetAccount(BaseModel):
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


class CogsAccount(BaseModel):
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


class IncomeAccount(BaseModel):
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


class Parent(BaseModel):
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


class PreferredVendor(BaseModel):
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


class PurchaseTaxCode(BaseModel):
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


class SalesTaxCode(BaseModel):
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


class UnitOfMeasureSet(BaseModel):
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


class InventoryItem(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks for this inventory item.

    This ID is unique among all inventory items but not across different object
    types.
    """

    asset_account: Optional[AssetAccount] = FieldInfo(alias="assetAccount", default=None)
    """
    The asset account used to track the current value of this inventory item in
    inventory.
    """

    average_cost: Optional[str] = FieldInfo(alias="averageCost", default=None)
    """
    The average cost per unit of this inventory item, represented as a decimal
    string.
    """

    bar_code: Optional[str] = FieldInfo(alias="barCode", default=None)
    """The barcode value for this inventory item."""

    class_: Optional[Class] = FieldInfo(alias="class", default=None)
    """
    The inventory item's class, used for categorization (e.g., by department,
    location, or type of work).
    """

    cogs_account: Optional[CogsAccount] = FieldInfo(alias="cogsAccount", default=None)
    """
    The Cost of Goods Sold (COGS) account for this inventory item, tracking the
    original direct costs of producing goods sold.
    """

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when this inventory item was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """

    custom_fields: List[CustomField] = FieldInfo(alias="customFields")
    """
    The custom fields added by the user to this inventory item object as a data
    extension. These fields are not part of the standard QuickBooks object.
    """

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """
    A developer-assigned globally unique identifier (GUID) for tracking this object
    in external systems. Must be formatted as a valid GUID; otherwise, QuickBooks
    will return an error.
    """

    full_name: str = FieldInfo(alias="fullName")
    """
    The fully-qualified unique name for this inventory item, formed by combining the
    names of its parent objects with its own `name`, separated by colons. For
    example, if an inventory item is under 'Furniture:Kitchen' and has the `name`
    'Cabinet', its `fullName` would be 'Furniture:Kitchen:Cabinet'. Unlike `name`,
    `fullName` is guaranteed to be unique across all inventory item objects.
    """

    income_account: Optional[IncomeAccount] = FieldInfo(alias="incomeAccount", default=None)
    """
    The income account associated with this inventory item, used to track revenue
    from sales.
    """

    is_active: bool = FieldInfo(alias="isActive")
    """Indicates whether this inventory item is active.

    Inactive objects are typically hidden from views and reports in QuickBooks
    Desktop.
    """

    manufacturer_part_number: Optional[str] = FieldInfo(alias="manufacturerPartNumber", default=None)
    """The manufacturer's part number for this inventory item."""

    maximum_on_hand_quantity: Optional[float] = FieldInfo(alias="maximumOnHandQuantity", default=None)
    """The maximum quantity of this inventory item desired in inventory."""

    name: str
    """The case-insensitive name of this inventory item.

    Not guaranteed to be unique because it does not include the names of its parent
    objects like `fullName` does. For example, two objects could both have the
    `name` "Cabinet", but they could have unique `fullName` values, such as
    "Kitchen:Cabinet" and "Garage:Cabinet".
    """

    object_type: Literal["qbd_inventory_item"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_inventory_item"`."""

    parent: Optional[Parent] = None
    """The parent inventory item one level above this one in the hierarchy.

    For example, if this inventory item has a `fullName` of
    "Furniture:Kitchen:Cabinet", its parent has a `fullName` of "Furniture:Kitchen".
    If this inventory item is at the top level, `parent` will be `null`.
    """

    preferred_vendor: Optional[PreferredVendor] = FieldInfo(alias="preferredVendor", default=None)
    """The preferred vendor from whom this inventory item is typically purchased."""

    purchase_cost: Optional[str] = FieldInfo(alias="purchaseCost", default=None)
    """
    The cost at which this inventory item is purchased from vendors, represented as
    a decimal string.
    """

    purchase_description: Optional[str] = FieldInfo(alias="purchaseDescription", default=None)
    """
    The description of this inventory item that appears on purchase forms (e.g.,
    checks, bills, item receipts) when ordered or bought from vendors.
    """

    purchase_tax_code: Optional[PurchaseTaxCode] = FieldInfo(alias="purchaseTaxCode", default=None)
    """The tax code applied to purchases of this inventory item.

    Applicable in regions where purchase taxes are used, such as Canada or the UK.
    """

    quantity_on_hand: Optional[float] = FieldInfo(alias="quantityOnHand", default=None)
    """The current quantity of this inventory item available in inventory.

    To change the `quantityOnHand` for an inventory item, you must create an
    inventory-adjustment instead of updating this inventory item directly.
    """

    quantity_on_order: Optional[float] = FieldInfo(alias="quantityOnOrder", default=None)
    """
    The number of units of this inventory item that have been ordered from vendors
    (as recorded in purchase orders) but not yet received.
    """

    quantity_on_sales_order: Optional[float] = FieldInfo(alias="quantityOnSalesOrder", default=None)
    """
    The number of units of this inventory item that have been sold (as recorded in
    sales orders) but not yet fulfilled or delivered to customers.
    """

    reorder_point: Optional[float] = FieldInfo(alias="reorderPoint", default=None)
    """
    The minimum quantity of this inventory item at which QuickBooks prompts for
    reordering.
    """

    sales_description: Optional[str] = FieldInfo(alias="salesDescription", default=None)
    """
    The description of this inventory item that appears on sales forms (e.g.,
    invoices, sales receipts) when sold to customers. For fixed assets, it details
    the sale of the asset for accounting purposes.
    """

    sales_price: Optional[str] = FieldInfo(alias="salesPrice", default=None)
    """
    The price at which this inventory item is sold to customers, represented as a
    decimal string.
    """

    sales_tax_code: Optional[SalesTaxCode] = FieldInfo(alias="salesTaxCode", default=None)
    """
    The sales tax code associated with this inventory item, indicating whether it is
    taxable or non-taxable. Default codes include 'NON' (non-taxable) and 'TAX'
    (taxable). If QuickBooks is not set up to charge sales tax, it will assign the
    default non-taxable code to all sales.
    """

    sublevel: float
    """The depth level of this inventory item in the hierarchy.

    A top-level inventory item has a `sublevel` of 0; each subsequent sublevel
    increases this number by 1. For example, a inventory item with a `fullName` of
    "Furniture:Kitchen:Cabinet" would have a `sublevel` of 2.
    """

    unit_of_measure_set: Optional[UnitOfMeasureSet] = FieldInfo(alias="unitOfMeasureSet", default=None)
    """
    The unit of measure set associated with this inventory item, which consists of a
    base unit and related units.
    """

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when this inventory item was last updated, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """

    version: str
    """
    The current version identifier for this inventory item, which changes each time
    the object is modified. When updating this object, you must provide the most
    recent `version` to ensure you're working with the latest data; otherwise, the
    update will fail. This value is opaque and should not be interpreted.
    """
