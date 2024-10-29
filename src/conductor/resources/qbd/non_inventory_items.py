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
from ...types.qbd import (
    non_inventory_item_list_params,
    non_inventory_item_create_params,
    non_inventory_item_update_params,
)
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.qbd.non_inventory_item import NonInventoryItem

__all__ = ["NonInventoryItemsResource", "AsyncNonInventoryItemsResource"]


class NonInventoryItemsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NonInventoryItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return NonInventoryItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NonInventoryItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return NonInventoryItemsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        conductor_end_user_id: str,
        barcode: non_inventory_item_create_params.Barcode | NotGiven = NOT_GIVEN,
        class_id: str | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        manufacturer_part_number: str | NotGiven = NOT_GIVEN,
        parent_id: str | NotGiven = NOT_GIVEN,
        sales_and_purchase_details: non_inventory_item_create_params.SalesAndPurchaseDetails | NotGiven = NOT_GIVEN,
        sales_or_purchase_details: non_inventory_item_create_params.SalesOrPurchaseDetails | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        unit_of_measure_set_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NonInventoryItem:
        """
        Creates a non-inventory item.

        Args:
          name: The case-insensitive name of this non-inventory item. Not guaranteed to be
              unique because it does not include the names of its parent objects like
              `fullName` does. For example, two non-inventory items could both have the `name`
              "Printer Ink Cartridge", but they could have unique `fullName` values, such as
              "Office-Supplies:Printer Ink Cartridge" and "Miscellaneous:Printer Ink
              Cartridge".

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          barcode: The non-inventory item's barcode.

          class_id: The non-inventory item's class. Classes can be used to categorize objects into
              meaningful segments, such as department, location, or type of work. In
              QuickBooks, class tracking is off by default.

          external_id: A globally unique identifier (GUID) you can provide for tracking this object in
              your external system. Must be formatted as a valid GUID; otherwise, QuickBooks
              will return an error. This field is immutable and can only be set during object
              creation.

          is_active: Indicates whether this non-inventory item is active. Inactive objects are
              typically hidden from views and reports in QuickBooks.

          manufacturer_part_number: The manufacturer's part number for this non-inventory item, which is often the
              stock keeping unit (SKU).

          parent_id: The parent non-inventory item one level above this one in the hierarchy. For
              example, if this non-inventory item has a `fullName` of "Office-Supplies:Printer
              Ink Cartridge", its parent has a `fullName` of "Office-Supplies". If this
              non-inventory item is at the top level, this field will be `null`.

          sales_tax_code_id: The sales-tax code associated with this non-inventory item, determining whether
              it is taxable or non-taxable. It's used to assign a default tax status to all
              transactions for this non-inventory item. Default codes include "Non"
              (non-taxable) and "Tax" (taxable), but custom codes can also be created in
              QuickBooks. If QuickBooks is not set up to charge sales tax (via the "Do You
              Charge Sales Tax?" preference), it will assign the default non-taxable code to
              all sales.

          unit_of_measure_set_id: The unit of measure set associated with this non-inventory item, which consists
              of a base unit and related units.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            "/quickbooks-desktop/non-inventory-items",
            body=maybe_transform(
                {
                    "name": name,
                    "barcode": barcode,
                    "class_id": class_id,
                    "external_id": external_id,
                    "is_active": is_active,
                    "manufacturer_part_number": manufacturer_part_number,
                    "parent_id": parent_id,
                    "sales_and_purchase_details": sales_and_purchase_details,
                    "sales_or_purchase_details": sales_or_purchase_details,
                    "sales_tax_code_id": sales_tax_code_id,
                    "unit_of_measure_set_id": unit_of_measure_set_id,
                },
                non_inventory_item_create_params.NonInventoryItemCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NonInventoryItem,
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
    ) -> NonInventoryItem:
        """
        Retrieves a non-inventory item by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the non-inventory item to retrieve.

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
            f"/quickbooks-desktop/non-inventory-items/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NonInventoryItem,
        )

    def update(
        self,
        id: str,
        *,
        version: str,
        conductor_end_user_id: str,
        barcode: non_inventory_item_update_params.Barcode | NotGiven = NOT_GIVEN,
        class_id: str | NotGiven = NOT_GIVEN,
        force_unit_of_measure_change: bool | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        manufacturer_part_number: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        parent_id: str | NotGiven = NOT_GIVEN,
        sales_and_purchase_details: non_inventory_item_update_params.SalesAndPurchaseDetails | NotGiven = NOT_GIVEN,
        sales_or_purchase_details: non_inventory_item_update_params.SalesOrPurchaseDetails | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        unit_of_measure_set_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NonInventoryItem:
        """
        Updates an existing non-inventory item.

        Args:
          id: The QuickBooks-assigned unique identifier of the non-inventory item to update.

          version: The current version identifier of the non-inventory item you are updating, which
              you can get by fetching the object first. Provide the most recent `version` to
              ensure you're working with the latest data; otherwise, the update will fail.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          barcode: The non-inventory item's barcode.

          class_id: The non-inventory item's class. Classes can be used to categorize objects into
              meaningful segments, such as department, location, or type of work. In
              QuickBooks, class tracking is off by default.

          force_unit_of_measure_change: Indicates whether to allow changing the non-inventory item's Unit of Measure
              (UOM) set (using the `unitOfMeasureSetId` field) when the base unit of the new
              UOM set does not match that of the currently assigned UOM set. Without setting
              this field to `true` in this scenario, the request will fail with an error;
              hence, this field is equivalent to accepting the warning prompt in the
              QuickBooks UI.

              Important: Changing the base unit requires you to update the item's
              quantities-on-hand and cost to reflect the new unit; otherwise, these values
              will be inaccurate. Alternatively, consider creating a new item with the desired
              UOM set and deactivating the old item.

          is_active: Indicates whether this non-inventory item is active. Inactive objects are
              typically hidden from views and reports in QuickBooks.

          manufacturer_part_number: The manufacturer's part number for this non-inventory item, which is often the
              stock keeping unit (SKU).

          name: The case-insensitive name of this non-inventory item. Not guaranteed to be
              unique because it does not include the names of its parent objects like
              `fullName` does. For example, two non-inventory items could both have the `name`
              "Printer Ink Cartridge", but they could have unique `fullName` values, such as
              "Office-Supplies:Printer Ink Cartridge" and "Miscellaneous:Printer Ink
              Cartridge".

          parent_id: The parent non-inventory item one level above this one in the hierarchy. For
              example, if this non-inventory item has a `fullName` of "Office-Supplies:Printer
              Ink Cartridge", its parent has a `fullName` of "Office-Supplies". If this
              non-inventory item is at the top level, this field will be `null`.

          sales_and_purchase_details: Details for non-inventory items that are both purchased and sold, such as
              reimbursable expenses or inventory items that are bought from vendors and sold
              to customers. Do not use this field alongside `salesOrPurchaseDetails` because
              an item cannot have both configurations.

          sales_or_purchase_details: Details for non-inventory items that are exclusively sold or exclusively
              purchased, but not both. This typically applies to non-inventory items (like a
              purchased office supply that isn't resold) or service items (like consulting
              services that are sold but not purchased). Do not use this field alongside
              `salesAndPurchaseDetails` because an item cannot have both configurations.

          sales_tax_code_id: The sales-tax code associated with this non-inventory item, determining whether
              it is taxable or non-taxable. It's used to assign a default tax status to all
              transactions for this non-inventory item. Default codes include "Non"
              (non-taxable) and "Tax" (taxable), but custom codes can also be created in
              QuickBooks. If QuickBooks is not set up to charge sales tax (via the "Do You
              Charge Sales Tax?" preference), it will assign the default non-taxable code to
              all sales.

          unit_of_measure_set_id: The unit of measure set associated with this non-inventory item, which consists
              of a base unit and related units.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            f"/quickbooks-desktop/non-inventory-items/{id}",
            body=maybe_transform(
                {
                    "version": version,
                    "barcode": barcode,
                    "class_id": class_id,
                    "force_unit_of_measure_change": force_unit_of_measure_change,
                    "is_active": is_active,
                    "manufacturer_part_number": manufacturer_part_number,
                    "name": name,
                    "parent_id": parent_id,
                    "sales_and_purchase_details": sales_and_purchase_details,
                    "sales_or_purchase_details": sales_or_purchase_details,
                    "sales_tax_code_id": sales_tax_code_id,
                    "unit_of_measure_set_id": unit_of_measure_set_id,
                },
                non_inventory_item_update_params.NonInventoryItemUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NonInventoryItem,
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
    ) -> SyncCursorPage[NonInventoryItem]:
        """
        Returns a list of non-inventory items.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          class_ids: Filter for non-inventory items of this class or classes. Specify a single class
              ID or multiple using a comma-separated list (e.g., `classIds=1,2,3`). A class is
              a way end-users can categorize non-inventory items in QuickBooks.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Retrieve this value from the `nextCursor` field in the
              previous response. If omitted, the API returns the first page of results.

          full_names: Filter for specific non-inventory items by their full-name(s). Specify a single
              full-name or multiple using a comma-separated list (e.g., `fullNames=1,2,3`).
              Like `id`, a `fullName` is a unique identifier for a non-inventory item, and is
              formed by by combining the names of its parent objects with its own `name`,
              separated by colons. For example, if a non-inventory item is under "Office
              Supplies" and has the `name` "Printer Ink Cartridge", its `fullName` would be
              "Office Supplies:Printer Ink Cartridge". Unlike `name`, `fullName` is guaranteed
              to be unique across all non-inventory item objects. Not case-sensitive. NOTE: If
              you include this parameter, all other query parameters will be ignored.

          ids: Filter for specific non-inventory items by their QuickBooks-assigned unique
              identifier(s). Specify a single ID or multiple using a comma-separated list
              (e.g., `ids=1,2,3`). NOTE: If you include this parameter, all other query
              parameters will be ignored.

          limit: The maximum number of objects to return, ranging from 1 to 500. Defaults to 500.
              Use this parameter in conjunction with the `cursor` parameter to paginate
              through results. The response will include a `nextCursor` field, which can be
              used as the `cursor` parameter value in subsequent requests to fetch the next
              set of results.

          name_contains: Filter for non-inventory items whose `name` contains this substring. If you use
              this parameter, you cannot use `nameStartsWith` or `nameEndsWith`.

          name_ends_with: Filter for non-inventory items whose `name` ends with this substring. If you use
              this parameter, you cannot use `nameContains` or `nameStartsWith`.

          name_from: Filter for non-inventory items whose `name` is alphabetically greater than or
              equal to this value.

          name_starts_with: Filter for non-inventory items whose `name` starts with this substring. If you
              use this parameter, you cannot use `nameContains` or `nameEndsWith`.

          name_to: Filter for non-inventory items whose `name` is alphabetically less than or equal
              to this value.

          status: Filter for non-inventory items that are active, inactive, or both.

          updated_after: Filter for non-inventory items updated on or after this date and time, in ISO
              8601 format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the
              time is assumed to be 00:00:00 of that day.

          updated_before: Filter for non-inventory items updated on or before this date and time, in ISO
              8601 format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the
              time is assumed to be 23:59:59 of that day.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get_api_list(
            "/quickbooks-desktop/non-inventory-items",
            page=SyncCursorPage[NonInventoryItem],
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
                    non_inventory_item_list_params.NonInventoryItemListParams,
                ),
            ),
            model=NonInventoryItem,
        )


class AsyncNonInventoryItemsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNonInventoryItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/conductor-is/conductor-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNonInventoryItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNonInventoryItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/conductor-is/conductor-python#with_streaming_response
        """
        return AsyncNonInventoryItemsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        conductor_end_user_id: str,
        barcode: non_inventory_item_create_params.Barcode | NotGiven = NOT_GIVEN,
        class_id: str | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        manufacturer_part_number: str | NotGiven = NOT_GIVEN,
        parent_id: str | NotGiven = NOT_GIVEN,
        sales_and_purchase_details: non_inventory_item_create_params.SalesAndPurchaseDetails | NotGiven = NOT_GIVEN,
        sales_or_purchase_details: non_inventory_item_create_params.SalesOrPurchaseDetails | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        unit_of_measure_set_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NonInventoryItem:
        """
        Creates a non-inventory item.

        Args:
          name: The case-insensitive name of this non-inventory item. Not guaranteed to be
              unique because it does not include the names of its parent objects like
              `fullName` does. For example, two non-inventory items could both have the `name`
              "Printer Ink Cartridge", but they could have unique `fullName` values, such as
              "Office-Supplies:Printer Ink Cartridge" and "Miscellaneous:Printer Ink
              Cartridge".

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          barcode: The non-inventory item's barcode.

          class_id: The non-inventory item's class. Classes can be used to categorize objects into
              meaningful segments, such as department, location, or type of work. In
              QuickBooks, class tracking is off by default.

          external_id: A globally unique identifier (GUID) you can provide for tracking this object in
              your external system. Must be formatted as a valid GUID; otherwise, QuickBooks
              will return an error. This field is immutable and can only be set during object
              creation.

          is_active: Indicates whether this non-inventory item is active. Inactive objects are
              typically hidden from views and reports in QuickBooks.

          manufacturer_part_number: The manufacturer's part number for this non-inventory item, which is often the
              stock keeping unit (SKU).

          parent_id: The parent non-inventory item one level above this one in the hierarchy. For
              example, if this non-inventory item has a `fullName` of "Office-Supplies:Printer
              Ink Cartridge", its parent has a `fullName` of "Office-Supplies". If this
              non-inventory item is at the top level, this field will be `null`.

          sales_tax_code_id: The sales-tax code associated with this non-inventory item, determining whether
              it is taxable or non-taxable. It's used to assign a default tax status to all
              transactions for this non-inventory item. Default codes include "Non"
              (non-taxable) and "Tax" (taxable), but custom codes can also be created in
              QuickBooks. If QuickBooks is not set up to charge sales tax (via the "Do You
              Charge Sales Tax?" preference), it will assign the default non-taxable code to
              all sales.

          unit_of_measure_set_id: The unit of measure set associated with this non-inventory item, which consists
              of a base unit and related units.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            "/quickbooks-desktop/non-inventory-items",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "barcode": barcode,
                    "class_id": class_id,
                    "external_id": external_id,
                    "is_active": is_active,
                    "manufacturer_part_number": manufacturer_part_number,
                    "parent_id": parent_id,
                    "sales_and_purchase_details": sales_and_purchase_details,
                    "sales_or_purchase_details": sales_or_purchase_details,
                    "sales_tax_code_id": sales_tax_code_id,
                    "unit_of_measure_set_id": unit_of_measure_set_id,
                },
                non_inventory_item_create_params.NonInventoryItemCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NonInventoryItem,
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
    ) -> NonInventoryItem:
        """
        Retrieves a non-inventory item by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the non-inventory item to retrieve.

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
            f"/quickbooks-desktop/non-inventory-items/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NonInventoryItem,
        )

    async def update(
        self,
        id: str,
        *,
        version: str,
        conductor_end_user_id: str,
        barcode: non_inventory_item_update_params.Barcode | NotGiven = NOT_GIVEN,
        class_id: str | NotGiven = NOT_GIVEN,
        force_unit_of_measure_change: bool | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        manufacturer_part_number: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        parent_id: str | NotGiven = NOT_GIVEN,
        sales_and_purchase_details: non_inventory_item_update_params.SalesAndPurchaseDetails | NotGiven = NOT_GIVEN,
        sales_or_purchase_details: non_inventory_item_update_params.SalesOrPurchaseDetails | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        unit_of_measure_set_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NonInventoryItem:
        """
        Updates an existing non-inventory item.

        Args:
          id: The QuickBooks-assigned unique identifier of the non-inventory item to update.

          version: The current version identifier of the non-inventory item you are updating, which
              you can get by fetching the object first. Provide the most recent `version` to
              ensure you're working with the latest data; otherwise, the update will fail.

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          barcode: The non-inventory item's barcode.

          class_id: The non-inventory item's class. Classes can be used to categorize objects into
              meaningful segments, such as department, location, or type of work. In
              QuickBooks, class tracking is off by default.

          force_unit_of_measure_change: Indicates whether to allow changing the non-inventory item's Unit of Measure
              (UOM) set (using the `unitOfMeasureSetId` field) when the base unit of the new
              UOM set does not match that of the currently assigned UOM set. Without setting
              this field to `true` in this scenario, the request will fail with an error;
              hence, this field is equivalent to accepting the warning prompt in the
              QuickBooks UI.

              Important: Changing the base unit requires you to update the item's
              quantities-on-hand and cost to reflect the new unit; otherwise, these values
              will be inaccurate. Alternatively, consider creating a new item with the desired
              UOM set and deactivating the old item.

          is_active: Indicates whether this non-inventory item is active. Inactive objects are
              typically hidden from views and reports in QuickBooks.

          manufacturer_part_number: The manufacturer's part number for this non-inventory item, which is often the
              stock keeping unit (SKU).

          name: The case-insensitive name of this non-inventory item. Not guaranteed to be
              unique because it does not include the names of its parent objects like
              `fullName` does. For example, two non-inventory items could both have the `name`
              "Printer Ink Cartridge", but they could have unique `fullName` values, such as
              "Office-Supplies:Printer Ink Cartridge" and "Miscellaneous:Printer Ink
              Cartridge".

          parent_id: The parent non-inventory item one level above this one in the hierarchy. For
              example, if this non-inventory item has a `fullName` of "Office-Supplies:Printer
              Ink Cartridge", its parent has a `fullName` of "Office-Supplies". If this
              non-inventory item is at the top level, this field will be `null`.

          sales_and_purchase_details: Details for non-inventory items that are both purchased and sold, such as
              reimbursable expenses or inventory items that are bought from vendors and sold
              to customers. Do not use this field alongside `salesOrPurchaseDetails` because
              an item cannot have both configurations.

          sales_or_purchase_details: Details for non-inventory items that are exclusively sold or exclusively
              purchased, but not both. This typically applies to non-inventory items (like a
              purchased office supply that isn't resold) or service items (like consulting
              services that are sold but not purchased). Do not use this field alongside
              `salesAndPurchaseDetails` because an item cannot have both configurations.

          sales_tax_code_id: The sales-tax code associated with this non-inventory item, determining whether
              it is taxable or non-taxable. It's used to assign a default tax status to all
              transactions for this non-inventory item. Default codes include "Non"
              (non-taxable) and "Tax" (taxable), but custom codes can also be created in
              QuickBooks. If QuickBooks is not set up to charge sales tax (via the "Do You
              Charge Sales Tax?" preference), it will assign the default non-taxable code to
              all sales.

          unit_of_measure_set_id: The unit of measure set associated with this non-inventory item, which consists
              of a base unit and related units.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            f"/quickbooks-desktop/non-inventory-items/{id}",
            body=await async_maybe_transform(
                {
                    "version": version,
                    "barcode": barcode,
                    "class_id": class_id,
                    "force_unit_of_measure_change": force_unit_of_measure_change,
                    "is_active": is_active,
                    "manufacturer_part_number": manufacturer_part_number,
                    "name": name,
                    "parent_id": parent_id,
                    "sales_and_purchase_details": sales_and_purchase_details,
                    "sales_or_purchase_details": sales_or_purchase_details,
                    "sales_tax_code_id": sales_tax_code_id,
                    "unit_of_measure_set_id": unit_of_measure_set_id,
                },
                non_inventory_item_update_params.NonInventoryItemUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NonInventoryItem,
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
    ) -> AsyncPaginator[NonInventoryItem, AsyncCursorPage[NonInventoryItem]]:
        """
        Returns a list of non-inventory items.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          class_ids: Filter for non-inventory items of this class or classes. Specify a single class
              ID or multiple using a comma-separated list (e.g., `classIds=1,2,3`). A class is
              a way end-users can categorize non-inventory items in QuickBooks.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Retrieve this value from the `nextCursor` field in the
              previous response. If omitted, the API returns the first page of results.

          full_names: Filter for specific non-inventory items by their full-name(s). Specify a single
              full-name or multiple using a comma-separated list (e.g., `fullNames=1,2,3`).
              Like `id`, a `fullName` is a unique identifier for a non-inventory item, and is
              formed by by combining the names of its parent objects with its own `name`,
              separated by colons. For example, if a non-inventory item is under "Office
              Supplies" and has the `name` "Printer Ink Cartridge", its `fullName` would be
              "Office Supplies:Printer Ink Cartridge". Unlike `name`, `fullName` is guaranteed
              to be unique across all non-inventory item objects. Not case-sensitive. NOTE: If
              you include this parameter, all other query parameters will be ignored.

          ids: Filter for specific non-inventory items by their QuickBooks-assigned unique
              identifier(s). Specify a single ID or multiple using a comma-separated list
              (e.g., `ids=1,2,3`). NOTE: If you include this parameter, all other query
              parameters will be ignored.

          limit: The maximum number of objects to return, ranging from 1 to 500. Defaults to 500.
              Use this parameter in conjunction with the `cursor` parameter to paginate
              through results. The response will include a `nextCursor` field, which can be
              used as the `cursor` parameter value in subsequent requests to fetch the next
              set of results.

          name_contains: Filter for non-inventory items whose `name` contains this substring. If you use
              this parameter, you cannot use `nameStartsWith` or `nameEndsWith`.

          name_ends_with: Filter for non-inventory items whose `name` ends with this substring. If you use
              this parameter, you cannot use `nameContains` or `nameStartsWith`.

          name_from: Filter for non-inventory items whose `name` is alphabetically greater than or
              equal to this value.

          name_starts_with: Filter for non-inventory items whose `name` starts with this substring. If you
              use this parameter, you cannot use `nameContains` or `nameEndsWith`.

          name_to: Filter for non-inventory items whose `name` is alphabetically less than or equal
              to this value.

          status: Filter for non-inventory items that are active, inactive, or both.

          updated_after: Filter for non-inventory items updated on or after this date and time, in ISO
              8601 format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the
              time is assumed to be 00:00:00 of that day.

          updated_before: Filter for non-inventory items updated on or before this date and time, in ISO
              8601 format (YYYY-MM-DDTHH:mm:ss). If you only provide a date (YYYY-MM-DD), the
              time is assumed to be 23:59:59 of that day.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._get_api_list(
            "/quickbooks-desktop/non-inventory-items",
            page=AsyncCursorPage[NonInventoryItem],
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
                    non_inventory_item_list_params.NonInventoryItemListParams,
                ),
            ),
            model=NonInventoryItem,
        )


class NonInventoryItemsResourceWithRawResponse:
    def __init__(self, non_inventory_items: NonInventoryItemsResource) -> None:
        self._non_inventory_items = non_inventory_items

        self.create = to_raw_response_wrapper(
            non_inventory_items.create,
        )
        self.retrieve = to_raw_response_wrapper(
            non_inventory_items.retrieve,
        )
        self.update = to_raw_response_wrapper(
            non_inventory_items.update,
        )
        self.list = to_raw_response_wrapper(
            non_inventory_items.list,
        )


class AsyncNonInventoryItemsResourceWithRawResponse:
    def __init__(self, non_inventory_items: AsyncNonInventoryItemsResource) -> None:
        self._non_inventory_items = non_inventory_items

        self.create = async_to_raw_response_wrapper(
            non_inventory_items.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            non_inventory_items.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            non_inventory_items.update,
        )
        self.list = async_to_raw_response_wrapper(
            non_inventory_items.list,
        )


class NonInventoryItemsResourceWithStreamingResponse:
    def __init__(self, non_inventory_items: NonInventoryItemsResource) -> None:
        self._non_inventory_items = non_inventory_items

        self.create = to_streamed_response_wrapper(
            non_inventory_items.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            non_inventory_items.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            non_inventory_items.update,
        )
        self.list = to_streamed_response_wrapper(
            non_inventory_items.list,
        )


class AsyncNonInventoryItemsResourceWithStreamingResponse:
    def __init__(self, non_inventory_items: AsyncNonInventoryItemsResource) -> None:
        self._non_inventory_items = non_inventory_items

        self.create = async_to_streamed_response_wrapper(
            non_inventory_items.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            non_inventory_items.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            non_inventory_items.update,
        )
        self.list = async_to_streamed_response_wrapper(
            non_inventory_items.list,
        )
