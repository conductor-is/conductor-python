# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["QbdStandardTerm"]


class QbdStandardTerm(BaseModel):
    id: str
    """
    The QuickBooks-assigned identifier for this standard-term, unique across all
    standard-terms.
    """

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when the object was created, in ISO 8601 format
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
    The discount percentage applied to the payment if received within the discount
    period defined by `discountDays`. The value is between 0 and 100.
    """

    due_days: Optional[float] = FieldInfo(alias="dueDays", default=None)
    """The number of days until payment is due."""

    is_active: bool = FieldInfo(alias="isActive")
    """Whether this standard-term is active.

    QuickBooks hides inactive objects from most views and reports in the UI.
    """

    name: str
    """
    The standard-term's case-insensitive unique name, unique across all
    standard-terms.
    """

    object_type: Literal["qbd_standard_term"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_standard_term"`."""

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when the object was last updated, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """

    version: str
    """The current version identifier of the object that changes with each
    modification.

    Provide this value when updating the object to verify you are working with the
    latest version; mismatched values will fail.
    """
