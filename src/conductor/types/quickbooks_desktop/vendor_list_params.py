# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["VendorListParams"]


class VendorListParams(TypedDict, total=False):
    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    id: Union[str, List[str]]
    """Filter for vendors with the specified QuickBooks-assigned unique identifier(s).

    If your request includes this parameter, all other query parameters will be
    ignored.
    """

    class_id: Annotated[Union[str, List[str]], PropertyInfo(alias="classId")]
    """Filter for vendors of this class or classes.

    A class is a way end-users can categorize vendors in QuickBooks.
    """

    currency_id: Annotated[Union[str, List[str]], PropertyInfo(alias="currencyId")]
    """Filter for vendors in this currency or currencies."""

    cursor: str
    """
    The pagination token to use with the `cursor` request parameter to fetch the
    next set of results. This value was returned in the `nextCursor` field of the
    previous response when using the `limit` parameter.
    """

    full_name: Annotated[Union[str, List[str]], PropertyInfo(alias="fullName")]
    """Filter for vendors with this full-name or full-names.

    Like `id`, a full-name is a unique identifier for a vendor, and is created by
    prefixing the vendor's name with the names of each ancestor. If your request
    includes this parameter, all other query parameters will be ignored.
    """

    limit: int
    """The maximum number of objects to return, ranging from 1 to 500.

    Defaults to 500. Include this parameter to paginate through the results. The
    `nextCursor` field in the response will contain the value to use with the
    `cursor` request parameter to fetch the next set of results.
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

    total_balance: Annotated[str, PropertyInfo(alias="totalBalance")]
    """Filter for objects whose `totalBalance` equals this amount.

    You can only use one total-balance filter at a time.
    """

    total_balance_gt: Annotated[str, PropertyInfo(alias="totalBalanceGt")]
    """Filter for objects whose `totalBalance` is greater than this amount.

    You can only use one total-balance filter at a time.
    """

    total_balance_gte: Annotated[str, PropertyInfo(alias="totalBalanceGte")]
    """Filter for objects whose `totalBalance` is greater than or equal to this amount.

    You can only use one total-balance filter at a time.
    """

    total_balance_lt: Annotated[str, PropertyInfo(alias="totalBalanceLt")]
    """Filter for objects whose `totalBalance` is less than this amount.

    You can only use one total-balance filter at a time.
    """

    total_balance_lte: Annotated[str, PropertyInfo(alias="totalBalanceLte")]
    """Filter for objects whose `totalBalance` is less than or equal to this amount.

    You can only use one total-balance filter at a time.
    """

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
