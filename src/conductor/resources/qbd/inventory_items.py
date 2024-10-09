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
from ...types.qbd import inventory_item_list_params, inventory_item_create_params
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

    def create(
        self,
        *,
        name: str,
        conductor_end_user_id: str,
        asset_account_id: str | NotGiven = NOT_GIVEN,
        barcode: inventory_item_create_params.Barcode | NotGiven = NOT_GIVEN,
        class_id: str | NotGiven = NOT_GIVEN,
        cogs_account_id: str | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        income_account_id: str | NotGiven = NOT_GIVEN,
        inventory_date: Union[str, date] | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        is_tax_included: bool | NotGiven = NOT_GIVEN,
        manufacturer_part_number: str | NotGiven = NOT_GIVEN,
        maximum_on_hand_quantity: float | NotGiven = NOT_GIVEN,
        parent_id: str | NotGiven = NOT_GIVEN,
        preferred_vendor_id: str | NotGiven = NOT_GIVEN,
        purchase_cost: str | NotGiven = NOT_GIVEN,
        purchase_description: str | NotGiven = NOT_GIVEN,
        purchase_tax_code_id: str | NotGiven = NOT_GIVEN,
        quantity_on_hand: float | NotGiven = NOT_GIVEN,
        reorder_point: float | NotGiven = NOT_GIVEN,
        sales_description: str | NotGiven = NOT_GIVEN,
        sales_price: str | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        total_value: str | NotGiven = NOT_GIVEN,
        unit_of_measure_set_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InventoryItem:
        """
        Creates an inventory item.

        Args:
          name: The case-insensitive name of this inventory item. Not guaranteed to be unique
              because it does not include the names of its parent objects like `fullName`
              does. For example, two inventory items could both have the `name` "Widget", but
              they could have unique `fullName` values, such as "Products:Widget" and
              "Inventory:Widget".

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          asset_account_id: The asset account used to track the current value of this inventory item in
              inventory.

          barcode: The inventory item's barcode.

          class_id: The inventory item's class. Classes can be used to categorize objects into
              meaningful segments, such as department, location, or type of work. In
              QuickBooks, class tracking is off by default.

          cogs_account_id: The Cost of Goods Sold (COGS) account for this inventory item, tracking the
              original direct costs of producing goods sold.

          external_id: A developer-assigned globally unique identifier (GUID) for tracking this object
              in external systems. Must be formatted as a valid GUID; otherwise, QuickBooks
              will return an error.

          income_account_id: The inventory item's income account, used to track revenue from sales.

          inventory_date: The date when this inventory item was converted into an inventory item from some
              other type of item, in ISO 8601 format (YYYY-MM-DD).

          is_active: Indicates whether this inventory item is active. Inactive objects are typically
              hidden from views and reports in QuickBooks.

          is_tax_included: Indicates whether the price of this inventory item includes tax. This is
              primarily used in international versions of QuickBooks.

          manufacturer_part_number: The manufacturer's part number for this inventory item.

          maximum_on_hand_quantity: The maximum quantity of this inventory item desired in inventory.

          parent_id: The parent inventory item one level above this one in the hierarchy. For
              example, if this inventory item has a `fullName` of
              "Products:Electronics:Widgets", its parent has a `fullName` of
              "Products:Electronics". If this inventory item is at the top level, `parent`
              will be `null`.

          preferred_vendor_id: The preferred vendor from whom this inventory item is typically purchased.

          purchase_cost: The cost at which this inventory item is purchased from vendors, represented as
              a decimal string.

          purchase_description: The description of this inventory item that appears on purchase forms (e.g.,
              checks, bills, item receipts) when ordered or bought from vendors.

          purchase_tax_code_id: The tax code applied to purchases of this inventory item. Applicable in regions
              where purchase taxes are used, such as Canada or the UK.

          quantity_on_hand: The current quantity of this inventory item available in inventory. To change
              the `quantityOnHand` for an inventory item, you must create an
              inventory-adjustment instead of updating this inventory item directly.

          reorder_point: The minimum quantity of this inventory item at which QuickBooks prompts for
              reordering.

          sales_description: The description of this inventory item that appears on sales forms (e.g.,
              invoices, sales receipts) when sold to customers. For fixed assets, it details
              the sale of the asset for accounting purposes.

          sales_price: The price at which this inventory item is sold to customers, represented as a
              decimal string.

          sales_tax_code_id: The sales tax code associated with this inventory item, determining whether it
              is taxable or non-taxable. It's used to assign a default tax status to all
              transactions for this inventory item. Default codes include 'NON' (non-taxable)
              and 'TAX' (taxable), but custom codes can also be created in QuickBooks. If
              QuickBooks is not set up to charge sales tax, it will assign the default
              non-taxable code to all sales.

          total_value: The total value of this inventory item. If `totalValue` is provided,
              `quantityOnHand` must also be provided and must be greater than zero. If both
              `quantityOnHand` and `purchaseCost` are provided, then `totalValue` will be set
              to `quantityOnHand` times `purchaseCost`, regardless of what `totalValue` is
              explicitly set to.

          unit_of_measure_set_id: The unit of measure set associated with this inventory item, which consists of a
              base unit and related units.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return self._post(
            "/quickbooks-desktop/inventory-items",
            body=maybe_transform(
                {
                    "name": name,
                    "asset_account_id": asset_account_id,
                    "barcode": barcode,
                    "class_id": class_id,
                    "cogs_account_id": cogs_account_id,
                    "external_id": external_id,
                    "income_account_id": income_account_id,
                    "inventory_date": inventory_date,
                    "is_active": is_active,
                    "is_tax_included": is_tax_included,
                    "manufacturer_part_number": manufacturer_part_number,
                    "maximum_on_hand_quantity": maximum_on_hand_quantity,
                    "parent_id": parent_id,
                    "preferred_vendor_id": preferred_vendor_id,
                    "purchase_cost": purchase_cost,
                    "purchase_description": purchase_description,
                    "purchase_tax_code_id": purchase_tax_code_id,
                    "quantity_on_hand": quantity_on_hand,
                    "reorder_point": reorder_point,
                    "sales_description": sales_description,
                    "sales_price": sales_price,
                    "sales_tax_code_id": sales_tax_code_id,
                    "total_value": total_value,
                    "unit_of_measure_set_id": unit_of_measure_set_id,
                },
                inventory_item_create_params.InventoryItemCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InventoryItem,
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
    ) -> InventoryItem:
        """
        Retrieves an inventory item by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the inventory item to retrieve.

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
        Returns a list of inventory items.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          class_ids: Filter for inventory items of this class or classes. Specify a single class ID
              or multiple using a comma-separated list (e.g., `classIds=1,2,3`). A class is a
              way end-users can categorize inventory items in QuickBooks.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Retrieve this value from the `nextCursor` field in the
              previous response. If omitted, the API returns the first page of results.

          full_names: Filter for specific inventory items by their full-name(s). Specify a single
              full-name or multiple using a comma-separated list (e.g., `fullNames=1,2,3`).
              Like `id`, a `fullName` is a unique identifier for an inventory item, and is
              formed by by combining the names of its parent objects with its own `name`,
              separated by colons. For example, if an inventory item is under
              'Furniture:Kitchen' and has the `name` 'Cabinet', its `fullName` would be
              'Furniture:Kitchen:Cabinet'. Unlike `name`, `fullName` is guaranteed to be
              unique across all inventory item objects. Not case-sensitive. NOTE: If you
              include this parameter, all other query parameters will be ignored.

          ids: Filter for specific inventory items by their QuickBooks-assigned unique
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

    async def create(
        self,
        *,
        name: str,
        conductor_end_user_id: str,
        asset_account_id: str | NotGiven = NOT_GIVEN,
        barcode: inventory_item_create_params.Barcode | NotGiven = NOT_GIVEN,
        class_id: str | NotGiven = NOT_GIVEN,
        cogs_account_id: str | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        income_account_id: str | NotGiven = NOT_GIVEN,
        inventory_date: Union[str, date] | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        is_tax_included: bool | NotGiven = NOT_GIVEN,
        manufacturer_part_number: str | NotGiven = NOT_GIVEN,
        maximum_on_hand_quantity: float | NotGiven = NOT_GIVEN,
        parent_id: str | NotGiven = NOT_GIVEN,
        preferred_vendor_id: str | NotGiven = NOT_GIVEN,
        purchase_cost: str | NotGiven = NOT_GIVEN,
        purchase_description: str | NotGiven = NOT_GIVEN,
        purchase_tax_code_id: str | NotGiven = NOT_GIVEN,
        quantity_on_hand: float | NotGiven = NOT_GIVEN,
        reorder_point: float | NotGiven = NOT_GIVEN,
        sales_description: str | NotGiven = NOT_GIVEN,
        sales_price: str | NotGiven = NOT_GIVEN,
        sales_tax_code_id: str | NotGiven = NOT_GIVEN,
        total_value: str | NotGiven = NOT_GIVEN,
        unit_of_measure_set_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InventoryItem:
        """
        Creates an inventory item.

        Args:
          name: The case-insensitive name of this inventory item. Not guaranteed to be unique
              because it does not include the names of its parent objects like `fullName`
              does. For example, two inventory items could both have the `name` "Widget", but
              they could have unique `fullName` values, such as "Products:Widget" and
              "Inventory:Widget".

          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          asset_account_id: The asset account used to track the current value of this inventory item in
              inventory.

          barcode: The inventory item's barcode.

          class_id: The inventory item's class. Classes can be used to categorize objects into
              meaningful segments, such as department, location, or type of work. In
              QuickBooks, class tracking is off by default.

          cogs_account_id: The Cost of Goods Sold (COGS) account for this inventory item, tracking the
              original direct costs of producing goods sold.

          external_id: A developer-assigned globally unique identifier (GUID) for tracking this object
              in external systems. Must be formatted as a valid GUID; otherwise, QuickBooks
              will return an error.

          income_account_id: The inventory item's income account, used to track revenue from sales.

          inventory_date: The date when this inventory item was converted into an inventory item from some
              other type of item, in ISO 8601 format (YYYY-MM-DD).

          is_active: Indicates whether this inventory item is active. Inactive objects are typically
              hidden from views and reports in QuickBooks.

          is_tax_included: Indicates whether the price of this inventory item includes tax. This is
              primarily used in international versions of QuickBooks.

          manufacturer_part_number: The manufacturer's part number for this inventory item.

          maximum_on_hand_quantity: The maximum quantity of this inventory item desired in inventory.

          parent_id: The parent inventory item one level above this one in the hierarchy. For
              example, if this inventory item has a `fullName` of
              "Products:Electronics:Widgets", its parent has a `fullName` of
              "Products:Electronics". If this inventory item is at the top level, `parent`
              will be `null`.

          preferred_vendor_id: The preferred vendor from whom this inventory item is typically purchased.

          purchase_cost: The cost at which this inventory item is purchased from vendors, represented as
              a decimal string.

          purchase_description: The description of this inventory item that appears on purchase forms (e.g.,
              checks, bills, item receipts) when ordered or bought from vendors.

          purchase_tax_code_id: The tax code applied to purchases of this inventory item. Applicable in regions
              where purchase taxes are used, such as Canada or the UK.

          quantity_on_hand: The current quantity of this inventory item available in inventory. To change
              the `quantityOnHand` for an inventory item, you must create an
              inventory-adjustment instead of updating this inventory item directly.

          reorder_point: The minimum quantity of this inventory item at which QuickBooks prompts for
              reordering.

          sales_description: The description of this inventory item that appears on sales forms (e.g.,
              invoices, sales receipts) when sold to customers. For fixed assets, it details
              the sale of the asset for accounting purposes.

          sales_price: The price at which this inventory item is sold to customers, represented as a
              decimal string.

          sales_tax_code_id: The sales tax code associated with this inventory item, determining whether it
              is taxable or non-taxable. It's used to assign a default tax status to all
              transactions for this inventory item. Default codes include 'NON' (non-taxable)
              and 'TAX' (taxable), but custom codes can also be created in QuickBooks. If
              QuickBooks is not set up to charge sales tax, it will assign the default
              non-taxable code to all sales.

          total_value: The total value of this inventory item. If `totalValue` is provided,
              `quantityOnHand` must also be provided and must be greater than zero. If both
              `quantityOnHand` and `purchaseCost` are provided, then `totalValue` will be set
              to `quantityOnHand` times `purchaseCost`, regardless of what `totalValue` is
              explicitly set to.

          unit_of_measure_set_id: The unit of measure set associated with this inventory item, which consists of a
              base unit and related units.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Conductor-End-User-Id": conductor_end_user_id, **(extra_headers or {})}
        return await self._post(
            "/quickbooks-desktop/inventory-items",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "asset_account_id": asset_account_id,
                    "barcode": barcode,
                    "class_id": class_id,
                    "cogs_account_id": cogs_account_id,
                    "external_id": external_id,
                    "income_account_id": income_account_id,
                    "inventory_date": inventory_date,
                    "is_active": is_active,
                    "is_tax_included": is_tax_included,
                    "manufacturer_part_number": manufacturer_part_number,
                    "maximum_on_hand_quantity": maximum_on_hand_quantity,
                    "parent_id": parent_id,
                    "preferred_vendor_id": preferred_vendor_id,
                    "purchase_cost": purchase_cost,
                    "purchase_description": purchase_description,
                    "purchase_tax_code_id": purchase_tax_code_id,
                    "quantity_on_hand": quantity_on_hand,
                    "reorder_point": reorder_point,
                    "sales_description": sales_description,
                    "sales_price": sales_price,
                    "sales_tax_code_id": sales_tax_code_id,
                    "total_value": total_value,
                    "unit_of_measure_set_id": unit_of_measure_set_id,
                },
                inventory_item_create_params.InventoryItemCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InventoryItem,
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
    ) -> InventoryItem:
        """
        Retrieves an inventory item by ID.

        Args:
          id: The QuickBooks-assigned unique identifier of the inventory item to retrieve.

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
        Returns a list of inventory items.

        Args:
          conductor_end_user_id: The ID of the EndUser to receive this request (e.g.,
              `"Conductor-End-User-Id: {{END_USER_ID}}"`).

          class_ids: Filter for inventory items of this class or classes. Specify a single class ID
              or multiple using a comma-separated list (e.g., `classIds=1,2,3`). A class is a
              way end-users can categorize inventory items in QuickBooks.

          cursor: The pagination token to fetch the next set of results when paginating with the
              `limit` parameter. Retrieve this value from the `nextCursor` field in the
              previous response. If omitted, the API returns the first page of results.

          full_names: Filter for specific inventory items by their full-name(s). Specify a single
              full-name or multiple using a comma-separated list (e.g., `fullNames=1,2,3`).
              Like `id`, a `fullName` is a unique identifier for an inventory item, and is
              formed by by combining the names of its parent objects with its own `name`,
              separated by colons. For example, if an inventory item is under
              'Furniture:Kitchen' and has the `name` 'Cabinet', its `fullName` would be
              'Furniture:Kitchen:Cabinet'. Unlike `name`, `fullName` is guaranteed to be
              unique across all inventory item objects. Not case-sensitive. NOTE: If you
              include this parameter, all other query parameters will be ignored.

          ids: Filter for specific inventory items by their QuickBooks-assigned unique
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

        self.create = to_raw_response_wrapper(
            inventory_items.create,
        )
        self.retrieve = to_raw_response_wrapper(
            inventory_items.retrieve,
        )
        self.list = to_raw_response_wrapper(
            inventory_items.list,
        )


class AsyncInventoryItemsResourceWithRawResponse:
    def __init__(self, inventory_items: AsyncInventoryItemsResource) -> None:
        self._inventory_items = inventory_items

        self.create = async_to_raw_response_wrapper(
            inventory_items.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            inventory_items.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            inventory_items.list,
        )


class InventoryItemsResourceWithStreamingResponse:
    def __init__(self, inventory_items: InventoryItemsResource) -> None:
        self._inventory_items = inventory_items

        self.create = to_streamed_response_wrapper(
            inventory_items.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            inventory_items.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            inventory_items.list,
        )


class AsyncInventoryItemsResourceWithStreamingResponse:
    def __init__(self, inventory_items: AsyncInventoryItemsResource) -> None:
        self._inventory_items = inventory_items

        self.create = async_to_streamed_response_wrapper(
            inventory_items.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            inventory_items.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            inventory_items.list,
        )
