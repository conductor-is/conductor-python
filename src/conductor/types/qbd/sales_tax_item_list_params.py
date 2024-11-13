# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SalesTaxItemListParams"]


class SalesTaxItemListParams(TypedDict, total=False):
    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    class_ids: Annotated[List[str], PropertyInfo(alias="classIds")]
    """Filter for sales-tax items of this class or classes.

    A class is a way end-users can categorize sales-tax items in QuickBooks.
    """

    cursor: str
    """
    The pagination token to fetch the next set of results when paginating with the
    `limit` parameter. Retrieve this value from the `nextCursor` field in the
    previous response. If omitted, the API returns the first page of results.
    """

    full_names: Annotated[List[str], PropertyInfo(alias="fullNames")]
    """Filter for specific sales-tax items by their full-name(s), case-insensitive.

    Like `id`, `fullName` is a unique identifier for a sales-tax item, formed by by
    combining the names of its parent objects with its own `name`, separated by
    colons. For example, if a sales-tax item is under "State" and has the `name` "CA
    Sales Tax", its `fullName` would be "State:CA Sales Tax".

    Unlike `name`, `fullName` is guaranteed to be unique across all sales-tax item
    objects. Also, unlike `id`, `fullName` can be arbitrarily changed by the
    QuickBooks user when modifying its underlying `name` field.

    NOTE: If you include this parameter, QuickBooks will ignore all other query
    parameters.
    """

    ids: List[str]
    """
    Filter for specific sales-tax items by their QuickBooks-assigned unique
    identifier(s).

    NOTE: If you include this parameter, QuickBooks will ignore all other query
    parameters.
    """

    limit: int
    """The maximum number of objects to return.

    Ranging from 1 to 150, defaults to 150. Use this parameter in conjunction with
    the `cursor` parameter to paginate through results. The response will include a
    `nextCursor` field, which can be used as the `cursor` parameter value in
    subsequent requests to fetch the next set of results.
    """

    name_contains: Annotated[str, PropertyInfo(alias="nameContains")]
    """
    Filter for sales-tax items whose `name` contains this substring,
    case-insensitive. NOTE: If you use this parameter, you cannot also use
    `nameStartsWith` or `nameEndsWith`.
    """

    name_ends_with: Annotated[str, PropertyInfo(alias="nameEndsWith")]
    """
    Filter for sales-tax items whose `name` ends with this substring,
    case-insensitive. NOTE: If you use this parameter, you cannot also use
    `nameContains` or `nameStartsWith`.
    """

    name_from: Annotated[str, PropertyInfo(alias="nameFrom")]
    """
    Filter for sales-tax items whose `name` is alphabetically greater than or equal
    to this value.
    """

    name_starts_with: Annotated[str, PropertyInfo(alias="nameStartsWith")]
    """
    Filter for sales-tax items whose `name` starts with this substring,
    case-insensitive. NOTE: If you use this parameter, you cannot also use
    `nameContains` or `nameEndsWith`.
    """

    name_to: Annotated[str, PropertyInfo(alias="nameTo")]
    """
    Filter for sales-tax items whose `name` is alphabetically less than or equal to
    this value.
    """

    status: Literal["active", "all", "inactive"]
    """Filter for sales-tax items that are active, inactive, or both."""

    updated_after: Annotated[str, PropertyInfo(alias="updatedAfter")]
    """
    Filter for sales-tax items updated on or after this date and time, in ISO 8601
    format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time
    is assumed to be 00:00:00 of that day.
    """

    updated_before: Annotated[str, PropertyInfo(alias="updatedBefore")]
    """
    Filter for sales-tax items updated on or before this date and time, in ISO 8601
    format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time
    is assumed to be 23:59:59 of that day.
    """
