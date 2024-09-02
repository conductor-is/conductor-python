# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from conductor import Conductor, AsyncConductor
from tests.utils import assert_matches_type
from conductor.types import AuthSession

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuthSessions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Conductor) -> None:
        auth_session = client.auth_sessions.create(
            end_user_id="end_usr_1234567abcdefg",
            publishable_key="{{YOUR_PUBLISHABLE_KEY}}",
        )
        assert_matches_type(AuthSession, auth_session, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Conductor) -> None:
        auth_session = client.auth_sessions.create(
            end_user_id="end_usr_1234567abcdefg",
            publishable_key="{{YOUR_PUBLISHABLE_KEY}}",
            link_expiry_mins=0,
            redirect_url="https://example.com/auth/conductor-callback",
        )
        assert_matches_type(AuthSession, auth_session, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Conductor) -> None:
        response = client.auth_sessions.with_raw_response.create(
            end_user_id="end_usr_1234567abcdefg",
            publishable_key="{{YOUR_PUBLISHABLE_KEY}}",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_session = response.parse()
        assert_matches_type(AuthSession, auth_session, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Conductor) -> None:
        with client.auth_sessions.with_streaming_response.create(
            end_user_id="end_usr_1234567abcdefg",
            publishable_key="{{YOUR_PUBLISHABLE_KEY}}",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth_session = response.parse()
            assert_matches_type(AuthSession, auth_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Conductor) -> None:
        auth_session = client.auth_sessions.retrieve(
            "auth_sess_1234567abcdefg",
        )
        assert_matches_type(AuthSession, auth_session, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Conductor) -> None:
        response = client.auth_sessions.with_raw_response.retrieve(
            "auth_sess_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_session = response.parse()
        assert_matches_type(AuthSession, auth_session, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Conductor) -> None:
        with client.auth_sessions.with_streaming_response.retrieve(
            "auth_sess_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth_session = response.parse()
            assert_matches_type(AuthSession, auth_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.auth_sessions.with_raw_response.retrieve(
                "",
            )


class TestAsyncAuthSessions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncConductor) -> None:
        auth_session = await async_client.auth_sessions.create(
            end_user_id="end_usr_1234567abcdefg",
            publishable_key="{{YOUR_PUBLISHABLE_KEY}}",
        )
        assert_matches_type(AuthSession, auth_session, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncConductor) -> None:
        auth_session = await async_client.auth_sessions.create(
            end_user_id="end_usr_1234567abcdefg",
            publishable_key="{{YOUR_PUBLISHABLE_KEY}}",
            link_expiry_mins=0,
            redirect_url="https://example.com/auth/conductor-callback",
        )
        assert_matches_type(AuthSession, auth_session, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncConductor) -> None:
        response = await async_client.auth_sessions.with_raw_response.create(
            end_user_id="end_usr_1234567abcdefg",
            publishable_key="{{YOUR_PUBLISHABLE_KEY}}",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_session = await response.parse()
        assert_matches_type(AuthSession, auth_session, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncConductor) -> None:
        async with async_client.auth_sessions.with_streaming_response.create(
            end_user_id="end_usr_1234567abcdefg",
            publishable_key="{{YOUR_PUBLISHABLE_KEY}}",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth_session = await response.parse()
            assert_matches_type(AuthSession, auth_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncConductor) -> None:
        auth_session = await async_client.auth_sessions.retrieve(
            "auth_sess_1234567abcdefg",
        )
        assert_matches_type(AuthSession, auth_session, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncConductor) -> None:
        response = await async_client.auth_sessions.with_raw_response.retrieve(
            "auth_sess_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_session = await response.parse()
        assert_matches_type(AuthSession, auth_session, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncConductor) -> None:
        async with async_client.auth_sessions.with_streaming_response.retrieve(
            "auth_sess_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth_session = await response.parse()
            assert_matches_type(AuthSession, auth_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.auth_sessions.with_raw_response.retrieve(
                "",
            )
