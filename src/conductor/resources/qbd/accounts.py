# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal

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
from ...types.qbd import account_list_params, account_create_params
from ..._base_client import make_request_options
from ...types.qbd.qbd_account import QbdAccount
from ...types.qbd.account_list_response import AccountListResponse

__all__ = ["AccountsResource", "AsyncAccountsResource"]


class AccountsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccountsResourceWithRawResponse:
        return AccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountsResourceWithStreamingResponse:
        return AccountsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_type: Literal[
            "accounts_payable",
            "accounts_receivable",
            "bank",
            "cost_of_goods_sold",
            "credit_card",
            "equity",
            "expense",
            "fixed_asset",
            "income",
            "long_term_liability",
            "non_posting",
            "other_asset",
            "other_current_asset",
            "other_current_liability",
            "other_expense",
            "other_income",
        ],
        name: str,
        conductor_end_user_id: str,
        account_number: str | NotGiven = NOT_GIVEN,
        bank_number: str | NotGiven = NOT_GIVEN,
        currency_id: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        opening_balance: str | NotGiven = NOT_GIVEN,
        opening_balance_date: str | NotGiven = NOT_GIVEN,
        parent_id: str | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        tax_line_id: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QbdAccount:
        """
        Creates a financial account.

        Args:
          account_type: The type of QuickBooks account.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          is_active: Whether this account is active. QuickBooks hides inactive objects from most
              views and reports in the UI.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            "/quickbooks-desktop/accounts",
            body=maybe_transform(
                {
                    "account_type": account_type,
                    "name": name,
                    "account_number": account_number,
                    "bank_number": bank_number,
                    "currency_id": currency_id,
                    "description": description,
                    "is_active": is_active,
                    "opening_balance": opening_balance,
                    "opening_balance_date": opening_balance_date,
                    "parent_id": parent_id,
                    "sales_tax_code_id": sales_tax_code_id,
                    "tax_line_id": tax_line_id,
                },
                account_create_params.AccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QbdAccount,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        id: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        account_type: Literal[
            "accounts_payable",
            "accounts_receivable",
            "bank",
            "cost_of_goods_sold",
            "credit_card",
            "equity",
            "expense",
            "fixed_asset",
            "income",
            "long_term_liability",
            "non_posting",
            "other_asset",
            "other_current_asset",
            "other_current_liability",
            "other_expense",
            "other_income",
        ]
        | NotGiven = NOT_GIVEN,
        currency_id: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        full_name: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name_contains: str | NotGiven = NOT_GIVEN,
        name_ends_with: str | NotGiven = NOT_GIVEN,
        name_from: str | NotGiven = NOT_GIVEN,
        name_starts_with: str | NotGiven = NOT_GIVEN,
        name_to: str | NotGiven = NOT_GIVEN,
        status: Literal["active", "all", "inactive"] | NotGiven = NOT_GIVEN,
        updated_after: str | NotGiven = NOT_GIVEN,
        updated_before: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountListResponse:
        """
        Returns a list of accounts.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          id: Filter for accounts with the specified QuickBooks-assigned unique identifier(s).
              If your request includes this parameter, all other query parameters will be
              ignored.

          account_type: Filter for accounts of this type.

          currency_id: Filter for accounts in this currency or currencies.

          full_name: Filter for accounts with this full-name or full-names. Like `id`, a full-name is
              a unique identifier for an account, and is created by prefixing the account's
              name with the names of each ancestor. If your request includes this parameter,
              all other query parameters will be ignored.

          limit: The maximum number of objects to return, ranging from 1 to 500. Defaults to 500.
              NOTE: QuickBooks Desktop does not support cursor-based pagination for this
              endpoint. Hence, this parameter will limit the response size, but you will not
              be able to fetch the next set of results. If you must paginate through the
              results, try iterating via the date-range query parameters.

          name_contains: Filter for objects whose `name` contains this substring. If you use this
              parameter, you cannot use `nameStartsWith` or `nameEndsWith`.

          name_ends_with: Filter for objects whose `name` ends with this substring. If you use this
              parameter, you cannot use `nameContains` or `nameStartsWith`.

          name_from: Filter for objects whose `name` is alphabetically greater than or equal to this
              value.

          name_starts_with: Filter for objects whose `name` starts with this substring. If you use this
              parameter, you cannot use `nameContains` or `nameEndsWith`.

          name_to: Filter for objects whose `name` is alphabetically less than or equal to this
              value.

          status: Filter for objects that are active, inactive, or both.

          updated_after: Filter for objects updated on or after this date and time, in ISO 8601 format
              (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
              assumed to be 00:00:00 of that day.

          updated_before: Filter for objects updated on or before this date and time, in ISO 8601 format
              (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
              assumed to be 23:59:59 of that day.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get(
            "/quickbooks-desktop/accounts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "account_type": account_type,
                        "currency_id": currency_id,
                        "full_name": full_name,
                        "limit": limit,
                        "name_contains": name_contains,
                        "name_ends_with": name_ends_with,
                        "name_from": name_from,
                        "name_starts_with": name_starts_with,
                        "name_to": name_to,
                        "status": status,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                    },
                    account_list_params.AccountListParams,
                ),
            ),
            cast_to=AccountListResponse,
        )


class AsyncAccountsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccountsResourceWithRawResponse:
        return AsyncAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountsResourceWithStreamingResponse:
        return AsyncAccountsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_type: Literal[
            "accounts_payable",
            "accounts_receivable",
            "bank",
            "cost_of_goods_sold",
            "credit_card",
            "equity",
            "expense",
            "fixed_asset",
            "income",
            "long_term_liability",
            "non_posting",
            "other_asset",
            "other_current_asset",
            "other_current_liability",
            "other_expense",
            "other_income",
        ],
        name: str,
        conductor_end_user_id: str,
        account_number: str | NotGiven = NOT_GIVEN,
        bank_number: str | NotGiven = NOT_GIVEN,
        currency_id: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        opening_balance: str | NotGiven = NOT_GIVEN,
        opening_balance_date: str | NotGiven = NOT_GIVEN,
        parent_id: str | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        tax_line_id: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QbdAccount:
        """
        Creates a financial account.

        Args:
          account_type: The type of QuickBooks account.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          is_active: Whether this account is active. QuickBooks hides inactive objects from most
              views and reports in the UI.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            "/quickbooks-desktop/accounts",
            body=await async_maybe_transform(
                {
                    "account_type": account_type,
                    "name": name,
                    "account_number": account_number,
                    "bank_number": bank_number,
                    "currency_id": currency_id,
                    "description": description,
                    "is_active": is_active,
                    "opening_balance": opening_balance,
                    "opening_balance_date": opening_balance_date,
                    "parent_id": parent_id,
                    "sales_tax_code_id": sales_tax_code_id,
                    "tax_line_id": tax_line_id,
                },
                account_create_params.AccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QbdAccount,
        )

    async def list(
        self,
        *,
        conductor_end_user_id: str,
        id: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        account_type: Literal[
            "accounts_payable",
            "accounts_receivable",
            "bank",
            "cost_of_goods_sold",
            "credit_card",
            "equity",
            "expense",
            "fixed_asset",
            "income",
            "long_term_liability",
            "non_posting",
            "other_asset",
            "other_current_asset",
            "other_current_liability",
            "other_expense",
            "other_income",
        ]
        | NotGiven = NOT_GIVEN,
        currency_id: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        full_name: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name_contains: str | NotGiven = NOT_GIVEN,
        name_ends_with: str | NotGiven = NOT_GIVEN,
        name_from: str | NotGiven = NOT_GIVEN,
        name_starts_with: str | NotGiven = NOT_GIVEN,
        name_to: str | NotGiven = NOT_GIVEN,
        status: Literal["active", "all", "inactive"] | NotGiven = NOT_GIVEN,
        updated_after: str | NotGiven = NOT_GIVEN,
        updated_before: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountListResponse:
        """
        Returns a list of accounts.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          id: Filter for accounts with the specified QuickBooks-assigned unique identifier(s).
              If your request includes this parameter, all other query parameters will be
              ignored.

          account_type: Filter for accounts of this type.

          currency_id: Filter for accounts in this currency or currencies.

          full_name: Filter for accounts with this full-name or full-names. Like `id`, a full-name is
              a unique identifier for an account, and is created by prefixing the account's
              name with the names of each ancestor. If your request includes this parameter,
              all other query parameters will be ignored.

          limit: The maximum number of objects to return, ranging from 1 to 500. Defaults to 500.
              NOTE: QuickBooks Desktop does not support cursor-based pagination for this
              endpoint. Hence, this parameter will limit the response size, but you will not
              be able to fetch the next set of results. If you must paginate through the
              results, try iterating via the date-range query parameters.

          name_contains: Filter for objects whose `name` contains this substring. If you use this
              parameter, you cannot use `nameStartsWith` or `nameEndsWith`.

          name_ends_with: Filter for objects whose `name` ends with this substring. If you use this
              parameter, you cannot use `nameContains` or `nameStartsWith`.

          name_from: Filter for objects whose `name` is alphabetically greater than or equal to this
              value.

          name_starts_with: Filter for objects whose `name` starts with this substring. If you use this
              parameter, you cannot use `nameContains` or `nameEndsWith`.

          name_to: Filter for objects whose `name` is alphabetically less than or equal to this
              value.

          status: Filter for objects that are active, inactive, or both.

          updated_after: Filter for objects updated on or after this date and time, in ISO 8601 format
              (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
              assumed to be 00:00:00 of that day.

          updated_before: Filter for objects updated on or before this date and time, in ISO 8601 format
              (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
              assumed to be 23:59:59 of that day.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._get(
            "/quickbooks-desktop/accounts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "id": id,
                        "account_type": account_type,
                        "currency_id": currency_id,
                        "full_name": full_name,
                        "limit": limit,
                        "name_contains": name_contains,
                        "name_ends_with": name_ends_with,
                        "name_from": name_from,
                        "name_starts_with": name_starts_with,
                        "name_to": name_to,
                        "status": status,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                    },
                    account_list_params.AccountListParams,
                ),
            ),
            cast_to=AccountListResponse,
        )


class AccountsResourceWithRawResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.create = to_raw_response_wrapper(
            accounts.create,
        )
        self.list = to_raw_response_wrapper(
            accounts.list,
        )


class AsyncAccountsResourceWithRawResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.create = async_to_raw_response_wrapper(
            accounts.create,
        )
        self.list = async_to_raw_response_wrapper(
            accounts.list,
        )


class AccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.create = to_streamed_response_wrapper(
            accounts.create,
        )
        self.list = to_streamed_response_wrapper(
            accounts.list,
        )


class AsyncAccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.create = async_to_streamed_response_wrapper(
            accounts.create,
        )
        self.list = async_to_streamed_response_wrapper(
            accounts.list,
        )
