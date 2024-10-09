# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...types.qbd import service_item_list_params, service_item_create_params
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.qbd.service_item import ServiceItem

__all__ = ["ServiceItemsResource", "AsyncServiceItemsResource"]


class ServiceItemsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ServiceItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return ServiceItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ServiceItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return ServiceItemsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        conductor_end_user_id: str,
        barcode: service_item_create_params.Barcode | NotGiven = NOT_GIVEN,
        class_id: str | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        is_tax_included: bool | NotGiven = NOT_GIVEN,
        parent_id: str | NotGiven = NOT_GIVEN,
        sales_and_purchase_details: service_item_create_params.SalesAndPurchaseDetails | NotGiven = NOT_GIVEN,
        sales_or_purchase_details: service_item_create_params.SalesOrPurchaseDetails | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        unit_of_measure_set_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServiceItem:
        """
        Creates a service item.

        Args:
          name: The case-insensitive name of this service item. Not guaranteed to be unique
              because it does not include the names of its parent objects like `fullName`
              does. For example, two service items could both have the `name` "Web-Design",
              but they could have unique `fullName` values, such as "Consulting:Web-Design"
              and "Contracting:Web-Design".

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          barcode: The service item's barcode.

          class_id: The service item's class. Classes can be used to categorize objects into
              meaningful segments, such as department, location, or type of work. In
              QuickBooks, class tracking is off by default.

          external_id: A developer-assigned globally unique identifier (GUID) for tracking this object
              in external systems. Must be formatted as a valid GUID; otherwise, QuickBooks
              will return an error.

          is_active: Indicates whether this service item is active. Inactive objects are typically
              hidden from views and reports in QuickBooks.

          is_tax_included: Indicates whether the price of this service item includes tax. This is primarily
              used in international versions of QuickBooks.

          parent_id: The parent service item one level above this one in the hierarchy. For example,
              if this service item has a `fullName` of "Services:Consulting:Web-Design", its
              parent has a `fullName` of "Services:Consulting". If this service item is at the
              top level, `parent` will be `null`.

          sales_tax_code_id: The sales tax code associated with this service item, determining whether it is
              taxable or non-taxable. It's used to assign a default tax status to all
              transactions for this service item. Default codes include "NON" (non-taxable)
              and "TAX" (taxable), but custom codes can also be created in QuickBooks. If
              QuickBooks is not set up to charge sales tax, it will assign the default
              non-taxable code to all sales.

          unit_of_measure_set_id: The unit of measure set associated with this service item, which consists of a
              base unit and related units.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            "/quickbooks-desktop/service-items",
            body=maybe_transform(
                {
                    "name": name,
                    "barcode": barcode,
                    "class_id": class_id,
                    "external_id": external_id,
                    "is_active": is_active,
                    "is_tax_included": is_tax_included,
                    "parent_id": parent_id,
                    "sales_and_purchase_details": sales_and_purchase_details,
                    "sales_or_purchase_details": sales_or_purchase_details,
                    "sales_tax_code_id": sales_tax_code_id,
                    "unit_of_measure_set_id": unit_of_measure_set_id,
                },
                service_item_create_params.ServiceItemCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServiceItem,
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
    ) -> ServiceItem:
        """
        Retrieves a service item by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the service item to retrieve.

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
            f"/quickbooks-desktop/service-items/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServiceItem,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        class_ids: str | NotGiven = NOT_GIVEN,
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
        updated_after: str | NotGiven = NOT_GIVEN,
        updated_before: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorPage[ServiceItem]:
        """
        Returns a list of service items.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          class_ids: Filter for service items of this class or classes. Specify a single class ID or
              multiple using a comma-separated list (e.g., `classIds=1,2,3`). A class is a way
              end-users can categorize service items in QuickBooks.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Retrieve this value from the `nextCursor` field in the
              previous response. If omitted, the API returns the first page of results.

          full_names: Filter for specific service items by their full-name(s). Specify a single
              full-name or multiple using a comma-separated list (e.g., `fullNames=1,2,3`).
              Like `id`, a `fullName` is a unique identifier for a service item, and is formed
              by by combining the names of its parent objects with its own `name`, separated
              by colons. For example, if a service item is under "Professional Services" and
              has the `name` "Consulting", its `fullName` would be "Professional
              Services:Consulting". Unlike `name`, `fullName` is guaranteed to be unique
              across all service item objects. Not case-sensitive. NOTE: If you include this
              parameter, all other query parameters will be ignored.

          ids: Filter for specific service items by their QuickBooks-assigned unique
              identifier(s). Specify a single ID or multiple using a comma-separated list
              (e.g., `ids=1,2,3`). NOTE: If you include this parameter, all other query
              parameters will be ignored.

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
            "/quickbooks-desktop/service-items",
            page=SyncCursorPage[ServiceItem],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "class_ids": class_ids,
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
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                    },
                    service_item_list_params.ServiceItemListParams,
                ),
            ),
            model=ServiceItem,
        )


class AsyncServiceItemsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncServiceItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return AsyncServiceItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncServiceItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return AsyncServiceItemsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        conductor_end_user_id: str,
        barcode: service_item_create_params.Barcode | NotGiven = NOT_GIVEN,
        class_id: str | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        is_tax_included: bool | NotGiven = NOT_GIVEN,
        parent_id: str | NotGiven = NOT_GIVEN,
        sales_and_purchase_details: service_item_create_params.SalesAndPurchaseDetails | NotGiven = NOT_GIVEN,
        sales_or_purchase_details: service_item_create_params.SalesOrPurchaseDetails | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        unit_of_measure_set_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServiceItem:
        """
        Creates a service item.

        Args:
          name: The case-insensitive name of this service item. Not guaranteed to be unique
              because it does not include the names of its parent objects like `fullName`
              does. For example, two service items could both have the `name` "Web-Design",
              but they could have unique `fullName` values, such as "Consulting:Web-Design"
              and "Contracting:Web-Design".

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          barcode: The service item's barcode.

          class_id: The service item's class. Classes can be used to categorize objects into
              meaningful segments, such as department, location, or type of work. In
              QuickBooks, class tracking is off by default.

          external_id: A developer-assigned globally unique identifier (GUID) for tracking this object
              in external systems. Must be formatted as a valid GUID; otherwise, QuickBooks
              will return an error.

          is_active: Indicates whether this service item is active. Inactive objects are typically
              hidden from views and reports in QuickBooks.

          is_tax_included: Indicates whether the price of this service item includes tax. This is primarily
              used in international versions of QuickBooks.

          parent_id: The parent service item one level above this one in the hierarchy. For example,
              if this service item has a `fullName` of "Services:Consulting:Web-Design", its
              parent has a `fullName` of "Services:Consulting". If this service item is at the
              top level, `parent` will be `null`.

          sales_tax_code_id: The sales tax code associated with this service item, determining whether it is
              taxable or non-taxable. It's used to assign a default tax status to all
              transactions for this service item. Default codes include "NON" (non-taxable)
              and "TAX" (taxable), but custom codes can also be created in QuickBooks. If
              QuickBooks is not set up to charge sales tax, it will assign the default
              non-taxable code to all sales.

          unit_of_measure_set_id: The unit of measure set associated with this service item, which consists of a
              base unit and related units.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            "/quickbooks-desktop/service-items",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "barcode": barcode,
                    "class_id": class_id,
                    "external_id": external_id,
                    "is_active": is_active,
                    "is_tax_included": is_tax_included,
                    "parent_id": parent_id,
                    "sales_and_purchase_details": sales_and_purchase_details,
                    "sales_or_purchase_details": sales_or_purchase_details,
                    "sales_tax_code_id": sales_tax_code_id,
                    "unit_of_measure_set_id": unit_of_measure_set_id,
                },
                service_item_create_params.ServiceItemCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServiceItem,
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
    ) -> ServiceItem:
        """
        Retrieves a service item by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the service item to retrieve.

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
            f"/quickbooks-desktop/service-items/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServiceItem,
        )

    def list(
        self,
        *,
        conductor_end_user_id: str,
        class_ids: str | NotGiven = NOT_GIVEN,
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
        updated_after: str | NotGiven = NOT_GIVEN,
        updated_before: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[ServiceItem, AsyncCursorPage[ServiceItem]]:
        """
        Returns a list of service items.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          class_ids: Filter for service items of this class or classes. Specify a single class ID or
              multiple using a comma-separated list (e.g., `classIds=1,2,3`). A class is a way
              end-users can categorize service items in QuickBooks.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Retrieve this value from the `nextCursor` field in the
              previous response. If omitted, the API returns the first page of results.

          full_names: Filter for specific service items by their full-name(s). Specify a single
              full-name or multiple using a comma-separated list (e.g., `fullNames=1,2,3`).
              Like `id`, a `fullName` is a unique identifier for a service item, and is formed
              by by combining the names of its parent objects with its own `name`, separated
              by colons. For example, if a service item is under "Professional Services" and
              has the `name` "Consulting", its `fullName` would be "Professional
              Services:Consulting". Unlike `name`, `fullName` is guaranteed to be unique
              across all service item objects. Not case-sensitive. NOTE: If you include this
              parameter, all other query parameters will be ignored.

          ids: Filter for specific service items by their QuickBooks-assigned unique
              identifier(s). Specify a single ID or multiple using a comma-separated list
              (e.g., `ids=1,2,3`). NOTE: If you include this parameter, all other query
              parameters will be ignored.

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
            "/quickbooks-desktop/service-items",
            page=AsyncCursorPage[ServiceItem],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "class_ids": class_ids,
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
                        "updated_after": updated_after,
                        "updated_before": updated_before,
                    },
                    service_item_list_params.ServiceItemListParams,
                ),
            ),
            model=ServiceItem,
        )


class ServiceItemsResourceWithRawResponse:
    def __init__(self, service_items: ServiceItemsResource) -> None:
        self._service_items = service_items

        self.create = to_raw_response_wrapper(
            service_items.create,
        )
        self.retrieve = to_raw_response_wrapper(
            service_items.retrieve,
        )
        self.list = to_raw_response_wrapper(
            service_items.list,
        )


class AsyncServiceItemsResourceWithRawResponse:
    def __init__(self, service_items: AsyncServiceItemsResource) -> None:
        self._service_items = service_items

        self.create = async_to_raw_response_wrapper(
            service_items.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            service_items.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            service_items.list,
        )


class ServiceItemsResourceWithStreamingResponse:
    def __init__(self, service_items: ServiceItemsResource) -> None:
        self._service_items = service_items

        self.create = to_streamed_response_wrapper(
            service_items.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            service_items.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            service_items.list,
        )


class AsyncServiceItemsResourceWithStreamingResponse:
    def __init__(self, service_items: AsyncServiceItemsResource) -> None:
        self._service_items = service_items

        self.create = async_to_streamed_response_wrapper(
            service_items.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            service_items.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            service_items.list,
        )
