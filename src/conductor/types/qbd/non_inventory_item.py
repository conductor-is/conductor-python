# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "NonInventoryItem",
    "Class",
    "CustomField",
    "Parent",
    "SalesAndPurchaseDetails",
    "SalesAndPurchaseDetailsExpenseAccount",
    "SalesAndPurchaseDetailsIncomeAccount",
    "SalesAndPurchaseDetailsPreferredVendor",
    "SalesAndPurchaseDetailsPurchaseTaxCode",
    "SalesOrPurchaseDetails",
    "SalesOrPurchaseDetailsAccount",
    "SalesTaxCode",
    "UnitOfMeasureSet",
]


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


class SalesAndPurchaseDetailsExpenseAccount(BaseModel):
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


class SalesAndPurchaseDetailsIncomeAccount(BaseModel):
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


class SalesAndPurchaseDetailsPreferredVendor(BaseModel):
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


class SalesAndPurchaseDetailsPurchaseTaxCode(BaseModel):
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


class SalesAndPurchaseDetails(BaseModel):
    expense_account: Optional[SalesAndPurchaseDetailsExpenseAccount] = FieldInfo(alias="expenseAccount", default=None)
    """The expense account to use when purchasing this item."""

    income_account: Optional[SalesAndPurchaseDetailsIncomeAccount] = FieldInfo(alias="incomeAccount", default=None)
    """The income account to use when selling this item."""

    preferred_vendor: Optional[SalesAndPurchaseDetailsPreferredVendor] = FieldInfo(
        alias="preferredVendor", default=None
    )
    """The preferred vendor for this item."""

    purchase_cost: Optional[str] = FieldInfo(alias="purchaseCost", default=None)
    """The cost of this item when purchased, represented as a decimal string.

    This is the amount the business expects to pay when ordering or buying this
    item, or the amount that was actually paid.
    """

    purchase_description: Optional[str] = FieldInfo(alias="purchaseDescription", default=None)
    """
    The description that appears on purchase forms (e.g., checks, bills, item
    receipts) when this item is bought. For fixed assets, this describes the item as
    it was when purchased.
    """

    purchase_tax_code: Optional[SalesAndPurchaseDetailsPurchaseTaxCode] = FieldInfo(
        alias="purchaseTaxCode", default=None
    )
    """The tax code to use when purchasing this item.

    Applicable in regions where purchase taxes are used, such as Canada or the UK.
    """

    sales_description: Optional[str] = FieldInfo(alias="salesDescription", default=None)
    """
    The description that appears on sales forms (e.g., invoices, sales receipts)
    when selling this item. For fixed assets, this describes the sale of the asset
    for accounting purposes.
    """

    sales_price: Optional[str] = FieldInfo(alias="salesPrice", default=None)
    """The price to charge for this item, represented as a decimal string."""


class SalesOrPurchaseDetailsAccount(BaseModel):
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


class SalesOrPurchaseDetails(BaseModel):
    account: Optional[SalesOrPurchaseDetailsAccount] = None
    """
    The account associated with this item, used when recording transactions
    involving this item. This could be an income account when selling or an expense
    account when purchasing.
    """

    description: Optional[str] = None
    """
    A description of the item that appears on sales or purchase forms, depending on
    whether the item is being sold or purchased.
    """

    price: Optional[str] = None
    """
    The purchase price or sales price of this item, represented as a decimal string.
    """

    price_percentage: Optional[str] = FieldInfo(alias="pricePercentage", default=None)
    """
    The price expressed as a percentage, used instead of `price` when the item's
    cost is calculated as a percentage of another amount. For example, a service
    item that costs a percentage of another item's price.
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


class NonInventoryItem(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks for this non-inventory item.

    This ID is unique among all non-inventory items but not across different object
    types.
    """

    bar_code: Optional[str] = FieldInfo(alias="barCode", default=None)
    """The barcode value for this non-inventory item."""

    class_: Optional[Class] = FieldInfo(alias="class", default=None)
    """
    The non-inventory item's class, used for categorization (e.g., by department,
    location, or type of work).
    """

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when this non-inventory item was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """

    custom_fields: List[CustomField] = FieldInfo(alias="customFields")
    """
    The custom fields added by the user to this non-inventory item object as a data
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
    The fully-qualified unique name for this non-inventory item, formed by combining
    the names of its parent objects with its own `name`, separated by colons. For
    example, if a non-inventory item is under 'Office Supplies' and has the `name`
    'Printer Ink Cartridge', its `fullName` would be 'Office Supplies:Printer Ink
    Cartridge'. Unlike `name`, `fullName` is guaranteed to be unique across all
    non-inventory item objects.
    """

    is_active: bool = FieldInfo(alias="isActive")
    """Indicates whether this non-inventory item is active.

    Inactive objects are typically hidden from views and reports in QuickBooks
    Desktop.
    """

    manufacturer_part_number: Optional[str] = FieldInfo(alias="manufacturerPartNumber", default=None)
    """The manufacturer's part number for this non-inventory item."""

    name: str
    """The case-insensitive name of this non-inventory item.

    Not guaranteed to be unique because it does not include the names of its parent
    objects like `fullName` does. For example, two objects could both have the
    `name` "Printer Ink Cartridge", but they could have unique `fullName` values,
    such as "Office Supplies:Printer Ink Cartridge" and "Miscellaneous:Printer Ink
    Cartridge".
    """

    object_type: Literal["qbd_non_inventory_item"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_non_inventory_item"`."""

    parent: Optional[Parent] = None
    """The parent non-inventory item one level above this one in the hierarchy.

    For example, if this non-inventory item has a `fullName` of "Office
    Supplies:Printer Ink Cartridge", its parent has a `fullName` of "Office
    Supplies". If this non-inventory item is at the top level, `parent` will be
    `null`.
    """

    sales_and_purchase_details: Optional[SalesAndPurchaseDetails] = FieldInfo(
        alias="salesAndPurchaseDetails", default=None
    )
    """
    Details specific to non-inventory items that are both purchased and sold by the
    business. Used for items like inventory products (e.g., goods resold to
    customers) or reimbursable expenses.
    """

    sales_or_purchase_details: Optional[SalesOrPurchaseDetails] = FieldInfo(
        alias="salesOrPurchaseDetails", default=None
    )
    """
    Details specific to non-inventory items that are either purchased by the
    business or sold to customers, but not both. Used for items like services that
    are only sold (e.g., consulting services) or goods that are only purchased for
    internal use (e.g., office supplies).
    """

    sales_tax_code: Optional[SalesTaxCode] = FieldInfo(alias="salesTaxCode", default=None)
    """
    The sales tax code associated with this non-inventory item, indicating whether
    it is taxable or non-taxable. Default codes include 'NON' (non-taxable) and
    'TAX' (taxable). If QuickBooks is not set up to charge sales tax, it will assign
    the default non-taxable code to all sales.
    """

    sublevel: float
    """The depth level of this non-inventory item in the hierarchy.

    A top-level non-inventory item has a `sublevel` of 0; each subsequent sublevel
    increases this number by 1. For example, a non-inventory item with a `fullName`
    of "Office Supplies:Printer Ink Cartridge" would have a `sublevel` of 1.
    """

    unit_of_measure_set: Optional[UnitOfMeasureSet] = FieldInfo(alias="unitOfMeasureSet", default=None)
    """
    The unit of measure set associated with this non-inventory item, which consists
    of a base unit and related units.
    """

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when this non-inventory item was last updated, in ISO 8601
    format (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time
    zone in QuickBooks.
    """

    version: str
    """
    The current version identifier for this non-inventory item, which changes each
    time the object is modified. When updating this object, you must provide the
    most recent `version` to ensure you're working with the latest data; otherwise,
    the update will fail. This value is opaque and should not be interpreted.
    """
