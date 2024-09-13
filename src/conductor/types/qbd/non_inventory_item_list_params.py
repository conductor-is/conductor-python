# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["NonInventoryItemListParams"]


class NonInventoryItemListParams(TypedDict, total=False):
    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    class_ids: Annotated[str, PropertyInfo(alias="classIds")]
    """Filter for non-inventory-items of this class or classes.

    Specify a single class ID or multiple using a comma-separated list (e.g.,
    `classIds=1,2,3`). A class is a way end-users can categorize non-inventory-items
    in QuickBooks.
    """

    cursor: str
    """
    The pagination token to fetch the next set of results when paginating with the
    `limit` parameter. Retrieve this value from the `nextCursor` field in the
    previous response. If omitted, the API returns the first page of results.
    """

    full_names: Annotated[str, PropertyInfo(alias="fullNames")]
    """Filter for specific non-inventory-items by their full-name(s).

    Specify a single full-name or multiple using a comma-separated list (e.g.,
    `fullNames=1,2,3`). Like `id`, a `fullName` is a unique identifier for a
    non-inventory-item, and is formed by by combining the names of its parent
    objects with its own `name`, separated by colons. For example, if a
    non-inventory-item is under 'Office Supplies' and has the `name` 'Printer Ink
    Cartridge', its `fullName` would be 'Office Supplies:Printer Ink Cartridge'.
    Unlike `name`, `fullName` is guaranteed to be unique across all
    non-inventory-item objects. NOTE: If you include this parameter, all other query
    parameters will be ignored.
    """

    ids: str
    """
    Filter for specific non-inventory-items by their QuickBooks-assigned unique
    identifier(s). Specify a single ID or multiple using a comma-separated list
    (e.g., `ids=1,2,3`). NOTE: If you include this parameter, all other query
    parameters will be ignored.
    """

    limit: int
    """The maximum number of objects to return, ranging from 1 to 500.

    Defaults to 500. Use this parameter in conjunction with the `cursor` parameter
    to paginate through results. The response will include a `nextCursor` field,
    which can be used as the `cursor` parameter value in subsequent requests to
    fetch the next set of results.
    """

    name_contains: Annotated[str, PropertyInfo(alias="nameContains")]
    """Filter for objects whose `name` contains this substring.

    If you use this parameter, you cannot use `nameStartsWith` or `nameEndsWith`.
    """

    name_ends_with: Annotated[str, PropertyInfo(alias="nameEndsWith")]
    """Filter for objects whose `name` ends with this substring.

    If you use this parameter, you cannot use `nameContains` or `nameStartsWith`.
    """

    name_from: Annotated[str, PropertyInfo(alias="nameFrom")]
    """
    Filter for objects whose `name` is alphabetically greater than or equal to this
    value.
    """

    name_starts_with: Annotated[str, PropertyInfo(alias="nameStartsWith")]
    """Filter for objects whose `name` starts with this substring.

    If you use this parameter, you cannot use `nameContains` or `nameEndsWith`.
    """

    name_to: Annotated[str, PropertyInfo(alias="nameTo")]
    """
    Filter for objects whose `name` is alphabetically less than or equal to this
    value.
    """

    status: Literal["active", "all", "inactive"]
    """Filter for objects that are active, inactive, or both."""

    updated_after: Annotated[str, PropertyInfo(alias="updatedAfter")]
    """
    Filter for objects updated on or after this date and time, in ISO 8601 format
    (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
    assumed to be 00:00:00 of that day.
    """

    updated_before: Annotated[str, PropertyInfo(alias="updatedBefore")]
    """
    Filter for objects updated on or before this date and time, in ISO 8601 format
    (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
    assumed to be 23:59:59 of that day.
    """
