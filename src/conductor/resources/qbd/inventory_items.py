# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.qbd import inventory_item_list_params
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.qbd.inventory_item import InventoryItem

__all__ = ["InventoryItemsResource", "AsyncInventoryItemsResource"]


class InventoryItemsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InventoryItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return InventoryItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InventoryItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return InventoryItemsResourceWithStreamingResponse(self)

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
    ) -> InventoryItem:
        """
        Retrieves an inventory-item by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the inventory-item to retrieve.

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
            f"/quickbooks-desktop/inventory-items/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InventoryItem,
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
    ) -> SyncCursorPage[InventoryItem]:
        """
        Returns a list of inventory-items.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          class_ids: Filter for inventory-items of this class or classes. Specify a single class ID
              or multiple using a comma-separated list (e.g., `classIds=1,2,3`). A class is a
              way end-users can categorize inventory-items in QuickBooks.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Retrieve this value from the `nextCursor` field in the
              previous response. If omitted, the API returns the first page of results.

          full_names: Filter for specific inventory-items by their full-name(s). Specify a single
              full-name or multiple using a comma-separated list (e.g., `fullNames=1,2,3`).
              Like `id`, a `fullName` is a unique identifier for an inventory-item, and is
              formed by by combining the names of its parent objects with its own `name`,
              separated by colons. For example, if an inventory-item is under
              'Furniture:Kitchen' and has the `name` 'Cabinet', its `fullName` would be
              'Furniture:Kitchen:Cabinet'. Unlike `name`, `fullName` is guaranteed to be
              unique across all inventory-item objects. NOTE: If you include this parameter,
              all other query parameters will be ignored.

          ids: Filter for specific inventory-items by their QuickBooks-assigned unique
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
            "/quickbooks-desktop/inventory-items",
            page=SyncCursorPage[InventoryItem],
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
                    inventory_item_list_params.InventoryItemListParams,
                ),
            ),
            model=InventoryItem,
        )


class AsyncInventoryItemsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInventoryItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInventoryItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInventoryItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return AsyncInventoryItemsResourceWithStreamingResponse(self)

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
    ) -> InventoryItem:
        """
        Retrieves an inventory-item by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the inventory-item to retrieve.

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
            f"/quickbooks-desktop/inventory-items/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InventoryItem,
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
    ) -> AsyncPaginator[InventoryItem, AsyncCursorPage[InventoryItem]]:
        """
        Returns a list of inventory-items.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          class_ids: Filter for inventory-items of this class or classes. Specify a single class ID
              or multiple using a comma-separated list (e.g., `classIds=1,2,3`). A class is a
              way end-users can categorize inventory-items in QuickBooks.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Retrieve this value from the `nextCursor` field in the
              previous response. If omitted, the API returns the first page of results.

          full_names: Filter for specific inventory-items by their full-name(s). Specify a single
              full-name or multiple using a comma-separated list (e.g., `fullNames=1,2,3`).
              Like `id`, a `fullName` is a unique identifier for an inventory-item, and is
              formed by by combining the names of its parent objects with its own `name`,
              separated by colons. For example, if an inventory-item is under
              'Furniture:Kitchen' and has the `name` 'Cabinet', its `fullName` would be
              'Furniture:Kitchen:Cabinet'. Unlike `name`, `fullName` is guaranteed to be
              unique across all inventory-item objects. NOTE: If you include this parameter,
              all other query parameters will be ignored.

          ids: Filter for specific inventory-items by their QuickBooks-assigned unique
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
            "/quickbooks-desktop/inventory-items",
            page=AsyncCursorPage[InventoryItem],
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
                    inventory_item_list_params.InventoryItemListParams,
                ),
            ),
            model=InventoryItem,
        )


class InventoryItemsResourceWithRawResponse:
    def __init__(self, inventory_items: InventoryItemsResource) -> None:
        self._inventory_items = inventory_items

        self.retrieve = to_raw_response_wrapper(
            inventory_items.retrieve,
        )
        self.list = to_raw_response_wrapper(
            inventory_items.list,
        )


class AsyncInventoryItemsResourceWithRawResponse:
    def __init__(self, inventory_items: AsyncInventoryItemsResource) -> None:
        self._inventory_items = inventory_items

        self.retrieve = async_to_raw_response_wrapper(
            inventory_items.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            inventory_items.list,
        )


class InventoryItemsResourceWithStreamingResponse:
    def __init__(self, inventory_items: InventoryItemsResource) -> None:
        self._inventory_items = inventory_items

        self.retrieve = to_streamed_response_wrapper(
            inventory_items.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            inventory_items.list,
        )


class AsyncInventoryItemsResourceWithStreamingResponse:
    def __init__(self, inventory_items: AsyncInventoryItemsResource) -> None:
        self._inventory_items = inventory_items

        self.retrieve = async_to_streamed_response_wrapper(
            inventory_items.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            inventory_items.list,
        )
