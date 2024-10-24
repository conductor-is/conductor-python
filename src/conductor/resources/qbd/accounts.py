# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
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
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return AccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
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
        bank_account_number: str | NotGiven = NOT_GIVEN,
        currency_id: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        opening_balance: str | NotGiven = NOT_GIVEN,
        opening_balance_date: Union[str, date] | NotGiven = NOT_GIVEN,
        parent_id: str | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        tax_line_id: float | NotGiven = NOT_GIVEN,
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
          account_type: The classification of this account, indicating its purpose within the chart of
              accounts. You cannot create an account of type "non_posting" through the API
              because QuickBooks creates these accounts behind the scenes.

          name: The case-insensitive name of this account. Not guaranteed to be unique because
              it does not include the names of its parent objects like `fullName` does. For
              example, two accounts could both have the `name` "Accounts-Payable", but they
              could have unique `fullName` values, such as "Corporate:Accounts-Payable" and
              "Finance:Accounts-Payable".

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          account_number: The account's account number, which appears in the QuickBooks chart of accounts,
              reports, and graphs. Note that if the "Use Account Numbers" preference is turned
              off in QuickBooks, the account number may not be visible in the user interface,
              but it can still be set and retrieved through the API.

          bank_account_number: The bank account number or identifying note for this account. Access to this
              field may be restricted based on permissions.

          currency_id: The account's currency. For built-in currencies, the name and code are standard
              international values. For user-defined currencies, all values are editable.

          description: A description of this account.

          is_active: Indicates whether this account is active. Inactive objects are typically hidden
              from views and reports in QuickBooks.

          opening_balance: The amount of money in, or the value of, this account as of
              `openingBalanceDate`. On a bank statement, this would be the amount of money in
              the account at the beginning of the statement period.

          opening_balance_date: The date of the opening balance for this account, in ISO 8601 format
              (YYYY-MM-DD).

          parent_id: The parent account one level above this one in the hierarchy. For example, if
              this account has a `fullName` of "Corporate:Accounts-Payable", its parent has a
              `fullName` of "Corporate". If this account is at the top level, `parent` will be
              `null`.

          sales_tax_code_id: The sales-tax code associated with this account, determining whether
              transactions in this account are taxable or non-taxable. It's used to assign a
              default tax status to all transactions for this account. Default codes include
              "Non" (non-taxable) and "Tax" (taxable), but custom codes can also be created in
              QuickBooks. If QuickBooks is not set up to charge sales tax (via the "Do You
              Charge Sales Tax?" preference), it will assign the default non-taxable code to
              all sales.

          tax_line_id: The identifier of the tax line associated with this account.

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
                    "bank_account_number": bank_account_number,
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
    ) -> QbdAccount:
        """
        Retrieves an account by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the account to retrieve.

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
            f"/quickbooks-desktop/accounts/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QbdAccount,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
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
        currency_ids: str | NotGiven = NOT_GIVEN,
        full_names: str | NotGiven = NOT_GIVEN,
        ids: str | NotGiven = NOT_GIVEN,
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

          account_type: Filter for accounts of this type.

          currency_ids: Filter for accounts in this currency or currencies. Specify a single currency ID
              or multiple using a comma-separated list (e.g., `currencyIds=1,2,3`).

          full_names: Filter for specific accounts by their full-name(s). Specify a single full-name
              or multiple using a comma-separated list (e.g., `fullNames=1,2,3`). Like `id`, a
              `fullName` is a unique identifier for an account, and is formed by by combining
              the names of its parent objects with its own `name`, separated by colons. For
              example, if an account is under "Expenses:Utilities" and has the `name`
              "Electricity", its `fullName` would be "Expenses:Utilities:Electricity". Unlike
              `name`, `fullName` is guaranteed to be unique across all account objects. Not
              case-sensitive. NOTE: If you include this parameter, all other query parameters
              will be ignored.

          ids: Filter for specific accounts by their QuickBooks-assigned unique identifier(s).
              Specify a single ID or multiple using a comma-separated list (e.g.,
              `ids=1,2,3`). NOTE: If you include this parameter, all other query parameters
              will be ignored.

          limit: The maximum number of objects to return, ranging from 1 to 500. Defaults to 500.
              NOTE: QuickBooks Desktop does not support cursor-based pagination for accounts.
              Hence, this parameter will limit the response size, but you will not be able to
              fetch the next set of results. To paginate through the results for this
              endpoint, try fetching batches via the date-range query parameters.

          name_contains: Filter for accounts whose `name` contains this substring. If you use this
              parameter, you cannot use `nameStartsWith` or `nameEndsWith`.

          name_ends_with: Filter for accounts whose `name` ends with this substring. If you use this
              parameter, you cannot use `nameContains` or `nameStartsWith`.

          name_from: Filter for accounts whose `name` is alphabetically greater than or equal to this
              value.

          name_starts_with: Filter for accounts whose `name` starts with this substring. If you use this
              parameter, you cannot use `nameContains` or `nameEndsWith`.

          name_to: Filter for accounts whose `name` is alphabetically less than or equal to this
              value.

          status: Filter for accounts that are active, inactive, or both.

          updated_after: Filter for accounts updated on or after this date and time, in ISO 8601 format
              (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
              assumed to be 00:00:00 of that day.

          updated_before: Filter for accounts updated on or before this date and time, in ISO 8601 format
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
                        "account_type": account_type,
                        "currency_ids": currency_ids,
                        "full_names": full_names,
                        "ids": ids,
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
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
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
        bank_account_number: str | NotGiven = NOT_GIVEN,
        currency_id: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        opening_balance: str | NotGiven = NOT_GIVEN,
        opening_balance_date: Union[str, date] | NotGiven = NOT_GIVEN,
        parent_id: str | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        tax_line_id: float | NotGiven = NOT_GIVEN,
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
          account_type: The classification of this account, indicating its purpose within the chart of
              accounts. You cannot create an account of type "non_posting" through the API
              because QuickBooks creates these accounts behind the scenes.

          name: The case-insensitive name of this account. Not guaranteed to be unique because
              it does not include the names of its parent objects like `fullName` does. For
              example, two accounts could both have the `name` "Accounts-Payable", but they
              could have unique `fullName` values, such as "Corporate:Accounts-Payable" and
              "Finance:Accounts-Payable".

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          account_number: The account's account number, which appears in the QuickBooks chart of accounts,
              reports, and graphs. Note that if the "Use Account Numbers" preference is turned
              off in QuickBooks, the account number may not be visible in the user interface,
              but it can still be set and retrieved through the API.

          bank_account_number: The bank account number or identifying note for this account. Access to this
              field may be restricted based on permissions.

          currency_id: The account's currency. For built-in currencies, the name and code are standard
              international values. For user-defined currencies, all values are editable.

          description: A description of this account.

          is_active: Indicates whether this account is active. Inactive objects are typically hidden
              from views and reports in QuickBooks.

          opening_balance: The amount of money in, or the value of, this account as of
              `openingBalanceDate`. On a bank statement, this would be the amount of money in
              the account at the beginning of the statement period.

          opening_balance_date: The date of the opening balance for this account, in ISO 8601 format
              (YYYY-MM-DD).

          parent_id: The parent account one level above this one in the hierarchy. For example, if
              this account has a `fullName` of "Corporate:Accounts-Payable", its parent has a
              `fullName` of "Corporate". If this account is at the top level, `parent` will be
              `null`.

          sales_tax_code_id: The sales-tax code associated with this account, determining whether
              transactions in this account are taxable or non-taxable. It's used to assign a
              default tax status to all transactions for this account. Default codes include
              "Non" (non-taxable) and "Tax" (taxable), but custom codes can also be created in
              QuickBooks. If QuickBooks is not set up to charge sales tax (via the "Do You
              Charge Sales Tax?" preference), it will assign the default non-taxable code to
              all sales.

          tax_line_id: The identifier of the tax line associated with this account.

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
                    "bank_account_number": bank_account_number,
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
    ) -> QbdAccount:
        """
        Retrieves an account by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the account to retrieve.

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
            f"/quickbooks-desktop/accounts/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QbdAccount,
        )

    async def list(
        self,
        *,
        conductor_end_user_id: str,
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
        currency_ids: str | NotGiven = NOT_GIVEN,
        full_names: str | NotGiven = NOT_GIVEN,
        ids: str | NotGiven = NOT_GIVEN,
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

          account_type: Filter for accounts of this type.

          currency_ids: Filter for accounts in this currency or currencies. Specify a single currency ID
              or multiple using a comma-separated list (e.g., `currencyIds=1,2,3`).

          full_names: Filter for specific accounts by their full-name(s). Specify a single full-name
              or multiple using a comma-separated list (e.g., `fullNames=1,2,3`). Like `id`, a
              `fullName` is a unique identifier for an account, and is formed by by combining
              the names of its parent objects with its own `name`, separated by colons. For
              example, if an account is under "Expenses:Utilities" and has the `name`
              "Electricity", its `fullName` would be "Expenses:Utilities:Electricity". Unlike
              `name`, `fullName` is guaranteed to be unique across all account objects. Not
              case-sensitive. NOTE: If you include this parameter, all other query parameters
              will be ignored.

          ids: Filter for specific accounts by their QuickBooks-assigned unique identifier(s).
              Specify a single ID or multiple using a comma-separated list (e.g.,
              `ids=1,2,3`). NOTE: If you include this parameter, all other query parameters
              will be ignored.

          limit: The maximum number of objects to return, ranging from 1 to 500. Defaults to 500.
              NOTE: QuickBooks Desktop does not support cursor-based pagination for accounts.
              Hence, this parameter will limit the response size, but you will not be able to
              fetch the next set of results. To paginate through the results for this
              endpoint, try fetching batches via the date-range query parameters.

          name_contains: Filter for accounts whose `name` contains this substring. If you use this
              parameter, you cannot use `nameStartsWith` or `nameEndsWith`.

          name_ends_with: Filter for accounts whose `name` ends with this substring. If you use this
              parameter, you cannot use `nameContains` or `nameStartsWith`.

          name_from: Filter for accounts whose `name` is alphabetically greater than or equal to this
              value.

          name_starts_with: Filter for accounts whose `name` starts with this substring. If you use this
              parameter, you cannot use `nameContains` or `nameEndsWith`.

          name_to: Filter for accounts whose `name` is alphabetically less than or equal to this
              value.

          status: Filter for accounts that are active, inactive, or both.

          updated_after: Filter for accounts updated on or after this date and time, in ISO 8601 format
              (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
              assumed to be 00:00:00 of that day.

          updated_before: Filter for accounts updated on or before this date and time, in ISO 8601 format
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
                        "account_type": account_type,
                        "currency_ids": currency_ids,
                        "full_names": full_names,
                        "ids": ids,
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
        self.retrieve = to_raw_response_wrapper(
            accounts.retrieve,
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
        self.retrieve = async_to_raw_response_wrapper(
            accounts.retrieve,
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
        self.retrieve = to_streamed_response_wrapper(
            accounts.retrieve,
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
        self.retrieve = async_to_streamed_response_wrapper(
            accounts.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            accounts.list,
        )
