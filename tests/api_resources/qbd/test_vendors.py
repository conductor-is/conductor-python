# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from conductor import Conductor, AsyncConductor
from tests.utils import assert_matches_type
from conductor.types.qbd import QbdVendor
from conductor.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVendors:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Conductor) -> None:
        vendor = client.qbd.vendors.create(
            name="Acme Supplies Inc.",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(QbdVendor, vendor, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Conductor) -> None:
        vendor = client.qbd.vendors.create(
            name="Acme Supplies Inc.",
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_number="1010",
            additional_notes=[{"note": "This is a note."}, {"note": "This is a note."}, {"note": "This is a note."}],
            alternate_contact="Bob Johnson",
            alternate_phone="+1-555-987-6543",
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
            billing_rate_id="80000015-1234567890",
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
            email="vendor@example.com",
            external_id="12345678-abcd-1234-abcd-1234567890ab",
            fax="+1-555-555-1212",
            first_name="John",
            is_active=True,
            is_eligible_for1099=True,
            is_sales_tax_agency=False,
            is_tax_on_tax=False,
            is_tax_tracked_on_purchases=True,
            is_tax_tracked_on_sales=True,
            job_title="Purchasing Manager",
            last_name="Doe",
            middle_name="A.",
            name_on_check="Acme Supplies Ltd.",
            note="Preferred vendor for office supplies.",
            opening_balance="1000.00",
            opening_balance_date="openingBalanceDate",
            phone="+1-555-123-4567",
            prefill_account_ids=["80000029-1234567890"],
            reporting_period="monthly",
            sales_tax_code_id="80000004-1234567890",
            sales_tax_country="australia",
            sales_tax_return_id="80000026-1234567890",
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
            tax_identification_number="12-3456789",
            tax_on_purchases_account_id="80000027-1234567890",
            tax_on_sales_account_id="80000028-1234567890",
            tax_registration_number="GB123456789",
            terms_id="80000013-1234567890",
            vendor_type_id="80000025-1234567890",
        )
        assert_matches_type(QbdVendor, vendor, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Conductor) -> None:
        response = client.qbd.vendors.with_raw_response.create(
            name="Acme Supplies Inc.",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vendor = response.parse()
        assert_matches_type(QbdVendor, vendor, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Conductor) -> None:
        with client.qbd.vendors.with_streaming_response.create(
            name="Acme Supplies Inc.",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vendor = response.parse()
            assert_matches_type(QbdVendor, vendor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Conductor) -> None:
        vendor = client.qbd.vendors.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(QbdVendor, vendor, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Conductor) -> None:
        response = client.qbd.vendors.with_raw_response.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vendor = response.parse()
        assert_matches_type(QbdVendor, vendor, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Conductor) -> None:
        with client.qbd.vendors.with_streaming_response.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vendor = response.parse()
            assert_matches_type(QbdVendor, vendor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.vendors.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    def test_method_list(self, client: Conductor) -> None:
        vendor = client.qbd.vendors.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(SyncCursorPage[QbdVendor], vendor, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Conductor) -> None:
        vendor = client.qbd.vendors.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            class_ids="80000001-1234567890",
            currency_ids="80000001-1234567890",
            cursor="12345678-abcd-abcd-example-1234567890ab",
            full_names="Suppliers:ABC Office Supplies",
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
        assert_matches_type(SyncCursorPage[QbdVendor], vendor, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Conductor) -> None:
        response = client.qbd.vendors.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vendor = response.parse()
        assert_matches_type(SyncCursorPage[QbdVendor], vendor, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Conductor) -> None:
        with client.qbd.vendors.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vendor = response.parse()
            assert_matches_type(SyncCursorPage[QbdVendor], vendor, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncVendors:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncConductor) -> None:
        vendor = await async_client.qbd.vendors.create(
            name="Acme Supplies Inc.",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(QbdVendor, vendor, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncConductor) -> None:
        vendor = await async_client.qbd.vendors.create(
            name="Acme Supplies Inc.",
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_number="1010",
            additional_notes=[{"note": "This is a note."}, {"note": "This is a note."}, {"note": "This is a note."}],
            alternate_contact="Bob Johnson",
            alternate_phone="+1-555-987-6543",
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
            billing_rate_id="80000015-1234567890",
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
            email="vendor@example.com",
            external_id="12345678-abcd-1234-abcd-1234567890ab",
            fax="+1-555-555-1212",
            first_name="John",
            is_active=True,
            is_eligible_for1099=True,
            is_sales_tax_agency=False,
            is_tax_on_tax=False,
            is_tax_tracked_on_purchases=True,
            is_tax_tracked_on_sales=True,
            job_title="Purchasing Manager",
            last_name="Doe",
            middle_name="A.",
            name_on_check="Acme Supplies Ltd.",
            note="Preferred vendor for office supplies.",
            opening_balance="1000.00",
            opening_balance_date="openingBalanceDate",
            phone="+1-555-123-4567",
            prefill_account_ids=["80000029-1234567890"],
            reporting_period="monthly",
            sales_tax_code_id="80000004-1234567890",
            sales_tax_country="australia",
            sales_tax_return_id="80000026-1234567890",
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
            tax_identification_number="12-3456789",
            tax_on_purchases_account_id="80000027-1234567890",
            tax_on_sales_account_id="80000028-1234567890",
            tax_registration_number="GB123456789",
            terms_id="80000013-1234567890",
            vendor_type_id="80000025-1234567890",
        )
        assert_matches_type(QbdVendor, vendor, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.vendors.with_raw_response.create(
            name="Acme Supplies Inc.",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vendor = await response.parse()
        assert_matches_type(QbdVendor, vendor, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.vendors.with_streaming_response.create(
            name="Acme Supplies Inc.",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vendor = await response.parse()
            assert_matches_type(QbdVendor, vendor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncConductor) -> None:
        vendor = await async_client.qbd.vendors.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(QbdVendor, vendor, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.vendors.with_raw_response.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vendor = await response.parse()
        assert_matches_type(QbdVendor, vendor, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.vendors.with_streaming_response.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vendor = await response.parse()
            assert_matches_type(QbdVendor, vendor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.vendors.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncConductor) -> None:
        vendor = await async_client.qbd.vendors.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(AsyncCursorPage[QbdVendor], vendor, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncConductor) -> None:
        vendor = await async_client.qbd.vendors.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            class_ids="80000001-1234567890",
            currency_ids="80000001-1234567890",
            cursor="12345678-abcd-abcd-example-1234567890ab",
            full_names="Suppliers:ABC Office Supplies",
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
        assert_matches_type(AsyncCursorPage[QbdVendor], vendor, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.vendors.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vendor = await response.parse()
        assert_matches_type(AsyncCursorPage[QbdVendor], vendor, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.vendors.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vendor = await response.parse()
            assert_matches_type(AsyncCursorPage[QbdVendor], vendor, path=["response"])

        assert cast(Any, response.is_closed) is True
