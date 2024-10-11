# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["QbdSalesTaxItem", "Class", "CustomField", "SalesTaxReturnLine", "TaxVendor"]


class Class(BaseModel):
    id: Optional[str] = None
    """The unique identifier assigned by QuickBooks for this object.

    This ID is unique among all objects of the same type, but not across different
    QuickBooks object types.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The fully-qualified unique name for this object, formed by combining the names
    of its parent objects with its own `name`, separated by colons. Not
    case-sensitive.
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


class SalesTaxReturnLine(BaseModel):
    id: Optional[str] = None
    """The unique identifier assigned by QuickBooks for this object.

    This ID is unique among all objects of the same type, but not across different
    QuickBooks object types.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The fully-qualified unique name for this object, formed by combining the names
    of its parent objects with its own `name`, separated by colons. Not
    case-sensitive.
    """


class TaxVendor(BaseModel):
    id: Optional[str] = None
    """The unique identifier assigned by QuickBooks for this object.

    This ID is unique among all objects of the same type, but not across different
    QuickBooks object types.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The fully-qualified unique name for this object, formed by combining the names
    of its parent objects with its own `name`, separated by colons. Not
    case-sensitive.
    """


class QbdSalesTaxItem(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks for this sales-tax item.

    This ID is unique among all sales-tax items but not across different QuickBooks
    object types.
    """

    barcode: Optional[str] = None
    """The sales-tax item's barcode."""

    class_: Optional[Class] = FieldInfo(alias="class", default=None)
    """The sales-tax item's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default.
    """

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when this sales-tax item was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """

    custom_fields: List[CustomField] = FieldInfo(alias="customFields")
    """
    The custom fields added by the user to this sales-tax item object as a data
    extension. These fields are not part of the standard QuickBooks object.
    """

    description: Optional[str] = None
    """
    The sales-tax item's description that will appear on sales forms that include
    this item.
    """

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """
    A developer-assigned globally unique identifier (GUID) for tracking this object
    in external systems. Must be formatted as a valid GUID; otherwise, QuickBooks
    will return an error.
    """

    is_active: bool = FieldInfo(alias="isActive")
    """Indicates whether this sales-tax item is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    """

    name: str
    """
    The case-insensitive unique name of this sales-tax item, unique across all
    sales-tax items.
    """

    object_type: Literal["qbd_sales_tax_item"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_sales_tax_item"`."""

    sales_tax_return_line: Optional[SalesTaxReturnLine] = FieldInfo(alias="salesTaxReturnLine", default=None)
    """
    The specific line on the sales tax return form where the tax collected using
    this sales-tax item should be reported.
    """

    tax_rate: Optional[str] = FieldInfo(alias="taxRate", default=None)
    """The tax rate defined by this sales-tax item, represented as a decimal string.

    For example, "7.5" represents a 7.5% tax rate. If a non-zero `taxRate` is
    specified, the `taxVendor` field becomes required. This rate determines the
    amount of sales tax applied when this item is used in transactions.
    """

    tax_vendor: Optional[TaxVendor] = FieldInfo(alias="taxVendor", default=None)
    """
    The tax agency (vendor) to whom collected sales taxes are owed for this
    sales-tax item. This field refers to a vendor in QuickBooks that represents the
    tax authority. If a non-zero `taxRate` is specified, then `taxVendor` is
    required.
    """

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when this sales-tax item was last updated, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """

    version: str
    """
    The current version identifier for this sales-tax item, which changes each time
    the object is modified. When updating this object, you must provide the most
    recent `version` to ensure you're working with the latest data; otherwise, the
    update will fail. This value is opaque and should not be interpreted.
    """
