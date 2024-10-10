# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from conductor import Conductor, AsyncConductor
from tests.utils import assert_matches_type
from conductor._utils import parse_date
from conductor.types.qbd import QbdCustomer
from conductor.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustomers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Conductor) -> None:
        customer = client.qbd.customers.create(
            name="Kitchen-Renovation",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(QbdCustomer, customer, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Conductor) -> None:
        customer = client.qbd.customers.create(
            name="Kitchen-Renovation",
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_number="1010",
            additional_notes=[{"note": "This is a note."}, {"note": "This is a note."}, {"note": "This is a note."}],
            alternate_contact="Bob Johnson",
            alternate_phone="+1-555-987-6543",
            alternate_shipping_addresses=[
                {
                    "name": "Acme Inc.",
                    "city": "San Francisco",
                    "country": "United States",
                    "default_ship_to": True,
                    "line1": "548 Market St.",
                    "line2": "Suite 100",
                    "line3": "line3",
                    "line4": "line4",
                    "line5": "line5",
                    "note": "Conductor HQ",
                    "postal_code": "94110",
                    "state": "CA",
                },
                {
                    "name": "Acme Inc.",
                    "city": "San Francisco",
                    "country": "United States",
                    "default_ship_to": True,
                    "line1": "548 Market St.",
                    "line2": "Suite 100",
                    "line3": "line3",
                    "line4": "line4",
                    "line5": "line5",
                    "note": "Conductor HQ",
                    "postal_code": "94110",
                    "state": "CA",
                },
                {
                    "name": "Acme Inc.",
                    "city": "San Francisco",
                    "country": "United States",
                    "default_ship_to": True,
                    "line1": "548 Market St.",
                    "line2": "Suite 100",
                    "line3": "line3",
                    "line4": "line4",
                    "line5": "line5",
                    "note": "Conductor HQ",
                    "postal_code": "94110",
                    "state": "CA",
                },
            ],
            billing_address={
                "city": "San Francisco",
                "country": "United States",
                "line1": "548 Market St.",
                "line2": "Suite 100",
                "line3": "line3",
                "line4": "line4",
                "line5": "line5",
                "note": "Conductor HQ",
                "postal_code": "94110",
                "state": "CA",
            },
            cc_email="manager@example.com",
            class_id="80000001-1234567890",
            company_name="Acme Corporation",
            contact="Jane Smith",
            contacts=[
                {
                    "first_name": "John",
                    "custom_contact_fields": [
                        {
                            "name": "Main Phone",
                            "value": "555-555-5555",
                        },
                        {
                            "name": "Main Phone",
                            "value": "555-555-5555",
                        },
                        {
                            "name": "Main Phone",
                            "value": "555-555-5555",
                        },
                    ],
                    "job_title": "CEO",
                    "last_name": "Doe",
                    "middle_name": "Q.",
                    "salutation": "Mr.",
                },
                {
                    "first_name": "John",
                    "custom_contact_fields": [
                        {
                            "name": "Main Phone",
                            "value": "555-555-5555",
                        },
                        {
                            "name": "Main Phone",
                            "value": "555-555-5555",
                        },
                        {
                            "name": "Main Phone",
                            "value": "555-555-5555",
                        },
                    ],
                    "job_title": "CEO",
                    "last_name": "Doe",
                    "middle_name": "Q.",
                    "salutation": "Mr.",
                },
                {
                    "first_name": "John",
                    "custom_contact_fields": [
                        {
                            "name": "Main Phone",
                            "value": "555-555-5555",
                        },
                        {
                            "name": "Main Phone",
                            "value": "555-555-5555",
                        },
                        {
                            "name": "Main Phone",
                            "value": "555-555-5555",
                        },
                    ],
                    "job_title": "CEO",
                    "last_name": "Doe",
                    "middle_name": "Q.",
                    "salutation": "Mr.",
                },
            ],
            credit_card={
                "address": "1234 Main St, Anytown, USA, 12345",
                "address_zip": "12345",
                "expiration_month": 12,
                "expiration_year": 2024,
                "name": "John Doe",
                "number": "xxxxxxxxxxxx1234",
            },
            credit_limit="5000.00",
            currency_id="80000012-1234567890",
            custom_contact_fields=[
                {
                    "name": "Main Phone",
                    "value": "555-555-5555",
                },
                {
                    "name": "Main Phone",
                    "value": "555-555-5555",
                },
                {
                    "name": "Main Phone",
                    "value": "555-555-5555",
                },
            ],
            customer_type_id="80000025-1234567890",
            email="customer@example.com",
            external_id="12345678-abcd-1234-abcd-1234567890ab",
            fax="+1-555-555-1212",
            first_name="John",
            is_active=True,
            item_sales_tax_id="80000010-1234567890",
            job_description="Kitchen renovation project for residential client.",
            job_end_date=parse_date("2019-12-27"),
            job_projected_end_date=parse_date("2019-12-27"),
            job_start_date=parse_date("2019-12-27"),
            job_status="awarded",
            job_title="Purchasing Manager",
            job_type_id="80000035-1234567890",
            last_name="Doe",
            middle_name="A.",
            note="Our favorite customer.",
            opening_balance="1000.00",
            opening_balance_date="openingBalanceDate",
            parent_id="80000002-1234567890",
            phone="+1-555-123-4567",
            preferred_delivery_method="email",
            preferred_payment_method_id="80000014-1234567890",
            price_level_id="80000040-1234567890",
            resale_number="123456789",
            sales_representative_id="80000030-1234567890",
            sales_tax_code_id="80000004-1234567890",
            sales_tax_country="australia",
            salutation="Dr.",
            shipping_address={
                "city": "San Francisco",
                "country": "United States",
                "line1": "548 Market St.",
                "line2": "Suite 100",
                "line3": "line3",
                "line4": "line4",
                "line5": "line5",
                "note": "Conductor HQ",
                "postal_code": "94110",
                "state": "CA",
            },
            tax_registration_number="GB123456789",
            terms_id="80000013-1234567890",
        )
        assert_matches_type(QbdCustomer, customer, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Conductor) -> None:
        response = client.qbd.customers.with_raw_response.create(
            name="Kitchen-Renovation",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(QbdCustomer, customer, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Conductor) -> None:
        with client.qbd.customers.with_streaming_response.create(
            name="Kitchen-Renovation",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(QbdCustomer, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Conductor) -> None:
        customer = client.qbd.customers.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(QbdCustomer, customer, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Conductor) -> None:
        response = client.qbd.customers.with_raw_response.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(QbdCustomer, customer, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Conductor) -> None:
        with client.qbd.customers.with_streaming_response.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(QbdCustomer, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.customers.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    def test_method_list(self, client: Conductor) -> None:
        customer = client.qbd.customers.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(SyncCursorPage[QbdCustomer], customer, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Conductor) -> None:
        customer = client.qbd.customers.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            class_ids="80000001-1234567890",
            currency_ids="80000001-1234567890",
            cursor="12345678-abcd-abcd-example-1234567890ab",
            full_names="ABC Corporation:Website Redesign Project",
            ids="80000001-1234567890",
            limit=1,
            name_contains="nameContains",
            name_ends_with="nameEndsWith",
            name_from="nameFrom",
            name_starts_with="nameStartsWith",
            name_to="nameTo",
            status="active",
            total_balance="totalBalance",
            total_balance_gt="totalBalanceGt",
            total_balance_gte="totalBalanceGte",
            total_balance_lt="totalBalanceLt",
            total_balance_lte="totalBalanceLte",
            updated_after="updatedAfter",
            updated_before="updatedBefore",
        )
        assert_matches_type(SyncCursorPage[QbdCustomer], customer, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Conductor) -> None:
        response = client.qbd.customers.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(SyncCursorPage[QbdCustomer], customer, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Conductor) -> None:
        with client.qbd.customers.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(SyncCursorPage[QbdCustomer], customer, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCustomers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncConductor) -> None:
        customer = await async_client.qbd.customers.create(
            name="Kitchen-Renovation",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(QbdCustomer, customer, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncConductor) -> None:
        customer = await async_client.qbd.customers.create(
            name="Kitchen-Renovation",
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_number="1010",
            additional_notes=[{"note": "This is a note."}, {"note": "This is a note."}, {"note": "This is a note."}],
            alternate_contact="Bob Johnson",
            alternate_phone="+1-555-987-6543",
            alternate_shipping_addresses=[
                {
                    "name": "Acme Inc.",
                    "city": "San Francisco",
                    "country": "United States",
                    "default_ship_to": True,
                    "line1": "548 Market St.",
                    "line2": "Suite 100",
                    "line3": "line3",
                    "line4": "line4",
                    "line5": "line5",
                    "note": "Conductor HQ",
                    "postal_code": "94110",
                    "state": "CA",
                },
                {
                    "name": "Acme Inc.",
                    "city": "San Francisco",
                    "country": "United States",
                    "default_ship_to": True,
                    "line1": "548 Market St.",
                    "line2": "Suite 100",
                    "line3": "line3",
                    "line4": "line4",
                    "line5": "line5",
                    "note": "Conductor HQ",
                    "postal_code": "94110",
                    "state": "CA",
                },
                {
                    "name": "Acme Inc.",
                    "city": "San Francisco",
                    "country": "United States",
                    "default_ship_to": True,
                    "line1": "548 Market St.",
                    "line2": "Suite 100",
                    "line3": "line3",
                    "line4": "line4",
                    "line5": "line5",
                    "note": "Conductor HQ",
                    "postal_code": "94110",
                    "state": "CA",
                },
            ],
            billing_address={
                "city": "San Francisco",
                "country": "United States",
                "line1": "548 Market St.",
                "line2": "Suite 100",
                "line3": "line3",
                "line4": "line4",
                "line5": "line5",
                "note": "Conductor HQ",
                "postal_code": "94110",
                "state": "CA",
            },
            cc_email="manager@example.com",
            class_id="80000001-1234567890",
            company_name="Acme Corporation",
            contact="Jane Smith",
            contacts=[
                {
                    "first_name": "John",
                    "custom_contact_fields": [
                        {
                            "name": "Main Phone",
                            "value": "555-555-5555",
                        },
                        {
                            "name": "Main Phone",
                            "value": "555-555-5555",
                        },
                        {
                            "name": "Main Phone",
                            "value": "555-555-5555",
                        },
                    ],
                    "job_title": "CEO",
                    "last_name": "Doe",
                    "middle_name": "Q.",
                    "salutation": "Mr.",
                },
                {
                    "first_name": "John",
                    "custom_contact_fields": [
                        {
                            "name": "Main Phone",
                            "value": "555-555-5555",
                        },
                        {
                            "name": "Main Phone",
                            "value": "555-555-5555",
                        },
                        {
                            "name": "Main Phone",
                            "value": "555-555-5555",
                        },
                    ],
                    "job_title": "CEO",
                    "last_name": "Doe",
                    "middle_name": "Q.",
                    "salutation": "Mr.",
                },
                {
                    "first_name": "John",
                    "custom_contact_fields": [
                        {
                            "name": "Main Phone",
                            "value": "555-555-5555",
                        },
                        {
                            "name": "Main Phone",
                            "value": "555-555-5555",
                        },
                        {
                            "name": "Main Phone",
                            "value": "555-555-5555",
                        },
                    ],
                    "job_title": "CEO",
                    "last_name": "Doe",
                    "middle_name": "Q.",
                    "salutation": "Mr.",
                },
            ],
            credit_card={
                "address": "1234 Main St, Anytown, USA, 12345",
                "address_zip": "12345",
                "expiration_month": 12,
                "expiration_year": 2024,
                "name": "John Doe",
                "number": "xxxxxxxxxxxx1234",
            },
            credit_limit="5000.00",
            currency_id="80000012-1234567890",
            custom_contact_fields=[
                {
                    "name": "Main Phone",
                    "value": "555-555-5555",
                },
                {
                    "name": "Main Phone",
                    "value": "555-555-5555",
                },
                {
                    "name": "Main Phone",
                    "value": "555-555-5555",
                },
            ],
            customer_type_id="80000025-1234567890",
            email="customer@example.com",
            external_id="12345678-abcd-1234-abcd-1234567890ab",
            fax="+1-555-555-1212",
            first_name="John",
            is_active=True,
            item_sales_tax_id="80000010-1234567890",
            job_description="Kitchen renovation project for residential client.",
            job_end_date=parse_date("2019-12-27"),
            job_projected_end_date=parse_date("2019-12-27"),
            job_start_date=parse_date("2019-12-27"),
            job_status="awarded",
            job_title="Purchasing Manager",
            job_type_id="80000035-1234567890",
            last_name="Doe",
            middle_name="A.",
            note="Our favorite customer.",
            opening_balance="1000.00",
            opening_balance_date="openingBalanceDate",
            parent_id="80000002-1234567890",
            phone="+1-555-123-4567",
            preferred_delivery_method="email",
            preferred_payment_method_id="80000014-1234567890",
            price_level_id="80000040-1234567890",
            resale_number="123456789",
            sales_representative_id="80000030-1234567890",
            sales_tax_code_id="80000004-1234567890",
            sales_tax_country="australia",
            salutation="Dr.",
            shipping_address={
                "city": "San Francisco",
                "country": "United States",
                "line1": "548 Market St.",
                "line2": "Suite 100",
                "line3": "line3",
                "line4": "line4",
                "line5": "line5",
                "note": "Conductor HQ",
                "postal_code": "94110",
                "state": "CA",
            },
            tax_registration_number="GB123456789",
            terms_id="80000013-1234567890",
        )
        assert_matches_type(QbdCustomer, customer, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.customers.with_raw_response.create(
            name="Kitchen-Renovation",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(QbdCustomer, customer, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.customers.with_streaming_response.create(
            name="Kitchen-Renovation",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(QbdCustomer, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncConductor) -> None:
        customer = await async_client.qbd.customers.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(QbdCustomer, customer, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.customers.with_raw_response.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(QbdCustomer, customer, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.customers.with_streaming_response.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(QbdCustomer, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.customers.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncConductor) -> None:
        customer = await async_client.qbd.customers.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(AsyncCursorPage[QbdCustomer], customer, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncConductor) -> None:
        customer = await async_client.qbd.customers.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            class_ids="80000001-1234567890",
            currency_ids="80000001-1234567890",
            cursor="12345678-abcd-abcd-example-1234567890ab",
            full_names="ABC Corporation:Website Redesign Project",
            ids="80000001-1234567890",
            limit=1,
            name_contains="nameContains",
            name_ends_with="nameEndsWith",
            name_from="nameFrom",
            name_starts_with="nameStartsWith",
            name_to="nameTo",
            status="active",
            total_balance="totalBalance",
            total_balance_gt="totalBalanceGt",
            total_balance_gte="totalBalanceGte",
            total_balance_lt="totalBalanceLt",
            total_balance_lte="totalBalanceLte",
            updated_after="updatedAfter",
            updated_before="updatedBefore",
        )
        assert_matches_type(AsyncCursorPage[QbdCustomer], customer, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.customers.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(AsyncCursorPage[QbdCustomer], customer, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.customers.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(AsyncCursorPage[QbdCustomer], customer, path=["response"])

        assert cast(Any, response.is_closed) is True
