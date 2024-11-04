# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from conductor import Conductor, AsyncConductor
from tests.utils import assert_matches_type
from conductor._utils import parse_date
from conductor.types.qbd import QbdCheck
from conductor.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChecks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Conductor) -> None:
        check = client.qbd.checks.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(QbdCheck, check, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Conductor) -> None:
        response = client.qbd.checks.with_raw_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check = response.parse()
        assert_matches_type(QbdCheck, check, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Conductor) -> None:
        with client.qbd.checks.with_streaming_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check = response.parse()
            assert_matches_type(QbdCheck, check, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.checks.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    def test_method_list(self, client: Conductor) -> None:
        check = client.qbd.checks.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(SyncCursorPage[QbdCheck], check, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Conductor) -> None:
        check = client.qbd.checks.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_ids=["80000001-1234567890"],
            currency_ids=["80000001-1234567890"],
            cursor="12345678-abcd-abcd-example-1234567890ab",
            ids=["123ABC-1234567890"],
            include_line_items=True,
            include_linked_transactions=False,
            limit=150,
            payee_ids=["80000001-1234567890"],
            ref_number_contains="CHECK-1234",
            ref_number_ends_with="1234",
            ref_number_from="CHECK-0001",
            ref_numbers=["CHECK-1234"],
            ref_number_starts_with="CHECK",
            ref_number_to="CHECK-9999",
            transaction_date_from=parse_date("2019-12-27"),
            transaction_date_to=parse_date("2019-12-27"),
            updated_after="updatedAfter",
            updated_before="updatedBefore",
        )
        assert_matches_type(SyncCursorPage[QbdCheck], check, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Conductor) -> None:
        response = client.qbd.checks.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check = response.parse()
        assert_matches_type(SyncCursorPage[QbdCheck], check, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Conductor) -> None:
        with client.qbd.checks.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check = response.parse()
            assert_matches_type(SyncCursorPage[QbdCheck], check, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncChecks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncConductor) -> None:
        check = await async_client.qbd.checks.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(QbdCheck, check, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.checks.with_raw_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check = await response.parse()
        assert_matches_type(QbdCheck, check, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.checks.with_streaming_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check = await response.parse()
            assert_matches_type(QbdCheck, check, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.checks.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncConductor) -> None:
        check = await async_client.qbd.checks.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(AsyncCursorPage[QbdCheck], check, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncConductor) -> None:
        check = await async_client.qbd.checks.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_ids=["80000001-1234567890"],
            currency_ids=["80000001-1234567890"],
            cursor="12345678-abcd-abcd-example-1234567890ab",
            ids=["123ABC-1234567890"],
            include_line_items=True,
            include_linked_transactions=False,
            limit=150,
            payee_ids=["80000001-1234567890"],
            ref_number_contains="CHECK-1234",
            ref_number_ends_with="1234",
            ref_number_from="CHECK-0001",
            ref_numbers=["CHECK-1234"],
            ref_number_starts_with="CHECK",
            ref_number_to="CHECK-9999",
            transaction_date_from=parse_date("2019-12-27"),
            transaction_date_to=parse_date("2019-12-27"),
            updated_after="updatedAfter",
            updated_before="updatedBefore",
        )
        assert_matches_type(AsyncCursorPage[QbdCheck], check, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.checks.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check = await response.parse()
        assert_matches_type(AsyncCursorPage[QbdCheck], check, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.checks.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check = await response.parse()
            assert_matches_type(AsyncCursorPage[QbdCheck], check, path=["response"])

        assert cast(Any, response.is_closed) is True
