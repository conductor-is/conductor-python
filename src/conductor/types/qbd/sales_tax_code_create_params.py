# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SalesTaxCodeCreateParams"]


class SalesTaxCodeCreateParams(TypedDict, total=False):
    is_taxable: Required[Annotated[bool, PropertyInfo(alias="isTaxable")]]
    """Indicates whether this sales-tax code is tracking taxable sales.

    For any particular sales-tax code, `isTaxable` cannot be modified once the
    sales-tax code has been used in a transaction. The default value depends on the
    "Do You Charge Sales Tax?" preference in QuickBooks.
    """

    name: Required[str]
    """
    The case-insensitive unique name of this sales-tax code, unique across all
    sales-tax codes.
    """

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    description: str
    """A description of this sales-tax code."""

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]
    """Indicates whether this sales-tax code is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    """

    item_sales_tax_id: Annotated[str, PropertyInfo(alias="itemSalesTaxId")]
    """
    The specific sales-tax item used to calculate the actual tax amount for this
    sales-tax code's transactions. It represents a single tax rate collected for a
    single tax agency. This is more specific than `salesTaxCode`, which only
    indicates taxability, and is used for the actual tax calculation and reporting.
    """
