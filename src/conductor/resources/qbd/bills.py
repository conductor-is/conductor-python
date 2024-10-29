# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
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
from ...types.qbd import bill_list_params, bill_create_params, bill_update_params
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.qbd.qbd_bill import QbdBill

__all__ = ["BillsResource", "AsyncBillsResource"]


class BillsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BillsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return BillsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BillsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return BillsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        transaction_date: Union[str, date],
        vendor_id: str,
        conductor_end_user_id: str,
        due_date: Union[str, date] | NotGiven = NOT_GIVEN,
        exchange_rate: float | NotGiven = NOT_GIVEN,
        expense_lines: Iterable[bill_create_params.ExpenseLine] | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        item_group_lines: Iterable[bill_create_params.ItemGroupLine] | NotGiven = NOT_GIVEN,
        item_lines: Iterable[bill_create_params.ItemLine] | NotGiven = NOT_GIVEN,
        link_to_transaction_ids: List[str] | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        payables_account_id: str | NotGiven = NOT_GIVEN,
        ref_number: str | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        terms_id: str | NotGiven = NOT_GIVEN,
        vendor_address: bill_create_params.VendorAddress | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QbdBill:
        """
        Creates a bill.

        Args:
          transaction_date: The date of this bill, in ISO 8601 format (YYYY-MM-DD).

          vendor_id: The vendor who sent this bill for goods or services purchased.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          due_date: The date by which this bill must be paid, in ISO 8601 format (YYYY-MM-DD).

          exchange_rate: The market exchange rate between this bill's currency and the home currency in
              QuickBooks at the time of this transaction. Represented as a decimal value
              (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).

          expense_lines: The bill's expense lines, each representing one line in this expense.

          external_id: A globally unique identifier (GUID) you can provide for tracking this object in
              your external system. Must be formatted as a valid GUID; otherwise, QuickBooks
              will return an error. This field is immutable and can only be set during object
              creation.

          item_group_lines: The bill's item group lines, each representing a predefined set of items bundled
              together because they are commonly purchased together or grouped for faster
              entry.

          item_lines: The bill's item lines, each representing the purchase of a specific item or
              service.

          link_to_transaction_ids: IDs of existing transactions that you wish to link to this bill, such as
              payments applied, credits used, or associated purchase orders. Note that this
              links entire transactions, not individual transaction lines. If you want to link
              individual lines in a transaction, instead use the field `linkToTransactionLine`
              on this bill's lines, if available.

              Transactions can only be linked when creating this bill and cannot be unlinked
              later.

              You can use both `linkToTransactionIds` (on this bill) and
              `linkToTransactionLine` (on its transaction lines) as long as they do NOT link
              to the same transaction (otherwise, QuickBooks will return an error). QuickBooks
              will also return an error if you attempt to link a transaction that is empty or
              already closed.

              Note that QuickBooks will not return any information about these links in this
              endpoint's response even though they are created. To see the transactions linked
              via this field, refetch the bill and check the `linkedTransactions` field. If
              fetching a list of bills, you must also specify the parameter
              `includeLinkedTransactions` to return the `linkedTransactions` field.

          memo: A memo or note for this bill, as entered by the user. Appears in the Accounts
              Payable register and relevant reports.

          payables_account_id: The accounts payable account to which this bill is assigned, used to track the
              amount owed. If not specified, the default accounts payable account in
              QuickBooks is used.

          ref_number: The case-sensitive user-defined reference number for this bill, which can be
              used to identify the transaction in QuickBooks. This value is not required to be
              unique and can be arbitrarily changed by the QuickBooks user.

          sales_tax_code_id: The sales-tax code associated with this bill, determining whether it is taxable
              or non-taxable. It's used to assign a default tax status to all transactions for
              this bill. Default codes include "Non" (non-taxable) and "Tax" (taxable), but
              custom codes can also be created in QuickBooks. If QuickBooks is not set up to
              charge sales tax (via the "Do You Charge Sales Tax?" preference), it will assign
              the default non-taxable code to all sales.

          terms_id: The bill's payment terms, defining when payment is due and any applicable
              discounts.

          vendor_address: The address of the vendor who sent this bill.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            "/quickbooks-desktop/bills",
            body=maybe_transform(
                {
                    "transaction_date": transaction_date,
                    "vendor_id": vendor_id,
                    "due_date": due_date,
                    "exchange_rate": exchange_rate,
                    "expense_lines": expense_lines,
                    "external_id": external_id,
                    "item_group_lines": item_group_lines,
                    "item_lines": item_lines,
                    "link_to_transaction_ids": link_to_transaction_ids,
                    "memo": memo,
                    "payables_account_id": payables_account_id,
                    "ref_number": ref_number,
                    "sales_tax_code_id": sales_tax_code_id,
                    "terms_id": terms_id,
                    "vendor_address": vendor_address,
                },
                bill_create_params.BillCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QbdBill,
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
    ) -> QbdBill:
        """
        Retrieves a bill by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the bill to retrieve.

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
            f"/quickbooks-desktop/bills/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QbdBill,
        )

    def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        clear_expense_lines: bool | NotGiven = NOT_GIVEN,
        clear_item_lines: bool | NotGiven = NOT_GIVEN,
        due_date: Union[str, date] | NotGiven = NOT_GIVEN,
        exchange_rate: float | NotGiven = NOT_GIVEN,
        expense_lines: Iterable[bill_update_params.ExpenseLine] | NotGiven = NOT_GIVEN,
        item_group_lines: Iterable[bill_update_params.ItemGroupLine] | NotGiven = NOT_GIVEN,
        item_lines: Iterable[bill_update_params.ItemLine] | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        payables_account_id: str | NotGiven = NOT_GIVEN,
        ref_number: str | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        terms_id: str | NotGiven = NOT_GIVEN,
        transaction_date: Union[str, date] | NotGiven = NOT_GIVEN,
        vendor_address: bill_update_params.VendorAddress | NotGiven = NOT_GIVEN,
        vendor_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QbdBill:
        """
        Updates an existing bill.

        Args:
          id: The QuickBooks-assigned unique identifier of the bill to update.

          revision_number: The current revision number of the bill you are updating, which you can get by
              fetching the object first. Provide the most recent `revisionNumber` to ensure
              you're working with the latest data; otherwise, the update will return an error.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          clear_expense_lines: Indicates whether to clear all the expense lines of this bill. To modify
              individual lines, use the field `expenseLines`.

          clear_item_lines: Indicates whether to clear all the item lines of this bill. To modify individual
              lines, use the field `itemLines`.

          due_date: The date by which this bill must be paid, in ISO 8601 format (YYYY-MM-DD).

          exchange_rate: The market exchange rate between this bill's currency and the home currency in
              QuickBooks at the time of this transaction. Represented as a decimal value
              (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).

          expense_lines: The bill's expense lines, each representing one line in this expense.

              IMPORTANT: When updating a bill's expense lines, this array completely REPLACES
              all existing expense lines for that bill. To retain any current expense lines,
              include them in this array, even if they have not changed. Any expense lines not
              included will be removed. To add a new expense line, include it with its `id`
              set to `-1`. If you do not wish to modify the expense lines, you can omit this
              field entirely to keep them unchanged.

          item_group_lines: The bill's item group lines, each representing a predefined set of items bundled
              together because they are commonly purchased together or grouped for faster
              entry.

              IMPORTANT: When updating a bill's item group lines, this array completely
              REPLACES all existing item group lines for that bill. To retain any current item
              group lines, include them in this array, even if they have not changed. Any item
              group lines not included will be removed. To add a new item group line, include
              it with its `id` set to `-1`. If you do not wish to modify the item group lines,
              you can omit this field entirely to keep them unchanged.

          item_lines: The bill's item lines, each representing the purchase of a specific item or
              service.

              IMPORTANT: When updating a bill's item lines, this array completely REPLACES all
              existing item lines for that bill. To retain any current item lines, include
              them in this array, even if they have not changed. Any item lines not included
              will be removed. To add a new item line, include it with its `id` set to `-1`.
              If you do not wish to modify the item lines, you can omit this field entirely to
              keep them unchanged.

          memo: A memo or note for this bill, as entered by the user. Appears in the Accounts
              Payable register and relevant reports.

          payables_account_id: The accounts payable account to which this bill is assigned, used to track the
              amount owed. If not specified, the default accounts payable account in
              QuickBooks is used.

          ref_number: The case-sensitive user-defined reference number for this bill, which can be
              used to identify the transaction in QuickBooks. This value is not required to be
              unique and can be arbitrarily changed by the QuickBooks user.

          sales_tax_code_id: The sales-tax code associated with this bill, determining whether it is taxable
              or non-taxable. It's used to assign a default tax status to all transactions for
              this bill. Default codes include "Non" (non-taxable) and "Tax" (taxable), but
              custom codes can also be created in QuickBooks. If QuickBooks is not set up to
              charge sales tax (via the "Do You Charge Sales Tax?" preference), it will assign
              the default non-taxable code to all sales.

          terms_id: The bill's payment terms, defining when payment is due and any applicable
              discounts.

          transaction_date: The date of this bill, in ISO 8601 format (YYYY-MM-DD).

          vendor_address: The address of the vendor who sent this bill.

          vendor_id: The vendor who sent this bill for goods or services purchased.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            f"/quickbooks-desktop/bills/{id}",
            body=maybe_transform(
                {
                    "revision_number": revision_number,
                    "clear_expense_lines": clear_expense_lines,
                    "clear_item_lines": clear_item_lines,
                    "due_date": due_date,
                    "exchange_rate": exchange_rate,
                    "expense_lines": expense_lines,
                    "item_group_lines": item_group_lines,
                    "item_lines": item_lines,
                    "memo": memo,
                    "payables_account_id": payables_account_id,
                    "ref_number": ref_number,
                    "sales_tax_code_id": sales_tax_code_id,
                    "terms_id": terms_id,
                    "transaction_date": transaction_date,
                    "vendor_address": vendor_address,
                    "vendor_id": vendor_id,
                },
                bill_update_params.BillUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QbdBill,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        account_ids: str | NotGiven = NOT_GIVEN,
        currency_ids: str | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        ids: str | NotGiven = NOT_GIVEN,
        include_line_items: bool | NotGiven = NOT_GIVEN,
        include_linked_transactions: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        payment_status: Literal["all", "paid", "not_paid"] | NotGiven = NOT_GIVEN,
        ref_number_contains: str | NotGiven = NOT_GIVEN,
        ref_number_ends_with: str | NotGiven = NOT_GIVEN,
        ref_number_from: str | NotGiven = NOT_GIVEN,
        ref_numbers: str | NotGiven = NOT_GIVEN,
        ref_number_starts_with: str | NotGiven = NOT_GIVEN,
        ref_number_to: str | NotGiven = NOT_GIVEN,
        transaction_date_from: Union[str, date] | NotGiven = NOT_GIVEN,
        transaction_date_to: Union[str, date] | NotGiven = NOT_GIVEN,
        updated_after: str | NotGiven = NOT_GIVEN,
        updated_before: str | NotGiven = NOT_GIVEN,
        vendor_ids: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorPage[QbdBill]:
        """
        Returns a list of bills.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          account_ids: Filter for bills from this account or accounts. Specify a single account ID or
              multiple using a comma-separated list (e.g., `accountIds=1,2,3`).

          currency_ids: Filter for bills in this currency or currencies. Specify a single currency ID or
              multiple using a comma-separated list (e.g., `currencyIds=1,2,3`).

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Retrieve this value from the `nextCursor` field in the
              previous response. If omitted, the API returns the first page of results.

          ids: Filter for specific bills by their QuickBooks-assigned unique identifier(s).
              Specify a single ID or multiple using a comma-separated list (e.g.,
              `ids=1,2,3`). NOTE: If you include this parameter, all other query parameters
              will be ignored.

          include_line_items: Whether to include line items in the response.

          include_linked_transactions: Whether to include linked transactions in the response. For example, a payment
              linked to the corresponding bill.

          limit: The maximum number of objects to return, ranging from 1 to 500. Defaults to 500.
              Use this parameter in conjunction with the `cursor` parameter to paginate
              through results. The response will include a `nextCursor` field, which can be
              used as the `cursor` parameter value in subsequent requests to fetch the next
              set of results.

          payment_status: Filter for bills that are paid, not paid, or both.

          ref_number_contains: Filter for bills whose `refNumber` contains this substring. If you use this
              parameter, you cannot use `refNumberStartsWith` or `refNumberEndsWith`.

          ref_number_ends_with: Filter for bills whose `refNumber` ends with this substring. If you use this
              parameter, you cannot use `refNumberContains` or `refNumberStartsWith`.

          ref_number_from: Filter for bills whose `refNumber` is greater than or equal to this value. If
              omitted, the range will begin with the first number of the list. Uses a
              numerical comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          ref_numbers: Filter for specific bills by their ref-number(s), case-sensitive. Specify a
              single ref-number or multiple using a comma-separated list (e.g.,
              `refNumbers=1,2,3`). In QuickBooks, ref-numbers are not required to be unique
              and can be arbitrarily changed by the QuickBooks user. NOTE: If you include this
              parameter, all other query parameters will be ignored.

          ref_number_starts_with: Filter for bills whose `refNumber` starts with this substring. If you use this
              parameter, you cannot use `refNumberContains` or `refNumberEndsWith`.

          ref_number_to: Filter for bills whose `refNumber` is less than or equal to this value. If
              omitted, the range will end with the last number of the list. Uses a numerical
              comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          transaction_date_from: Filter for bills created on or after this date, in ISO 8601 format (YYYY-MM-DD).

          transaction_date_to: Filter for bills created on or before this date, in ISO 8601 format
              (YYYY-MM-DD).

          updated_after: Filter for bills updated on or after this date and time, in ISO 8601 format
              (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
              assumed to be 00:00:00 of that day.

          updated_before: Filter for bills updated on or before this date and time, in ISO 8601 format
              (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
              assumed to be 23:59:59 of that day.

          vendor_ids: Filter for bills from this vendor or vendors. Specify a single vendor ID or
              multiple using a comma-separated list (e.g., `vendorIds=1,2,3`).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get_api_list(
            "/quickbooks-desktop/bills",
            page=SyncCursorPage[QbdBill],
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
                        "payment_status": payment_status,
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
                    bill_list_params.BillListParams,
                ),
            ),
            model=QbdBill,
        )


class AsyncBillsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBillsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBillsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBillsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return AsyncBillsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        transaction_date: Union[str, date],
        vendor_id: str,
        conductor_end_user_id: str,
        due_date: Union[str, date] | NotGiven = NOT_GIVEN,
        exchange_rate: float | NotGiven = NOT_GIVEN,
        expense_lines: Iterable[bill_create_params.ExpenseLine] | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        item_group_lines: Iterable[bill_create_params.ItemGroupLine] | NotGiven = NOT_GIVEN,
        item_lines: Iterable[bill_create_params.ItemLine] | NotGiven = NOT_GIVEN,
        link_to_transaction_ids: List[str] | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        payables_account_id: str | NotGiven = NOT_GIVEN,
        ref_number: str | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        terms_id: str | NotGiven = NOT_GIVEN,
        vendor_address: bill_create_params.VendorAddress | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QbdBill:
        """
        Creates a bill.

        Args:
          transaction_date: The date of this bill, in ISO 8601 format (YYYY-MM-DD).

          vendor_id: The vendor who sent this bill for goods or services purchased.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          due_date: The date by which this bill must be paid, in ISO 8601 format (YYYY-MM-DD).

          exchange_rate: The market exchange rate between this bill's currency and the home currency in
              QuickBooks at the time of this transaction. Represented as a decimal value
              (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).

          expense_lines: The bill's expense lines, each representing one line in this expense.

          external_id: A globally unique identifier (GUID) you can provide for tracking this object in
              your external system. Must be formatted as a valid GUID; otherwise, QuickBooks
              will return an error. This field is immutable and can only be set during object
              creation.

          item_group_lines: The bill's item group lines, each representing a predefined set of items bundled
              together because they are commonly purchased together or grouped for faster
              entry.

          item_lines: The bill's item lines, each representing the purchase of a specific item or
              service.

          link_to_transaction_ids: IDs of existing transactions that you wish to link to this bill, such as
              payments applied, credits used, or associated purchase orders. Note that this
              links entire transactions, not individual transaction lines. If you want to link
              individual lines in a transaction, instead use the field `linkToTransactionLine`
              on this bill's lines, if available.

              Transactions can only be linked when creating this bill and cannot be unlinked
              later.

              You can use both `linkToTransactionIds` (on this bill) and
              `linkToTransactionLine` (on its transaction lines) as long as they do NOT link
              to the same transaction (otherwise, QuickBooks will return an error). QuickBooks
              will also return an error if you attempt to link a transaction that is empty or
              already closed.

              Note that QuickBooks will not return any information about these links in this
              endpoint's response even though they are created. To see the transactions linked
              via this field, refetch the bill and check the `linkedTransactions` field. If
              fetching a list of bills, you must also specify the parameter
              `includeLinkedTransactions` to return the `linkedTransactions` field.

          memo: A memo or note for this bill, as entered by the user. Appears in the Accounts
              Payable register and relevant reports.

          payables_account_id: The accounts payable account to which this bill is assigned, used to track the
              amount owed. If not specified, the default accounts payable account in
              QuickBooks is used.

          ref_number: The case-sensitive user-defined reference number for this bill, which can be
              used to identify the transaction in QuickBooks. This value is not required to be
              unique and can be arbitrarily changed by the QuickBooks user.

          sales_tax_code_id: The sales-tax code associated with this bill, determining whether it is taxable
              or non-taxable. It's used to assign a default tax status to all transactions for
              this bill. Default codes include "Non" (non-taxable) and "Tax" (taxable), but
              custom codes can also be created in QuickBooks. If QuickBooks is not set up to
              charge sales tax (via the "Do You Charge Sales Tax?" preference), it will assign
              the default non-taxable code to all sales.

          terms_id: The bill's payment terms, defining when payment is due and any applicable
              discounts.

          vendor_address: The address of the vendor who sent this bill.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            "/quickbooks-desktop/bills",
            body=await async_maybe_transform(
                {
                    "transaction_date": transaction_date,
                    "vendor_id": vendor_id,
                    "due_date": due_date,
                    "exchange_rate": exchange_rate,
                    "expense_lines": expense_lines,
                    "external_id": external_id,
                    "item_group_lines": item_group_lines,
                    "item_lines": item_lines,
                    "link_to_transaction_ids": link_to_transaction_ids,
                    "memo": memo,
                    "payables_account_id": payables_account_id,
                    "ref_number": ref_number,
                    "sales_tax_code_id": sales_tax_code_id,
                    "terms_id": terms_id,
                    "vendor_address": vendor_address,
                },
                bill_create_params.BillCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QbdBill,
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
    ) -> QbdBill:
        """
        Retrieves a bill by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the bill to retrieve.

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
            f"/quickbooks-desktop/bills/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QbdBill,
        )

    async def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        clear_expense_lines: bool | NotGiven = NOT_GIVEN,
        clear_item_lines: bool | NotGiven = NOT_GIVEN,
        due_date: Union[str, date] | NotGiven = NOT_GIVEN,
        exchange_rate: float | NotGiven = NOT_GIVEN,
        expense_lines: Iterable[bill_update_params.ExpenseLine] | NotGiven = NOT_GIVEN,
        item_group_lines: Iterable[bill_update_params.ItemGroupLine] | NotGiven = NOT_GIVEN,
        item_lines: Iterable[bill_update_params.ItemLine] | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        payables_account_id: str | NotGiven = NOT_GIVEN,
        ref_number: str | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        terms_id: str | NotGiven = NOT_GIVEN,
        transaction_date: Union[str, date] | NotGiven = NOT_GIVEN,
        vendor_address: bill_update_params.VendorAddress | NotGiven = NOT_GIVEN,
        vendor_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QbdBill:
        """
        Updates an existing bill.

        Args:
          id: The QuickBooks-assigned unique identifier of the bill to update.

          revision_number: The current revision number of the bill you are updating, which you can get by
              fetching the object first. Provide the most recent `revisionNumber` to ensure
              you're working with the latest data; otherwise, the update will return an error.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          clear_expense_lines: Indicates whether to clear all the expense lines of this bill. To modify
              individual lines, use the field `expenseLines`.

          clear_item_lines: Indicates whether to clear all the item lines of this bill. To modify individual
              lines, use the field `itemLines`.

          due_date: The date by which this bill must be paid, in ISO 8601 format (YYYY-MM-DD).

          exchange_rate: The market exchange rate between this bill's currency and the home currency in
              QuickBooks at the time of this transaction. Represented as a decimal value
              (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).

          expense_lines: The bill's expense lines, each representing one line in this expense.

              IMPORTANT: When updating a bill's expense lines, this array completely REPLACES
              all existing expense lines for that bill. To retain any current expense lines,
              include them in this array, even if they have not changed. Any expense lines not
              included will be removed. To add a new expense line, include it with its `id`
              set to `-1`. If you do not wish to modify the expense lines, you can omit this
              field entirely to keep them unchanged.

          item_group_lines: The bill's item group lines, each representing a predefined set of items bundled
              together because they are commonly purchased together or grouped for faster
              entry.

              IMPORTANT: When updating a bill's item group lines, this array completely
              REPLACES all existing item group lines for that bill. To retain any current item
              group lines, include them in this array, even if they have not changed. Any item
              group lines not included will be removed. To add a new item group line, include
              it with its `id` set to `-1`. If you do not wish to modify the item group lines,
              you can omit this field entirely to keep them unchanged.

          item_lines: The bill's item lines, each representing the purchase of a specific item or
              service.

              IMPORTANT: When updating a bill's item lines, this array completely REPLACES all
              existing item lines for that bill. To retain any current item lines, include
              them in this array, even if they have not changed. Any item lines not included
              will be removed. To add a new item line, include it with its `id` set to `-1`.
              If you do not wish to modify the item lines, you can omit this field entirely to
              keep them unchanged.

          memo: A memo or note for this bill, as entered by the user. Appears in the Accounts
              Payable register and relevant reports.

          payables_account_id: The accounts payable account to which this bill is assigned, used to track the
              amount owed. If not specified, the default accounts payable account in
              QuickBooks is used.

          ref_number: The case-sensitive user-defined reference number for this bill, which can be
              used to identify the transaction in QuickBooks. This value is not required to be
              unique and can be arbitrarily changed by the QuickBooks user.

          sales_tax_code_id: The sales-tax code associated with this bill, determining whether it is taxable
              or non-taxable. It's used to assign a default tax status to all transactions for
              this bill. Default codes include "Non" (non-taxable) and "Tax" (taxable), but
              custom codes can also be created in QuickBooks. If QuickBooks is not set up to
              charge sales tax (via the "Do You Charge Sales Tax?" preference), it will assign
              the default non-taxable code to all sales.

          terms_id: The bill's payment terms, defining when payment is due and any applicable
              discounts.

          transaction_date: The date of this bill, in ISO 8601 format (YYYY-MM-DD).

          vendor_address: The address of the vendor who sent this bill.

          vendor_id: The vendor who sent this bill for goods or services purchased.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            f"/quickbooks-desktop/bills/{id}",
            body=await async_maybe_transform(
                {
                    "revision_number": revision_number,
                    "clear_expense_lines": clear_expense_lines,
                    "clear_item_lines": clear_item_lines,
                    "due_date": due_date,
                    "exchange_rate": exchange_rate,
                    "expense_lines": expense_lines,
                    "item_group_lines": item_group_lines,
                    "item_lines": item_lines,
                    "memo": memo,
                    "payables_account_id": payables_account_id,
                    "ref_number": ref_number,
                    "sales_tax_code_id": sales_tax_code_id,
                    "terms_id": terms_id,
                    "transaction_date": transaction_date,
                    "vendor_address": vendor_address,
                    "vendor_id": vendor_id,
                },
                bill_update_params.BillUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QbdBill,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        account_ids: str | NotGiven = NOT_GIVEN,
        currency_ids: str | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        ids: str | NotGiven = NOT_GIVEN,
        include_line_items: bool | NotGiven = NOT_GIVEN,
        include_linked_transactions: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        payment_status: Literal["all", "paid", "not_paid"] | NotGiven = NOT_GIVEN,
        ref_number_contains: str | NotGiven = NOT_GIVEN,
        ref_number_ends_with: str | NotGiven = NOT_GIVEN,
        ref_number_from: str | NotGiven = NOT_GIVEN,
        ref_numbers: str | NotGiven = NOT_GIVEN,
        ref_number_starts_with: str | NotGiven = NOT_GIVEN,
        ref_number_to: str | NotGiven = NOT_GIVEN,
        transaction_date_from: Union[str, date] | NotGiven = NOT_GIVEN,
        transaction_date_to: Union[str, date] | NotGiven = NOT_GIVEN,
        updated_after: str | NotGiven = NOT_GIVEN,
        updated_before: str | NotGiven = NOT_GIVEN,
        vendor_ids: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[QbdBill, AsyncCursorPage[QbdBill]]:
        """
        Returns a list of bills.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          account_ids: Filter for bills from this account or accounts. Specify a single account ID or
              multiple using a comma-separated list (e.g., `accountIds=1,2,3`).

          currency_ids: Filter for bills in this currency or currencies. Specify a single currency ID or
              multiple using a comma-separated list (e.g., `currencyIds=1,2,3`).

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Retrieve this value from the `nextCursor` field in the
              previous response. If omitted, the API returns the first page of results.

          ids: Filter for specific bills by their QuickBooks-assigned unique identifier(s).
              Specify a single ID or multiple using a comma-separated list (e.g.,
              `ids=1,2,3`). NOTE: If you include this parameter, all other query parameters
              will be ignored.

          include_line_items: Whether to include line items in the response.

          include_linked_transactions: Whether to include linked transactions in the response. For example, a payment
              linked to the corresponding bill.

          limit: The maximum number of objects to return, ranging from 1 to 500. Defaults to 500.
              Use this parameter in conjunction with the `cursor` parameter to paginate
              through results. The response will include a `nextCursor` field, which can be
              used as the `cursor` parameter value in subsequent requests to fetch the next
              set of results.

          payment_status: Filter for bills that are paid, not paid, or both.

          ref_number_contains: Filter for bills whose `refNumber` contains this substring. If you use this
              parameter, you cannot use `refNumberStartsWith` or `refNumberEndsWith`.

          ref_number_ends_with: Filter for bills whose `refNumber` ends with this substring. If you use this
              parameter, you cannot use `refNumberContains` or `refNumberStartsWith`.

          ref_number_from: Filter for bills whose `refNumber` is greater than or equal to this value. If
              omitted, the range will begin with the first number of the list. Uses a
              numerical comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          ref_numbers: Filter for specific bills by their ref-number(s), case-sensitive. Specify a
              single ref-number or multiple using a comma-separated list (e.g.,
              `refNumbers=1,2,3`). In QuickBooks, ref-numbers are not required to be unique
              and can be arbitrarily changed by the QuickBooks user. NOTE: If you include this
              parameter, all other query parameters will be ignored.

          ref_number_starts_with: Filter for bills whose `refNumber` starts with this substring. If you use this
              parameter, you cannot use `refNumberContains` or `refNumberEndsWith`.

          ref_number_to: Filter for bills whose `refNumber` is less than or equal to this value. If
              omitted, the range will end with the last number of the list. Uses a numerical
              comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          transaction_date_from: Filter for bills created on or after this date, in ISO 8601 format (YYYY-MM-DD).

          transaction_date_to: Filter for bills created on or before this date, in ISO 8601 format
              (YYYY-MM-DD).

          updated_after: Filter for bills updated on or after this date and time, in ISO 8601 format
              (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
              assumed to be 00:00:00 of that day.

          updated_before: Filter for bills updated on or before this date and time, in ISO 8601 format
              (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
              assumed to be 23:59:59 of that day.

          vendor_ids: Filter for bills from this vendor or vendors. Specify a single vendor ID or
              multiple using a comma-separated list (e.g., `vendorIds=1,2,3`).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get_api_list(
            "/quickbooks-desktop/bills",
            page=AsyncCursorPage[QbdBill],
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
                        "payment_status": payment_status,
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
                    bill_list_params.BillListParams,
                ),
            ),
            model=QbdBill,
        )


class BillsResourceWithRawResponse:
    def __init__(self, bills: BillsResource) -> None:
        self._bills = bills

        self.create = to_raw_response_wrapper(
            bills.create,
        )
        self.retrieve = to_raw_response_wrapper(
            bills.retrieve,
        )
        self.update = to_raw_response_wrapper(
            bills.update,
        )
        self.list = to_raw_response_wrapper(
            bills.list,
        )


class AsyncBillsResourceWithRawResponse:
    def __init__(self, bills: AsyncBillsResource) -> None:
        self._bills = bills

        self.create = async_to_raw_response_wrapper(
            bills.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            bills.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            bills.update,
        )
        self.list = async_to_raw_response_wrapper(
            bills.list,
        )


class BillsResourceWithStreamingResponse:
    def __init__(self, bills: BillsResource) -> None:
        self._bills = bills

        self.create = to_streamed_response_wrapper(
            bills.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            bills.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            bills.update,
        )
        self.list = to_streamed_response_wrapper(
            bills.list,
        )


class AsyncBillsResourceWithStreamingResponse:
    def __init__(self, bills: AsyncBillsResource) -> None:
        self._bills = bills

        self.create = async_to_streamed_response_wrapper(
            bills.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            bills.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            bills.update,
        )
        self.list = async_to_streamed_response_wrapper(
            bills.list,
        )
