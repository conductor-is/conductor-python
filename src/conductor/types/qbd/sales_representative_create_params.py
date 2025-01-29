# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SalesRepresentativeCreateParams"]


class SalesRepresentativeCreateParams(TypedDict, total=False):
    sales_representative_id: Required[Annotated[str, PropertyInfo(alias="salesRepresentativeId")]]
    """
    The sales representative's corresponding complete record in QuickBooks, stored
    as either an employee, vendor, or other-name entry.
    """

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    initial: str
    """The initials of this sales representative's name."""

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]
    """Indicates whether this sales representative is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    Defaults to `true`.
    """
