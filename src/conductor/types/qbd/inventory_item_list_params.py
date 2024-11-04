# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["InventoryItemListParams"]


class InventoryItemListParams(TypedDict, total=False):
    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    class_ids: Annotated[List[str], PropertyInfo(alias="classIds")]
    """Filter for inventory items of this class or classes.

    Specify a single class ID or multiple using a comma-separated list (e.g.,
    `classIds=1,2,3`). A class is a way end-users can categorize inventory items in
    QuickBooks.
    """

    cursor: str
    """
    The pagination token to fetch the next set of results when paginating with the
    `limit` parameter. Retrieve this value from the `nextCursor` field in the
    previous response. If omitted, the API returns the first page of results.
    """

    full_names: Annotated[List[str], PropertyInfo(alias="fullNames")]
    """Filter for specific inventory items by their full-name(s), case-insensitive.

    Specify a single full-name or multiple using a comma-separated list (e.g.,
    `fullNames=1,2,3`). Like `id`, a `fullName` is a unique identifier for an
    inventory item, and is formed by by combining the names of its parent objects
    with its own `name`, separated by colons. For example, if an inventory item is
    under "Furniture:Kitchen" and has the `name` "Cabinet", its `fullName` would be
    "Furniture:Kitchen:Cabinet". Unlike `name`, `fullName` is guaranteed to be
    unique across all inventory item objects.

    NOTE: If you include this parameter, QuickBooks will ignore all other query
    parameters.
    """

    ids: List[str]
    """
    Filter for specific inventory items by their QuickBooks-assigned unique
    identifier(s). Specify a single ID or multiple using a comma-separated list
    (e.g., `ids=1,2,3`).

    NOTE: If you include this parameter, QuickBooks will ignore all other query
    parameters.
    """

    limit: int
    """The maximum number of objects to return.

    Ranging from 1 to 200, defaults to 200. Use this parameter in conjunction with
    the `cursor` parameter to paginate through results. The response will include a
    `nextCursor` field, which can be used as the `cursor` parameter value in
    subsequent requests to fetch the next set of results.
    """

    name_contains: Annotated[str, PropertyInfo(alias="nameContains")]
    """
    Filter for inventory items whose `name` contains this substring,
    case-insensitive. NOTE: If you use this parameter, you cannot also use
    `nameStartsWith` or `nameEndsWith`.
    """

    name_ends_with: Annotated[str, PropertyInfo(alias="nameEndsWith")]
    """
    Filter for inventory items whose `name` ends with this substring,
    case-insensitive. NOTE: If you use this parameter, you cannot also use
    `nameContains` or `nameStartsWith`.
    """

    name_from: Annotated[str, PropertyInfo(alias="nameFrom")]
    """
    Filter for inventory items whose `name` is alphabetically greater than or equal
    to this value.
    """

    name_starts_with: Annotated[str, PropertyInfo(alias="nameStartsWith")]
    """
    Filter for inventory items whose `name` starts with this substring,
    case-insensitive. NOTE: If you use this parameter, you cannot also use
    `nameContains` or `nameEndsWith`.
    """

    name_to: Annotated[str, PropertyInfo(alias="nameTo")]
    """
    Filter for inventory items whose `name` is alphabetically less than or equal to
    this value.
    """

    status: Literal["active", "all", "inactive"]
    """Filter for inventory items that are active, inactive, or both."""

    updated_after: Annotated[str, PropertyInfo(alias="updatedAfter")]
    """
    Filter for inventory items updated on or after this date and time, in ISO 8601
    format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time
    is assumed to be 00:00:00 of that day.

    WARNING: Due to a known issue in QuickBooks Desktop, the `updatedAfter`
    parameter may not correctly filter inventory items by their updated dates. To
    accurately retrieve the desired inventory items, we recommend avoiding this
    parameter and instead fetching a broader dataset, then filtering the results
    locally using the `updatedAt` property.
    """

    updated_before: Annotated[str, PropertyInfo(alias="updatedBefore")]
    """
    Filter for inventory items updated on or before this date and time, in ISO 8601
    format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time
    is assumed to be 23:59:59 of that day.

    WARNING: Due to a known issue in QuickBooks Desktop, the `updatedBefore`
    parameter may not correctly filter inventory items by their updated dates. To
    accurately retrieve the desired inventory items, we recommend avoiding this
    parameter and instead fetching a broader dataset, then filtering the results
    locally using the `updatedAt` property.
    """
