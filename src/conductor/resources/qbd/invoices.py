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
from ...types.qbd import invoice_list_params, invoice_create_params
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.qbd.qbd_invoice import QbdInvoice

__all__ = ["InvoicesResource", "AsyncInvoicesResource"]


class InvoicesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InvoicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return InvoicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InvoicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return InvoicesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        customer_id: str,
        transaction_date: Union[str, date],
        conductor_end_user_id: str,
        accounts_receivable_account_id: str | NotGiven = NOT_GIVEN,
        billing_address: invoice_create_params.BillingAddress | NotGiven = NOT_GIVEN,
        class_id: str | NotGiven = NOT_GIVEN,
        customer_message_id: str | NotGiven = NOT_GIVEN,
        document_template_id: str | NotGiven = NOT_GIVEN,
        due_date: Union[str, date] | NotGiven = NOT_GIVEN,
        exchange_rate: float | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        invoice_line_groups: Iterable[invoice_create_params.InvoiceLineGroup] | NotGiven = NOT_GIVEN,
        invoice_lines: Iterable[invoice_create_params.InvoiceLine] | NotGiven = NOT_GIVEN,
        is_finance_charge: bool | NotGiven = NOT_GIVEN,
        is_pending: bool | NotGiven = NOT_GIVEN,
        is_to_be_emailed: bool | NotGiven = NOT_GIVEN,
        is_to_be_printed: bool | NotGiven = NOT_GIVEN,
        item_sales_tax_id: str | NotGiven = NOT_GIVEN,
        link_to_transaction_ids: List[str] | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        other_custom_field: str | NotGiven = NOT_GIVEN,
        purchase_order_number: str | NotGiven = NOT_GIVEN,
        ref_number: str | NotGiven = NOT_GIVEN,
        sales_representative_id: str | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        set_credits: Iterable[invoice_create_params.SetCredit] | NotGiven = NOT_GIVEN,
        shipping_address: invoice_create_params.ShippingAddress | NotGiven = NOT_GIVEN,
        shipping_date: Union[str, date] | NotGiven = NOT_GIVEN,
        shipping_method_id: str | NotGiven = NOT_GIVEN,
        shipping_origin: str | NotGiven = NOT_GIVEN,
        terms_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QbdInvoice:
        """
        Creates an invoice.

        Args:
          customer_id: The customer or customer-job associated with this invoice.

          transaction_date: The date of this invoice, in ISO 8601 format (YYYY-MM-DD).

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          accounts_receivable_account_id: The Accounts Receivable account to which this invoice is assigned, used to track
              the amount owed. If not specified, the default Accounts Receivable account in
              QuickBooks is used. If this invoice is linked to other transactions, make sure
              this `accountsReceivableAccount` matches the `accountsReceivableAccount` used in
              the other transactions.

          billing_address: The invoice's billing address.

          class_id: The invoice's class. Classes can be used to categorize objects into meaningful
              segments, such as department, location, or type of work. In QuickBooks, class
              tracking is off by default. A class defined here is automatically used in this
              invoice's line items unless overridden at the line item level.

          customer_message_id: The message to display to the customer on the invoice.

          document_template_id: The predefined template in QuickBooks that determines the layout and formatting
              for this invoice when printed or displayed.

          due_date: The date by which this invoice must be paid, in ISO 8601 format (YYYY-MM-DD).

          exchange_rate: The market exchange rate between this invoice's currency and the home currency
              in QuickBooks at the time of this transaction. Represented as a decimal value
              (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).

          external_id: A globally unique identifier (GUID) you can provide for tracking this object in
              your external system. Must be formatted as a valid GUID; otherwise, QuickBooks
              will return an error. This field is immutable and can only be set during object
              creation.

          invoice_line_groups: The invoice's line item groups. Each group represents a predefined set of
              related items.

          invoice_lines: The invoice's invoice lines, each representing a single product or service sold.

          is_finance_charge: Whether this invoice includes a finance charge.

          is_pending: Indicates whether this invoice is pending approval or completion. If `true`, the
              invoice is in a draft state and has not been finalized.

          is_to_be_emailed: Indicates whether this invoice is queued to be emailed to the customer. If set
              to `true`, the invoice will appear in the list of documents to be emailed in
              QuickBooks.

          is_to_be_printed: Indicates whether this invoice is queued for printing. If set to `true`, the
              invoice will appear in the list of documents to be printed in QuickBooks.

          item_sales_tax_id: The sales-tax item used to calculate the actual tax amount for this invoice's
              transactions by applying a specific tax rate collected for a single tax agency.
              Unlike `salesTaxCode`, which only indicates general taxability, this field
              drives the actual tax calculation and reporting.

          link_to_transaction_ids: IDs of existing transactions that you wish to link to this invoice, such as
              payments applied, credits used, or associated purchase orders. Note that this
              links entire transactions, not individual transaction lines. If you want to link
              individual lines in a transaction, instead use the field `linkToTransactionLine`
              on this invoice's lines, if available.

              You can use both `linkToTransactionIds` (on this invoice) and
              `linkToTransactionLine` (on its transaction lines) as long as they do NOT link
              to the same transaction (otherwise, QuickBooks will return an error). QuickBooks
              will also return an error if you attempt to link a transaction that is empty or
              already closed.

              Note that QuickBooks will not return any information about these links in this
              endpoint's response even though they are created. To see the transactions linked
              via this field, refetch the invoice and check the `linkedTransactions` field. If
              fetching a list of invoices, you must also specify the parameter
              `includeLinkedTransactions` to return the `linkedTransactions` field.

          memo: A memo or note for this invoice, as entered by the user. This appears in
              reports, but not on the invoice. Use `customerMessage` to add a note to the
              invoice.

          other_custom_field: A built-in custom field for additional information specific to this invoice.
              Unlike the user-defined fields in the `customFields` array, this is a standard
              QuickBooks field that exists for all invoices for convenience. Developers often
              use this field for tracking information that doesn't fit into other standard
              QuickBooks fields. Unlike `otherCustomField1` and `otherCustomField2`, which are
              line item fields, this exists at the transaction level. Hidden by default in the
              QuickBooks UI.

          purchase_order_number: The customer's Purchase Order (PO) number associated with this invoice. This
              field is often used to cross-reference the invoice with the customer's
              purchasing system.

          ref_number: The case-sensitive user-defined reference number for this invoice, which can be
              used to identify the transaction in QuickBooks. This value is not required to be
              unique and can be arbitrarily changed by the QuickBooks user.

          sales_representative_id: The invoice's sales representative. Sales representatives can be employees,
              vendors, or other names in QuickBooks.

          sales_tax_code_id: The sales-tax code for items sold to the `customer` of this invoice, determining
              whether items sold to this customer are taxable or non-taxable. Default codes
              include "Non" (non-taxable) and "Tax" (taxable), but custom codes can also be
              created in QuickBooks. If QuickBooks is not set up to charge sales tax (via the
              "Do You Charge Sales Tax?" preference), it will assign the default non-taxable
              code to all sales.

          set_credits: Credits to apply to this invoice. Applying a credit uses an available credit to
              reduce the balance of this invoice. This creates a link between this invoice and
              the corresponding existing credit memo.

              Note that QuickBooks will not return any information about these links in this
              endpoint's response even though they are created. To see the transactions linked
              via this field, refetch the invoice and check the `linkedTransactions` field. If
              fetching a list of invoices, you must also specify the parameter
              `includeLinkedTransactions` to see the `linkedTransactions` field.

          shipping_address: The invoice's shipping address.

          shipping_date: The date when the products or services for this invoice were shipped or are
              expected to be shipped, in ISO 8601 format (YYYY-MM-DD).

          shipping_method_id: The shipping method used for this invoice, such as standard mail or overnight
              delivery.

          shipping_origin: The point of origin from where the product associated with this invoice is
              shipped. This is the point at which ownership and liability for goods transfer
              from seller to buyer. Internally, QuickBooks uses the term "FOB" for this field,
              which stands for "freight on board". This field is informational and has no
              accounting implications.

          terms_id: The invoice's payment terms, defining when payment is due and any applicable
              discounts.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            "/quickbooks-desktop/invoices",
            body=maybe_transform(
                {
                    "customer_id": customer_id,
                    "transaction_date": transaction_date,
                    "accounts_receivable_account_id": accounts_receivable_account_id,
                    "billing_address": billing_address,
                    "class_id": class_id,
                    "customer_message_id": customer_message_id,
                    "document_template_id": document_template_id,
                    "due_date": due_date,
                    "exchange_rate": exchange_rate,
                    "external_id": external_id,
                    "invoice_line_groups": invoice_line_groups,
                    "invoice_lines": invoice_lines,
                    "is_finance_charge": is_finance_charge,
                    "is_pending": is_pending,
                    "is_to_be_emailed": is_to_be_emailed,
                    "is_to_be_printed": is_to_be_printed,
                    "item_sales_tax_id": item_sales_tax_id,
                    "link_to_transaction_ids": link_to_transaction_ids,
                    "memo": memo,
                    "other_custom_field": other_custom_field,
                    "purchase_order_number": purchase_order_number,
                    "ref_number": ref_number,
                    "sales_representative_id": sales_representative_id,
                    "sales_tax_code_id": sales_tax_code_id,
                    "set_credits": set_credits,
                    "shipping_address": shipping_address,
                    "shipping_date": shipping_date,
                    "shipping_method_id": shipping_method_id,
                    "shipping_origin": shipping_origin,
                    "terms_id": terms_id,
                },
                invoice_create_params.InvoiceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QbdInvoice,
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
    ) -> QbdInvoice:
        """
        Retrieves an invoice by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the invoice to retrieve.

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
            f"/quickbooks-desktop/invoices/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QbdInvoice,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        account_ids: str | NotGiven = NOT_GIVEN,
        currency_ids: str | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        customer_ids: str | NotGiven = NOT_GIVEN,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorPage[QbdInvoice]:
        """
        Returns a list of invoices.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          account_ids: Filter for invoices from this account or accounts. Specify a single account ID
              or multiple using a comma-separated list (e.g., `accountIds=1,2,3`).

          currency_ids: Filter for invoices in this currency or currencies. Specify a single currency ID
              or multiple using a comma-separated list (e.g., `currencyIds=1,2,3`).

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Retrieve this value from the `nextCursor` field in the
              previous response. If omitted, the API returns the first page of results.

          customer_ids: Filter for invoices from this customer or customers. Specify a single customer
              ID or multiple using a comma-separated list (e.g., `customerIds=1,2,3`).

          ids: Filter for specific invoices by their QuickBooks-assigned unique identifier(s).
              Specify a single ID or multiple using a comma-separated list (e.g.,
              `ids=1,2,3`). NOTE: If you include this parameter, all other query parameters
              will be ignored.

          include_line_items: Whether to include line items in the response.

          include_linked_transactions: Whether to include linked transactions in the response. For example, a payment
              linked to the corresponding invoice.

          limit: The maximum number of objects to return, ranging from 1 to 500. Defaults to 500.
              Use this parameter in conjunction with the `cursor` parameter to paginate
              through results. The response will include a `nextCursor` field, which can be
              used as the `cursor` parameter value in subsequent requests to fetch the next
              set of results.

          payment_status: Filter for invoices that are paid, not paid, or both.

          ref_number_contains: Filter for invoices whose `refNumber` contains this substring. If you use this
              parameter, you cannot use `refNumberStartsWith` or `refNumberEndsWith`.

          ref_number_ends_with: Filter for invoices whose `refNumber` ends with this substring. If you use this
              parameter, you cannot use `refNumberContains` or `refNumberStartsWith`.

          ref_number_from: Filter for invoices whose `refNumber` is greater than or equal to this value. If
              omitted, the range will begin with the first number of the list. Uses a
              numerical comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          ref_numbers: Filter for specific invoices by their ref-number(s), case-sensitive. Specify a
              single ref-number or multiple using a comma-separated list (e.g.,
              `refNumbers=1,2,3`). In QuickBooks, ref-numbers are not required to be unique
              and can be arbitrarily changed by the QuickBooks user. NOTE: If you include this
              parameter, all other query parameters will be ignored.

          ref_number_starts_with: Filter for invoices whose `refNumber` starts with this substring. If you use
              this parameter, you cannot use `refNumberContains` or `refNumberEndsWith`.

          ref_number_to: Filter for invoices whose `refNumber` is less than or equal to this value. If
              omitted, the range will end with the last number of the list. Uses a numerical
              comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          transaction_date_from: Filter for invoices created on or after this date, in ISO 8601 format
              (YYYY-MM-DD).

          transaction_date_to: Filter for invoices created on or before this date, in ISO 8601 format
              (YYYY-MM-DD).

          updated_after: Filter for invoices updated on or after this date and time, in ISO 8601 format
              (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
              assumed to be 00:00:00 of that day.

          updated_before: Filter for invoices updated on or before this date and time, in ISO 8601 format
              (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
              assumed to be 23:59:59 of that day.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get_api_list(
            "/quickbooks-desktop/invoices",
            page=SyncCursorPage[QbdInvoice],
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
                        "customer_ids": customer_ids,
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
                    },
                    invoice_list_params.InvoiceListParams,
                ),
            ),
            model=QbdInvoice,
        )


class AsyncInvoicesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInvoicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInvoicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInvoicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return AsyncInvoicesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        customer_id: str,
        transaction_date: Union[str, date],
        conductor_end_user_id: str,
        accounts_receivable_account_id: str | NotGiven = NOT_GIVEN,
        billing_address: invoice_create_params.BillingAddress | NotGiven = NOT_GIVEN,
        class_id: str | NotGiven = NOT_GIVEN,
        customer_message_id: str | NotGiven = NOT_GIVEN,
        document_template_id: str | NotGiven = NOT_GIVEN,
        due_date: Union[str, date] | NotGiven = NOT_GIVEN,
        exchange_rate: float | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        invoice_line_groups: Iterable[invoice_create_params.InvoiceLineGroup] | NotGiven = NOT_GIVEN,
        invoice_lines: Iterable[invoice_create_params.InvoiceLine] | NotGiven = NOT_GIVEN,
        is_finance_charge: bool | NotGiven = NOT_GIVEN,
        is_pending: bool | NotGiven = NOT_GIVEN,
        is_to_be_emailed: bool | NotGiven = NOT_GIVEN,
        is_to_be_printed: bool | NotGiven = NOT_GIVEN,
        item_sales_tax_id: str | NotGiven = NOT_GIVEN,
        link_to_transaction_ids: List[str] | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        other_custom_field: str | NotGiven = NOT_GIVEN,
        purchase_order_number: str | NotGiven = NOT_GIVEN,
        ref_number: str | NotGiven = NOT_GIVEN,
        sales_representative_id: str | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        set_credits: Iterable[invoice_create_params.SetCredit] | NotGiven = NOT_GIVEN,
        shipping_address: invoice_create_params.ShippingAddress | NotGiven = NOT_GIVEN,
        shipping_date: Union[str, date] | NotGiven = NOT_GIVEN,
        shipping_method_id: str | NotGiven = NOT_GIVEN,
        shipping_origin: str | NotGiven = NOT_GIVEN,
        terms_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QbdInvoice:
        """
        Creates an invoice.

        Args:
          customer_id: The customer or customer-job associated with this invoice.

          transaction_date: The date of this invoice, in ISO 8601 format (YYYY-MM-DD).

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          accounts_receivable_account_id: The Accounts Receivable account to which this invoice is assigned, used to track
              the amount owed. If not specified, the default Accounts Receivable account in
              QuickBooks is used. If this invoice is linked to other transactions, make sure
              this `accountsReceivableAccount` matches the `accountsReceivableAccount` used in
              the other transactions.

          billing_address: The invoice's billing address.

          class_id: The invoice's class. Classes can be used to categorize objects into meaningful
              segments, such as department, location, or type of work. In QuickBooks, class
              tracking is off by default. A class defined here is automatically used in this
              invoice's line items unless overridden at the line item level.

          customer_message_id: The message to display to the customer on the invoice.

          document_template_id: The predefined template in QuickBooks that determines the layout and formatting
              for this invoice when printed or displayed.

          due_date: The date by which this invoice must be paid, in ISO 8601 format (YYYY-MM-DD).

          exchange_rate: The market exchange rate between this invoice's currency and the home currency
              in QuickBooks at the time of this transaction. Represented as a decimal value
              (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).

          external_id: A globally unique identifier (GUID) you can provide for tracking this object in
              your external system. Must be formatted as a valid GUID; otherwise, QuickBooks
              will return an error. This field is immutable and can only be set during object
              creation.

          invoice_line_groups: The invoice's line item groups. Each group represents a predefined set of
              related items.

          invoice_lines: The invoice's invoice lines, each representing a single product or service sold.

          is_finance_charge: Whether this invoice includes a finance charge.

          is_pending: Indicates whether this invoice is pending approval or completion. If `true`, the
              invoice is in a draft state and has not been finalized.

          is_to_be_emailed: Indicates whether this invoice is queued to be emailed to the customer. If set
              to `true`, the invoice will appear in the list of documents to be emailed in
              QuickBooks.

          is_to_be_printed: Indicates whether this invoice is queued for printing. If set to `true`, the
              invoice will appear in the list of documents to be printed in QuickBooks.

          item_sales_tax_id: The sales-tax item used to calculate the actual tax amount for this invoice's
              transactions by applying a specific tax rate collected for a single tax agency.
              Unlike `salesTaxCode`, which only indicates general taxability, this field
              drives the actual tax calculation and reporting.

          link_to_transaction_ids: IDs of existing transactions that you wish to link to this invoice, such as
              payments applied, credits used, or associated purchase orders. Note that this
              links entire transactions, not individual transaction lines. If you want to link
              individual lines in a transaction, instead use the field `linkToTransactionLine`
              on this invoice's lines, if available.

              You can use both `linkToTransactionIds` (on this invoice) and
              `linkToTransactionLine` (on its transaction lines) as long as they do NOT link
              to the same transaction (otherwise, QuickBooks will return an error). QuickBooks
              will also return an error if you attempt to link a transaction that is empty or
              already closed.

              Note that QuickBooks will not return any information about these links in this
              endpoint's response even though they are created. To see the transactions linked
              via this field, refetch the invoice and check the `linkedTransactions` field. If
              fetching a list of invoices, you must also specify the parameter
              `includeLinkedTransactions` to return the `linkedTransactions` field.

          memo: A memo or note for this invoice, as entered by the user. This appears in
              reports, but not on the invoice. Use `customerMessage` to add a note to the
              invoice.

          other_custom_field: A built-in custom field for additional information specific to this invoice.
              Unlike the user-defined fields in the `customFields` array, this is a standard
              QuickBooks field that exists for all invoices for convenience. Developers often
              use this field for tracking information that doesn't fit into other standard
              QuickBooks fields. Unlike `otherCustomField1` and `otherCustomField2`, which are
              line item fields, this exists at the transaction level. Hidden by default in the
              QuickBooks UI.

          purchase_order_number: The customer's Purchase Order (PO) number associated with this invoice. This
              field is often used to cross-reference the invoice with the customer's
              purchasing system.

          ref_number: The case-sensitive user-defined reference number for this invoice, which can be
              used to identify the transaction in QuickBooks. This value is not required to be
              unique and can be arbitrarily changed by the QuickBooks user.

          sales_representative_id: The invoice's sales representative. Sales representatives can be employees,
              vendors, or other names in QuickBooks.

          sales_tax_code_id: The sales-tax code for items sold to the `customer` of this invoice, determining
              whether items sold to this customer are taxable or non-taxable. Default codes
              include "Non" (non-taxable) and "Tax" (taxable), but custom codes can also be
              created in QuickBooks. If QuickBooks is not set up to charge sales tax (via the
              "Do You Charge Sales Tax?" preference), it will assign the default non-taxable
              code to all sales.

          set_credits: Credits to apply to this invoice. Applying a credit uses an available credit to
              reduce the balance of this invoice. This creates a link between this invoice and
              the corresponding existing credit memo.

              Note that QuickBooks will not return any information about these links in this
              endpoint's response even though they are created. To see the transactions linked
              via this field, refetch the invoice and check the `linkedTransactions` field. If
              fetching a list of invoices, you must also specify the parameter
              `includeLinkedTransactions` to see the `linkedTransactions` field.

          shipping_address: The invoice's shipping address.

          shipping_date: The date when the products or services for this invoice were shipped or are
              expected to be shipped, in ISO 8601 format (YYYY-MM-DD).

          shipping_method_id: The shipping method used for this invoice, such as standard mail or overnight
              delivery.

          shipping_origin: The point of origin from where the product associated with this invoice is
              shipped. This is the point at which ownership and liability for goods transfer
              from seller to buyer. Internally, QuickBooks uses the term "FOB" for this field,
              which stands for "freight on board". This field is informational and has no
              accounting implications.

          terms_id: The invoice's payment terms, defining when payment is due and any applicable
              discounts.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            "/quickbooks-desktop/invoices",
            body=await async_maybe_transform(
                {
                    "customer_id": customer_id,
                    "transaction_date": transaction_date,
                    "accounts_receivable_account_id": accounts_receivable_account_id,
                    "billing_address": billing_address,
                    "class_id": class_id,
                    "customer_message_id": customer_message_id,
                    "document_template_id": document_template_id,
                    "due_date": due_date,
                    "exchange_rate": exchange_rate,
                    "external_id": external_id,
                    "invoice_line_groups": invoice_line_groups,
                    "invoice_lines": invoice_lines,
                    "is_finance_charge": is_finance_charge,
                    "is_pending": is_pending,
                    "is_to_be_emailed": is_to_be_emailed,
                    "is_to_be_printed": is_to_be_printed,
                    "item_sales_tax_id": item_sales_tax_id,
                    "link_to_transaction_ids": link_to_transaction_ids,
                    "memo": memo,
                    "other_custom_field": other_custom_field,
                    "purchase_order_number": purchase_order_number,
                    "ref_number": ref_number,
                    "sales_representative_id": sales_representative_id,
                    "sales_tax_code_id": sales_tax_code_id,
                    "set_credits": set_credits,
                    "shipping_address": shipping_address,
                    "shipping_date": shipping_date,
                    "shipping_method_id": shipping_method_id,
                    "shipping_origin": shipping_origin,
                    "terms_id": terms_id,
                },
                invoice_create_params.InvoiceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QbdInvoice,
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
    ) -> QbdInvoice:
        """
        Retrieves an invoice by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the invoice to retrieve.

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
            f"/quickbooks-desktop/invoices/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QbdInvoice,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        account_ids: str | NotGiven = NOT_GIVEN,
        currency_ids: str | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        customer_ids: str | NotGiven = NOT_GIVEN,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[QbdInvoice, AsyncCursorPage[QbdInvoice]]:
        """
        Returns a list of invoices.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          account_ids: Filter for invoices from this account or accounts. Specify a single account ID
              or multiple using a comma-separated list (e.g., `accountIds=1,2,3`).

          currency_ids: Filter for invoices in this currency or currencies. Specify a single currency ID
              or multiple using a comma-separated list (e.g., `currencyIds=1,2,3`).

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Retrieve this value from the `nextCursor` field in the
              previous response. If omitted, the API returns the first page of results.

          customer_ids: Filter for invoices from this customer or customers. Specify a single customer
              ID or multiple using a comma-separated list (e.g., `customerIds=1,2,3`).

          ids: Filter for specific invoices by their QuickBooks-assigned unique identifier(s).
              Specify a single ID or multiple using a comma-separated list (e.g.,
              `ids=1,2,3`). NOTE: If you include this parameter, all other query parameters
              will be ignored.

          include_line_items: Whether to include line items in the response.

          include_linked_transactions: Whether to include linked transactions in the response. For example, a payment
              linked to the corresponding invoice.

          limit: The maximum number of objects to return, ranging from 1 to 500. Defaults to 500.
              Use this parameter in conjunction with the `cursor` parameter to paginate
              through results. The response will include a `nextCursor` field, which can be
              used as the `cursor` parameter value in subsequent requests to fetch the next
              set of results.

          payment_status: Filter for invoices that are paid, not paid, or both.

          ref_number_contains: Filter for invoices whose `refNumber` contains this substring. If you use this
              parameter, you cannot use `refNumberStartsWith` or `refNumberEndsWith`.

          ref_number_ends_with: Filter for invoices whose `refNumber` ends with this substring. If you use this
              parameter, you cannot use `refNumberContains` or `refNumberStartsWith`.

          ref_number_from: Filter for invoices whose `refNumber` is greater than or equal to this value. If
              omitted, the range will begin with the first number of the list. Uses a
              numerical comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          ref_numbers: Filter for specific invoices by their ref-number(s), case-sensitive. Specify a
              single ref-number or multiple using a comma-separated list (e.g.,
              `refNumbers=1,2,3`). In QuickBooks, ref-numbers are not required to be unique
              and can be arbitrarily changed by the QuickBooks user. NOTE: If you include this
              parameter, all other query parameters will be ignored.

          ref_number_starts_with: Filter for invoices whose `refNumber` starts with this substring. If you use
              this parameter, you cannot use `refNumberContains` or `refNumberEndsWith`.

          ref_number_to: Filter for invoices whose `refNumber` is less than or equal to this value. If
              omitted, the range will end with the last number of the list. Uses a numerical
              comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          transaction_date_from: Filter for invoices created on or after this date, in ISO 8601 format
              (YYYY-MM-DD).

          transaction_date_to: Filter for invoices created on or before this date, in ISO 8601 format
              (YYYY-MM-DD).

          updated_after: Filter for invoices updated on or after this date and time, in ISO 8601 format
              (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
              assumed to be 00:00:00 of that day.

          updated_before: Filter for invoices updated on or before this date and time, in ISO 8601 format
              (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
              assumed to be 23:59:59 of that day.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get_api_list(
            "/quickbooks-desktop/invoices",
            page=AsyncCursorPage[QbdInvoice],
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
                        "customer_ids": customer_ids,
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
                    },
                    invoice_list_params.InvoiceListParams,
                ),
            ),
            model=QbdInvoice,
        )


class InvoicesResourceWithRawResponse:
    def __init__(self, invoices: InvoicesResource) -> None:
        self._invoices = invoices

        self.create = to_raw_response_wrapper(
            invoices.create,
        )
        self.retrieve = to_raw_response_wrapper(
            invoices.retrieve,
        )
        self.list = to_raw_response_wrapper(
            invoices.list,
        )


class AsyncInvoicesResourceWithRawResponse:
    def __init__(self, invoices: AsyncInvoicesResource) -> None:
        self._invoices = invoices

        self.create = async_to_raw_response_wrapper(
            invoices.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            invoices.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            invoices.list,
        )


class InvoicesResourceWithStreamingResponse:
    def __init__(self, invoices: InvoicesResource) -> None:
        self._invoices = invoices

        self.create = to_streamed_response_wrapper(
            invoices.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            invoices.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            invoices.list,
        )


class AsyncInvoicesResourceWithStreamingResponse:
    def __init__(self, invoices: AsyncInvoicesResource) -> None:
        self._invoices = invoices

        self.create = async_to_streamed_response_wrapper(
            invoices.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            invoices.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            invoices.list,
        )
