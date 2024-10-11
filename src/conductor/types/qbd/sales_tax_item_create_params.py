# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SalesTaxItemCreateParams", "Barcode"]


class SalesTaxItemCreateParams(TypedDict, total=False):
    name: Required[str]
    """
    The case-insensitive unique name of this sales-tax item, unique across all
    sales-tax items.
    """

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    barcode: Barcode
    """The sales-tax item's barcode."""

    class_id: Annotated[str, PropertyInfo(alias="classId")]
    """The sales-tax item's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default.
    """

    description: str
    """
    The sales-tax item's description that will appear on sales forms that include
    this item.
    """

    external_id: Annotated[str, PropertyInfo(alias="externalId")]
    """
    A developer-assigned globally unique identifier (GUID) for tracking this object
    in external systems. Must be formatted as a valid GUID; otherwise, QuickBooks
    will return an error.
    """

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]
    """Indicates whether this sales-tax item is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    """

    sales_tax_return_line_id: Annotated[str, PropertyInfo(alias="salesTaxReturnLineId")]
    """
    The specific line on the sales tax return form where the tax collected using
    this sales-tax item should be reported.
    """

    tax_rate: Annotated[str, PropertyInfo(alias="taxRate")]
    """The tax rate defined by this sales-tax item, represented as a decimal string.

    For example, "7.5" represents a 7.5% tax rate. This rate determines the amount
    of sales tax applied when this item is used in transactions. If a non-zero
    `taxRate` is specified, then the `taxVendor` field is required.
    """

    tax_vendor_id: Annotated[str, PropertyInfo(alias="taxVendorId")]
    """
    The tax agency (vendor) to whom collected sales taxes are owed for this
    sales-tax item. This field refers to a vendor in QuickBooks that represents the
    tax authority. If a non-zero `taxRate` is specified, then `taxVendor` is
    required.
    """


class Barcode(TypedDict, total=False):
    allow_override: Annotated[bool, PropertyInfo(alias="allowOverride")]
    """Whether to allow the barcode to be overridden."""

    assign_even_if_used: Annotated[bool, PropertyInfo(alias="assignEvenIfUsed")]
    """Whether to assign the barcode even if it is already used."""

    bar_code_value: Annotated[str, PropertyInfo(alias="barCodeValue")]
    """The item's barcode value."""
