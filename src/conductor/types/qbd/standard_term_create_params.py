# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["StandardTermCreateParams"]


class StandardTermCreateParams(TypedDict, total=False):
    name: Required[str]
    """
    The case-insensitive unique name of this standard term, unique across all
    standard terms.
    """

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    discount_days: Annotated[float, PropertyInfo(alias="discountDays")]
    """
    The number of days within which payment must be received to qualify for the
    discount specified by `discountPercentage`.
    """

    discount_percentage: Annotated[str, PropertyInfo(alias="discountPercentage")]
    """
    The discount percentage applied to the payment if received within the number of
    days specified by `discountDays`. The value is between 0 and 100.
    """

    due_days: Annotated[float, PropertyInfo(alias="dueDays")]
    """The number of days until payment is due."""

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]
    """Indicates whether this standard term is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    """
