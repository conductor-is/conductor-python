# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from conductor import Conductor, AsyncConductor
from tests.utils import assert_matches_type
from conductor._utils import parse_date
from conductor.types.qbd import (
    QbdBillPaymentCreditCard,
)
from conductor.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBillPaymentCreditCards:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Conductor) -> None:
        bill_payment_credit_card = client.qbd.bill_payment_credit_cards.create(
            apply_to_transactions=[{"transaction_id": "123ABC-1234567890"}],
            credit_card_account_id="80000007-1234567890",
            transaction_date=parse_date("2019-12-27"),
            vendor_id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(QbdBillPaymentCreditCard, bill_payment_credit_card, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Conductor) -> None:
        bill_payment_credit_card = client.qbd.bill_payment_credit_cards.create(
            apply_to_transactions=[
                {
                    "transaction_id": "123ABC-1234567890",
                    "apply_credits": [
                        {
                            "applied_amount": "100.00",
                            "credit_memo_id": "ABCDEF-1234567890",
                            "override_credit_application": False,
                        }
                    ],
                    "discount_account_id": "80000008-1234567890",
                    "discount_amount": "50.00",
                    "discount_class_id": "80000008-1234567890",
                    "payment_amount": "25.00",
                }
            ],
            credit_card_account_id="80000007-1234567890",
            transaction_date=parse_date("2019-12-27"),
            vendor_id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
            exchange_rate=1.2345,
            external_id="12345678-abcd-1234-abcd-1234567890ab",
            memo="Payment for office supplies - Invoice INV-1234",
            payables_account_id="80000002-1234567890",
            ref_number="CARD-1234",
        )
        assert_matches_type(QbdBillPaymentCreditCard, bill_payment_credit_card, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Conductor) -> None:
        response = client.qbd.bill_payment_credit_cards.with_raw_response.create(
            apply_to_transactions=[{"transaction_id": "123ABC-1234567890"}],
            credit_card_account_id="80000007-1234567890",
            transaction_date=parse_date("2019-12-27"),
            vendor_id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bill_payment_credit_card = response.parse()
        assert_matches_type(QbdBillPaymentCreditCard, bill_payment_credit_card, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Conductor) -> None:
        with client.qbd.bill_payment_credit_cards.with_streaming_response.create(
            apply_to_transactions=[{"transaction_id": "123ABC-1234567890"}],
            credit_card_account_id="80000007-1234567890",
            transaction_date=parse_date("2019-12-27"),
            vendor_id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bill_payment_credit_card = response.parse()
            assert_matches_type(QbdBillPaymentCreditCard, bill_payment_credit_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Conductor) -> None:
        bill_payment_credit_card = client.qbd.bill_payment_credit_cards.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(QbdBillPaymentCreditCard, bill_payment_credit_card, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Conductor) -> None:
        response = client.qbd.bill_payment_credit_cards.with_raw_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bill_payment_credit_card = response.parse()
        assert_matches_type(QbdBillPaymentCreditCard, bill_payment_credit_card, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Conductor) -> None:
        with client.qbd.bill_payment_credit_cards.with_streaming_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bill_payment_credit_card = response.parse()
            assert_matches_type(QbdBillPaymentCreditCard, bill_payment_credit_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.bill_payment_credit_cards.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    def test_method_list(self, client: Conductor) -> None:
        bill_payment_credit_card = client.qbd.bill_payment_credit_cards.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(SyncCursorPage[QbdBillPaymentCreditCard], bill_payment_credit_card, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Conductor) -> None:
        bill_payment_credit_card = client.qbd.bill_payment_credit_cards.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_ids=["80000001-1234567890"],
            currency_ids=["80000001-1234567890"],
            cursor="12345678-abcd-abcd-example-1234567890ab",
            ids=["123ABC-1234567890"],
            include_line_items=True,
            limit=150,
            ref_number_contains="CARD-1234",
            ref_number_ends_with="1234",
            ref_number_from="CARD-0001",
            ref_numbers=["BILL PAYMENT CREDIT CARD-1234"],
            ref_number_starts_with="CARD",
            ref_number_to="CARD-9999",
            transaction_date_from=parse_date("2019-12-27"),
            transaction_date_to=parse_date("2019-12-27"),
            updated_after="updatedAfter",
            updated_before="updatedBefore",
            vendor_ids=["80000001-1234567890"],
        )
        assert_matches_type(SyncCursorPage[QbdBillPaymentCreditCard], bill_payment_credit_card, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Conductor) -> None:
        response = client.qbd.bill_payment_credit_cards.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bill_payment_credit_card = response.parse()
        assert_matches_type(SyncCursorPage[QbdBillPaymentCreditCard], bill_payment_credit_card, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Conductor) -> None:
        with client.qbd.bill_payment_credit_cards.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bill_payment_credit_card = response.parse()
            assert_matches_type(SyncCursorPage[QbdBillPaymentCreditCard], bill_payment_credit_card, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBillPaymentCreditCards:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncConductor) -> None:
        bill_payment_credit_card = await async_client.qbd.bill_payment_credit_cards.create(
            apply_to_transactions=[{"transaction_id": "123ABC-1234567890"}],
            credit_card_account_id="80000007-1234567890",
            transaction_date=parse_date("2019-12-27"),
            vendor_id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(QbdBillPaymentCreditCard, bill_payment_credit_card, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncConductor) -> None:
        bill_payment_credit_card = await async_client.qbd.bill_payment_credit_cards.create(
            apply_to_transactions=[
                {
                    "transaction_id": "123ABC-1234567890",
                    "apply_credits": [
                        {
                            "applied_amount": "100.00",
                            "credit_memo_id": "ABCDEF-1234567890",
                            "override_credit_application": False,
                        }
                    ],
                    "discount_account_id": "80000008-1234567890",
                    "discount_amount": "50.00",
                    "discount_class_id": "80000008-1234567890",
                    "payment_amount": "25.00",
                }
            ],
            credit_card_account_id="80000007-1234567890",
            transaction_date=parse_date("2019-12-27"),
            vendor_id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
            exchange_rate=1.2345,
            external_id="12345678-abcd-1234-abcd-1234567890ab",
            memo="Payment for office supplies - Invoice INV-1234",
            payables_account_id="80000002-1234567890",
            ref_number="CARD-1234",
        )
        assert_matches_type(QbdBillPaymentCreditCard, bill_payment_credit_card, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.bill_payment_credit_cards.with_raw_response.create(
            apply_to_transactions=[{"transaction_id": "123ABC-1234567890"}],
            credit_card_account_id="80000007-1234567890",
            transaction_date=parse_date("2019-12-27"),
            vendor_id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bill_payment_credit_card = await response.parse()
        assert_matches_type(QbdBillPaymentCreditCard, bill_payment_credit_card, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.bill_payment_credit_cards.with_streaming_response.create(
            apply_to_transactions=[{"transaction_id": "123ABC-1234567890"}],
            credit_card_account_id="80000007-1234567890",
            transaction_date=parse_date("2019-12-27"),
            vendor_id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bill_payment_credit_card = await response.parse()
            assert_matches_type(QbdBillPaymentCreditCard, bill_payment_credit_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncConductor) -> None:
        bill_payment_credit_card = await async_client.qbd.bill_payment_credit_cards.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(QbdBillPaymentCreditCard, bill_payment_credit_card, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.bill_payment_credit_cards.with_raw_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bill_payment_credit_card = await response.parse()
        assert_matches_type(QbdBillPaymentCreditCard, bill_payment_credit_card, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.bill_payment_credit_cards.with_streaming_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bill_payment_credit_card = await response.parse()
            assert_matches_type(QbdBillPaymentCreditCard, bill_payment_credit_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.bill_payment_credit_cards.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncConductor) -> None:
        bill_payment_credit_card = await async_client.qbd.bill_payment_credit_cards.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(AsyncCursorPage[QbdBillPaymentCreditCard], bill_payment_credit_card, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncConductor) -> None:
        bill_payment_credit_card = await async_client.qbd.bill_payment_credit_cards.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_ids=["80000001-1234567890"],
            currency_ids=["80000001-1234567890"],
            cursor="12345678-abcd-abcd-example-1234567890ab",
            ids=["123ABC-1234567890"],
            include_line_items=True,
            limit=150,
            ref_number_contains="CARD-1234",
            ref_number_ends_with="1234",
            ref_number_from="CARD-0001",
            ref_numbers=["BILL PAYMENT CREDIT CARD-1234"],
            ref_number_starts_with="CARD",
            ref_number_to="CARD-9999",
            transaction_date_from=parse_date("2019-12-27"),
            transaction_date_to=parse_date("2019-12-27"),
            updated_after="updatedAfter",
            updated_before="updatedBefore",
            vendor_ids=["80000001-1234567890"],
        )
        assert_matches_type(AsyncCursorPage[QbdBillPaymentCreditCard], bill_payment_credit_card, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.bill_payment_credit_cards.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bill_payment_credit_card = await response.parse()
        assert_matches_type(AsyncCursorPage[QbdBillPaymentCreditCard], bill_payment_credit_card, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.bill_payment_credit_cards.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bill_payment_credit_card = await response.parse()
            assert_matches_type(AsyncCursorPage[QbdBillPaymentCreditCard], bill_payment_credit_card, path=["response"])

        assert cast(Any, response.is_closed) is True
