# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from conductor import Conductor, AsyncConductor
from tests.utils import assert_matches_type
from conductor.types.qbd import QbdSalesTaxItem
from conductor.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSalesTaxItems:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Conductor) -> None:
        sales_tax_item = client.qbd.sales_tax_items.create(
            name="Standard Tax",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(QbdSalesTaxItem, sales_tax_item, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Conductor) -> None:
        sales_tax_item = client.qbd.sales_tax_items.create(
            name="Standard Tax",
            conductor_end_user_id="end_usr_1234567abcdefg",
            barcode={
                "allow_override": False,
                "assign_even_if_used": False,
                "bar_code_value": "1234567890",
            },
            class_id="80000001-1234567890",
            description="Standard rate sales tax for California",
            external_id="12345678-abcd-1234-abcd-1234567890ab",
            is_active=True,
            sales_tax_return_line_id="80000021-1234567890",
            tax_rate="7.5",
            tax_vendor_id="80000020-1234567890",
        )
        assert_matches_type(QbdSalesTaxItem, sales_tax_item, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Conductor) -> None:
        response = client.qbd.sales_tax_items.with_raw_response.create(
            name="Standard Tax",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sales_tax_item = response.parse()
        assert_matches_type(QbdSalesTaxItem, sales_tax_item, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Conductor) -> None:
        with client.qbd.sales_tax_items.with_streaming_response.create(
            name="Standard Tax",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sales_tax_item = response.parse()
            assert_matches_type(QbdSalesTaxItem, sales_tax_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Conductor) -> None:
        sales_tax_item = client.qbd.sales_tax_items.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(QbdSalesTaxItem, sales_tax_item, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Conductor) -> None:
        response = client.qbd.sales_tax_items.with_raw_response.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sales_tax_item = response.parse()
        assert_matches_type(QbdSalesTaxItem, sales_tax_item, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Conductor) -> None:
        with client.qbd.sales_tax_items.with_streaming_response.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sales_tax_item = response.parse()
            assert_matches_type(QbdSalesTaxItem, sales_tax_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.sales_tax_items.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    def test_method_list(self, client: Conductor) -> None:
        sales_tax_item = client.qbd.sales_tax_items.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(SyncCursorPage[QbdSalesTaxItem], sales_tax_item, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Conductor) -> None:
        sales_tax_item = client.qbd.sales_tax_items.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            class_ids="80000001-1234567890",
            cursor="12345678-abcd-abcd-example-1234567890ab",
            full_names="State:CA Sales Tax",
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
        assert_matches_type(SyncCursorPage[QbdSalesTaxItem], sales_tax_item, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Conductor) -> None:
        response = client.qbd.sales_tax_items.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sales_tax_item = response.parse()
        assert_matches_type(SyncCursorPage[QbdSalesTaxItem], sales_tax_item, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Conductor) -> None:
        with client.qbd.sales_tax_items.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sales_tax_item = response.parse()
            assert_matches_type(SyncCursorPage[QbdSalesTaxItem], sales_tax_item, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSalesTaxItems:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncConductor) -> None:
        sales_tax_item = await async_client.qbd.sales_tax_items.create(
            name="Standard Tax",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(QbdSalesTaxItem, sales_tax_item, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncConductor) -> None:
        sales_tax_item = await async_client.qbd.sales_tax_items.create(
            name="Standard Tax",
            conductor_end_user_id="end_usr_1234567abcdefg",
            barcode={
                "allow_override": False,
                "assign_even_if_used": False,
                "bar_code_value": "1234567890",
            },
            class_id="80000001-1234567890",
            description="Standard rate sales tax for California",
            external_id="12345678-abcd-1234-abcd-1234567890ab",
            is_active=True,
            sales_tax_return_line_id="80000021-1234567890",
            tax_rate="7.5",
            tax_vendor_id="80000020-1234567890",
        )
        assert_matches_type(QbdSalesTaxItem, sales_tax_item, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.sales_tax_items.with_raw_response.create(
            name="Standard Tax",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sales_tax_item = await response.parse()
        assert_matches_type(QbdSalesTaxItem, sales_tax_item, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.sales_tax_items.with_streaming_response.create(
            name="Standard Tax",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sales_tax_item = await response.parse()
            assert_matches_type(QbdSalesTaxItem, sales_tax_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncConductor) -> None:
        sales_tax_item = await async_client.qbd.sales_tax_items.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(QbdSalesTaxItem, sales_tax_item, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.sales_tax_items.with_raw_response.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sales_tax_item = await response.parse()
        assert_matches_type(QbdSalesTaxItem, sales_tax_item, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.sales_tax_items.with_streaming_response.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sales_tax_item = await response.parse()
            assert_matches_type(QbdSalesTaxItem, sales_tax_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.sales_tax_items.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncConductor) -> None:
        sales_tax_item = await async_client.qbd.sales_tax_items.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(AsyncCursorPage[QbdSalesTaxItem], sales_tax_item, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncConductor) -> None:
        sales_tax_item = await async_client.qbd.sales_tax_items.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            class_ids="80000001-1234567890",
            cursor="12345678-abcd-abcd-example-1234567890ab",
            full_names="State:CA Sales Tax",
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
        assert_matches_type(AsyncCursorPage[QbdSalesTaxItem], sales_tax_item, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.sales_tax_items.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sales_tax_item = await response.parse()
        assert_matches_type(AsyncCursorPage[QbdSalesTaxItem], sales_tax_item, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.sales_tax_items.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sales_tax_item = await response.parse()
            assert_matches_type(AsyncCursorPage[QbdSalesTaxItem], sales_tax_item, path=["response"])

        assert cast(Any, response.is_closed) is True
