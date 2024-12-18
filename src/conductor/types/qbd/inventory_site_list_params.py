# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["InventorySiteListParams"]


class InventorySiteListParams(TypedDict, total=False):
    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    ids: List[str]
    """
    Filter for specific inventory sites by their QuickBooks-assigned unique
    identifier(s).

    **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
    query parameters for this request.
    """

    name_contains: Annotated[str, PropertyInfo(alias="nameContains")]
    """
    Filter for inventory sites whose `name` contains this substring,
    case-insensitive. NOTE: If you use this parameter, you cannot also use
    `nameStartsWith` or `nameEndsWith`.
    """

    name_ends_with: Annotated[str, PropertyInfo(alias="nameEndsWith")]
    """
    Filter for inventory sites whose `name` ends with this substring,
    case-insensitive. NOTE: If you use this parameter, you cannot also use
    `nameContains` or `nameStartsWith`.
    """

    name_from: Annotated[str, PropertyInfo(alias="nameFrom")]
    """
    Filter for inventory sites whose `name` is alphabetically greater than or equal
    to this value.
    """

    names: List[str]
    """Filter for specific inventory sites by their name(s), case-insensitive.

    Like `id`, `name` is a unique identifier for an inventory site.

    **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
    query parameters for this request.
    """

    name_starts_with: Annotated[str, PropertyInfo(alias="nameStartsWith")]
    """
    Filter for inventory sites whose `name` starts with this substring,
    case-insensitive. NOTE: If you use this parameter, you cannot also use
    `nameContains` or `nameEndsWith`.
    """

    name_to: Annotated[str, PropertyInfo(alias="nameTo")]
    """
    Filter for inventory sites whose `name` is alphabetically less than or equal to
    this value.
    """

    status: Literal["active", "all", "inactive"]
    """Filter for inventory sites that are active, inactive, or both."""

    updated_after: Annotated[str, PropertyInfo(alias="updatedAfter")]
    """
    Filter for inventory sites updated on or after this date and time, in ISO 8601
    format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time
    is assumed to be 00:00:00 of that day.
    """

    updated_before: Annotated[str, PropertyInfo(alias="updatedBefore")]
    """
    Filter for inventory sites updated on or before this date and time, in ISO 8601
    format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time
    is assumed to be 23:59:59 of that day.
    """