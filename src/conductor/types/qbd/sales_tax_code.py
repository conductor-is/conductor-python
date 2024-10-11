# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SalesTaxCode", "ItemSalesTax"]


class ItemSalesTax(BaseModel):
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


class SalesTaxCode(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks for this sales-tax code.

    This ID is unique among all sales-tax codes but not across different QuickBooks
    object types.
    """

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when this sales-tax code was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """

    description: Optional[str] = None
    """A description of this sales-tax code."""

    is_active: bool = FieldInfo(alias="isActive")
    """Indicates whether this sales-tax code is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    """

    is_taxable: bool = FieldInfo(alias="isTaxable")
    """Indicates whether this sales-tax code is tracking taxable sales.

    For any particular sales-tax code, `isTaxable` cannot be modified once the
    sales-tax code has been used in a transaction. The default value depends on the
    "Do You Charge Sales Tax?" preference in QuickBooks.
    """

    item_sales_tax: Optional[ItemSalesTax] = FieldInfo(alias="itemSalesTax", default=None)
    """
    The sales-tax item used to calculate the actual tax amount for this sales-tax
    code's transactions by applying a specific tax rate collected for a single tax
    agency. Unlike `salesTaxCode`, which only indicates general taxability, this
    field drives the actual tax calculation and reporting.
    """

    name: str
    """
    The case-insensitive unique name of this sales-tax code, unique across all
    sales-tax codes.
    """

    object_type: Literal["qbd_sales_tax_code"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_sales_tax_code"`."""

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when this sales-tax code was last updated, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """

    version: str
    """
    The current version identifier for this sales-tax code, which changes each time
    the object is modified. When updating this object, you must provide the most
    recent `version` to ensure you're working with the latest data; otherwise, the
    update will fail. This value is opaque and should not be interpreted.
    """
