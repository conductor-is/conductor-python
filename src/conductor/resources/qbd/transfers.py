# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.qbd import transfer_list_params, transfer_create_params, transfer_update_params
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.qbd.transfer import Transfer

__all__ = ["TransfersResource", "AsyncTransfersResource"]


class TransfersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TransfersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return TransfersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TransfersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return TransfersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        transaction_date: Union[str, date],
        conductor_end_user_id: str,
        amount: str | NotGiven = NOT_GIVEN,
        class_id: str | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        transfer_from_account_id: str | NotGiven = NOT_GIVEN,
        transfer_to_account_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Transfer:
        """
        Creates a transfer.

        Args:
          transaction_date: The date of this transfer, in ISO 8601 format (YYYY-MM-DD).

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          amount: The monetary amount of this transfer, represented as a decimal string.

          class_id: The transfer's class. Classes can be used to categorize objects into meaningful
              segments, such as department, location, or type of work. In QuickBooks, class
              tracking is off by default.

          memo: A memo or note for this transfer, as entered by the user.

          transfer_from_account_id: The account from which money will be transferred.

          transfer_to_account_id: The account to which money will be transferred.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            "/quickbooks-desktop/transfers",
            body=maybe_transform(
                {
                    "transaction_date": transaction_date,
                    "amount": amount,
                    "class_id": class_id,
                    "memo": memo,
                    "transfer_from_account_id": transfer_from_account_id,
                    "transfer_to_account_id": transfer_to_account_id,
                },
                transfer_create_params.TransferCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Transfer,
        )

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
    ) -> Transfer:
        """
        Retrieves a transfer by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the transfer to retrieve.

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
            f"/quickbooks-desktop/transfers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Transfer,
        )

    def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        amount: str | NotGiven = NOT_GIVEN,
        class_id: str | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        transaction_date: Union[str, date] | NotGiven = NOT_GIVEN,
        transfer_from_account_id: str | NotGiven = NOT_GIVEN,
        transfer_to_account_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Transfer:
        """
        Updates an existing transfer.

        Args:
          id: The QuickBooks-assigned unique identifier of the transfer to update.

          revision_number: The current revision number of the transfer you are updating, which you can get
              by fetching the object first. Provide the most recent `revisionNumber` to ensure
              you're working with the latest data; otherwise, the update will return an error.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          amount: The monetary amount of this transfer, represented as a decimal string.

          class_id: The transfer's class. Classes can be used to categorize objects into meaningful
              segments, such as department, location, or type of work. In QuickBooks, class
              tracking is off by default.

          memo: A memo or note for this transfer, as entered by the user.

          transaction_date: The date of this transfer, in ISO 8601 format (YYYY-MM-DD).

          transfer_from_account_id: The account from which money will be transferred.

          transfer_to_account_id: The account to which money will be transferred.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            f"/quickbooks-desktop/transfers/{id}",
            body=maybe_transform(
                {
                    "revision_number": revision_number,
                    "amount": amount,
                    "class_id": class_id,
                    "memo": memo,
                    "transaction_date": transaction_date,
                    "transfer_from_account_id": transfer_from_account_id,
                    "transfer_to_account_id": transfer_to_account_id,
                },
                transfer_update_params.TransferUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Transfer,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        cursor: str | NotGiven = NOT_GIVEN,
        ids: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
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
    ) -> SyncCursorPage[Transfer]:
        """
        Returns a list of transfers.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Retrieve this value from the `nextCursor` field in the
              previous response. If omitted, the API returns the first page of results.

          ids: Filter for specific transfers by their QuickBooks-assigned unique identifier(s).
              Specify a single ID or multiple using a comma-separated list (e.g.,
              `ids=1,2,3`).

              NOTE: If you include this parameter, all other query parameters will be ignored.

          limit: The maximum number of objects to return. Ranging from 1 to 200, defaults to 200.
              Use this parameter in conjunction with the `cursor` parameter to paginate
              through results. The response will include a `nextCursor` field, which can be
              used as the `cursor` parameter value in subsequent requests to fetch the next
              set of results.

          transaction_date_from: Filter for transfers created on or after this date, in ISO 8601 format
              (YYYY-MM-DD).

          transaction_date_to: Filter for transfers created on or before this date, in ISO 8601 format
              (YYYY-MM-DD).

          updated_after: Filter for transfers updated on or after this date and time, in ISO 8601 format
              (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
              assumed to be 00:00:00 of that day.

          updated_before: Filter for transfers updated on or before this date and time, in ISO 8601 format
              (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
              assumed to be 23:59:59 of that day.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get_api_list(
            "/quickbooks-desktop/transfers",
            page=SyncCursorPage[Transfer],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "ids": ids,
                        "limit": limit,
                        "transaction_date_from": transaction_date_from,
                        "transaction_date_to": transaction_date_to,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                    },
                    transfer_list_params.TransferListParams,
                ),
            ),
            model=Transfer,
        )


class AsyncTransfersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTransfersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTransfersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTransfersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return AsyncTransfersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        transaction_date: Union[str, date],
        conductor_end_user_id: str,
        amount: str | NotGiven = NOT_GIVEN,
        class_id: str | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        transfer_from_account_id: str | NotGiven = NOT_GIVEN,
        transfer_to_account_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Transfer:
        """
        Creates a transfer.

        Args:
          transaction_date: The date of this transfer, in ISO 8601 format (YYYY-MM-DD).

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          amount: The monetary amount of this transfer, represented as a decimal string.

          class_id: The transfer's class. Classes can be used to categorize objects into meaningful
              segments, such as department, location, or type of work. In QuickBooks, class
              tracking is off by default.

          memo: A memo or note for this transfer, as entered by the user.

          transfer_from_account_id: The account from which money will be transferred.

          transfer_to_account_id: The account to which money will be transferred.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            "/quickbooks-desktop/transfers",
            body=await async_maybe_transform(
                {
                    "transaction_date": transaction_date,
                    "amount": amount,
                    "class_id": class_id,
                    "memo": memo,
                    "transfer_from_account_id": transfer_from_account_id,
                    "transfer_to_account_id": transfer_to_account_id,
                },
                transfer_create_params.TransferCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Transfer,
        )

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
    ) -> Transfer:
        """
        Retrieves a transfer by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the transfer to retrieve.

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
            f"/quickbooks-desktop/transfers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Transfer,
        )

    async def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        amount: str | NotGiven = NOT_GIVEN,
        class_id: str | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        transaction_date: Union[str, date] | NotGiven = NOT_GIVEN,
        transfer_from_account_id: str | NotGiven = NOT_GIVEN,
        transfer_to_account_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Transfer:
        """
        Updates an existing transfer.

        Args:
          id: The QuickBooks-assigned unique identifier of the transfer to update.

          revision_number: The current revision number of the transfer you are updating, which you can get
              by fetching the object first. Provide the most recent `revisionNumber` to ensure
              you're working with the latest data; otherwise, the update will return an error.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          amount: The monetary amount of this transfer, represented as a decimal string.

          class_id: The transfer's class. Classes can be used to categorize objects into meaningful
              segments, such as department, location, or type of work. In QuickBooks, class
              tracking is off by default.

          memo: A memo or note for this transfer, as entered by the user.

          transaction_date: The date of this transfer, in ISO 8601 format (YYYY-MM-DD).

          transfer_from_account_id: The account from which money will be transferred.

          transfer_to_account_id: The account to which money will be transferred.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            f"/quickbooks-desktop/transfers/{id}",
            body=await async_maybe_transform(
                {
                    "revision_number": revision_number,
                    "amount": amount,
                    "class_id": class_id,
                    "memo": memo,
                    "transaction_date": transaction_date,
                    "transfer_from_account_id": transfer_from_account_id,
                    "transfer_to_account_id": transfer_to_account_id,
                },
                transfer_update_params.TransferUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Transfer,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        cursor: str | NotGiven = NOT_GIVEN,
        ids: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
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
    ) -> AsyncPaginator[Transfer, AsyncCursorPage[Transfer]]:
        """
        Returns a list of transfers.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Retrieve this value from the `nextCursor` field in the
              previous response. If omitted, the API returns the first page of results.

          ids: Filter for specific transfers by their QuickBooks-assigned unique identifier(s).
              Specify a single ID or multiple using a comma-separated list (e.g.,
              `ids=1,2,3`).

              NOTE: If you include this parameter, all other query parameters will be ignored.

          limit: The maximum number of objects to return. Ranging from 1 to 200, defaults to 200.
              Use this parameter in conjunction with the `cursor` parameter to paginate
              through results. The response will include a `nextCursor` field, which can be
              used as the `cursor` parameter value in subsequent requests to fetch the next
              set of results.

          transaction_date_from: Filter for transfers created on or after this date, in ISO 8601 format
              (YYYY-MM-DD).

          transaction_date_to: Filter for transfers created on or before this date, in ISO 8601 format
              (YYYY-MM-DD).

          updated_after: Filter for transfers updated on or after this date and time, in ISO 8601 format
              (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
              assumed to be 00:00:00 of that day.

          updated_before: Filter for transfers updated on or before this date and time, in ISO 8601 format
              (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
              assumed to be 23:59:59 of that day.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get_api_list(
            "/quickbooks-desktop/transfers",
            page=AsyncCursorPage[Transfer],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "ids": ids,
                        "limit": limit,
                        "transaction_date_from": transaction_date_from,
                        "transaction_date_to": transaction_date_to,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                    },
                    transfer_list_params.TransferListParams,
                ),
            ),
            model=Transfer,
        )


class TransfersResourceWithRawResponse:
    def __init__(self, transfers: TransfersResource) -> None:
        self._transfers = transfers

        self.create = to_raw_response_wrapper(
            transfers.create,
        )
        self.retrieve = to_raw_response_wrapper(
            transfers.retrieve,
        )
        self.update = to_raw_response_wrapper(
            transfers.update,
        )
        self.list = to_raw_response_wrapper(
            transfers.list,
        )


class AsyncTransfersResourceWithRawResponse:
    def __init__(self, transfers: AsyncTransfersResource) -> None:
        self._transfers = transfers

        self.create = async_to_raw_response_wrapper(
            transfers.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            transfers.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            transfers.update,
        )
        self.list = async_to_raw_response_wrapper(
            transfers.list,
        )


class TransfersResourceWithStreamingResponse:
    def __init__(self, transfers: TransfersResource) -> None:
        self._transfers = transfers

        self.create = to_streamed_response_wrapper(
            transfers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            transfers.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            transfers.update,
        )
        self.list = to_streamed_response_wrapper(
            transfers.list,
        )


class AsyncTransfersResourceWithStreamingResponse:
    def __init__(self, transfers: AsyncTransfersResource) -> None:
        self._transfers = transfers

        self.create = async_to_streamed_response_wrapper(
            transfers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            transfers.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            transfers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            transfers.list,
        )
