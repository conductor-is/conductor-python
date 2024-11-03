# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CreditCardCreditListParams"]


class CreditCardCreditListParams(TypedDict, total=False):
    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    account_ids: Annotated[str, PropertyInfo(alias="accountIds")]
    """Filter for credit card credits from this account or accounts.

    Specify a single account ID or multiple using a comma-separated list (e.g.,
    `accountIds=1,2,3`).
    """

    currency_ids: Annotated[str, PropertyInfo(alias="currencyIds")]
    """Filter for credit card credits in this currency or currencies.

    Specify a single currency ID or multiple using a comma-separated list (e.g.,
    `currencyIds=1,2,3`).
    """

    cursor: str
    """
    The pagination token to fetch the next set of results when paginating with the
    `limit` parameter. Retrieve this value from the `nextCursor` field in the
    previous response. If omitted, the API returns the first page of results.
    """

    ids: str
    """
    Filter for specific credit card credits by their QuickBooks-assigned unique
    identifier(s). Specify a single ID or multiple using a comma-separated list
    (e.g., `ids=1,2,3`).

    NOTE: If you include this parameter, all other query parameters will be ignored.
    """

    include_line_items: Annotated[bool, PropertyInfo(alias="includeLineItems")]
    """Whether to include line items in the response."""

    limit: int
    """The maximum number of objects to return.

    Ranging from 1 to 200, defaults to 200. Use this parameter in conjunction with
    the `cursor` parameter to paginate through results. The response will include a
    `nextCursor` field, which can be used as the `cursor` parameter value in
    subsequent requests to fetch the next set of results.
    """

    payee_ids: Annotated[str, PropertyInfo(alias="payeeIds")]
    """Filter for credit card credits from this payee or payees.

    Specify a single payee ID or multiple using a comma-separated list (e.g.,
    `payeeIds=1,2,3`). These are the vendors or companies from whom the credits were
    received.
    """

    ref_number_contains: Annotated[str, PropertyInfo(alias="refNumberContains")]
    """Filter for credit card credits whose `refNumber` contains this substring.

    If you use this parameter, you cannot also use `refNumberStartsWith` or
    `refNumberEndsWith`.
    """

    ref_number_ends_with: Annotated[str, PropertyInfo(alias="refNumberEndsWith")]
    """Filter for credit card credits whose `refNumber` ends with this substring.

    If you use this parameter, you cannot also use `refNumberContains` or
    `refNumberStartsWith`.
    """

    ref_number_from: Annotated[str, PropertyInfo(alias="refNumberFrom")]
    """
    Filter for credit card credits whose `refNumber` is greater than or equal to
    this value. If omitted, the range will begin with the first number of the list.
    Uses a numerical comparison for values that contain only digits; otherwise, uses
    a lexicographical comparison.
    """

    ref_numbers: Annotated[str, PropertyInfo(alias="refNumbers")]
    """Filter for specific credit card credits by their ref-number(s), case-sensitive.

    Specify a single ref-number or multiple using a comma-separated list (e.g.,
    `refNumbers=1,2,3`). In QuickBooks, ref-numbers are not required to be unique
    and can be arbitrarily changed by the QuickBooks user.

    NOTE: If you include this parameter, all other query parameters will be ignored.
    """

    ref_number_starts_with: Annotated[str, PropertyInfo(alias="refNumberStartsWith")]
    """Filter for credit card credits whose `refNumber` starts with this substring.

    If you use this parameter, you cannot also use `refNumberContains` or
    `refNumberEndsWith`.
    """

    ref_number_to: Annotated[str, PropertyInfo(alias="refNumberTo")]
    """
    Filter for credit card credits whose `refNumber` is less than or equal to this
    value. If omitted, the range will end with the last number of the list. Uses a
    numerical comparison for values that contain only digits; otherwise, uses a
    lexicographical comparison.
    """

    transaction_date_from: Annotated[Union[str, date], PropertyInfo(alias="transactionDateFrom", format="iso8601")]
    """
    Filter for credit card credits created on or after this date, in ISO 8601 format
    (YYYY-MM-DD).
    """

    transaction_date_to: Annotated[Union[str, date], PropertyInfo(alias="transactionDateTo", format="iso8601")]
    """
    Filter for credit card credits created on or before this date, in ISO 8601
    format (YYYY-MM-DD).
    """

    updated_after: Annotated[str, PropertyInfo(alias="updatedAfter")]
    """
    Filter for credit card credits updated on or after this date and time, in ISO
    8601 format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the
    time is assumed to be 00:00:00 of that day.
    """

    updated_before: Annotated[str, PropertyInfo(alias="updatedBefore")]
    """
    Filter for credit card credits updated on or before this date and time, in ISO
    8601 format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the
    time is assumed to be 23:59:59 of that day.
    """
