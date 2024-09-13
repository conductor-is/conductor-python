# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from conductor import Conductor, AsyncConductor
from tests.utils import assert_matches_type
from conductor.types.qbd import NonInventoryItem
from conductor.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNonInventoryItems:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Conductor) -> None:
        non_inventory_item = client.qbd.non_inventory_items.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(NonInventoryItem, non_inventory_item, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Conductor) -> None:
        response = client.qbd.non_inventory_items.with_raw_response.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        non_inventory_item = response.parse()
        assert_matches_type(NonInventoryItem, non_inventory_item, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Conductor) -> None:
        with client.qbd.non_inventory_items.with_streaming_response.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            non_inventory_item = response.parse()
            assert_matches_type(NonInventoryItem, non_inventory_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.non_inventory_items.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    def test_method_list(self, client: Conductor) -> None:
        non_inventory_item = client.qbd.non_inventory_items.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(SyncCursorPage[NonInventoryItem], non_inventory_item, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Conductor) -> None:
        non_inventory_item = client.qbd.non_inventory_items.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            class_ids="80000001-1234567890",
            cursor="12345678-abcd-abcd-example-1234567890ab",
            full_names="Office Supplies:Printer Ink Cartridge",
            ids="80000001-1234567890",
            limit=1,
            name_contains="nameContains",
            name_ends_with="nameEndsWith",
            name_from="nameFrom",
            name_starts_with="nameStartsWith",
            name_to="nameTo",
            status="active",
            updated_after="updatedAfter",
            updated_before="updatedBefore",
        )
        assert_matches_type(SyncCursorPage[NonInventoryItem], non_inventory_item, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Conductor) -> None:
        response = client.qbd.non_inventory_items.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        non_inventory_item = response.parse()
        assert_matches_type(SyncCursorPage[NonInventoryItem], non_inventory_item, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Conductor) -> None:
        with client.qbd.non_inventory_items.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            non_inventory_item = response.parse()
            assert_matches_type(SyncCursorPage[NonInventoryItem], non_inventory_item, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncNonInventoryItems:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncConductor) -> None:
        non_inventory_item = await async_client.qbd.non_inventory_items.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(NonInventoryItem, non_inventory_item, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.non_inventory_items.with_raw_response.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        non_inventory_item = await response.parse()
        assert_matches_type(NonInventoryItem, non_inventory_item, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.non_inventory_items.with_streaming_response.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            non_inventory_item = await response.parse()
            assert_matches_type(NonInventoryItem, non_inventory_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.non_inventory_items.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncConductor) -> None:
        non_inventory_item = await async_client.qbd.non_inventory_items.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(AsyncCursorPage[NonInventoryItem], non_inventory_item, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncConductor) -> None:
        non_inventory_item = await async_client.qbd.non_inventory_items.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            class_ids="80000001-1234567890",
            cursor="12345678-abcd-abcd-example-1234567890ab",
            full_names="Office Supplies:Printer Ink Cartridge",
            ids="80000001-1234567890",
            limit=1,
            name_contains="nameContains",
            name_ends_with="nameEndsWith",
            name_from="nameFrom",
            name_starts_with="nameStartsWith",
            name_to="nameTo",
            status="active",
            updated_after="updatedAfter",
            updated_before="updatedBefore",
        )
        assert_matches_type(AsyncCursorPage[NonInventoryItem], non_inventory_item, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.non_inventory_items.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        non_inventory_item = await response.parse()
        assert_matches_type(AsyncCursorPage[NonInventoryItem], non_inventory_item, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.non_inventory_items.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            non_inventory_item = await response.parse()
            assert_matches_type(AsyncCursorPage[NonInventoryItem], non_inventory_item, path=["response"])

        assert cast(Any, response.is_closed) is True
