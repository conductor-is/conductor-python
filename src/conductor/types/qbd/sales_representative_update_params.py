# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SalesRepresentativeUpdateParams"]


class SalesRepresentativeUpdateParams(TypedDict, total=False):
    revision_number: Required[Annotated[str, PropertyInfo(alias="revisionNumber")]]
    """
    The current QuickBooks-assigned revision number of the sales representative
    object you are updating, which you can get by fetching the object first. Provide
    the most recent `revisionNumber` to ensure you're working with the latest data;
    otherwise, the update will return an error.
    """

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    entity_id: Annotated[str, PropertyInfo(alias="entityId")]
    """
    The sales representative's corresponding person entity in QuickBooks, stored as
    either an employee, vendor, or other-name entry.
    """

    initial: str
    """The initials of this sales representative's name."""

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]
    """Indicates whether this sales representative is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    Defaults to `true`.
    """
