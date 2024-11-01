# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ClassListParams"]


class ClassListParams(TypedDict, total=False):
    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    full_names: Annotated[str, PropertyInfo(alias="fullNames")]
    """Filter for specific classes by their full-name(s).

    Specify a single full-name or multiple using a comma-separated list (e.g.,
    `fullNames=1,2,3`). Like `id`, a `fullName` is a unique identifier for a class,
    and is formed by by combining the names of its parent objects with its own
    `name`, separated by colons. For example, if a class is under "Department" and
    has the `name` "Marketing", its `fullName` would be "Department:Marketing".
    Unlike `name`, `fullName` is guaranteed to be unique across all class objects.
    Not case-sensitive. NOTE: If you include this parameter, all other query
    parameters will be ignored.
    """

    ids: str
    """Filter for specific classes by their QuickBooks-assigned unique identifier(s).

    Specify a single ID or multiple using a comma-separated list (e.g.,
    `ids=1,2,3`). NOTE: If you include this parameter, all other query parameters
    will be ignored.
    """

    limit: int
    """The maximum number of objects to return, ranging from 1 to 500.

    Defaults to 500. NOTE: QuickBooks Desktop does not support cursor-based
    pagination for classes. Hence, this parameter will limit the response size, but
    you will not be able to fetch the next set of results. To paginate through the
    results for this endpoint, try fetching batches via the date-range query
    parameters.
    """

    name_contains: Annotated[str, PropertyInfo(alias="nameContains")]
    """Filter for classes whose `name` contains this substring (case insensitive).

    If you use this parameter, you cannot use `nameStartsWith` or `nameEndsWith`.
    """

    name_ends_with: Annotated[str, PropertyInfo(alias="nameEndsWith")]
    """Filter for classes whose `name` ends with this substring (case insensitive).

    If you use this parameter, you cannot use `nameContains` or `nameStartsWith`.
    """

    name_from: Annotated[str, PropertyInfo(alias="nameFrom")]
    """
    Filter for classes whose `name` is alphabetically greater than or equal to this
    value.
    """

    name_starts_with: Annotated[str, PropertyInfo(alias="nameStartsWith")]
    """Filter for classes whose `name` starts with this substring (case insensitive).

    If you use this parameter, you cannot use `nameContains` or `nameEndsWith`.
    """

    name_to: Annotated[str, PropertyInfo(alias="nameTo")]
    """
    Filter for classes whose `name` is alphabetically less than or equal to this
    value.
    """

    status: Literal["active", "all", "inactive"]
    """Filter for classes that are active, inactive, or both."""

    updated_after: Annotated[str, PropertyInfo(alias="updatedAfter")]
    """
    Filter for classes updated on or after this date and time, in ISO 8601 format
    (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
    assumed to be 00:00:00 of that day.
    """

    updated_before: Annotated[str, PropertyInfo(alias="updatedBefore")]
    """
    Filter for classes updated on or before this date and time, in ISO 8601 format
    (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
    assumed to be 23:59:59 of that day.
    """
