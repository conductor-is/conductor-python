# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BillListParams"]


class BillListParams(TypedDict, total=False):
    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    id: Union[str, List[str]]
    """The QuickBooks-assigned unique identifier of the transaction to return.

    You can provide one or multiple instances of this parameter to fetch specific
    transactions.
    """

    account_id: Annotated[Union[str, List[str]], PropertyInfo(alias="accountId")]
    """
    Filter for bills from this account (e.g., accounts receivable, accounts
    payable).
    """

    cursor: str
    """
    The pagination token to use with the `cursor` request parameter to fetch the
    next set of results. This value was returned in the `nextCursor` field of the
    previous response when using the `limit` parameter.
    """

    include_line_items: Annotated[bool, PropertyInfo(alias="includeLineItems")]
    """Whether to include line items in the response."""

    include_linked_transactions: Annotated[bool, PropertyInfo(alias="includeLinkedTransactions")]
    """Whether to include linked transactions in the response.

    For example, a bill payment linked to a bill.
    """

    limit: int
    """The maximum number of objects to return, ranging from 1 to 500.

    Defaults to 500. Include this parameter to paginate through the results. The
    `nextCursor` field in the response will contain the value to use with the
    `cursor` request parameter to fetch the next set of results.
    """

    paid_status: Annotated[Literal["all", "paid", "not_paid"], PropertyInfo(alias="paidStatus")]
    """Filter for transactions that are paid, not paid, or both."""

    ref_number: Annotated[Union[str, List[str]], PropertyInfo(alias="refNumber")]
    """The user-defined identifier for the transaction.

    It is not required to be unique and can be arbitrarily changed by the QuickBooks
    user. Case sensitive. You can provide one or multiple instances of this
    parameter to fetch specific transactions.
    """

    ref_number_contains: Annotated[str, PropertyInfo(alias="refNumberContains")]
    """Filter for transactions whose `refNumber` contains this substring.

    If you use this parameter, you cannot use `refNumberStartsWith` or
    `refNumberEndsWith`.
    """

    ref_number_ends_with: Annotated[str, PropertyInfo(alias="refNumberEndsWith")]
    """Filter for transactions whose `refNumber` ends with this substring.

    If you use this parameter, you cannot use `refNumberContains` or
    `refNumberStartsWith`.
    """

    ref_number_from: Annotated[str, PropertyInfo(alias="refNumberFrom")]
    """Filter for transactions whose `refNumber` is greater than or equal to this
    value.

    If omitted, the range will begin with the first number of the list. Uses a
    numerical comparison for values that contain only digits; otherwise, uses a
    lexicographical comparison.
    """

    ref_number_starts_with: Annotated[str, PropertyInfo(alias="refNumberStartsWith")]
    """Filter for transactions whose `refNumber` starts with this substring.

    If you use this parameter, you cannot use `refNumberContains` or
    `refNumberEndsWith`.
    """

    ref_number_to: Annotated[str, PropertyInfo(alias="refNumberTo")]
    """Filter for transactions whose `refNumber` is less than or equal to this value.

    If omitted, the range will end with the last number of the list. Uses a
    numerical comparison for values that contain only digits; otherwise, uses a
    lexicographical comparison.
    """

    transaction_date_from: Annotated[str, PropertyInfo(alias="transactionDateFrom")]
    """
    Filter for transactions created on or after this date, in ISO 8601 format
    (YYYY-MM-DD).
    """

    transaction_date_to: Annotated[str, PropertyInfo(alias="transactionDateTo")]
    """
    Filter for transactions created on or before this date, in ISO 8601 format
    (YYYY-MM-DD).
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

    vendor_id: Annotated[Union[str, List[str]], PropertyInfo(alias="vendorId")]
    """Filter for bills from this vendor."""
