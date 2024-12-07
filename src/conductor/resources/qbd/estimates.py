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
from ...types.qbd import estimate_list_params, estimate_create_params, estimate_update_params
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.qbd.estimate import Estimate

__all__ = ["EstimatesResource", "AsyncEstimatesResource"]


class EstimatesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EstimatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return EstimatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EstimatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return EstimatesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        customer_id: str,
        transaction_date: Union[str, date],
        conductor_end_user_id: str,
        billing_address: estimate_create_params.BillingAddress | NotGiven = NOT_GIVEN,
        class_id: str | NotGiven = NOT_GIVEN,
        customer_message_id: str | NotGiven = NOT_GIVEN,
        document_template_id: str | NotGiven = NOT_GIVEN,
        due_date: Union[str, date] | NotGiven = NOT_GIVEN,
        exchange_rate: float | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        is_queued_for_email: bool | NotGiven = NOT_GIVEN,
        line_groups: Iterable[estimate_create_params.LineGroup] | NotGiven = NOT_GIVEN,
        lines: Iterable[estimate_create_params.Line] | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        other_custom_field: str | NotGiven = NOT_GIVEN,
        purchase_order_number: str | NotGiven = NOT_GIVEN,
        ref_number: str | NotGiven = NOT_GIVEN,
        sales_representative_id: str | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        sales_tax_item_id: str | NotGiven = NOT_GIVEN,
        shipment_origin: str | NotGiven = NOT_GIVEN,
        shipping_address: estimate_create_params.ShippingAddress | NotGiven = NOT_GIVEN,
        terms_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Estimate:
        """
        Creates a new estimate.

        Args:
          customer_id: The customer or customer-job associated with this estimate.

          transaction_date: The date of this estimate, in ISO 8601 format (YYYY-MM-DD).

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          billing_address: The estimate's billing address.

          class_id: The estimate's class. Classes can be used to categorize objects into meaningful
              segments, such as department, location, or type of work. In QuickBooks, class
              tracking is off by default. A class defined here is automatically used in this
              estimate's line items unless overridden at the line item level.

          customer_message_id: The message to display to the customer on the estimate.

          document_template_id: The predefined template in QuickBooks that determines the layout and formatting
              for this estimate when printed or displayed.

          due_date: The date by which this estimate must be paid, in ISO 8601 format (YYYY-MM-DD).

          exchange_rate: The market exchange rate between this estimate's currency and the home currency
              in QuickBooks at the time of this transaction. Represented as a decimal value
              (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).

          external_id: A globally unique identifier (GUID) you can provide for tracking this object in
              your external system.

              **IMPORTANT**: Must be formatted as a valid GUID; otherwise, QuickBooks will
              return an error. This field is immutable and can only be set during object
              creation.

          is_active: Indicates whether this estimate is active. Inactive objects are typically hidden
              from views and reports in QuickBooks.

          is_queued_for_email: Indicates whether this estimate is included in the queue of documents for
              QuickBooks to email to the customer.

          line_groups: The estimate's line item groups, each representing a predefined set of related
              items.

              **IMPORTANT**: You must specify `lines`, `lineGroups`, or both when creating an
              estimate.

          lines: The estimate's line items, each representing a single product or service quoted.

              **IMPORTANT**: You must specify `lines`, `lineGroups`, or both when creating an
              estimate.

          memo: A memo or note for this estimate that appears in reports, but not on the
              estimate. Use `customerMessage` to add a note to this estimate.

          other_custom_field: A built-in custom field for additional information specific to this estimate.
              Unlike the user-defined fields in the `customFields` array, this is a standard
              QuickBooks field that exists for all estimates for convenience. Developers often
              use this field for tracking information that doesn't fit into other standard
              QuickBooks fields. Unlike `otherCustomField1` and `otherCustomField2`, which are
              line item fields, this exists at the transaction level. Hidden by default in the
              QuickBooks UI.

          purchase_order_number: The customer's Purchase Order (PO) number associated with this estimate. This
              field is often used to cross-reference the estimate with the customer's
              purchasing system.

          ref_number: The case-sensitive user-defined reference number for this estimate, which can be
              used to identify the transaction in QuickBooks. This value is not required to be
              unique and can be arbitrarily changed by the QuickBooks user.

          sales_representative_id: The estimate's sales representative. Sales representatives can be employees,
              vendors, or other names in QuickBooks.

          sales_tax_code_id: The sales-tax code for items sold to the `customer` of this estimate,
              determining whether items sold to this customer are taxable or non-taxable.
              Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
              can also be created in QuickBooks. If QuickBooks is not set up to charge sales
              tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
              non-taxable code to all sales.

          sales_tax_item_id: The sales-tax item used to calculate the actual tax amount for this estimate's
              transactions by applying a specific tax rate collected for a single tax agency.
              Unlike `salesTaxCode`, which only indicates general taxability, this field
              drives the actual tax calculation and reporting.

          shipment_origin: The origin location from where the product associated with this estimate is
              shipped. This is the point at which ownership and liability for goods transfer
              from seller to buyer. Internally, QuickBooks uses the term "FOB" for this field,
              which stands for "freight on board". This field is informational and has no
              accounting implications.

          shipping_address: The estimate's shipping address.

          terms_id: The estimate's payment terms, defining when payment is due and any applicable
              discounts.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            "/quickbooks-desktop/estimates",
            body=maybe_transform(
                {
                    "customer_id": customer_id,
                    "transaction_date": transaction_date,
                    "billing_address": billing_address,
                    "class_id": class_id,
                    "customer_message_id": customer_message_id,
                    "document_template_id": document_template_id,
                    "due_date": due_date,
                    "exchange_rate": exchange_rate,
                    "external_id": external_id,
                    "is_active": is_active,
                    "is_queued_for_email": is_queued_for_email,
                    "line_groups": line_groups,
                    "lines": lines,
                    "memo": memo,
                    "other_custom_field": other_custom_field,
                    "purchase_order_number": purchase_order_number,
                    "ref_number": ref_number,
                    "sales_representative_id": sales_representative_id,
                    "sales_tax_code_id": sales_tax_code_id,
                    "sales_tax_item_id": sales_tax_item_id,
                    "shipment_origin": shipment_origin,
                    "shipping_address": shipping_address,
                    "terms_id": terms_id,
                },
                estimate_create_params.EstimateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Estimate,
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
    ) -> Estimate:
        """
        Retrieves an estimate by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the estimate to retrieve.

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
            f"/quickbooks-desktop/estimates/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Estimate,
        )

    def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        billing_address: estimate_update_params.BillingAddress | NotGiven = NOT_GIVEN,
        class_id: str | NotGiven = NOT_GIVEN,
        create_change_order: bool | NotGiven = NOT_GIVEN,
        customer_id: str | NotGiven = NOT_GIVEN,
        customer_message_id: str | NotGiven = NOT_GIVEN,
        document_template_id: str | NotGiven = NOT_GIVEN,
        due_date: Union[str, date] | NotGiven = NOT_GIVEN,
        exchange_rate: float | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        is_queued_for_email: bool | NotGiven = NOT_GIVEN,
        line_groups: Iterable[estimate_update_params.LineGroup] | NotGiven = NOT_GIVEN,
        lines: Iterable[estimate_update_params.Line] | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        other_custom_field: str | NotGiven = NOT_GIVEN,
        purchase_order_number: str | NotGiven = NOT_GIVEN,
        ref_number: str | NotGiven = NOT_GIVEN,
        sales_representative_id: str | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        sales_tax_item_id: str | NotGiven = NOT_GIVEN,
        shipment_origin: str | NotGiven = NOT_GIVEN,
        shipping_address: estimate_update_params.ShippingAddress | NotGiven = NOT_GIVEN,
        terms_id: str | NotGiven = NOT_GIVEN,
        transaction_date: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Estimate:
        """
        Updates an existing estimate.

        Args:
          id: The QuickBooks-assigned unique identifier of the estimate to update.

          revision_number: The current revision number of the estimate object you are updating, which you
              can get by fetching the object first. Provide the most recent `revisionNumber`
              to ensure you're working with the latest data; otherwise, the update will return
              an error.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          billing_address: The estimate's billing address.

          class_id: The estimate's class. Classes can be used to categorize objects into meaningful
              segments, such as department, location, or type of work. In QuickBooks, class
              tracking is off by default. A class defined here is automatically used in this
              estimate's line items unless overridden at the line item level.

          create_change_order: When `true`, creates a “change order” that appears in this estimate's
              description field in QuickBooks's estimate form, specifying exactly what changed
              in this update request, the dollar amount of each change, and the net dollar
              change to this estimate.

          customer_id: The customer or customer-job associated with this estimate.

          customer_message_id: The message to display to the customer on the estimate.

          document_template_id: The predefined template in QuickBooks that determines the layout and formatting
              for this estimate when printed or displayed.

          due_date: The date by which this estimate must be paid, in ISO 8601 format (YYYY-MM-DD).

          exchange_rate: The market exchange rate between this estimate's currency and the home currency
              in QuickBooks at the time of this transaction. Represented as a decimal value
              (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).

          is_active: Indicates whether this estimate is active. Inactive objects are typically hidden
              from views and reports in QuickBooks.

          is_queued_for_email: Indicates whether this estimate is included in the queue of documents for
              QuickBooks to email to the customer.

          line_groups: The estimate's line item groups, each representing a predefined set of related
              items.

              **IMPORTANT**: When updating an estimate's line item groups, this array
              completely REPLACES all existing line item groups for that estimate. To retain
              any current line item groups, include them in this array, even if they have not
              changed. Any line item groups not included will be removed. To add a new line
              item group, include it with its `id` set to `-1`. If you do not wish to modify
              the line item groups, you can omit this field entirely to keep them unchanged.

          lines: The estimate's line items, each representing a single product or service quoted.

              **IMPORTANT**: When updating an estimate's line items, this array completely
              REPLACES all existing line items for that estimate. To retain any current line
              items, include them in this array, even if they have not changed. Any line items
              not included will be removed. To add a new line item, include it with its `id`
              set to `-1`. If you do not wish to modify the line items, you can omit this
              field entirely to keep them unchanged.

          memo: A memo or note for this estimate that appears in reports, but not on the
              estimate. Use `customerMessage` to add a note to this estimate.

          other_custom_field: A built-in custom field for additional information specific to this estimate.
              Unlike the user-defined fields in the `customFields` array, this is a standard
              QuickBooks field that exists for all estimates for convenience. Developers often
              use this field for tracking information that doesn't fit into other standard
              QuickBooks fields. Unlike `otherCustomField1` and `otherCustomField2`, which are
              line item fields, this exists at the transaction level. Hidden by default in the
              QuickBooks UI.

          purchase_order_number: The customer's Purchase Order (PO) number associated with this estimate. This
              field is often used to cross-reference the estimate with the customer's
              purchasing system.

          ref_number: The case-sensitive user-defined reference number for this estimate, which can be
              used to identify the transaction in QuickBooks. This value is not required to be
              unique and can be arbitrarily changed by the QuickBooks user.

          sales_representative_id: The estimate's sales representative. Sales representatives can be employees,
              vendors, or other names in QuickBooks.

          sales_tax_code_id: The sales-tax code for items sold to the `customer` of this estimate,
              determining whether items sold to this customer are taxable or non-taxable.
              Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
              can also be created in QuickBooks. If QuickBooks is not set up to charge sales
              tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
              non-taxable code to all sales.

          sales_tax_item_id: The sales-tax item used to calculate the actual tax amount for this estimate's
              transactions by applying a specific tax rate collected for a single tax agency.
              Unlike `salesTaxCode`, which only indicates general taxability, this field
              drives the actual tax calculation and reporting.

          shipment_origin: The origin location from where the product associated with this estimate is
              shipped. This is the point at which ownership and liability for goods transfer
              from seller to buyer. Internally, QuickBooks uses the term "FOB" for this field,
              which stands for "freight on board". This field is informational and has no
              accounting implications.

          shipping_address: The estimate's shipping address.

          terms_id: The estimate's payment terms, defining when payment is due and any applicable
              discounts.

          transaction_date: The date of this estimate, in ISO 8601 format (YYYY-MM-DD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            f"/quickbooks-desktop/estimates/{id}",
            body=maybe_transform(
                {
                    "revision_number": revision_number,
                    "billing_address": billing_address,
                    "class_id": class_id,
                    "create_change_order": create_change_order,
                    "customer_id": customer_id,
                    "customer_message_id": customer_message_id,
                    "document_template_id": document_template_id,
                    "due_date": due_date,
                    "exchange_rate": exchange_rate,
                    "is_active": is_active,
                    "is_queued_for_email": is_queued_for_email,
                    "line_groups": line_groups,
                    "lines": lines,
                    "memo": memo,
                    "other_custom_field": other_custom_field,
                    "purchase_order_number": purchase_order_number,
                    "ref_number": ref_number,
                    "sales_representative_id": sales_representative_id,
                    "sales_tax_code_id": sales_tax_code_id,
                    "sales_tax_item_id": sales_tax_item_id,
                    "shipment_origin": shipment_origin,
                    "shipping_address": shipping_address,
                    "terms_id": terms_id,
                    "transaction_date": transaction_date,
                },
                estimate_update_params.EstimateUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Estimate,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        account_ids: List[str] | NotGiven = NOT_GIVEN,
        currency_ids: List[str] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        customer_ids: List[str] | NotGiven = NOT_GIVEN,
        ids: List[str] | NotGiven = NOT_GIVEN,
        include_line_items: bool | NotGiven = NOT_GIVEN,
        include_linked_transactions: bool | NotGiven = NOT_GIVEN,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorPage[Estimate]:
        """
        Returns a list of estimates.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          account_ids: Filter for estimates associated with these accounts.

          currency_ids: Filter for estimates in these currencies.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Retrieve this value from the `nextCursor` field in the
              previous response. If omitted, the API returns the first page of results.

          customer_ids: Filter for estimates created for these customers.

          ids: Filter for specific estimates by their QuickBooks-assigned unique identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

          include_line_items: Whether to include line items in the response. Defaults to `true`.

          include_linked_transactions: Whether to include linked transactions in the response. Defaults to `false`. For
              example, a payment linked to the corresponding estimate.

          limit: The maximum number of objects to return. Ranging from 1 to 150, defaults to 150.
              Use this parameter in conjunction with the `cursor` parameter to paginate
              through results. The response will include a `nextCursor` field, which can be
              used as the `cursor` parameter value in subsequent requests to fetch the next
              set of results.

          ref_number_contains: Filter for estimates whose `refNumber` contains this substring. NOTE: If you use
              this parameter, you cannot also use `refNumberStartsWith` or
              `refNumberEndsWith`.

          ref_number_ends_with: Filter for estimates whose `refNumber` ends with this substring. NOTE: If you
              use this parameter, you cannot also use `refNumberContains` or
              `refNumberStartsWith`.

          ref_number_from: Filter for estimates whose `refNumber` is greater than or equal to this value.
              If omitted, the range will begin with the first number of the list. Uses a
              numerical comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          ref_numbers: Filter for specific estimates by their ref-number(s), case-sensitive. In
              QuickBooks, ref-numbers are not required to be unique and can be arbitrarily
              changed by the QuickBooks user.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

          ref_number_starts_with: Filter for estimates whose `refNumber` starts with this substring. NOTE: If you
              use this parameter, you cannot also use `refNumberContains` or
              `refNumberEndsWith`.

          ref_number_to: Filter for estimates whose `refNumber` is less than or equal to this value. If
              omitted, the range will end with the last number of the list. Uses a numerical
              comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          transaction_date_from: Filter for estimates created on or after this date, in ISO 8601 format
              (YYYY-MM-DD).

          transaction_date_to: Filter for estimates created on or before this date, in ISO 8601 format
              (YYYY-MM-DD).

          updated_after: Filter for estimates updated on or after this date and time, in ISO 8601 format
              (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
              assumed to be 00:00:00 of that day.

          updated_before: Filter for estimates updated on or before this date and time, in ISO 8601 format
              (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
              assumed to be 23:59:59 of that day.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get_api_list(
            "/quickbooks-desktop/estimates",
            page=SyncCursorPage[Estimate],
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
                    estimate_list_params.EstimateListParams,
                ),
            ),
            model=Estimate,
        )


class AsyncEstimatesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEstimatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEstimatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEstimatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return AsyncEstimatesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        customer_id: str,
        transaction_date: Union[str, date],
        conductor_end_user_id: str,
        billing_address: estimate_create_params.BillingAddress | NotGiven = NOT_GIVEN,
        class_id: str | NotGiven = NOT_GIVEN,
        customer_message_id: str | NotGiven = NOT_GIVEN,
        document_template_id: str | NotGiven = NOT_GIVEN,
        due_date: Union[str, date] | NotGiven = NOT_GIVEN,
        exchange_rate: float | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        is_queued_for_email: bool | NotGiven = NOT_GIVEN,
        line_groups: Iterable[estimate_create_params.LineGroup] | NotGiven = NOT_GIVEN,
        lines: Iterable[estimate_create_params.Line] | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        other_custom_field: str | NotGiven = NOT_GIVEN,
        purchase_order_number: str | NotGiven = NOT_GIVEN,
        ref_number: str | NotGiven = NOT_GIVEN,
        sales_representative_id: str | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        sales_tax_item_id: str | NotGiven = NOT_GIVEN,
        shipment_origin: str | NotGiven = NOT_GIVEN,
        shipping_address: estimate_create_params.ShippingAddress | NotGiven = NOT_GIVEN,
        terms_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Estimate:
        """
        Creates a new estimate.

        Args:
          customer_id: The customer or customer-job associated with this estimate.

          transaction_date: The date of this estimate, in ISO 8601 format (YYYY-MM-DD).

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          billing_address: The estimate's billing address.

          class_id: The estimate's class. Classes can be used to categorize objects into meaningful
              segments, such as department, location, or type of work. In QuickBooks, class
              tracking is off by default. A class defined here is automatically used in this
              estimate's line items unless overridden at the line item level.

          customer_message_id: The message to display to the customer on the estimate.

          document_template_id: The predefined template in QuickBooks that determines the layout and formatting
              for this estimate when printed or displayed.

          due_date: The date by which this estimate must be paid, in ISO 8601 format (YYYY-MM-DD).

          exchange_rate: The market exchange rate between this estimate's currency and the home currency
              in QuickBooks at the time of this transaction. Represented as a decimal value
              (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).

          external_id: A globally unique identifier (GUID) you can provide for tracking this object in
              your external system.

              **IMPORTANT**: Must be formatted as a valid GUID; otherwise, QuickBooks will
              return an error. This field is immutable and can only be set during object
              creation.

          is_active: Indicates whether this estimate is active. Inactive objects are typically hidden
              from views and reports in QuickBooks.

          is_queued_for_email: Indicates whether this estimate is included in the queue of documents for
              QuickBooks to email to the customer.

          line_groups: The estimate's line item groups, each representing a predefined set of related
              items.

              **IMPORTANT**: You must specify `lines`, `lineGroups`, or both when creating an
              estimate.

          lines: The estimate's line items, each representing a single product or service quoted.

              **IMPORTANT**: You must specify `lines`, `lineGroups`, or both when creating an
              estimate.

          memo: A memo or note for this estimate that appears in reports, but not on the
              estimate. Use `customerMessage` to add a note to this estimate.

          other_custom_field: A built-in custom field for additional information specific to this estimate.
              Unlike the user-defined fields in the `customFields` array, this is a standard
              QuickBooks field that exists for all estimates for convenience. Developers often
              use this field for tracking information that doesn't fit into other standard
              QuickBooks fields. Unlike `otherCustomField1` and `otherCustomField2`, which are
              line item fields, this exists at the transaction level. Hidden by default in the
              QuickBooks UI.

          purchase_order_number: The customer's Purchase Order (PO) number associated with this estimate. This
              field is often used to cross-reference the estimate with the customer's
              purchasing system.

          ref_number: The case-sensitive user-defined reference number for this estimate, which can be
              used to identify the transaction in QuickBooks. This value is not required to be
              unique and can be arbitrarily changed by the QuickBooks user.

          sales_representative_id: The estimate's sales representative. Sales representatives can be employees,
              vendors, or other names in QuickBooks.

          sales_tax_code_id: The sales-tax code for items sold to the `customer` of this estimate,
              determining whether items sold to this customer are taxable or non-taxable.
              Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
              can also be created in QuickBooks. If QuickBooks is not set up to charge sales
              tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
              non-taxable code to all sales.

          sales_tax_item_id: The sales-tax item used to calculate the actual tax amount for this estimate's
              transactions by applying a specific tax rate collected for a single tax agency.
              Unlike `salesTaxCode`, which only indicates general taxability, this field
              drives the actual tax calculation and reporting.

          shipment_origin: The origin location from where the product associated with this estimate is
              shipped. This is the point at which ownership and liability for goods transfer
              from seller to buyer. Internally, QuickBooks uses the term "FOB" for this field,
              which stands for "freight on board". This field is informational and has no
              accounting implications.

          shipping_address: The estimate's shipping address.

          terms_id: The estimate's payment terms, defining when payment is due and any applicable
              discounts.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            "/quickbooks-desktop/estimates",
            body=await async_maybe_transform(
                {
                    "customer_id": customer_id,
                    "transaction_date": transaction_date,
                    "billing_address": billing_address,
                    "class_id": class_id,
                    "customer_message_id": customer_message_id,
                    "document_template_id": document_template_id,
                    "due_date": due_date,
                    "exchange_rate": exchange_rate,
                    "external_id": external_id,
                    "is_active": is_active,
                    "is_queued_for_email": is_queued_for_email,
                    "line_groups": line_groups,
                    "lines": lines,
                    "memo": memo,
                    "other_custom_field": other_custom_field,
                    "purchase_order_number": purchase_order_number,
                    "ref_number": ref_number,
                    "sales_representative_id": sales_representative_id,
                    "sales_tax_code_id": sales_tax_code_id,
                    "sales_tax_item_id": sales_tax_item_id,
                    "shipment_origin": shipment_origin,
                    "shipping_address": shipping_address,
                    "terms_id": terms_id,
                },
                estimate_create_params.EstimateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Estimate,
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
    ) -> Estimate:
        """
        Retrieves an estimate by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the estimate to retrieve.

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
            f"/quickbooks-desktop/estimates/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Estimate,
        )

    async def update(
        self,
        id: str,
        *,
        revision_number: str,
        conductor_end_user_id: str,
        billing_address: estimate_update_params.BillingAddress | NotGiven = NOT_GIVEN,
        class_id: str | NotGiven = NOT_GIVEN,
        create_change_order: bool | NotGiven = NOT_GIVEN,
        customer_id: str | NotGiven = NOT_GIVEN,
        customer_message_id: str | NotGiven = NOT_GIVEN,
        document_template_id: str | NotGiven = NOT_GIVEN,
        due_date: Union[str, date] | NotGiven = NOT_GIVEN,
        exchange_rate: float | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        is_queued_for_email: bool | NotGiven = NOT_GIVEN,
        line_groups: Iterable[estimate_update_params.LineGroup] | NotGiven = NOT_GIVEN,
        lines: Iterable[estimate_update_params.Line] | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        other_custom_field: str | NotGiven = NOT_GIVEN,
        purchase_order_number: str | NotGiven = NOT_GIVEN,
        ref_number: str | NotGiven = NOT_GIVEN,
        sales_representative_id: str | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        sales_tax_item_id: str | NotGiven = NOT_GIVEN,
        shipment_origin: str | NotGiven = NOT_GIVEN,
        shipping_address: estimate_update_params.ShippingAddress | NotGiven = NOT_GIVEN,
        terms_id: str | NotGiven = NOT_GIVEN,
        transaction_date: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Estimate:
        """
        Updates an existing estimate.

        Args:
          id: The QuickBooks-assigned unique identifier of the estimate to update.

          revision_number: The current revision number of the estimate object you are updating, which you
              can get by fetching the object first. Provide the most recent `revisionNumber`
              to ensure you're working with the latest data; otherwise, the update will return
              an error.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          billing_address: The estimate's billing address.

          class_id: The estimate's class. Classes can be used to categorize objects into meaningful
              segments, such as department, location, or type of work. In QuickBooks, class
              tracking is off by default. A class defined here is automatically used in this
              estimate's line items unless overridden at the line item level.

          create_change_order: When `true`, creates a “change order” that appears in this estimate's
              description field in QuickBooks's estimate form, specifying exactly what changed
              in this update request, the dollar amount of each change, and the net dollar
              change to this estimate.

          customer_id: The customer or customer-job associated with this estimate.

          customer_message_id: The message to display to the customer on the estimate.

          document_template_id: The predefined template in QuickBooks that determines the layout and formatting
              for this estimate when printed or displayed.

          due_date: The date by which this estimate must be paid, in ISO 8601 format (YYYY-MM-DD).

          exchange_rate: The market exchange rate between this estimate's currency and the home currency
              in QuickBooks at the time of this transaction. Represented as a decimal value
              (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).

          is_active: Indicates whether this estimate is active. Inactive objects are typically hidden
              from views and reports in QuickBooks.

          is_queued_for_email: Indicates whether this estimate is included in the queue of documents for
              QuickBooks to email to the customer.

          line_groups: The estimate's line item groups, each representing a predefined set of related
              items.

              **IMPORTANT**: When updating an estimate's line item groups, this array
              completely REPLACES all existing line item groups for that estimate. To retain
              any current line item groups, include them in this array, even if they have not
              changed. Any line item groups not included will be removed. To add a new line
              item group, include it with its `id` set to `-1`. If you do not wish to modify
              the line item groups, you can omit this field entirely to keep them unchanged.

          lines: The estimate's line items, each representing a single product or service quoted.

              **IMPORTANT**: When updating an estimate's line items, this array completely
              REPLACES all existing line items for that estimate. To retain any current line
              items, include them in this array, even if they have not changed. Any line items
              not included will be removed. To add a new line item, include it with its `id`
              set to `-1`. If you do not wish to modify the line items, you can omit this
              field entirely to keep them unchanged.

          memo: A memo or note for this estimate that appears in reports, but not on the
              estimate. Use `customerMessage` to add a note to this estimate.

          other_custom_field: A built-in custom field for additional information specific to this estimate.
              Unlike the user-defined fields in the `customFields` array, this is a standard
              QuickBooks field that exists for all estimates for convenience. Developers often
              use this field for tracking information that doesn't fit into other standard
              QuickBooks fields. Unlike `otherCustomField1` and `otherCustomField2`, which are
              line item fields, this exists at the transaction level. Hidden by default in the
              QuickBooks UI.

          purchase_order_number: The customer's Purchase Order (PO) number associated with this estimate. This
              field is often used to cross-reference the estimate with the customer's
              purchasing system.

          ref_number: The case-sensitive user-defined reference number for this estimate, which can be
              used to identify the transaction in QuickBooks. This value is not required to be
              unique and can be arbitrarily changed by the QuickBooks user.

          sales_representative_id: The estimate's sales representative. Sales representatives can be employees,
              vendors, or other names in QuickBooks.

          sales_tax_code_id: The sales-tax code for items sold to the `customer` of this estimate,
              determining whether items sold to this customer are taxable or non-taxable.
              Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
              can also be created in QuickBooks. If QuickBooks is not set up to charge sales
              tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
              non-taxable code to all sales.

          sales_tax_item_id: The sales-tax item used to calculate the actual tax amount for this estimate's
              transactions by applying a specific tax rate collected for a single tax agency.
              Unlike `salesTaxCode`, which only indicates general taxability, this field
              drives the actual tax calculation and reporting.

          shipment_origin: The origin location from where the product associated with this estimate is
              shipped. This is the point at which ownership and liability for goods transfer
              from seller to buyer. Internally, QuickBooks uses the term "FOB" for this field,
              which stands for "freight on board". This field is informational and has no
              accounting implications.

          shipping_address: The estimate's shipping address.

          terms_id: The estimate's payment terms, defining when payment is due and any applicable
              discounts.

          transaction_date: The date of this estimate, in ISO 8601 format (YYYY-MM-DD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            f"/quickbooks-desktop/estimates/{id}",
            body=await async_maybe_transform(
                {
                    "revision_number": revision_number,
                    "billing_address": billing_address,
                    "class_id": class_id,
                    "create_change_order": create_change_order,
                    "customer_id": customer_id,
                    "customer_message_id": customer_message_id,
                    "document_template_id": document_template_id,
                    "due_date": due_date,
                    "exchange_rate": exchange_rate,
                    "is_active": is_active,
                    "is_queued_for_email": is_queued_for_email,
                    "line_groups": line_groups,
                    "lines": lines,
                    "memo": memo,
                    "other_custom_field": other_custom_field,
                    "purchase_order_number": purchase_order_number,
                    "ref_number": ref_number,
                    "sales_representative_id": sales_representative_id,
                    "sales_tax_code_id": sales_tax_code_id,
                    "sales_tax_item_id": sales_tax_item_id,
                    "shipment_origin": shipment_origin,
                    "shipping_address": shipping_address,
                    "terms_id": terms_id,
                    "transaction_date": transaction_date,
                },
                estimate_update_params.EstimateUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Estimate,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        account_ids: List[str] | NotGiven = NOT_GIVEN,
        currency_ids: List[str] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        customer_ids: List[str] | NotGiven = NOT_GIVEN,
        ids: List[str] | NotGiven = NOT_GIVEN,
        include_line_items: bool | NotGiven = NOT_GIVEN,
        include_linked_transactions: bool | NotGiven = NOT_GIVEN,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Estimate, AsyncCursorPage[Estimate]]:
        """
        Returns a list of estimates.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          account_ids: Filter for estimates associated with these accounts.

          currency_ids: Filter for estimates in these currencies.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Retrieve this value from the `nextCursor` field in the
              previous response. If omitted, the API returns the first page of results.

          customer_ids: Filter for estimates created for these customers.

          ids: Filter for specific estimates by their QuickBooks-assigned unique identifier(s).

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

          include_line_items: Whether to include line items in the response. Defaults to `true`.

          include_linked_transactions: Whether to include linked transactions in the response. Defaults to `false`. For
              example, a payment linked to the corresponding estimate.

          limit: The maximum number of objects to return. Ranging from 1 to 150, defaults to 150.
              Use this parameter in conjunction with the `cursor` parameter to paginate
              through results. The response will include a `nextCursor` field, which can be
              used as the `cursor` parameter value in subsequent requests to fetch the next
              set of results.

          ref_number_contains: Filter for estimates whose `refNumber` contains this substring. NOTE: If you use
              this parameter, you cannot also use `refNumberStartsWith` or
              `refNumberEndsWith`.

          ref_number_ends_with: Filter for estimates whose `refNumber` ends with this substring. NOTE: If you
              use this parameter, you cannot also use `refNumberContains` or
              `refNumberStartsWith`.

          ref_number_from: Filter for estimates whose `refNumber` is greater than or equal to this value.
              If omitted, the range will begin with the first number of the list. Uses a
              numerical comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          ref_numbers: Filter for specific estimates by their ref-number(s), case-sensitive. In
              QuickBooks, ref-numbers are not required to be unique and can be arbitrarily
              changed by the QuickBooks user.

              **IMPORTANT**: If you include this parameter, QuickBooks will ignore all other
              query parameters for this request.

          ref_number_starts_with: Filter for estimates whose `refNumber` starts with this substring. NOTE: If you
              use this parameter, you cannot also use `refNumberContains` or
              `refNumberEndsWith`.

          ref_number_to: Filter for estimates whose `refNumber` is less than or equal to this value. If
              omitted, the range will end with the last number of the list. Uses a numerical
              comparison for values that contain only digits; otherwise, uses a
              lexicographical comparison.

          transaction_date_from: Filter for estimates created on or after this date, in ISO 8601 format
              (YYYY-MM-DD).

          transaction_date_to: Filter for estimates created on or before this date, in ISO 8601 format
              (YYYY-MM-DD).

          updated_after: Filter for estimates updated on or after this date and time, in ISO 8601 format
              (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
              assumed to be 00:00:00 of that day.

          updated_before: Filter for estimates updated on or before this date and time, in ISO 8601 format
              (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the time is
              assumed to be 23:59:59 of that day.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get_api_list(
            "/quickbooks-desktop/estimates",
            page=AsyncCursorPage[Estimate],
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
                    estimate_list_params.EstimateListParams,
                ),
            ),
            model=Estimate,
        )


class EstimatesResourceWithRawResponse:
    def __init__(self, estimates: EstimatesResource) -> None:
        self._estimates = estimates

        self.create = to_raw_response_wrapper(
            estimates.create,
        )
        self.retrieve = to_raw_response_wrapper(
            estimates.retrieve,
        )
        self.update = to_raw_response_wrapper(
            estimates.update,
        )
        self.list = to_raw_response_wrapper(
            estimates.list,
        )


class AsyncEstimatesResourceWithRawResponse:
    def __init__(self, estimates: AsyncEstimatesResource) -> None:
        self._estimates = estimates

        self.create = async_to_raw_response_wrapper(
            estimates.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            estimates.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            estimates.update,
        )
        self.list = async_to_raw_response_wrapper(
            estimates.list,
        )


class EstimatesResourceWithStreamingResponse:
    def __init__(self, estimates: EstimatesResource) -> None:
        self._estimates = estimates

        self.create = to_streamed_response_wrapper(
            estimates.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            estimates.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            estimates.update,
        )
        self.list = to_streamed_response_wrapper(
            estimates.list,
        )


class AsyncEstimatesResourceWithStreamingResponse:
    def __init__(self, estimates: AsyncEstimatesResource) -> None:
        self._estimates = estimates

        self.create = async_to_streamed_response_wrapper(
            estimates.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            estimates.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            estimates.update,
        )
        self.list = async_to_streamed_response_wrapper(
            estimates.list,
        )
