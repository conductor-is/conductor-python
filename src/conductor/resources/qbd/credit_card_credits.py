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
    credit_card_credit_list_params,
    credit_card_credit_create_params,
    credit_card_credit_update_params,
)
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.qbd.credit_card_credit import CreditCardCredit

__all__ = ["CreditCardCreditsResource", "AsyncCreditCardCreditsResource"]


class CreditCardCreditsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CreditCardCreditsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return CreditCardCreditsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CreditCardCreditsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return CreditCardCreditsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        transaction_date: Union[str, date],
        conductor_end_user_id: str,
        exchange_rate: float | NotGiven = NOT_GIVEN,
        expense_lines: Iterable[credit_card_credit_create_params.ExpenseLine] | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        item_group_lines: Iterable[credit_card_credit_create_params.ItemGroupLine] | NotGiven = NOT_GIVEN,
        item_lines: Iterable[credit_card_credit_create_params.ItemLine] | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        payee_id: str | NotGiven = NOT_GIVEN,
        ref_number: str | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreditCardCredit:
        """
        Creates a credit card credit for the specified account.

        Args:
          account_id: The bank or credit card account to which the credit is applied.

          transaction_date: The date of this credit card credit, in ISO 8601 format (YYYY-MM-DD).

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          exchange_rate: The market exchange rate between this credit card credit's currency and the home
              currency in QuickBooks at the time of this transaction. Represented as a decimal
              value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).

          expense_lines: The credit card credit's expense lines, each representing one line in this
              expense.

          external_id: A globally unique identifier (GUID) you can provide for tracking this object in
              your external system. Must be formatted as a valid GUID; otherwise, QuickBooks
              will return an error. This field is immutable and can only be set during object
              creation.

          item_group_lines: The credit card credit's item group lines, each representing a predefined set of
              items bundled together because they are commonly purchased together or grouped
              for faster entry.

          item_lines: The credit card credit's item lines, each representing the purchase of a
              specific item or service.

          memo: A memo or note for this credit card credit, as entered by the user.

          payee_id: The vendor or company from whom this credit card credit was received for
              purchased merchandise or services.

          ref_number: The case-sensitive user-defined reference number for this credit card credit,
              which can be used to identify the transaction in QuickBooks. This value is not
              required to be unique and can be arbitrarily changed by the QuickBooks user.

          sales_tax_code_id: The sales-tax code associated with this credit card credit, determining whether
              it is taxable or non-taxable. It's used to assign a default tax status to all
              transactions for this credit card credit. Default codes include "Non"
              (non-taxable) and "Tax" (taxable), but custom codes can also be created in
              QuickBooks. If QuickBooks is not set up to charge sales tax (via the "Do You
              Charge Sales Tax?" preference), it will assign the default non-taxable code to
              all sales.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            "/quickbooks-desktop/credit-card-credits",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "transaction_date": transaction_date,
                    "exchange_rate": exchange_rate,
                    "expense_lines": expense_lines,
                    "external_id": external_id,
                    "item_group_lines": item_group_lines,
                    "item_lines": item_lines,
                    "memo": memo,
                    "payee_id": payee_id,
                    "ref_number": ref_number,
                    "sales_tax_code_id": sales_tax_code_id,
                },
                credit_card_credit_create_params.CreditCardCreditCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditCardCredit,
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
    ) -> CreditCardCredit:
        """
        Retrieves a credit card credit by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the credit card credit to retrieve.

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
            f"/quickbooks-desktop/credit-card-credits/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditCardCredit,
        )

    def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        account_id: str | NotGiven = NOT_GIVEN,
        clear_expense_lines: bool | NotGiven = NOT_GIVEN,
        clear_item_lines: bool | NotGiven = NOT_GIVEN,
        exchange_rate: float | NotGiven = NOT_GIVEN,
        expense_lines: Iterable[credit_card_credit_update_params.ExpenseLine] | NotGiven = NOT_GIVEN,
        item_group_lines: Iterable[credit_card_credit_update_params.ItemGroupLine] | NotGiven = NOT_GIVEN,
        item_lines: Iterable[credit_card_credit_update_params.ItemLine] | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        payee_id: str | NotGiven = NOT_GIVEN,
        ref_number: str | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        transaction_date: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreditCardCredit:
        """
        Updates an existing credit card credit.

        Args:
          id: The QuickBooks-assigned unique identifier of the credit card credit to update.

          revision_number: The current revision number of the credit card credit you are updating, which
              you can get by fetching the object first. Provide the most recent
              `revisionNumber` to ensure you're working with the latest data; otherwise, the
              update will return an error.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          account_id: The bank or credit card account to which the credit is applied.

          clear_expense_lines: When `true`, removes all existing expense lines associated with this credit card
              credit. To modify or add individual expense lines, use the field `expenseLines`
              instead.

          clear_item_lines: When `true`, removes all existing item lines associated with this credit card
              credit. To modify or add individual item lines, use the field `itemLines`
              instead.

          exchange_rate: The market exchange rate between this credit card credit's currency and the home
              currency in QuickBooks at the time of this transaction. Represented as a decimal
              value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).

          expense_lines: The credit card credit's expense lines, each representing one line in this
              expense.

              IMPORTANT: When updating a credit card credit's expense lines, this array
              completely REPLACES all existing expense lines for that credit card credit. To
              retain any current expense lines, include them in this array, even if they have
              not changed. Any expense lines not included will be removed. To add a new
              expense line, include it with its `id` set to `-1`. If you do not wish to modify
              the expense lines, you can omit this field entirely to keep them unchanged.

          item_group_lines: The credit card credit's item group lines, each representing a predefined set of
              items bundled together because they are commonly purchased together or grouped
              for faster entry.

              IMPORTANT: When updating a credit card credit's item group lines, this array
              completely REPLACES all existing item group lines for that credit card credit.
              To retain any current item group lines, include them in this array, even if they
              have not changed. Any item group lines not included will be removed. To add a
              new item group line, include it with its `id` set to `-1`. If you do not wish to
              modify the item group lines, you can omit this field entirely to keep them
              unchanged.

          item_lines: The credit card credit's item lines, each representing the purchase of a
              specific item or service.

              IMPORTANT: When updating a credit card credit's item lines, this array
              completely REPLACES all existing item lines for that credit card credit. To
              retain any current item lines, include them in this array, even if they have not
              changed. Any item lines not included will be removed. To add a new item line,
              include it with its `id` set to `-1`. If you do not wish to modify the item
              lines, you can omit this field entirely to keep them unchanged.

          memo: A memo or note for this credit card credit, as entered by the user.

          payee_id: The vendor or company from whom this credit card credit was received for
              purchased merchandise or services.

          ref_number: The case-sensitive user-defined reference number for this credit card credit,
              which can be used to identify the transaction in QuickBooks. This value is not
              required to be unique and can be arbitrarily changed by the QuickBooks user.

          sales_tax_code_id: The sales-tax code associated with this credit card credit, determining whether
              it is taxable or non-taxable. It's used to assign a default tax status to all
              transactions for this credit card credit. Default codes include "Non"
              (non-taxable) and "Tax" (taxable), but custom codes can also be created in
              QuickBooks. If QuickBooks is not set up to charge sales tax (via the "Do You
              Charge Sales Tax?" preference), it will assign the default non-taxable code to
              all sales.

          transaction_date: The date of this credit card credit, in ISO 8601 format (YYYY-MM-DD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            f"/quickbooks-desktop/credit-card-credits/{id}",
            body=maybe_transform(
                {
                    "revision_number": revision_number,
                    "account_id": account_id,
                    "clear_expense_lines": clear_expense_lines,
                    "clear_item_lines": clear_item_lines,
                    "exchange_rate": exchange_rate,
                    "expense_lines": expense_lines,
                    "item_group_lines": item_group_lines,
                    "item_lines": item_lines,
                    "memo": memo,
                    "payee_id": payee_id,
                    "ref_number": ref_number,
                    "sales_tax_code_id": sales_tax_code_id,
                    "transaction_date": transaction_date,
                },
                credit_card_credit_update_params.CreditCardCreditUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditCardCredit,
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
    ) -> SyncCursorPage[CreditCardCredit]:
        """
        Returns a list of credit card credits.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          account_ids: Filter for credit card credits from this account or accounts. Specify a single
              account ID or multiple using a comma-separated list (e.g., `accountIds=1,2,3`).

          currency_ids: Filter for credit card credits in this currency or currencies. Specify a single
              currency ID or multiple using a comma-separated list (e.g.,
              `currencyIds=1,2,3`).

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Retrieve this value from the `nextCursor` field in the
              previous response. If omitted, the API returns the first page of results.

          ids: Filter for specific credit card credits by their QuickBooks-assigned unique
              identifier(s).

              NOTE: If you include this parameter, QuickBooks will ignore all other query
              parameters.

          include_line_items: Whether to include line items in the response.

          limit: The maximum number of objects to return. Ranging from 1 to 150, defaults to 150.
              Use this parameter in conjunction with the `cursor` parameter to paginate
              through results. The response will include a `nextCursor` field, which can be
              used as the `cursor` parameter value in subsequent requests to fetch the next
              set of results.

          payee_ids: Filter for credit card credits from this payee or payees. Specify a single payee
              ID or multiple using a comma-separated list (e.g., `payeeIds=1,2,3`). These are
              the vendors or companies from whom the credits were received.

          ref_number_contains:
              Filter for credit card credits whose `refNumber` contains this substring. NOTE:
              If you use this parameter, you cannot also use `refNumberStartsWith` or
              `refNumberEndsWith`.

          ref_number_ends_with:
              Filter for credit card credits whose `refNumber` ends with this substring. NOTE:
              If you use this parameter, you cannot also use `refNumberContains` or
              `refNumberStartsWith`.

          ref_number_from: Filter for credit card credits whose `refNumber` is greater than or equal to
              this value. If omitted, the range will begin with the first number of the list.
              Uses a numerical comparison for values that contain only digits; otherwise, uses
              a lexicographical comparison.

          ref_numbers: Filter for specific credit card credits by their ref-number(s), case-sensitive.
              In QuickBooks, ref-numbers are not required to be unique and can be arbitrarily
              changed by the QuickBooks user.

              NOTE: If you include this parameter, QuickBooks will ignore all other query
              parameters.

          ref_number_starts_with: Filter for credit card credits whose `refNumber` starts with this substring.
              NOTE: If you use this parameter, you cannot also use `refNumberContains` or
              `refNumberEndsWith`.

          ref_number_to: Filter for credit card credits whose `refNumber` is less than or equal to this
              value. If omitted, the range will end with the last number of the list. Uses a
              numerical comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          transaction_date_from: Filter for credit card credits created on or after this date, in ISO 8601 format
              (YYYY-MM-DD).

          transaction_date_to: Filter for credit card credits created on or before this date, in ISO 8601
              format (YYYY-MM-DD).

          updated_after: Filter for credit card credits updated on or after this date and time, in ISO
              8601 format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the
              time is assumed to be 00:00:00 of that day.

          updated_before: Filter for credit card credits updated on or before this date and time, in ISO
              8601 format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the
              time is assumed to be 23:59:59 of that day.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get_api_list(
            "/quickbooks-desktop/credit-card-credits",
            page=SyncCursorPage[CreditCardCredit],
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
                    credit_card_credit_list_params.CreditCardCreditListParams,
                ),
            ),
            model=CreditCardCredit,
        )


class AsyncCreditCardCreditsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCreditCardCreditsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCreditCardCreditsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCreditCardCreditsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return AsyncCreditCardCreditsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        transaction_date: Union[str, date],
        conductor_end_user_id: str,
        exchange_rate: float | NotGiven = NOT_GIVEN,
        expense_lines: Iterable[credit_card_credit_create_params.ExpenseLine] | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        item_group_lines: Iterable[credit_card_credit_create_params.ItemGroupLine] | NotGiven = NOT_GIVEN,
        item_lines: Iterable[credit_card_credit_create_params.ItemLine] | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        payee_id: str | NotGiven = NOT_GIVEN,
        ref_number: str | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreditCardCredit:
        """
        Creates a credit card credit for the specified account.

        Args:
          account_id: The bank or credit card account to which the credit is applied.

          transaction_date: The date of this credit card credit, in ISO 8601 format (YYYY-MM-DD).

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          exchange_rate: The market exchange rate between this credit card credit's currency and the home
              currency in QuickBooks at the time of this transaction. Represented as a decimal
              value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).

          expense_lines: The credit card credit's expense lines, each representing one line in this
              expense.

          external_id: A globally unique identifier (GUID) you can provide for tracking this object in
              your external system. Must be formatted as a valid GUID; otherwise, QuickBooks
              will return an error. This field is immutable and can only be set during object
              creation.

          item_group_lines: The credit card credit's item group lines, each representing a predefined set of
              items bundled together because they are commonly purchased together or grouped
              for faster entry.

          item_lines: The credit card credit's item lines, each representing the purchase of a
              specific item or service.

          memo: A memo or note for this credit card credit, as entered by the user.

          payee_id: The vendor or company from whom this credit card credit was received for
              purchased merchandise or services.

          ref_number: The case-sensitive user-defined reference number for this credit card credit,
              which can be used to identify the transaction in QuickBooks. This value is not
              required to be unique and can be arbitrarily changed by the QuickBooks user.

          sales_tax_code_id: The sales-tax code associated with this credit card credit, determining whether
              it is taxable or non-taxable. It's used to assign a default tax status to all
              transactions for this credit card credit. Default codes include "Non"
              (non-taxable) and "Tax" (taxable), but custom codes can also be created in
              QuickBooks. If QuickBooks is not set up to charge sales tax (via the "Do You
              Charge Sales Tax?" preference), it will assign the default non-taxable code to
              all sales.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            "/quickbooks-desktop/credit-card-credits",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "transaction_date": transaction_date,
                    "exchange_rate": exchange_rate,
                    "expense_lines": expense_lines,
                    "external_id": external_id,
                    "item_group_lines": item_group_lines,
                    "item_lines": item_lines,
                    "memo": memo,
                    "payee_id": payee_id,
                    "ref_number": ref_number,
                    "sales_tax_code_id": sales_tax_code_id,
                },
                credit_card_credit_create_params.CreditCardCreditCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditCardCredit,
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
    ) -> CreditCardCredit:
        """
        Retrieves a credit card credit by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the credit card credit to retrieve.

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
            f"/quickbooks-desktop/credit-card-credits/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditCardCredit,
        )

    async def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        account_id: str | NotGiven = NOT_GIVEN,
        clear_expense_lines: bool | NotGiven = NOT_GIVEN,
        clear_item_lines: bool | NotGiven = NOT_GIVEN,
        exchange_rate: float | NotGiven = NOT_GIVEN,
        expense_lines: Iterable[credit_card_credit_update_params.ExpenseLine] | NotGiven = NOT_GIVEN,
        item_group_lines: Iterable[credit_card_credit_update_params.ItemGroupLine] | NotGiven = NOT_GIVEN,
        item_lines: Iterable[credit_card_credit_update_params.ItemLine] | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        payee_id: str | NotGiven = NOT_GIVEN,
        ref_number: str | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        transaction_date: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreditCardCredit:
        """
        Updates an existing credit card credit.

        Args:
          id: The QuickBooks-assigned unique identifier of the credit card credit to update.

          revision_number: The current revision number of the credit card credit you are updating, which
              you can get by fetching the object first. Provide the most recent
              `revisionNumber` to ensure you're working with the latest data; otherwise, the
              update will return an error.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          account_id: The bank or credit card account to which the credit is applied.

          clear_expense_lines: When `true`, removes all existing expense lines associated with this credit card
              credit. To modify or add individual expense lines, use the field `expenseLines`
              instead.

          clear_item_lines: When `true`, removes all existing item lines associated with this credit card
              credit. To modify or add individual item lines, use the field `itemLines`
              instead.

          exchange_rate: The market exchange rate between this credit card credit's currency and the home
              currency in QuickBooks at the time of this transaction. Represented as a decimal
              value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).

          expense_lines: The credit card credit's expense lines, each representing one line in this
              expense.

              IMPORTANT: When updating a credit card credit's expense lines, this array
              completely REPLACES all existing expense lines for that credit card credit. To
              retain any current expense lines, include them in this array, even if they have
              not changed. Any expense lines not included will be removed. To add a new
              expense line, include it with its `id` set to `-1`. If you do not wish to modify
              the expense lines, you can omit this field entirely to keep them unchanged.

          item_group_lines: The credit card credit's item group lines, each representing a predefined set of
              items bundled together because they are commonly purchased together or grouped
              for faster entry.

              IMPORTANT: When updating a credit card credit's item group lines, this array
              completely REPLACES all existing item group lines for that credit card credit.
              To retain any current item group lines, include them in this array, even if they
              have not changed. Any item group lines not included will be removed. To add a
              new item group line, include it with its `id` set to `-1`. If you do not wish to
              modify the item group lines, you can omit this field entirely to keep them
              unchanged.

          item_lines: The credit card credit's item lines, each representing the purchase of a
              specific item or service.

              IMPORTANT: When updating a credit card credit's item lines, this array
              completely REPLACES all existing item lines for that credit card credit. To
              retain any current item lines, include them in this array, even if they have not
              changed. Any item lines not included will be removed. To add a new item line,
              include it with its `id` set to `-1`. If you do not wish to modify the item
              lines, you can omit this field entirely to keep them unchanged.

          memo: A memo or note for this credit card credit, as entered by the user.

          payee_id: The vendor or company from whom this credit card credit was received for
              purchased merchandise or services.

          ref_number: The case-sensitive user-defined reference number for this credit card credit,
              which can be used to identify the transaction in QuickBooks. This value is not
              required to be unique and can be arbitrarily changed by the QuickBooks user.

          sales_tax_code_id: The sales-tax code associated with this credit card credit, determining whether
              it is taxable or non-taxable. It's used to assign a default tax status to all
              transactions for this credit card credit. Default codes include "Non"
              (non-taxable) and "Tax" (taxable), but custom codes can also be created in
              QuickBooks. If QuickBooks is not set up to charge sales tax (via the "Do You
              Charge Sales Tax?" preference), it will assign the default non-taxable code to
              all sales.

          transaction_date: The date of this credit card credit, in ISO 8601 format (YYYY-MM-DD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            f"/quickbooks-desktop/credit-card-credits/{id}",
            body=await async_maybe_transform(
                {
                    "revision_number": revision_number,
                    "account_id": account_id,
                    "clear_expense_lines": clear_expense_lines,
                    "clear_item_lines": clear_item_lines,
                    "exchange_rate": exchange_rate,
                    "expense_lines": expense_lines,
                    "item_group_lines": item_group_lines,
                    "item_lines": item_lines,
                    "memo": memo,
                    "payee_id": payee_id,
                    "ref_number": ref_number,
                    "sales_tax_code_id": sales_tax_code_id,
                    "transaction_date": transaction_date,
                },
                credit_card_credit_update_params.CreditCardCreditUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditCardCredit,
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
    ) -> AsyncPaginator[CreditCardCredit, AsyncCursorPage[CreditCardCredit]]:
        """
        Returns a list of credit card credits.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          account_ids: Filter for credit card credits from this account or accounts. Specify a single
              account ID or multiple using a comma-separated list (e.g., `accountIds=1,2,3`).

          currency_ids: Filter for credit card credits in this currency or currencies. Specify a single
              currency ID or multiple using a comma-separated list (e.g.,
              `currencyIds=1,2,3`).

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Retrieve this value from the `nextCursor` field in the
              previous response. If omitted, the API returns the first page of results.

          ids: Filter for specific credit card credits by their QuickBooks-assigned unique
              identifier(s).

              NOTE: If you include this parameter, QuickBooks will ignore all other query
              parameters.

          include_line_items: Whether to include line items in the response.

          limit: The maximum number of objects to return. Ranging from 1 to 150, defaults to 150.
              Use this parameter in conjunction with the `cursor` parameter to paginate
              through results. The response will include a `nextCursor` field, which can be
              used as the `cursor` parameter value in subsequent requests to fetch the next
              set of results.

          payee_ids: Filter for credit card credits from this payee or payees. Specify a single payee
              ID or multiple using a comma-separated list (e.g., `payeeIds=1,2,3`). These are
              the vendors or companies from whom the credits were received.

          ref_number_contains:
              Filter for credit card credits whose `refNumber` contains this substring. NOTE:
              If you use this parameter, you cannot also use `refNumberStartsWith` or
              `refNumberEndsWith`.

          ref_number_ends_with:
              Filter for credit card credits whose `refNumber` ends with this substring. NOTE:
              If you use this parameter, you cannot also use `refNumberContains` or
              `refNumberStartsWith`.

          ref_number_from: Filter for credit card credits whose `refNumber` is greater than or equal to
              this value. If omitted, the range will begin with the first number of the list.
              Uses a numerical comparison for values that contain only digits; otherwise, uses
              a lexicographical comparison.

          ref_numbers: Filter for specific credit card credits by their ref-number(s), case-sensitive.
              In QuickBooks, ref-numbers are not required to be unique and can be arbitrarily
              changed by the QuickBooks user.

              NOTE: If you include this parameter, QuickBooks will ignore all other query
              parameters.

          ref_number_starts_with: Filter for credit card credits whose `refNumber` starts with this substring.
              NOTE: If you use this parameter, you cannot also use `refNumberContains` or
              `refNumberEndsWith`.

          ref_number_to: Filter for credit card credits whose `refNumber` is less than or equal to this
              value. If omitted, the range will end with the last number of the list. Uses a
              numerical comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          transaction_date_from: Filter for credit card credits created on or after this date, in ISO 8601 format
              (YYYY-MM-DD).

          transaction_date_to: Filter for credit card credits created on or before this date, in ISO 8601
              format (YYYY-MM-DD).

          updated_after: Filter for credit card credits updated on or after this date and time, in ISO
              8601 format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the
              time is assumed to be 00:00:00 of that day.

          updated_before: Filter for credit card credits updated on or before this date and time, in ISO
              8601 format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the
              time is assumed to be 23:59:59 of that day.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get_api_list(
            "/quickbooks-desktop/credit-card-credits",
            page=AsyncCursorPage[CreditCardCredit],
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
                    credit_card_credit_list_params.CreditCardCreditListParams,
                ),
            ),
            model=CreditCardCredit,
        )


class CreditCardCreditsResourceWithRawResponse:
    def __init__(self, credit_card_credits: CreditCardCreditsResource) -> None:
        self._credit_card_credits = credit_card_credits

        self.create = to_raw_response_wrapper(
            credit_card_credits.create,
        )
        self.retrieve = to_raw_response_wrapper(
            credit_card_credits.retrieve,
        )
        self.update = to_raw_response_wrapper(
            credit_card_credits.update,
        )
        self.list = to_raw_response_wrapper(
            credit_card_credits.list,
        )


class AsyncCreditCardCreditsResourceWithRawResponse:
    def __init__(self, credit_card_credits: AsyncCreditCardCreditsResource) -> None:
        self._credit_card_credits = credit_card_credits

        self.create = async_to_raw_response_wrapper(
            credit_card_credits.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            credit_card_credits.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            credit_card_credits.update,
        )
        self.list = async_to_raw_response_wrapper(
            credit_card_credits.list,
        )


class CreditCardCreditsResourceWithStreamingResponse:
    def __init__(self, credit_card_credits: CreditCardCreditsResource) -> None:
        self._credit_card_credits = credit_card_credits

        self.create = to_streamed_response_wrapper(
            credit_card_credits.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            credit_card_credits.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            credit_card_credits.update,
        )
        self.list = to_streamed_response_wrapper(
            credit_card_credits.list,
        )


class AsyncCreditCardCreditsResourceWithStreamingResponse:
    def __init__(self, credit_card_credits: AsyncCreditCardCreditsResource) -> None:
        self._credit_card_credits = credit_card_credits

        self.create = async_to_streamed_response_wrapper(
            credit_card_credits.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            credit_card_credits.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            credit_card_credits.update,
        )
        self.list = async_to_streamed_response_wrapper(
            credit_card_credits.list,
        )
