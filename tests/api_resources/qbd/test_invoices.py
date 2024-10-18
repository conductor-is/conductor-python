# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from conductor import Conductor, AsyncConductor
from tests.utils import assert_matches_type
from conductor._utils import parse_date
from conductor.types.qbd import QbdInvoice
from conductor.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInvoices:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Conductor) -> None:
        invoice = client.qbd.invoices.create(
            customer_id="80000001-1234567890",
            transaction_date=parse_date("2019-12-27"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(QbdInvoice, invoice, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Conductor) -> None:
        invoice = client.qbd.invoices.create(
            customer_id="80000001-1234567890",
            transaction_date=parse_date("2019-12-27"),
            conductor_end_user_id="end_usr_1234567abcdefg",
            accounts_receivable_account_id="80000002-1234567890",
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
            class_id="80000001-1234567890",
            customer_message_id="80000001-1234567890",
            document_template_id="80000001-1234567890",
            due_date=parse_date("2019-12-27"),
            exchange_rate=1.2345,
            external_id="12345678-abcd-1234-abcd-1234567890ab",
            invoice_line_groups=[
                {
                    "item_group_id": "itemGroupId",
                    "custom_fields": [
                        {
                            "name": "Customer Rating",
                            "owner_id": "0",
                            "value": "Premium",
                        },
                        {
                            "name": "Customer Rating",
                            "owner_id": "0",
                            "value": "Premium",
                        },
                        {
                            "name": "Customer Rating",
                            "owner_id": "0",
                            "value": "Premium",
                        },
                    ],
                    "inventory_site_id": "inventorySiteId",
                    "inventory_site_location_id": "inventorySiteLocationId",
                    "quantity": 0,
                    "unit_of_measure": "unitOfMeasure",
                },
                {
                    "item_group_id": "itemGroupId",
                    "custom_fields": [
                        {
                            "name": "Customer Rating",
                            "owner_id": "0",
                            "value": "Premium",
                        },
                        {
                            "name": "Customer Rating",
                            "owner_id": "0",
                            "value": "Premium",
                        },
                        {
                            "name": "Customer Rating",
                            "owner_id": "0",
                            "value": "Premium",
                        },
                    ],
                    "inventory_site_id": "inventorySiteId",
                    "inventory_site_location_id": "inventorySiteLocationId",
                    "quantity": 0,
                    "unit_of_measure": "unitOfMeasure",
                },
                {
                    "item_group_id": "itemGroupId",
                    "custom_fields": [
                        {
                            "name": "Customer Rating",
                            "owner_id": "0",
                            "value": "Premium",
                        },
                        {
                            "name": "Customer Rating",
                            "owner_id": "0",
                            "value": "Premium",
                        },
                        {
                            "name": "Customer Rating",
                            "owner_id": "0",
                            "value": "Premium",
                        },
                    ],
                    "inventory_site_id": "inventorySiteId",
                    "inventory_site_location_id": "inventorySiteLocationId",
                    "quantity": 0,
                    "unit_of_measure": "unitOfMeasure",
                },
            ],
            invoice_lines=[
                {
                    "amount": "1000.00",
                    "class_id": "80000001-1234567890",
                    "custom_fields": [
                        {
                            "name": "Customer Rating",
                            "owner_id": "0",
                            "value": "Premium",
                        },
                        {
                            "name": "Customer Rating",
                            "owner_id": "0",
                            "value": "Premium",
                        },
                        {
                            "name": "Customer Rating",
                            "owner_id": "0",
                            "value": "Premium",
                        },
                    ],
                    "description": "High-quality widget with custom engraving",
                    "inventory_site_id": "80000001-1234567890",
                    "inventory_site_location_id": "80000002-1234567890",
                    "item_id": "80000010-1234567890",
                    "link_to_transaction_line": {
                        "transaction_id": "transactionId",
                        "transaction_line_id": "transactionLineId",
                    },
                    "lot_number": "LOT2023-001",
                    "other_custom_field1": "Special handling required",
                    "other_custom_field2": "Special handling required",
                    "override_item_account_id": "80000001-1234567890",
                    "price_level_id": "80000040-1234567890",
                    "price_rule_conflict_behavior": "base_price",
                    "quantity": 5,
                    "rate": "10.00",
                    "rate_percent": "10.5",
                    "sales_tax_code_id": "80000004-1234567890",
                    "serial_number": "SN1234567890",
                    "service_date": parse_date("2019-12-27"),
                    "unit_of_measure": "Each",
                },
                {
                    "amount": "1000.00",
                    "class_id": "80000001-1234567890",
                    "custom_fields": [
                        {
                            "name": "Customer Rating",
                            "owner_id": "0",
                            "value": "Premium",
                        },
                        {
                            "name": "Customer Rating",
                            "owner_id": "0",
                            "value": "Premium",
                        },
                        {
                            "name": "Customer Rating",
                            "owner_id": "0",
                            "value": "Premium",
                        },
                    ],
                    "description": "High-quality widget with custom engraving",
                    "inventory_site_id": "80000001-1234567890",
                    "inventory_site_location_id": "80000002-1234567890",
                    "item_id": "80000010-1234567890",
                    "link_to_transaction_line": {
                        "transaction_id": "transactionId",
                        "transaction_line_id": "transactionLineId",
                    },
                    "lot_number": "LOT2023-001",
                    "other_custom_field1": "Special handling required",
                    "other_custom_field2": "Special handling required",
                    "override_item_account_id": "80000001-1234567890",
                    "price_level_id": "80000040-1234567890",
                    "price_rule_conflict_behavior": "base_price",
                    "quantity": 5,
                    "rate": "10.00",
                    "rate_percent": "10.5",
                    "sales_tax_code_id": "80000004-1234567890",
                    "serial_number": "SN1234567890",
                    "service_date": parse_date("2019-12-27"),
                    "unit_of_measure": "Each",
                },
                {
                    "amount": "1000.00",
                    "class_id": "80000001-1234567890",
                    "custom_fields": [
                        {
                            "name": "Customer Rating",
                            "owner_id": "0",
                            "value": "Premium",
                        },
                        {
                            "name": "Customer Rating",
                            "owner_id": "0",
                            "value": "Premium",
                        },
                        {
                            "name": "Customer Rating",
                            "owner_id": "0",
                            "value": "Premium",
                        },
                    ],
                    "description": "High-quality widget with custom engraving",
                    "inventory_site_id": "80000001-1234567890",
                    "inventory_site_location_id": "80000002-1234567890",
                    "item_id": "80000010-1234567890",
                    "link_to_transaction_line": {
                        "transaction_id": "transactionId",
                        "transaction_line_id": "transactionLineId",
                    },
                    "lot_number": "LOT2023-001",
                    "other_custom_field1": "Special handling required",
                    "other_custom_field2": "Special handling required",
                    "override_item_account_id": "80000001-1234567890",
                    "price_level_id": "80000040-1234567890",
                    "price_rule_conflict_behavior": "base_price",
                    "quantity": 5,
                    "rate": "10.00",
                    "rate_percent": "10.5",
                    "sales_tax_code_id": "80000004-1234567890",
                    "serial_number": "SN1234567890",
                    "service_date": parse_date("2019-12-27"),
                    "unit_of_measure": "Each",
                },
            ],
            is_finance_charge=True,
            is_pending=False,
            is_to_be_emailed=True,
            is_to_be_printed=True,
            item_sales_tax_id="80000010-1234567890",
            link_to_transaction_ids=["string", "string", "string"],
            memo="Customer requested rush delivery",
            other_custom_field="Special handling required",
            purchase_order_number="PO-1234",
            ref_number="INV-1234",
            sales_representative_id="80000030-1234567890",
            sales_tax_code_id="80000004-1234567890",
            set_credits=[
                {
                    "applied_amount": "100.00",
                    "credit_id": "ABCDEF-1234567890",
                    "override": False,
                },
                {
                    "applied_amount": "100.00",
                    "credit_id": "ABCDEF-1234567890",
                    "override": False,
                },
                {
                    "applied_amount": "100.00",
                    "credit_id": "ABCDEF-1234567890",
                    "override": False,
                },
            ],
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
            shipping_date=parse_date("2019-12-27"),
            shipping_method_id="80000007-1234567890",
            shipping_origin="San Francisco, CA",
            terms_id="80000013-1234567890",
        )
        assert_matches_type(QbdInvoice, invoice, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Conductor) -> None:
        response = client.qbd.invoices.with_raw_response.create(
            customer_id="80000001-1234567890",
            transaction_date=parse_date("2019-12-27"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(QbdInvoice, invoice, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Conductor) -> None:
        with client.qbd.invoices.with_streaming_response.create(
            customer_id="80000001-1234567890",
            transaction_date=parse_date("2019-12-27"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(QbdInvoice, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Conductor) -> None:
        invoice = client.qbd.invoices.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(QbdInvoice, invoice, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Conductor) -> None:
        response = client.qbd.invoices.with_raw_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(QbdInvoice, invoice, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Conductor) -> None:
        with client.qbd.invoices.with_streaming_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(QbdInvoice, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.invoices.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    def test_method_list(self, client: Conductor) -> None:
        invoice = client.qbd.invoices.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(SyncCursorPage[QbdInvoice], invoice, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Conductor) -> None:
        invoice = client.qbd.invoices.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_ids="80000001-1234567890",
            currency_ids="80000001-1234567890",
            cursor="12345678-abcd-abcd-example-1234567890ab",
            customer_ids="80000001-1234567890",
            ids="123ABC-1234567890",
            include_line_items=True,
            include_linked_transactions=True,
            limit=1,
            payment_status="all",
            ref_number_contains="CHARGE",
            ref_number_ends_with="1234",
            ref_number_from="CHARGE-0001",
            ref_numbers="INVOICE-1234",
            ref_number_starts_with="SALE",
            ref_number_to="CHARGE-9999",
            transaction_date_from=parse_date("2019-12-27"),
            transaction_date_to=parse_date("2019-12-27"),
            updated_after="updatedAfter",
            updated_before="updatedBefore",
        )
        assert_matches_type(SyncCursorPage[QbdInvoice], invoice, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Conductor) -> None:
        response = client.qbd.invoices.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(SyncCursorPage[QbdInvoice], invoice, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Conductor) -> None:
        with client.qbd.invoices.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(SyncCursorPage[QbdInvoice], invoice, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInvoices:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncConductor) -> None:
        invoice = await async_client.qbd.invoices.create(
            customer_id="80000001-1234567890",
            transaction_date=parse_date("2019-12-27"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(QbdInvoice, invoice, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncConductor) -> None:
        invoice = await async_client.qbd.invoices.create(
            customer_id="80000001-1234567890",
            transaction_date=parse_date("2019-12-27"),
            conductor_end_user_id="end_usr_1234567abcdefg",
            accounts_receivable_account_id="80000002-1234567890",
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
            class_id="80000001-1234567890",
            customer_message_id="80000001-1234567890",
            document_template_id="80000001-1234567890",
            due_date=parse_date("2019-12-27"),
            exchange_rate=1.2345,
            external_id="12345678-abcd-1234-abcd-1234567890ab",
            invoice_line_groups=[
                {
                    "item_group_id": "itemGroupId",
                    "custom_fields": [
                        {
                            "name": "Customer Rating",
                            "owner_id": "0",
                            "value": "Premium",
                        },
                        {
                            "name": "Customer Rating",
                            "owner_id": "0",
                            "value": "Premium",
                        },
                        {
                            "name": "Customer Rating",
                            "owner_id": "0",
                            "value": "Premium",
                        },
                    ],
                    "inventory_site_id": "inventorySiteId",
                    "inventory_site_location_id": "inventorySiteLocationId",
                    "quantity": 0,
                    "unit_of_measure": "unitOfMeasure",
                },
                {
                    "item_group_id": "itemGroupId",
                    "custom_fields": [
                        {
                            "name": "Customer Rating",
                            "owner_id": "0",
                            "value": "Premium",
                        },
                        {
                            "name": "Customer Rating",
                            "owner_id": "0",
                            "value": "Premium",
                        },
                        {
                            "name": "Customer Rating",
                            "owner_id": "0",
                            "value": "Premium",
                        },
                    ],
                    "inventory_site_id": "inventorySiteId",
                    "inventory_site_location_id": "inventorySiteLocationId",
                    "quantity": 0,
                    "unit_of_measure": "unitOfMeasure",
                },
                {
                    "item_group_id": "itemGroupId",
                    "custom_fields": [
                        {
                            "name": "Customer Rating",
                            "owner_id": "0",
                            "value": "Premium",
                        },
                        {
                            "name": "Customer Rating",
                            "owner_id": "0",
                            "value": "Premium",
                        },
                        {
                            "name": "Customer Rating",
                            "owner_id": "0",
                            "value": "Premium",
                        },
                    ],
                    "inventory_site_id": "inventorySiteId",
                    "inventory_site_location_id": "inventorySiteLocationId",
                    "quantity": 0,
                    "unit_of_measure": "unitOfMeasure",
                },
            ],
            invoice_lines=[
                {
                    "amount": "1000.00",
                    "class_id": "80000001-1234567890",
                    "custom_fields": [
                        {
                            "name": "Customer Rating",
                            "owner_id": "0",
                            "value": "Premium",
                        },
                        {
                            "name": "Customer Rating",
                            "owner_id": "0",
                            "value": "Premium",
                        },
                        {
                            "name": "Customer Rating",
                            "owner_id": "0",
                            "value": "Premium",
                        },
                    ],
                    "description": "High-quality widget with custom engraving",
                    "inventory_site_id": "80000001-1234567890",
                    "inventory_site_location_id": "80000002-1234567890",
                    "item_id": "80000010-1234567890",
                    "link_to_transaction_line": {
                        "transaction_id": "transactionId",
                        "transaction_line_id": "transactionLineId",
                    },
                    "lot_number": "LOT2023-001",
                    "other_custom_field1": "Special handling required",
                    "other_custom_field2": "Special handling required",
                    "override_item_account_id": "80000001-1234567890",
                    "price_level_id": "80000040-1234567890",
                    "price_rule_conflict_behavior": "base_price",
                    "quantity": 5,
                    "rate": "10.00",
                    "rate_percent": "10.5",
                    "sales_tax_code_id": "80000004-1234567890",
                    "serial_number": "SN1234567890",
                    "service_date": parse_date("2019-12-27"),
                    "unit_of_measure": "Each",
                },
                {
                    "amount": "1000.00",
                    "class_id": "80000001-1234567890",
                    "custom_fields": [
                        {
                            "name": "Customer Rating",
                            "owner_id": "0",
                            "value": "Premium",
                        },
                        {
                            "name": "Customer Rating",
                            "owner_id": "0",
                            "value": "Premium",
                        },
                        {
                            "name": "Customer Rating",
                            "owner_id": "0",
                            "value": "Premium",
                        },
                    ],
                    "description": "High-quality widget with custom engraving",
                    "inventory_site_id": "80000001-1234567890",
                    "inventory_site_location_id": "80000002-1234567890",
                    "item_id": "80000010-1234567890",
                    "link_to_transaction_line": {
                        "transaction_id": "transactionId",
                        "transaction_line_id": "transactionLineId",
                    },
                    "lot_number": "LOT2023-001",
                    "other_custom_field1": "Special handling required",
                    "other_custom_field2": "Special handling required",
                    "override_item_account_id": "80000001-1234567890",
                    "price_level_id": "80000040-1234567890",
                    "price_rule_conflict_behavior": "base_price",
                    "quantity": 5,
                    "rate": "10.00",
                    "rate_percent": "10.5",
                    "sales_tax_code_id": "80000004-1234567890",
                    "serial_number": "SN1234567890",
                    "service_date": parse_date("2019-12-27"),
                    "unit_of_measure": "Each",
                },
                {
                    "amount": "1000.00",
                    "class_id": "80000001-1234567890",
                    "custom_fields": [
                        {
                            "name": "Customer Rating",
                            "owner_id": "0",
                            "value": "Premium",
                        },
                        {
                            "name": "Customer Rating",
                            "owner_id": "0",
                            "value": "Premium",
                        },
                        {
                            "name": "Customer Rating",
                            "owner_id": "0",
                            "value": "Premium",
                        },
                    ],
                    "description": "High-quality widget with custom engraving",
                    "inventory_site_id": "80000001-1234567890",
                    "inventory_site_location_id": "80000002-1234567890",
                    "item_id": "80000010-1234567890",
                    "link_to_transaction_line": {
                        "transaction_id": "transactionId",
                        "transaction_line_id": "transactionLineId",
                    },
                    "lot_number": "LOT2023-001",
                    "other_custom_field1": "Special handling required",
                    "other_custom_field2": "Special handling required",
                    "override_item_account_id": "80000001-1234567890",
                    "price_level_id": "80000040-1234567890",
                    "price_rule_conflict_behavior": "base_price",
                    "quantity": 5,
                    "rate": "10.00",
                    "rate_percent": "10.5",
                    "sales_tax_code_id": "80000004-1234567890",
                    "serial_number": "SN1234567890",
                    "service_date": parse_date("2019-12-27"),
                    "unit_of_measure": "Each",
                },
            ],
            is_finance_charge=True,
            is_pending=False,
            is_to_be_emailed=True,
            is_to_be_printed=True,
            item_sales_tax_id="80000010-1234567890",
            link_to_transaction_ids=["string", "string", "string"],
            memo="Customer requested rush delivery",
            other_custom_field="Special handling required",
            purchase_order_number="PO-1234",
            ref_number="INV-1234",
            sales_representative_id="80000030-1234567890",
            sales_tax_code_id="80000004-1234567890",
            set_credits=[
                {
                    "applied_amount": "100.00",
                    "credit_id": "ABCDEF-1234567890",
                    "override": False,
                },
                {
                    "applied_amount": "100.00",
                    "credit_id": "ABCDEF-1234567890",
                    "override": False,
                },
                {
                    "applied_amount": "100.00",
                    "credit_id": "ABCDEF-1234567890",
                    "override": False,
                },
            ],
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
            shipping_date=parse_date("2019-12-27"),
            shipping_method_id="80000007-1234567890",
            shipping_origin="San Francisco, CA",
            terms_id="80000013-1234567890",
        )
        assert_matches_type(QbdInvoice, invoice, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.invoices.with_raw_response.create(
            customer_id="80000001-1234567890",
            transaction_date=parse_date("2019-12-27"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(QbdInvoice, invoice, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.invoices.with_streaming_response.create(
            customer_id="80000001-1234567890",
            transaction_date=parse_date("2019-12-27"),
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(QbdInvoice, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncConductor) -> None:
        invoice = await async_client.qbd.invoices.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(QbdInvoice, invoice, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.invoices.with_raw_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(QbdInvoice, invoice, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.invoices.with_streaming_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(QbdInvoice, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.invoices.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncConductor) -> None:
        invoice = await async_client.qbd.invoices.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(AsyncCursorPage[QbdInvoice], invoice, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncConductor) -> None:
        invoice = await async_client.qbd.invoices.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_ids="80000001-1234567890",
            currency_ids="80000001-1234567890",
            cursor="12345678-abcd-abcd-example-1234567890ab",
            customer_ids="80000001-1234567890",
            ids="123ABC-1234567890",
            include_line_items=True,
            include_linked_transactions=True,
            limit=1,
            payment_status="all",
            ref_number_contains="CHARGE",
            ref_number_ends_with="1234",
            ref_number_from="CHARGE-0001",
            ref_numbers="INVOICE-1234",
            ref_number_starts_with="SALE",
            ref_number_to="CHARGE-9999",
            transaction_date_from=parse_date("2019-12-27"),
            transaction_date_to=parse_date("2019-12-27"),
            updated_after="updatedAfter",
            updated_before="updatedBefore",
        )
        assert_matches_type(AsyncCursorPage[QbdInvoice], invoice, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.invoices.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(AsyncCursorPage[QbdInvoice], invoice, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.invoices.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(AsyncCursorPage[QbdInvoice], invoice, path=["response"])

        assert cast(Any, response.is_closed) is True
