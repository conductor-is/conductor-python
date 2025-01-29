# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SalesRepresentative"]


class SalesRepresentative(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks to this sales representative.

    This ID is unique across all sales representatives but not across different
    QuickBooks object types.
    """

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when this sales representative was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """

    initial: Optional[str] = None
    """The initials of this sales representative's name."""

    is_active: bool = FieldInfo(alias="isActive")
    """Indicates whether this sales representative is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    Defaults to `true`.
    """

    object_type: Literal["qbd_sales_representative"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_sales_representative"`."""

    revision_number: str = FieldInfo(alias="revisionNumber")
    """
    The current revision number of this sales representative object, which changes
    each time the object is modified. When updating this object, you must provide
    the most recent `revisionNumber` to ensure you're working with the latest data;
    otherwise, the update will return an error.
    """

    sales_representative: SalesRepresentative = FieldInfo(alias="salesRepresentative")
    """
    The sales representative's corresponding complete record in QuickBooks, stored
    as either an employee, vendor, or other-name entry.
    """

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when this sales representative was last updated, in ISO 8601
    format (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time
    zone in QuickBooks.
    """
