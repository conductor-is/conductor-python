# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["QbdStandardTerm"]


class QbdStandardTerm(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks for this standard term.

    This ID is unique among all standard terms but not across different object
    types.
    """

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when this standard term was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """

    discount_days: Optional[float] = FieldInfo(alias="discountDays", default=None)
    """
    The number of days within which payment must be received to qualify for the
    discount defined by `discountPercentage`.
    """

    discount_percentage: Optional[str] = FieldInfo(alias="discountPercentage", default=None)
    """
    The discount percentage applied to the payment if received within `discountDays`
    number of days. The value is between 0 and 100.
    """

    due_days: Optional[float] = FieldInfo(alias="dueDays", default=None)
    """The number of days until payment is due."""

    is_active: bool = FieldInfo(alias="isActive")
    """Indicates whether this standard term is active.

    Inactive objects are typically hidden from views and reports in QuickBooks
    Desktop.
    """

    name: str
    """
    The case-insensitive unique name of this standard term, unique across all
    standard terms.
    """

    object_type: Literal["qbd_standard_term"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_standard_term"`."""

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when this standard term was last updated, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """

    version: str
    """
    The current version identifier for this standard term, which changes each time
    the object is modified. When updating this object, you must provide the most
    recent `version` to ensure you're working with the latest data; otherwise, the
    update will fail. This value is opaque and should not be interpreted.
    """
