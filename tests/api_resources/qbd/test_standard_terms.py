# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from conductor import Conductor, AsyncConductor
from tests.utils import assert_matches_type
from conductor.types.qbd import (
    QbdStandardTerm,
    StandardTermListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStandardTerms:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Conductor) -> None:
        standard_term = client.qbd.standard_terms.create(
            name="Net 30",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(QbdStandardTerm, standard_term, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Conductor) -> None:
        standard_term = client.qbd.standard_terms.create(
            name="Net 30",
            conductor_end_user_id="end_usr_1234567abcdefg",
            discount_days=10,
            discount_percentage="10",
            due_days=30,
            is_active=True,
        )
        assert_matches_type(QbdStandardTerm, standard_term, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Conductor) -> None:
        response = client.qbd.standard_terms.with_raw_response.create(
            name="Net 30",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        standard_term = response.parse()
        assert_matches_type(QbdStandardTerm, standard_term, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Conductor) -> None:
        with client.qbd.standard_terms.with_streaming_response.create(
            name="Net 30",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            standard_term = response.parse()
            assert_matches_type(QbdStandardTerm, standard_term, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Conductor) -> None:
        standard_term = client.qbd.standard_terms.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(QbdStandardTerm, standard_term, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Conductor) -> None:
        response = client.qbd.standard_terms.with_raw_response.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        standard_term = response.parse()
        assert_matches_type(QbdStandardTerm, standard_term, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Conductor) -> None:
        with client.qbd.standard_terms.with_streaming_response.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            standard_term = response.parse()
            assert_matches_type(QbdStandardTerm, standard_term, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.standard_terms.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    def test_method_list(self, client: Conductor) -> None:
        standard_term = client.qbd.standard_terms.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(StandardTermListResponse, standard_term, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Conductor) -> None:
        standard_term = client.qbd.standard_terms.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            full_names="Payment Terms:Net 15",
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
        assert_matches_type(StandardTermListResponse, standard_term, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Conductor) -> None:
        response = client.qbd.standard_terms.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        standard_term = response.parse()
        assert_matches_type(StandardTermListResponse, standard_term, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Conductor) -> None:
        with client.qbd.standard_terms.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            standard_term = response.parse()
            assert_matches_type(StandardTermListResponse, standard_term, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncStandardTerms:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncConductor) -> None:
        standard_term = await async_client.qbd.standard_terms.create(
            name="Net 30",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(QbdStandardTerm, standard_term, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncConductor) -> None:
        standard_term = await async_client.qbd.standard_terms.create(
            name="Net 30",
            conductor_end_user_id="end_usr_1234567abcdefg",
            discount_days=10,
            discount_percentage="10",
            due_days=30,
            is_active=True,
        )
        assert_matches_type(QbdStandardTerm, standard_term, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.standard_terms.with_raw_response.create(
            name="Net 30",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        standard_term = await response.parse()
        assert_matches_type(QbdStandardTerm, standard_term, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.standard_terms.with_streaming_response.create(
            name="Net 30",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            standard_term = await response.parse()
            assert_matches_type(QbdStandardTerm, standard_term, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncConductor) -> None:
        standard_term = await async_client.qbd.standard_terms.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(QbdStandardTerm, standard_term, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.standard_terms.with_raw_response.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        standard_term = await response.parse()
        assert_matches_type(QbdStandardTerm, standard_term, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.standard_terms.with_streaming_response.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            standard_term = await response.parse()
            assert_matches_type(QbdStandardTerm, standard_term, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.standard_terms.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncConductor) -> None:
        standard_term = await async_client.qbd.standard_terms.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(StandardTermListResponse, standard_term, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncConductor) -> None:
        standard_term = await async_client.qbd.standard_terms.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            full_names="Payment Terms:Net 15",
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
        assert_matches_type(StandardTermListResponse, standard_term, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.standard_terms.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        standard_term = await response.parse()
        assert_matches_type(StandardTermListResponse, standard_term, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.standard_terms.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            standard_term = await response.parse()
            assert_matches_type(StandardTermListResponse, standard_term, path=["response"])

        assert cast(Any, response.is_closed) is True
