# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["InventorySiteCreateParams", "Address"]


class InventorySiteCreateParams(TypedDict, total=False):
    name: Required[str]
    """
    The case-insensitive unique name of this inventory site, unique across all
    inventory sites.

    **NOTE**: Inventory sites do not have a `fullName` field because they are not
    hierarchical objects, which is why `name` is unique for them but not for objects
    that have parents. Maximum length: 31 characters.
    """

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    address: Address
    """The inventory site's address."""

    description: str
    """A description of this inventory site."""

    email: str
    """The inventory site's email address."""

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]
    """Indicates whether this inventory site is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    """

    parent_id: Annotated[str, PropertyInfo(alias="parentId")]
    """The parent inventory site one level above this one in the hierarchy."""


class Address(TypedDict, total=False):
    city: str
    """The city, district, suburb, town, or village name of the site address."""

    country: str
    """The country name of the site address."""

    line1: str
    """The first line of the site address (e.g., street, PO Box, or company name)."""

    line2: str
    """
    The second line of the site address, if needed (e.g., apartment, suite, unit, or
    building).
    """

    line3: str
    """The third line of the site address, if needed."""

    line4: str
    """The fourth line of the site address, if needed."""

    line5: str
    """The fifth line of the site address, if needed."""

    postal_code: Annotated[str, PropertyInfo(alias="postalCode")]
    """The postal code or ZIP code of the site address."""

    state: str
    """The state, county, province, or region name of the site address."""
