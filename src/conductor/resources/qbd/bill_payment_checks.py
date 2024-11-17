# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
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
from ...types.qbd import (
    bill_payment_check_list_params,
    bill_payment_check_create_params,
    bill_payment_check_update_params,
)
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.qbd.bill_payment_check import BillPaymentCheck

__all__ = ["BillPaymentChecksResource", "AsyncBillPaymentChecksResource"]


class BillPaymentChecksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BillPaymentChecksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return BillPaymentChecksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BillPaymentChecksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return BillPaymentChecksResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        apply_to_transactions: Iterable[bill_payment_check_create_params.ApplyToTransaction],
        bank_account_id: str,
        transaction_date: Union[str, date],
        vendor_id: str,
        conductor_end_user_id: str,
        exchange_rate: float | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        is_queued_for_print: bool | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        payables_account_id: str | NotGiven = NOT_GIVEN,
        ref_number: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BillPaymentCheck:
        """
        Creates a new bill payment check.

        Args:
          apply_to_transactions: The bills to be paid by this bill payment check. This will create a link between
              this bill payment check and the specified bills.

              **IMPORTANT**: In each `applyToTransactions` object, you must specify either
              `paymentAmount`, `applyCredits`, `discountAmount`, or any combination of these;
              if none of these are specified, you will receive an error for an empty
              transaction.

              **IMPORTANT**: The target bill must have `isPaid=false`, otherwise, QuickBooks
              will report this object as "cannot be found".

          bank_account_id: The bank account from which the funds are being drawn for this bill payment
              check; e.g., Checking or Savings. This bill payment check will decrease the
              balance of this account.

          transaction_date: The date of this bill payment check, in ISO 8601 format (YYYY-MM-DD).

          vendor_id: The vendor who sent the bill(s) that this check is paying and who will receive
              this payment.

              **IMPORTANT**: This vendor must match the `vendor` on the bill(s) specified in
              `applyToTransactions`; otherwise, QuickBooks will say the `transactionId` in
              `applyToTransactions` "does not exist".

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          exchange_rate: The market exchange rate between this bill payment check's currency and the home
              currency in QuickBooks at the time of this transaction. Represented as a decimal
              value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).

          external_id: A globally unique identifier (GUID) you can provide for tracking this object in
              your external system.

              **IMPORTANT**: Must be formatted as a valid GUID; otherwise, QuickBooks will
              return an error. This field is immutable and can only be set during object
              creation.

          is_queued_for_print: Indicates whether this bill payment check is included in the queue of documents
              for QuickBooks to print.

          memo: A memo or note for this bill payment check, as entered by the user.

          payables_account_id: The Accounts-Payable (A/P) account to which this bill payment check is assigned,
              used to track the amount owed. If not specified, QuickBooks Desktop will use its
              default Accounts-Payable account.

              **IMPORTANT**: If this bill payment check is linked to other transactions, this
              A/P account must match the `payablesAccount` used in the other transactions.

          ref_number: The case-sensitive user-defined reference number for this bill payment check,
              which can be used to identify the transaction in QuickBooks. This value is not
              required to be unique and can be arbitrarily changed by the QuickBooks user.

              **IMPORTANT**: For checks, this field is the check number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            "/quickbooks-desktop/bill-payment-checks",
            body=maybe_transform(
                {
                    "apply_to_transactions": apply_to_transactions,
                    "bank_account_id": bank_account_id,
                    "transaction_date": transaction_date,
                    "vendor_id": vendor_id,
                    "exchange_rate": exchange_rate,
                    "external_id": external_id,
                    "is_queued_for_print": is_queued_for_print,
                    "memo": memo,
                    "payables_account_id": payables_account_id,
                    "ref_number": ref_number,
                },
                bill_payment_check_create_params.BillPaymentCheckCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillPaymentCheck,
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
    ) -> BillPaymentCheck:
        """
        Retrieves a bill payment check by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the bill payment check to retrieve.

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
            f"/quickbooks-desktop/bill-payment-checks/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillPaymentCheck,
        )

    def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        amount: str | NotGiven = NOT_GIVEN,
        apply_to_transactions: Iterable[bill_payment_check_update_params.ApplyToTransaction] | NotGiven = NOT_GIVEN,
        bank_account_id: str | NotGiven = NOT_GIVEN,
        exchange_rate: float | NotGiven = NOT_GIVEN,
        is_queued_for_print: bool | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        ref_number: str | NotGiven = NOT_GIVEN,
        transaction_date: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BillPaymentCheck:
        """
        Updates an existing bill payment check.

        Args:
          id: The QuickBooks-assigned unique identifier of the bill payment check to update.

          revision_number: The current revision number of the bill payment check object you are updating,
              which you can get by fetching the object first. Provide the most recent
              `revisionNumber` to ensure you're working with the latest data; otherwise, the
              update will return an error.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          amount: The monetary amount of this bill payment check, represented as a decimal string.

          apply_to_transactions: The bills to be paid by this bill payment check. This will create a link between
              this bill payment check and the specified bills.

              **IMPORTANT**: In each `applyToTransactions` object, you must specify either
              `paymentAmount`, `applyCredits`, `discountAmount`, or any combination of these;
              if none of these are specified, you will receive an error for an empty
              transaction.

              **IMPORTANT**: The target bill must have `isPaid=false`, otherwise, QuickBooks
              will report this object as "cannot be found".

          bank_account_id: The bank account from which the funds are being drawn for this bill payment
              check; e.g., Checking or Savings. This bill payment check will decrease the
              balance of this account.

          exchange_rate: The market exchange rate between this bill payment check's currency and the home
              currency in QuickBooks at the time of this transaction. Represented as a decimal
              value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).

          is_queued_for_print: Indicates whether this bill payment check is included in the queue of documents
              for QuickBooks to print.

          memo: A memo or note for this bill payment check, as entered by the user.

          ref_number: The case-sensitive user-defined reference number for this bill payment check,
              which can be used to identify the transaction in QuickBooks. This value is not
              required to be unique and can be arbitrarily changed by the QuickBooks user.

              **IMPORTANT**: For checks, this field is the check number.

          transaction_date: The date of this bill payment check, in ISO 8601 format (YYYY-MM-DD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            f"/quickbooks-desktop/bill-payment-checks/{id}",
            body=maybe_transform(
                {
                    "revision_number": revision_number,
                    "amount": amount,
                    "apply_to_transactions": apply_to_transactions,
                    "bank_account_id": bank_account_id,
                    "exchange_rate": exchange_rate,
                    "is_queued_for_print": is_queued_for_print,
                    "memo": memo,
                    "ref_number": ref_number,
                    "transaction_date": transaction_date,
                },
                bill_payment_check_update_params.BillPaymentCheckUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillPaymentCheck,
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
        limit: int | NotGiven = NOT_GIVEN,
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
        vendor_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorPage[BillPaymentCheck]:
        """
        Returns a list of bill payment checks.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          account_ids: Filter for bill payment checks from this account or accounts.

          currency_ids: Filter for bill payment checks in this currency or currencies.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Retrieve this value from the `nextCursor` field in the
              previous response. If omitted, the API returns the first page of results.

          ids: Filter for specific bill payment checks by their QuickBooks-assigned unique
              identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters.

          include_line_items: Whether to include line items in the response. Defaults to `true`.

          limit: The maximum number of objects to return. Ranging from 1 to 150, defaults to 150.
              Use this parameter in conjunction with the `cursor` parameter to paginate
              through results. The response will include a `nextCursor` field, which can be
              used as the `cursor` parameter value in subsequent requests to fetch the next
              set of results.

          ref_number_contains: Filter for bill payment checks whose `refNumber` contains this substring. For
              checks, this is the check number. NOTE: If you use this parameter, you cannot
              also use `refNumberStartsWith` or `refNumberEndsWith`.

          ref_number_ends_with: Filter for bill payment checks whose `refNumber` ends with this substring. For
              checks, this is the check number. NOTE: If you use this parameter, you cannot
              also use `refNumberContains` or `refNumberStartsWith`.

          ref_number_from: Filter for bill payment checks whose `refNumber` is greater than or equal to
              this value. If omitted, the range will begin with the first number of the list.
              Uses a numerical comparison for values that contain only digits; otherwise, uses
              a lexicographical comparison.

          ref_numbers: Filter for specific bill payment checks by their ref-number(s), case-sensitive.
              In QuickBooks, ref-numbers are not required to be unique and can be arbitrarily
              changed by the QuickBooks user.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters.

          ref_number_starts_with: Filter for bill payment checks whose `refNumber` starts with this substring. For
              checks, this is the check number. NOTE: If you use this parameter, you cannot
              also use `refNumberContains` or `refNumberEndsWith`.

          ref_number_to: Filter for bill payment checks whose `refNumber` is less than or equal to this
              value. If omitted, the range will end with the last number of the list. Uses a
              numerical comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          transaction_date_from: Filter for bill payment checks created on or after this date, in ISO 8601 format
              (YYYY-MM-DD).

          transaction_date_to: Filter for bill payment checks created on or before this date, in ISO 8601
              format (YYYY-MM-DD).

          updated_after: Filter for bill payment checks updated on or after this date and time, in ISO
              8601 format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the
              time is assumed to be 00:00:00 of that day.

          updated_before: Filter for bill payment checks updated on or before this date and time, in ISO
              8601 format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the
              time is assumed to be 23:59:59 of that day.

          vendor_ids: Filter for bill payment checks to this vendor or vendors. These are the vendors
              who sent the bills paid by these checks.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get_api_list(
            "/quickbooks-desktop/bill-payment-checks",
            page=SyncCursorPage[BillPaymentCheck],
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
                        "limit": limit,
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
                        "vendor_ids": vendor_ids,
                    },
                    bill_payment_check_list_params.BillPaymentCheckListParams,
                ),
            ),
            model=BillPaymentCheck,
        )


class AsyncBillPaymentChecksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBillPaymentChecksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBillPaymentChecksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBillPaymentChecksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return AsyncBillPaymentChecksResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        apply_to_transactions: Iterable[bill_payment_check_create_params.ApplyToTransaction],
        bank_account_id: str,
        transaction_date: Union[str, date],
        vendor_id: str,
        conductor_end_user_id: str,
        exchange_rate: float | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        is_queued_for_print: bool | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        payables_account_id: str | NotGiven = NOT_GIVEN,
        ref_number: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BillPaymentCheck:
        """
        Creates a new bill payment check.

        Args:
          apply_to_transactions: The bills to be paid by this bill payment check. This will create a link between
              this bill payment check and the specified bills.

              **IMPORTANT**: In each `applyToTransactions` object, you must specify either
              `paymentAmount`, `applyCredits`, `discountAmount`, or any combination of these;
              if none of these are specified, you will receive an error for an empty
              transaction.

              **IMPORTANT**: The target bill must have `isPaid=false`, otherwise, QuickBooks
              will report this object as "cannot be found".

          bank_account_id: The bank account from which the funds are being drawn for this bill payment
              check; e.g., Checking or Savings. This bill payment check will decrease the
              balance of this account.

          transaction_date: The date of this bill payment check, in ISO 8601 format (YYYY-MM-DD).

          vendor_id: The vendor who sent the bill(s) that this check is paying and who will receive
              this payment.

              **IMPORTANT**: This vendor must match the `vendor` on the bill(s) specified in
              `applyToTransactions`; otherwise, QuickBooks will say the `transactionId` in
              `applyToTransactions` "does not exist".

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          exchange_rate: The market exchange rate between this bill payment check's currency and the home
              currency in QuickBooks at the time of this transaction. Represented as a decimal
              value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).

          external_id: A globally unique identifier (GUID) you can provide for tracking this object in
              your external system.

              **IMPORTANT**: Must be formatted as a valid GUID; otherwise, QuickBooks will
              return an error. This field is immutable and can only be set during object
              creation.

          is_queued_for_print: Indicates whether this bill payment check is included in the queue of documents
              for QuickBooks to print.

          memo: A memo or note for this bill payment check, as entered by the user.

          payables_account_id: The Accounts-Payable (A/P) account to which this bill payment check is assigned,
              used to track the amount owed. If not specified, QuickBooks Desktop will use its
              default Accounts-Payable account.

              **IMPORTANT**: If this bill payment check is linked to other transactions, this
              A/P account must match the `payablesAccount` used in the other transactions.

          ref_number: The case-sensitive user-defined reference number for this bill payment check,
              which can be used to identify the transaction in QuickBooks. This value is not
              required to be unique and can be arbitrarily changed by the QuickBooks user.

              **IMPORTANT**: For checks, this field is the check number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            "/quickbooks-desktop/bill-payment-checks",
            body=await async_maybe_transform(
                {
                    "apply_to_transactions": apply_to_transactions,
                    "bank_account_id": bank_account_id,
                    "transaction_date": transaction_date,
                    "vendor_id": vendor_id,
                    "exchange_rate": exchange_rate,
                    "external_id": external_id,
                    "is_queued_for_print": is_queued_for_print,
                    "memo": memo,
                    "payables_account_id": payables_account_id,
                    "ref_number": ref_number,
                },
                bill_payment_check_create_params.BillPaymentCheckCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillPaymentCheck,
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
    ) -> BillPaymentCheck:
        """
        Retrieves a bill payment check by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the bill payment check to retrieve.

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
            f"/quickbooks-desktop/bill-payment-checks/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillPaymentCheck,
        )

    async def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        amount: str | NotGiven = NOT_GIVEN,
        apply_to_transactions: Iterable[bill_payment_check_update_params.ApplyToTransaction] | NotGiven = NOT_GIVEN,
        bank_account_id: str | NotGiven = NOT_GIVEN,
        exchange_rate: float | NotGiven = NOT_GIVEN,
        is_queued_for_print: bool | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        ref_number: str | NotGiven = NOT_GIVEN,
        transaction_date: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BillPaymentCheck:
        """
        Updates an existing bill payment check.

        Args:
          id: The QuickBooks-assigned unique identifier of the bill payment check to update.

          revision_number: The current revision number of the bill payment check object you are updating,
              which you can get by fetching the object first. Provide the most recent
              `revisionNumber` to ensure you're working with the latest data; otherwise, the
              update will return an error.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          amount: The monetary amount of this bill payment check, represented as a decimal string.

          apply_to_transactions: The bills to be paid by this bill payment check. This will create a link between
              this bill payment check and the specified bills.

              **IMPORTANT**: In each `applyToTransactions` object, you must specify either
              `paymentAmount`, `applyCredits`, `discountAmount`, or any combination of these;
              if none of these are specified, you will receive an error for an empty
              transaction.

              **IMPORTANT**: The target bill must have `isPaid=false`, otherwise, QuickBooks
              will report this object as "cannot be found".

          bank_account_id: The bank account from which the funds are being drawn for this bill payment
              check; e.g., Checking or Savings. This bill payment check will decrease the
              balance of this account.

          exchange_rate: The market exchange rate between this bill payment check's currency and the home
              currency in QuickBooks at the time of this transaction. Represented as a decimal
              value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).

          is_queued_for_print: Indicates whether this bill payment check is included in the queue of documents
              for QuickBooks to print.

          memo: A memo or note for this bill payment check, as entered by the user.

          ref_number: The case-sensitive user-defined reference number for this bill payment check,
              which can be used to identify the transaction in QuickBooks. This value is not
              required to be unique and can be arbitrarily changed by the QuickBooks user.

              **IMPORTANT**: For checks, this field is the check number.

          transaction_date: The date of this bill payment check, in ISO 8601 format (YYYY-MM-DD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            f"/quickbooks-desktop/bill-payment-checks/{id}",
            body=await async_maybe_transform(
                {
                    "revision_number": revision_number,
                    "amount": amount,
                    "apply_to_transactions": apply_to_transactions,
                    "bank_account_id": bank_account_id,
                    "exchange_rate": exchange_rate,
                    "is_queued_for_print": is_queued_for_print,
                    "memo": memo,
                    "ref_number": ref_number,
                    "transaction_date": transaction_date,
                },
                bill_payment_check_update_params.BillPaymentCheckUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillPaymentCheck,
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
        limit: int | NotGiven = NOT_GIVEN,
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
        vendor_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[BillPaymentCheck, AsyncCursorPage[BillPaymentCheck]]:
        """
        Returns a list of bill payment checks.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          account_ids: Filter for bill payment checks from this account or accounts.

          currency_ids: Filter for bill payment checks in this currency or currencies.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Retrieve this value from the `nextCursor` field in the
              previous response. If omitted, the API returns the first page of results.

          ids: Filter for specific bill payment checks by their QuickBooks-assigned unique
              identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters.

          include_line_items: Whether to include line items in the response. Defaults to `true`.

          limit: The maximum number of objects to return. Ranging from 1 to 150, defaults to 150.
              Use this parameter in conjunction with the `cursor` parameter to paginate
              through results. The response will include a `nextCursor` field, which can be
              used as the `cursor` parameter value in subsequent requests to fetch the next
              set of results.

          ref_number_contains: Filter for bill payment checks whose `refNumber` contains this substring. For
              checks, this is the check number. NOTE: If you use this parameter, you cannot
              also use `refNumberStartsWith` or `refNumberEndsWith`.

          ref_number_ends_with: Filter for bill payment checks whose `refNumber` ends with this substring. For
              checks, this is the check number. NOTE: If you use this parameter, you cannot
              also use `refNumberContains` or `refNumberStartsWith`.

          ref_number_from: Filter for bill payment checks whose `refNumber` is greater than or equal to
              this value. If omitted, the range will begin with the first number of the list.
              Uses a numerical comparison for values that contain only digits; otherwise, uses
              a lexicographical comparison.

          ref_numbers: Filter for specific bill payment checks by their ref-number(s), case-sensitive.
              In QuickBooks, ref-numbers are not required to be unique and can be arbitrarily
              changed by the QuickBooks user.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters.

          ref_number_starts_with: Filter for bill payment checks whose `refNumber` starts with this substring. For
              checks, this is the check number. NOTE: If you use this parameter, you cannot
              also use `refNumberContains` or `refNumberEndsWith`.

          ref_number_to: Filter for bill payment checks whose `refNumber` is less than or equal to this
              value. If omitted, the range will end with the last number of the list. Uses a
              numerical comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          transaction_date_from: Filter for bill payment checks created on or after this date, in ISO 8601 format
              (YYYY-MM-DD).

          transaction_date_to: Filter for bill payment checks created on or before this date, in ISO 8601
              format (YYYY-MM-DD).

          updated_after: Filter for bill payment checks updated on or after this date and time, in ISO
              8601 format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the
              time is assumed to be 00:00:00 of that day.

          updated_before: Filter for bill payment checks updated on or before this date and time, in ISO
              8601 format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the
              time is assumed to be 23:59:59 of that day.

          vendor_ids: Filter for bill payment checks to this vendor or vendors. These are the vendors
              who sent the bills paid by these checks.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get_api_list(
            "/quickbooks-desktop/bill-payment-checks",
            page=AsyncCursorPage[BillPaymentCheck],
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
                        "limit": limit,
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
                        "vendor_ids": vendor_ids,
                    },
                    bill_payment_check_list_params.BillPaymentCheckListParams,
                ),
            ),
            model=BillPaymentCheck,
        )


class BillPaymentChecksResourceWithRawResponse:
    def __init__(self, bill_payment_checks: BillPaymentChecksResource) -> None:
        self._bill_payment_checks = bill_payment_checks

        self.create = to_raw_response_wrapper(
            bill_payment_checks.create,
        )
        self.retrieve = to_raw_response_wrapper(
            bill_payment_checks.retrieve,
        )
        self.update = to_raw_response_wrapper(
            bill_payment_checks.update,
        )
        self.list = to_raw_response_wrapper(
            bill_payment_checks.list,
        )


class AsyncBillPaymentChecksResourceWithRawResponse:
    def __init__(self, bill_payment_checks: AsyncBillPaymentChecksResource) -> None:
        self._bill_payment_checks = bill_payment_checks

        self.create = async_to_raw_response_wrapper(
            bill_payment_checks.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            bill_payment_checks.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            bill_payment_checks.update,
        )
        self.list = async_to_raw_response_wrapper(
            bill_payment_checks.list,
        )


class BillPaymentChecksResourceWithStreamingResponse:
    def __init__(self, bill_payment_checks: BillPaymentChecksResource) -> None:
        self._bill_payment_checks = bill_payment_checks

        self.create = to_streamed_response_wrapper(
            bill_payment_checks.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            bill_payment_checks.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            bill_payment_checks.update,
        )
        self.list = to_streamed_response_wrapper(
            bill_payment_checks.list,
        )


class AsyncBillPaymentChecksResourceWithStreamingResponse:
    def __init__(self, bill_payment_checks: AsyncBillPaymentChecksResource) -> None:
        self._bill_payment_checks = bill_payment_checks

        self.create = async_to_streamed_response_wrapper(
            bill_payment_checks.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            bill_payment_checks.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            bill_payment_checks.update,
        )
        self.list = async_to_streamed_response_wrapper(
            bill_payment_checks.list,
        )
