# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import date

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.qbd import check_list_params
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.qbd.qbd_check import QbdCheck

__all__ = ["ChecksResource", "AsyncChecksResource"]


class ChecksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ChecksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return ChecksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChecksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return ChecksResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        conductor_end_user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QbdCheck:
        """
        Retrieves a check by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the check to retrieve.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get(
            f"/quickbooks-desktop/checks/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QbdCheck,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        account_ids: List[str] | NotGiven = NOT_GIVEN,
        currency_ids: List[str] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        ids: List[str] | NotGiven = NOT_GIVEN,
        include_line_items: bool | NotGiven = NOT_GIVEN,
        include_linked_transactions: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        payee_ids: List[str] | NotGiven = NOT_GIVEN,
        ref_number_contains: str | NotGiven = NOT_GIVEN,
        ref_number_ends_with: str | NotGiven = NOT_GIVEN,
        ref_number_from: str | NotGiven = NOT_GIVEN,
        ref_numbers: List[str] | NotGiven = NOT_GIVEN,
        ref_number_starts_with: str | NotGiven = NOT_GIVEN,
        ref_number_to: str | NotGiven = NOT_GIVEN,
        transaction_date_from: Union[str, date] | NotGiven = NOT_GIVEN,
        transaction_date_to: Union[str, date] | NotGiven = NOT_GIVEN,
        updated_after: str | NotGiven = NOT_GIVEN,
        updated_before: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorPage[QbdCheck]:
        """
        Returns a list of checks.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          account_ids: Filter for checks from this account or accounts. Specify a single account ID or
              multiple using a comma-separated list (e.g., `accountIds=1,2,3`).

          currency_ids: Filter for checks in this currency or currencies. Specify a single currency ID
              or multiple using a comma-separated list (e.g., `currencyIds=1,2,3`).

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Retrieve this value from the `nextCursor` field in the
              previous response. If omitted, the API returns the first page of results.

          ids: Filter for specific checks by their QuickBooks-assigned unique identifier(s).

              NOTE: If you include this parameter, QuickBooks will ignore all other query
              parameters.

          include_line_items: Whether to include line items in the response.

          include_linked_transactions: Whether to include linked transactions in the response. For example, a payment
              linked to the corresponding check.

          limit: The maximum number of objects to return. Ranging from 1 to 150, defaults to 150.
              Use this parameter in conjunction with the `cursor` parameter to paginate
              through results. The response will include a `nextCursor` field, which can be
              used as the `cursor` parameter value in subsequent requests to fetch the next
              set of results.

          payee_ids: Filter for checks from this payee or payees. Specify a single payee ID or
              multiple using a comma-separated list (e.g., `payeeIds=1,2,3`). The person or
              company to whom the check is written.

          ref_number_contains: Filter for checks whose `refNumber` contains this substring. NOTE: If you use
              this parameter, you cannot also use `refNumberStartsWith` or
              `refNumberEndsWith`.

          ref_number_ends_with: Filter for checks whose `refNumber` ends with this substring. NOTE: If you use
              this parameter, you cannot also use `refNumberContains` or
              `refNumberStartsWith`.

          ref_number_from: Filter for checks whose `refNumber` is greater than or equal to this value. If
              omitted, the range will begin with the first number of the list. Uses a
              numerical comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          ref_numbers: Filter for specific checks by their ref-number(s), case-sensitive. In
              QuickBooks, ref-numbers are not required to be unique and can be arbitrarily
              changed by the QuickBooks user.

              NOTE: If you include this parameter, QuickBooks will ignore all other query
              parameters.

          ref_number_starts_with: Filter for checks whose `refNumber` starts with this substring. NOTE: If you use
              this parameter, you cannot also use `refNumberContains` or `refNumberEndsWith`.

          ref_number_to: Filter for checks whose `refNumber` is less than or equal to this value. If
              omitted, the range will end with the last number of the list. Uses a numerical
              comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          transaction_date_from: Filter for checks created on or after this date, in ISO 8601 format
              (YYYY-MM-DD).

          transaction_date_to: Filter for checks created on or before this date, in ISO 8601 format
              (YYYY-MM-DD).

          updated_after: Filter for checks updated on or after this date and time, in ISO 8601 format
              (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
              assumed to be 00:00:00 of that day.

          updated_before: Filter for checks updated on or before this date and time, in ISO 8601 format
              (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
              assumed to be 23:59:59 of that day.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get_api_list(
            "/quickbooks-desktop/checks",
            page=SyncCursorPage[QbdCheck],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_ids": account_ids,
                        "currency_ids": currency_ids,
                        "cursor": cursor,
                        "ids": ids,
                        "include_line_items": include_line_items,
                        "include_linked_transactions": include_linked_transactions,
                        "limit": limit,
                        "payee_ids": payee_ids,
                        "ref_number_contains": ref_number_contains,
                        "ref_number_ends_with": ref_number_ends_with,
                        "ref_number_from": ref_number_from,
                        "ref_numbers": ref_numbers,
                        "ref_number_starts_with": ref_number_starts_with,
                        "ref_number_to": ref_number_to,
                        "transaction_date_from": transaction_date_from,
                        "transaction_date_to": transaction_date_to,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                    },
                    check_list_params.CheckListParams,
                ),
            ),
            model=QbdCheck,
        )


class AsyncChecksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChecksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChecksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChecksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return AsyncChecksResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        conductor_end_user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QbdCheck:
        """
        Retrieves a check by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the check to retrieve.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._get(
            f"/quickbooks-desktop/checks/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QbdCheck,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        account_ids: List[str] | NotGiven = NOT_GIVEN,
        currency_ids: List[str] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        ids: List[str] | NotGiven = NOT_GIVEN,
        include_line_items: bool | NotGiven = NOT_GIVEN,
        include_linked_transactions: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        payee_ids: List[str] | NotGiven = NOT_GIVEN,
        ref_number_contains: str | NotGiven = NOT_GIVEN,
        ref_number_ends_with: str | NotGiven = NOT_GIVEN,
        ref_number_from: str | NotGiven = NOT_GIVEN,
        ref_numbers: List[str] | NotGiven = NOT_GIVEN,
        ref_number_starts_with: str | NotGiven = NOT_GIVEN,
        ref_number_to: str | NotGiven = NOT_GIVEN,
        transaction_date_from: Union[str, date] | NotGiven = NOT_GIVEN,
        transaction_date_to: Union[str, date] | NotGiven = NOT_GIVEN,
        updated_after: str | NotGiven = NOT_GIVEN,
        updated_before: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[QbdCheck, AsyncCursorPage[QbdCheck]]:
        """
        Returns a list of checks.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          account_ids: Filter for checks from this account or accounts. Specify a single account ID or
              multiple using a comma-separated list (e.g., `accountIds=1,2,3`).

          currency_ids: Filter for checks in this currency or currencies. Specify a single currency ID
              or multiple using a comma-separated list (e.g., `currencyIds=1,2,3`).

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Retrieve this value from the `nextCursor` field in the
              previous response. If omitted, the API returns the first page of results.

          ids: Filter for specific checks by their QuickBooks-assigned unique identifier(s).

              NOTE: If you include this parameter, QuickBooks will ignore all other query
              parameters.

          include_line_items: Whether to include line items in the response.

          include_linked_transactions: Whether to include linked transactions in the response. For example, a payment
              linked to the corresponding check.

          limit: The maximum number of objects to return. Ranging from 1 to 150, defaults to 150.
              Use this parameter in conjunction with the `cursor` parameter to paginate
              through results. The response will include a `nextCursor` field, which can be
              used as the `cursor` parameter value in subsequent requests to fetch the next
              set of results.

          payee_ids: Filter for checks from this payee or payees. Specify a single payee ID or
              multiple using a comma-separated list (e.g., `payeeIds=1,2,3`). The person or
              company to whom the check is written.

          ref_number_contains: Filter for checks whose `refNumber` contains this substring. NOTE: If you use
              this parameter, you cannot also use `refNumberStartsWith` or
              `refNumberEndsWith`.

          ref_number_ends_with: Filter for checks whose `refNumber` ends with this substring. NOTE: If you use
              this parameter, you cannot also use `refNumberContains` or
              `refNumberStartsWith`.

          ref_number_from: Filter for checks whose `refNumber` is greater than or equal to this value. If
              omitted, the range will begin with the first number of the list. Uses a
              numerical comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          ref_numbers: Filter for specific checks by their ref-number(s), case-sensitive. In
              QuickBooks, ref-numbers are not required to be unique and can be arbitrarily
              changed by the QuickBooks user.

              NOTE: If you include this parameter, QuickBooks will ignore all other query
              parameters.

          ref_number_starts_with: Filter for checks whose `refNumber` starts with this substring. NOTE: If you use
              this parameter, you cannot also use `refNumberContains` or `refNumberEndsWith`.

          ref_number_to: Filter for checks whose `refNumber` is less than or equal to this value. If
              omitted, the range will end with the last number of the list. Uses a numerical
              comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          transaction_date_from: Filter for checks created on or after this date, in ISO 8601 format
              (YYYY-MM-DD).

          transaction_date_to: Filter for checks created on or before this date, in ISO 8601 format
              (YYYY-MM-DD).

          updated_after: Filter for checks updated on or after this date and time, in ISO 8601 format
              (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
              assumed to be 00:00:00 of that day.

          updated_before: Filter for checks updated on or before this date and time, in ISO 8601 format
              (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
              assumed to be 23:59:59 of that day.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get_api_list(
            "/quickbooks-desktop/checks",
            page=AsyncCursorPage[QbdCheck],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_ids": account_ids,
                        "currency_ids": currency_ids,
                        "cursor": cursor,
                        "ids": ids,
                        "include_line_items": include_line_items,
                        "include_linked_transactions": include_linked_transactions,
                        "limit": limit,
                        "payee_ids": payee_ids,
                        "ref_number_contains": ref_number_contains,
                        "ref_number_ends_with": ref_number_ends_with,
                        "ref_number_from": ref_number_from,
                        "ref_numbers": ref_numbers,
                        "ref_number_starts_with": ref_number_starts_with,
                        "ref_number_to": ref_number_to,
                        "transaction_date_from": transaction_date_from,
                        "transaction_date_to": transaction_date_to,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                    },
                    check_list_params.CheckListParams,
                ),
            ),
            model=QbdCheck,
        )


class ChecksResourceWithRawResponse:
    def __init__(self, checks: ChecksResource) -> None:
        self._checks = checks

        self.retrieve = to_raw_response_wrapper(
            checks.retrieve,
        )
        self.list = to_raw_response_wrapper(
            checks.list,
        )


class AsyncChecksResourceWithRawResponse:
    def __init__(self, checks: AsyncChecksResource) -> None:
        self._checks = checks

        self.retrieve = async_to_raw_response_wrapper(
            checks.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            checks.list,
        )


class ChecksResourceWithStreamingResponse:
    def __init__(self, checks: ChecksResource) -> None:
        self._checks = checks

        self.retrieve = to_streamed_response_wrapper(
            checks.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            checks.list,
        )


class AsyncChecksResourceWithStreamingResponse:
    def __init__(self, checks: AsyncChecksResource) -> None:
        self._checks = checks

        self.retrieve = async_to_streamed_response_wrapper(
            checks.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            checks.list,
        )
