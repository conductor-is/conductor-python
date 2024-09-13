# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
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
from ...types.qbd import customer_list_params, customer_create_params
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.qbd.qbd_customer import QbdCustomer

__all__ = ["CustomersResource", "AsyncCustomersResource"]


class CustomersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CustomersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return CustomersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return CustomersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        conductor_end_user_id: str,
        account_number: str | NotGiven = NOT_GIVEN,
        additional_contacts: Iterable[customer_create_params.AdditionalContact] | NotGiven = NOT_GIVEN,
        additional_notes: List[str] | NotGiven = NOT_GIVEN,
        alternate_contact: str | NotGiven = NOT_GIVEN,
        alternate_phone: str | NotGiven = NOT_GIVEN,
        billing_address: customer_create_params.BillingAddress | NotGiven = NOT_GIVEN,
        cc: str | NotGiven = NOT_GIVEN,
        class_id: str | NotGiven = NOT_GIVEN,
        company_name: str | NotGiven = NOT_GIVEN,
        contact: str | NotGiven = NOT_GIVEN,
        credit_card: customer_create_params.CreditCard | NotGiven = NOT_GIVEN,
        credit_limit: str | NotGiven = NOT_GIVEN,
        currency_id: str | NotGiven = NOT_GIVEN,
        custom_contact_fields: Iterable[customer_create_params.CustomContactField] | NotGiven = NOT_GIVEN,
        customer_type_id: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        fax: str | NotGiven = NOT_GIVEN,
        first_name: str | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        item_sales_tax_id: str | NotGiven = NOT_GIVEN,
        job_description: str | NotGiven = NOT_GIVEN,
        job_end_date: str | NotGiven = NOT_GIVEN,
        job_projected_end_date: str | NotGiven = NOT_GIVEN,
        job_start_date: str | NotGiven = NOT_GIVEN,
        job_status: Literal["Awarded", "Closed", "InProgress", "None", "NotAwarded", "Pending"] | NotGiven = NOT_GIVEN,
        job_title: str | NotGiven = NOT_GIVEN,
        job_type_id: str | NotGiven = NOT_GIVEN,
        last_name: str | NotGiven = NOT_GIVEN,
        middle_name: str | NotGiven = NOT_GIVEN,
        open_balance: str | NotGiven = NOT_GIVEN,
        open_balance_date: str | NotGiven = NOT_GIVEN,
        parent_id: str | NotGiven = NOT_GIVEN,
        phone: str | NotGiven = NOT_GIVEN,
        preferred_delivery_method: Literal["Email", "Fax", "None"] | NotGiven = NOT_GIVEN,
        preferred_payment_method_id: str | NotGiven = NOT_GIVEN,
        price_level_id: str | NotGiven = NOT_GIVEN,
        resale_number: str | NotGiven = NOT_GIVEN,
        sales_representative_id: str | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        sales_tax_country: Literal["Australia", "Canada", "UK", "US"] | NotGiven = NOT_GIVEN,
        salutation: str | NotGiven = NOT_GIVEN,
        shipping_address: customer_create_params.ShippingAddress | NotGiven = NOT_GIVEN,
        ship_to_addresses: Iterable[customer_create_params.ShipToAddress] | NotGiven = NOT_GIVEN,
        tax_registration_number: str | NotGiven = NOT_GIVEN,
        terms_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QbdCustomer:
        """
        Creates a customer.

        Args:
          name: The customer's case-insensitive unique name, unique across all customers.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          account_number: The customer's account number, which appears in the QuickBooks chart of
              accounts, account fields, reports, and graphs.

          additional_contacts: Additional contacts.

          additional_notes: Additional information about this customer.

          alternate_contact: The customer's alternate contact name.

          alternate_phone: The customer's alternate phone number.

          billing_address: The customer's billing address.

          cc: The customer's CC email address.

          class_id: The class associated with this object. Classes can be used to categorize objects
              or transactions by department, location, or other meaningful segments.

          company_name: The name of the customer's business. This is used on invoices, checks, and other
              forms.

          contact: The customer's contact name.

          credit_card: The customer's credit card information.

          credit_limit: The customer's credit limit. This is the maximum amount of money that the
              customer can spend before being billed. If undefined, there is no credit limit.

          currency_id: The ID of the customer's currency.

          custom_contact_fields: Additional custom contact fields.

          customer_type_id: The ID of the customer type, used for categorizing customers (e.g., by industry
              or region).

          email: The customer's email address.

          external_id: An arbitrary globally unique identifier (GUID) the developer can provide to
              track this object in their own system. This value must be formatted as a GUID;
              otherwise, QuickBooks will return an error.

          fax: The customer's fax number.

          first_name: The customer's first name.

          is_active: Whether this customer is active. QuickBooks hides inactive objects from most
              views and reports in the UI.

          item_sales_tax_id: The ID of the item sales tax, used to calculate a single sales tax that is
              collected at a specified rate and paid to a single agency.

          job_description: The description of the job, if this is a job (i.e., sub-customer).

          job_end_date: The actual end date of the job, if applicable.

          job_projected_end_date: The projected end date of the job, if applicable.

          job_start_date: The start date of the job, if applicable.

          job_title: The customer's job title.

          job_type_id: The ID of the job type, if this is a job (i.e., sub-customer).

          last_name: The customer's last name.

          middle_name: The customer's middle name.

          open_balance: The opening balance of this customer's account.

          open_balance_date: The date of the opening balance for this customer.

          parent_id: The ID of the parent customer or job.

          phone: The customer's phone number.

          preferred_payment_method_id: The ID of the customer's preferred payment method, if they have one.

          price_level_id: The ID of the custom price level for this customer. QuickBooks will
              automatically use the custom price in new invoices, sales receipts, sales
              orders, or credit memos for that customer. You can override this automatic
              feature, however, when you create the invoices, sales receipts, etc. Notice that
              the affected sales transactions do not list the price level, but instead list
              the rate for the item, which was set using the price level.

          resale_number: The customer's resale number, if they have one. This number will not affect
              reports or sales tax calculations.

          sales_representative_id: The ID of the customer's sales representative.

          sales_tax_code_id: The ID of the sales tax code, indicating whether related items are taxable or
              non-taxable.

          salutation: The customer's formal salutation that precedes their name.

          shipping_address: The customer's shipping address.

          ship_to_addresses: The customer's ship-to addresses.

          tax_registration_number: The tax registration number associated with this customer, for use in Canada or
              the UK.

          terms_id: The ID of the customer's payment terms.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            "/quickbooks-desktop/customers",
            body=maybe_transform(
                {
                    "name": name,
                    "account_number": account_number,
                    "additional_contacts": additional_contacts,
                    "additional_notes": additional_notes,
                    "alternate_contact": alternate_contact,
                    "alternate_phone": alternate_phone,
                    "billing_address": billing_address,
                    "cc": cc,
                    "class_id": class_id,
                    "company_name": company_name,
                    "contact": contact,
                    "credit_card": credit_card,
                    "credit_limit": credit_limit,
                    "currency_id": currency_id,
                    "custom_contact_fields": custom_contact_fields,
                    "customer_type_id": customer_type_id,
                    "email": email,
                    "external_id": external_id,
                    "fax": fax,
                    "first_name": first_name,
                    "is_active": is_active,
                    "item_sales_tax_id": item_sales_tax_id,
                    "job_description": job_description,
                    "job_end_date": job_end_date,
                    "job_projected_end_date": job_projected_end_date,
                    "job_start_date": job_start_date,
                    "job_status": job_status,
                    "job_title": job_title,
                    "job_type_id": job_type_id,
                    "last_name": last_name,
                    "middle_name": middle_name,
                    "open_balance": open_balance,
                    "open_balance_date": open_balance_date,
                    "parent_id": parent_id,
                    "phone": phone,
                    "preferred_delivery_method": preferred_delivery_method,
                    "preferred_payment_method_id": preferred_payment_method_id,
                    "price_level_id": price_level_id,
                    "resale_number": resale_number,
                    "sales_representative_id": sales_representative_id,
                    "sales_tax_code_id": sales_tax_code_id,
                    "sales_tax_country": sales_tax_country,
                    "salutation": salutation,
                    "shipping_address": shipping_address,
                    "ship_to_addresses": ship_to_addresses,
                    "tax_registration_number": tax_registration_number,
                    "terms_id": terms_id,
                },
                customer_create_params.CustomerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QbdCustomer,
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
    ) -> QbdCustomer:
        """
        Retrieves a customer by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the customer to retrieve.

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
            f"/quickbooks-desktop/customers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QbdCustomer,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        class_ids: str | NotGiven = NOT_GIVEN,
        currency_ids: str | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        full_names: str | NotGiven = NOT_GIVEN,
        ids: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name_contains: str | NotGiven = NOT_GIVEN,
        name_ends_with: str | NotGiven = NOT_GIVEN,
        name_from: str | NotGiven = NOT_GIVEN,
        name_starts_with: str | NotGiven = NOT_GIVEN,
        name_to: str | NotGiven = NOT_GIVEN,
        status: Literal["active", "all", "inactive"] | NotGiven = NOT_GIVEN,
        total_balance: str | NotGiven = NOT_GIVEN,
        total_balance_gt: str | NotGiven = NOT_GIVEN,
        total_balance_gte: str | NotGiven = NOT_GIVEN,
        total_balance_lt: str | NotGiven = NOT_GIVEN,
        total_balance_lte: str | NotGiven = NOT_GIVEN,
        updated_after: str | NotGiven = NOT_GIVEN,
        updated_before: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorPage[QbdCustomer]:
        """
        Returns a list of customers.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          class_ids: Filter for customers of this class or classes. Specify a single class ID or
              multiple using a comma-separated list (e.g., `classIds=1,2,3`). A class is a way
              end-users can categorize customers in QuickBooks.

          currency_ids: Filter for customers in this currency or currencies. Specify a single currency
              ID or multiple using a comma-separated list (e.g., `currencyIds=1,2,3`).

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Retrieve this value from the `nextCursor` field in the
              previous response. If omitted, the API returns the first page of results.

          full_names: Filter for specific customers by their full-name(s). Specify a single full-name
              or multiple using a comma-separated list (e.g., `fullNames=1,2,3`). Like `id`, a
              `fullName` is a unique identifier for a customer, and is formed by by combining
              the names of its parent objects with its own `name`, separated by colons. For
              example, if a customer is under 'ABC Corporation' and has the `name` 'Website
              Redesign Project', its `fullName` would be 'ABC Corporation:Website Redesign
              Project'. Unlike `name`, `fullName` is guaranteed to be unique across all
              customer objects. NOTE: If you include this parameter, all other query
              parameters will be ignored.

          ids: Filter for specific customers by their QuickBooks-assigned unique identifier(s).
              Specify a single ID or multiple using a comma-separated list (e.g.,
              `ids=1,2,3`). NOTE: If you include this parameter, all other query parameters
              will be ignored.

          limit: The maximum number of objects to return, ranging from 1 to 500. Defaults to 500.
              Use this parameter in conjunction with the `cursor` parameter to paginate
              through results. The response will include a `nextCursor` field, which can be
              used as the `cursor` parameter value in subsequent requests to fetch the next
              set of results.

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

          total_balance: Filter for customers whose `totalBalance` equals this amount. You can only use
              one total-balance filter at a time.

          total_balance_gt: Filter for customers whose `totalBalance` is greater than this amount. You can
              only use one total-balance filter at a time.

          total_balance_gte: Filter for customers whose `totalBalance` is greater than or equal to this
              amount. You can only use one total-balance filter at a time.

          total_balance_lt: Filter for customers whose `totalBalance` is less than this amount. You can only
              use one total-balance filter at a time.

          total_balance_lte: Filter for customers whose `totalBalance` is less than or equal to this amount.
              You can only use one total-balance filter at a time.

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
        return self._get_api_list(
            "/quickbooks-desktop/customers",
            page=SyncCursorPage[QbdCustomer],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "class_ids": class_ids,
                        "currency_ids": currency_ids,
                        "cursor": cursor,
                        "full_names": full_names,
                        "ids": ids,
                        "limit": limit,
                        "name_contains": name_contains,
                        "name_ends_with": name_ends_with,
                        "name_from": name_from,
                        "name_starts_with": name_starts_with,
                        "name_to": name_to,
                        "status": status,
                        "total_balance": total_balance,
                        "total_balance_gt": total_balance_gt,
                        "total_balance_gte": total_balance_gte,
                        "total_balance_lt": total_balance_lt,
                        "total_balance_lte": total_balance_lte,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                    },
                    customer_list_params.CustomerListParams,
                ),
            ),
            model=QbdCustomer,
        )


class AsyncCustomersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCustomersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCustomersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return AsyncCustomersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        conductor_end_user_id: str,
        account_number: str | NotGiven = NOT_GIVEN,
        additional_contacts: Iterable[customer_create_params.AdditionalContact] | NotGiven = NOT_GIVEN,
        additional_notes: List[str] | NotGiven = NOT_GIVEN,
        alternate_contact: str | NotGiven = NOT_GIVEN,
        alternate_phone: str | NotGiven = NOT_GIVEN,
        billing_address: customer_create_params.BillingAddress | NotGiven = NOT_GIVEN,
        cc: str | NotGiven = NOT_GIVEN,
        class_id: str | NotGiven = NOT_GIVEN,
        company_name: str | NotGiven = NOT_GIVEN,
        contact: str | NotGiven = NOT_GIVEN,
        credit_card: customer_create_params.CreditCard | NotGiven = NOT_GIVEN,
        credit_limit: str | NotGiven = NOT_GIVEN,
        currency_id: str | NotGiven = NOT_GIVEN,
        custom_contact_fields: Iterable[customer_create_params.CustomContactField] | NotGiven = NOT_GIVEN,
        customer_type_id: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        fax: str | NotGiven = NOT_GIVEN,
        first_name: str | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        item_sales_tax_id: str | NotGiven = NOT_GIVEN,
        job_description: str | NotGiven = NOT_GIVEN,
        job_end_date: str | NotGiven = NOT_GIVEN,
        job_projected_end_date: str | NotGiven = NOT_GIVEN,
        job_start_date: str | NotGiven = NOT_GIVEN,
        job_status: Literal["Awarded", "Closed", "InProgress", "None", "NotAwarded", "Pending"] | NotGiven = NOT_GIVEN,
        job_title: str | NotGiven = NOT_GIVEN,
        job_type_id: str | NotGiven = NOT_GIVEN,
        last_name: str | NotGiven = NOT_GIVEN,
        middle_name: str | NotGiven = NOT_GIVEN,
        open_balance: str | NotGiven = NOT_GIVEN,
        open_balance_date: str | NotGiven = NOT_GIVEN,
        parent_id: str | NotGiven = NOT_GIVEN,
        phone: str | NotGiven = NOT_GIVEN,
        preferred_delivery_method: Literal["Email", "Fax", "None"] | NotGiven = NOT_GIVEN,
        preferred_payment_method_id: str | NotGiven = NOT_GIVEN,
        price_level_id: str | NotGiven = NOT_GIVEN,
        resale_number: str | NotGiven = NOT_GIVEN,
        sales_representative_id: str | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        sales_tax_country: Literal["Australia", "Canada", "UK", "US"] | NotGiven = NOT_GIVEN,
        salutation: str | NotGiven = NOT_GIVEN,
        shipping_address: customer_create_params.ShippingAddress | NotGiven = NOT_GIVEN,
        ship_to_addresses: Iterable[customer_create_params.ShipToAddress] | NotGiven = NOT_GIVEN,
        tax_registration_number: str | NotGiven = NOT_GIVEN,
        terms_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QbdCustomer:
        """
        Creates a customer.

        Args:
          name: The customer's case-insensitive unique name, unique across all customers.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          account_number: The customer's account number, which appears in the QuickBooks chart of
              accounts, account fields, reports, and graphs.

          additional_contacts: Additional contacts.

          additional_notes: Additional information about this customer.

          alternate_contact: The customer's alternate contact name.

          alternate_phone: The customer's alternate phone number.

          billing_address: The customer's billing address.

          cc: The customer's CC email address.

          class_id: The class associated with this object. Classes can be used to categorize objects
              or transactions by department, location, or other meaningful segments.

          company_name: The name of the customer's business. This is used on invoices, checks, and other
              forms.

          contact: The customer's contact name.

          credit_card: The customer's credit card information.

          credit_limit: The customer's credit limit. This is the maximum amount of money that the
              customer can spend before being billed. If undefined, there is no credit limit.

          currency_id: The ID of the customer's currency.

          custom_contact_fields: Additional custom contact fields.

          customer_type_id: The ID of the customer type, used for categorizing customers (e.g., by industry
              or region).

          email: The customer's email address.

          external_id: An arbitrary globally unique identifier (GUID) the developer can provide to
              track this object in their own system. This value must be formatted as a GUID;
              otherwise, QuickBooks will return an error.

          fax: The customer's fax number.

          first_name: The customer's first name.

          is_active: Whether this customer is active. QuickBooks hides inactive objects from most
              views and reports in the UI.

          item_sales_tax_id: The ID of the item sales tax, used to calculate a single sales tax that is
              collected at a specified rate and paid to a single agency.

          job_description: The description of the job, if this is a job (i.e., sub-customer).

          job_end_date: The actual end date of the job, if applicable.

          job_projected_end_date: The projected end date of the job, if applicable.

          job_start_date: The start date of the job, if applicable.

          job_title: The customer's job title.

          job_type_id: The ID of the job type, if this is a job (i.e., sub-customer).

          last_name: The customer's last name.

          middle_name: The customer's middle name.

          open_balance: The opening balance of this customer's account.

          open_balance_date: The date of the opening balance for this customer.

          parent_id: The ID of the parent customer or job.

          phone: The customer's phone number.

          preferred_payment_method_id: The ID of the customer's preferred payment method, if they have one.

          price_level_id: The ID of the custom price level for this customer. QuickBooks will
              automatically use the custom price in new invoices, sales receipts, sales
              orders, or credit memos for that customer. You can override this automatic
              feature, however, when you create the invoices, sales receipts, etc. Notice that
              the affected sales transactions do not list the price level, but instead list
              the rate for the item, which was set using the price level.

          resale_number: The customer's resale number, if they have one. This number will not affect
              reports or sales tax calculations.

          sales_representative_id: The ID of the customer's sales representative.

          sales_tax_code_id: The ID of the sales tax code, indicating whether related items are taxable or
              non-taxable.

          salutation: The customer's formal salutation that precedes their name.

          shipping_address: The customer's shipping address.

          ship_to_addresses: The customer's ship-to addresses.

          tax_registration_number: The tax registration number associated with this customer, for use in Canada or
              the UK.

          terms_id: The ID of the customer's payment terms.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            "/quickbooks-desktop/customers",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "account_number": account_number,
                    "additional_contacts": additional_contacts,
                    "additional_notes": additional_notes,
                    "alternate_contact": alternate_contact,
                    "alternate_phone": alternate_phone,
                    "billing_address": billing_address,
                    "cc": cc,
                    "class_id": class_id,
                    "company_name": company_name,
                    "contact": contact,
                    "credit_card": credit_card,
                    "credit_limit": credit_limit,
                    "currency_id": currency_id,
                    "custom_contact_fields": custom_contact_fields,
                    "customer_type_id": customer_type_id,
                    "email": email,
                    "external_id": external_id,
                    "fax": fax,
                    "first_name": first_name,
                    "is_active": is_active,
                    "item_sales_tax_id": item_sales_tax_id,
                    "job_description": job_description,
                    "job_end_date": job_end_date,
                    "job_projected_end_date": job_projected_end_date,
                    "job_start_date": job_start_date,
                    "job_status": job_status,
                    "job_title": job_title,
                    "job_type_id": job_type_id,
                    "last_name": last_name,
                    "middle_name": middle_name,
                    "open_balance": open_balance,
                    "open_balance_date": open_balance_date,
                    "parent_id": parent_id,
                    "phone": phone,
                    "preferred_delivery_method": preferred_delivery_method,
                    "preferred_payment_method_id": preferred_payment_method_id,
                    "price_level_id": price_level_id,
                    "resale_number": resale_number,
                    "sales_representative_id": sales_representative_id,
                    "sales_tax_code_id": sales_tax_code_id,
                    "sales_tax_country": sales_tax_country,
                    "salutation": salutation,
                    "shipping_address": shipping_address,
                    "ship_to_addresses": ship_to_addresses,
                    "tax_registration_number": tax_registration_number,
                    "terms_id": terms_id,
                },
                customer_create_params.CustomerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QbdCustomer,
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
    ) -> QbdCustomer:
        """
        Retrieves a customer by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the customer to retrieve.

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
            f"/quickbooks-desktop/customers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QbdCustomer,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        class_ids: str | NotGiven = NOT_GIVEN,
        currency_ids: str | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        full_names: str | NotGiven = NOT_GIVEN,
        ids: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name_contains: str | NotGiven = NOT_GIVEN,
        name_ends_with: str | NotGiven = NOT_GIVEN,
        name_from: str | NotGiven = NOT_GIVEN,
        name_starts_with: str | NotGiven = NOT_GIVEN,
        name_to: str | NotGiven = NOT_GIVEN,
        status: Literal["active", "all", "inactive"] | NotGiven = NOT_GIVEN,
        total_balance: str | NotGiven = NOT_GIVEN,
        total_balance_gt: str | NotGiven = NOT_GIVEN,
        total_balance_gte: str | NotGiven = NOT_GIVEN,
        total_balance_lt: str | NotGiven = NOT_GIVEN,
        total_balance_lte: str | NotGiven = NOT_GIVEN,
        updated_after: str | NotGiven = NOT_GIVEN,
        updated_before: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[QbdCustomer, AsyncCursorPage[QbdCustomer]]:
        """
        Returns a list of customers.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          class_ids: Filter for customers of this class or classes. Specify a single class ID or
              multiple using a comma-separated list (e.g., `classIds=1,2,3`). A class is a way
              end-users can categorize customers in QuickBooks.

          currency_ids: Filter for customers in this currency or currencies. Specify a single currency
              ID or multiple using a comma-separated list (e.g., `currencyIds=1,2,3`).

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Retrieve this value from the `nextCursor` field in the
              previous response. If omitted, the API returns the first page of results.

          full_names: Filter for specific customers by their full-name(s). Specify a single full-name
              or multiple using a comma-separated list (e.g., `fullNames=1,2,3`). Like `id`, a
              `fullName` is a unique identifier for a customer, and is formed by by combining
              the names of its parent objects with its own `name`, separated by colons. For
              example, if a customer is under 'ABC Corporation' and has the `name` 'Website
              Redesign Project', its `fullName` would be 'ABC Corporation:Website Redesign
              Project'. Unlike `name`, `fullName` is guaranteed to be unique across all
              customer objects. NOTE: If you include this parameter, all other query
              parameters will be ignored.

          ids: Filter for specific customers by their QuickBooks-assigned unique identifier(s).
              Specify a single ID or multiple using a comma-separated list (e.g.,
              `ids=1,2,3`). NOTE: If you include this parameter, all other query parameters
              will be ignored.

          limit: The maximum number of objects to return, ranging from 1 to 500. Defaults to 500.
              Use this parameter in conjunction with the `cursor` parameter to paginate
              through results. The response will include a `nextCursor` field, which can be
              used as the `cursor` parameter value in subsequent requests to fetch the next
              set of results.

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

          total_balance: Filter for customers whose `totalBalance` equals this amount. You can only use
              one total-balance filter at a time.

          total_balance_gt: Filter for customers whose `totalBalance` is greater than this amount. You can
              only use one total-balance filter at a time.

          total_balance_gte: Filter for customers whose `totalBalance` is greater than or equal to this
              amount. You can only use one total-balance filter at a time.

          total_balance_lt: Filter for customers whose `totalBalance` is less than this amount. You can only
              use one total-balance filter at a time.

          total_balance_lte: Filter for customers whose `totalBalance` is less than or equal to this amount.
              You can only use one total-balance filter at a time.

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
        return self._get_api_list(
            "/quickbooks-desktop/customers",
            page=AsyncCursorPage[QbdCustomer],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "class_ids": class_ids,
                        "currency_ids": currency_ids,
                        "cursor": cursor,
                        "full_names": full_names,
                        "ids": ids,
                        "limit": limit,
                        "name_contains": name_contains,
                        "name_ends_with": name_ends_with,
                        "name_from": name_from,
                        "name_starts_with": name_starts_with,
                        "name_to": name_to,
                        "status": status,
                        "total_balance": total_balance,
                        "total_balance_gt": total_balance_gt,
                        "total_balance_gte": total_balance_gte,
                        "total_balance_lt": total_balance_lt,
                        "total_balance_lte": total_balance_lte,
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                    },
                    customer_list_params.CustomerListParams,
                ),
            ),
            model=QbdCustomer,
        )


class CustomersResourceWithRawResponse:
    def __init__(self, customers: CustomersResource) -> None:
        self._customers = customers

        self.create = to_raw_response_wrapper(
            customers.create,
        )
        self.retrieve = to_raw_response_wrapper(
            customers.retrieve,
        )
        self.list = to_raw_response_wrapper(
            customers.list,
        )


class AsyncCustomersResourceWithRawResponse:
    def __init__(self, customers: AsyncCustomersResource) -> None:
        self._customers = customers

        self.create = async_to_raw_response_wrapper(
            customers.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            customers.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            customers.list,
        )


class CustomersResourceWithStreamingResponse:
    def __init__(self, customers: CustomersResource) -> None:
        self._customers = customers

        self.create = to_streamed_response_wrapper(
            customers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            customers.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            customers.list,
        )


class AsyncCustomersResourceWithStreamingResponse:
    def __init__(self, customers: AsyncCustomersResource) -> None:
        self._customers = customers

        self.create = async_to_streamed_response_wrapper(
            customers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            customers.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            customers.list,
        )
