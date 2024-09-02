# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from conductor import Conductor, AsyncConductor
from tests.utils import assert_matches_type
from conductor.types import IntegrationConnection, IntegrationConnectionListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIntegrationConnections:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Conductor) -> None:
        integration_connection = client.integration_connections.retrieve(
            "int_conn_1234567abcdefg",
        )
        assert_matches_type(IntegrationConnection, integration_connection, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Conductor) -> None:
        response = client.integration_connections.with_raw_response.retrieve(
            "int_conn_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration_connection = response.parse()
        assert_matches_type(IntegrationConnection, integration_connection, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Conductor) -> None:
        with client.integration_connections.with_streaming_response.retrieve(
            "int_conn_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration_connection = response.parse()
            assert_matches_type(IntegrationConnection, integration_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.integration_connections.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Conductor) -> None:
        integration_connection = client.integration_connections.list()
        assert_matches_type(IntegrationConnectionListResponse, integration_connection, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Conductor) -> None:
        response = client.integration_connections.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration_connection = response.parse()
        assert_matches_type(IntegrationConnectionListResponse, integration_connection, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Conductor) -> None:
        with client.integration_connections.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration_connection = response.parse()
            assert_matches_type(IntegrationConnectionListResponse, integration_connection, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncIntegrationConnections:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncConductor) -> None:
        integration_connection = await async_client.integration_connections.retrieve(
            "int_conn_1234567abcdefg",
        )
        assert_matches_type(IntegrationConnection, integration_connection, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncConductor) -> None:
        response = await async_client.integration_connections.with_raw_response.retrieve(
            "int_conn_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration_connection = await response.parse()
        assert_matches_type(IntegrationConnection, integration_connection, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncConductor) -> None:
        async with async_client.integration_connections.with_streaming_response.retrieve(
            "int_conn_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration_connection = await response.parse()
            assert_matches_type(IntegrationConnection, integration_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.integration_connections.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncConductor) -> None:
        integration_connection = await async_client.integration_connections.list()
        assert_matches_type(IntegrationConnectionListResponse, integration_connection, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncConductor) -> None:
        response = await async_client.integration_connections.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration_connection = await response.parse()
        assert_matches_type(IntegrationConnectionListResponse, integration_connection, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncConductor) -> None:
        async with async_client.integration_connections.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration_connection = await response.parse()
            assert_matches_type(IntegrationConnectionListResponse, integration_connection, path=["response"])

        assert cast(Any, response.is_closed) is True
