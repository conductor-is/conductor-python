# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SalesTaxCodeUpdateParams"]


class SalesTaxCodeUpdateParams(TypedDict, total=False):
    revision_number: Required[Annotated[str, PropertyInfo(alias="revisionNumber")]]
    """
    The current revision number of the sales-tax code you are updating, which you
    can get by fetching the object first. Provide the most recent `revisionNumber`
    to ensure you're working with the latest data; otherwise, the update will return
    an error.
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

    is_taxable: Annotated[bool, PropertyInfo(alias="isTaxable")]
    """Indicates whether this sales-tax code is tracking taxable sales.

    This field cannot be modified once the sales-tax code has been used in a
    transaction. For the default built-in sales-tax codes, "Non" always has
    `isTaxable` as `false`, while "Tax" always has it as `true`. Due to a bug in
    QuickBooks, for all other (custom) sales-tax codes, the value of this field
    cannot be reliably retrieved externally, resulting in `null` being returned.
    However, you can confidently set the `isTaxable` value when creating a sales-tax
    code; the issue solely affects the retrieval of the `isTaxable` value.
    """

    name: str
    """
    The case-insensitive unique name of this sales-tax code, unique across all
    sales-tax codes. This short name will appear on sales forms to identify the tax
    status of an item.
    """

    sales_tax_item_id: Annotated[str, PropertyInfo(alias="salesTaxItemId")]
    """
    The sales-tax item used to calculate the actual tax amount for this sales-tax
    code's transactions by applying a specific tax rate collected for a single tax
    agency. Unlike `salesTaxCode`, which only indicates general taxability, this
    field drives the actual tax calculation and reporting.
    """
