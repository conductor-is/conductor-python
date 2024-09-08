# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from conductor import Conductor, AsyncConductor
from tests.utils import assert_matches_type
from conductor.types.qbd import QbdInvoice
from conductor.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInvoices:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Conductor) -> None:
        invoice = client.qbd.invoices.create(
            customer_id="customerId",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(QbdInvoice, invoice, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Conductor) -> None:
        invoice = client.qbd.invoices.create(
            customer_id="customerId",
            conductor_end_user_id="end_usr_1234567abcdefg",
            accounts_receivable_account_id="accountsReceivableAccountId",
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
            customer_message_id="customerMessageId",
            customer_sales_tax_code_id="customerSalesTaxCodeId",
            due_date="dueDate",
            exchange_rate=0,
            external_id="12345678-abcd-1234-abcd-1234567890ab",
            invoice_line_groups=[
                {
                    "item_group_id": "itemGroupId",
                    "custom_fields": [
                        {
                            "name": "name",
                            "owner_id": "ownerId",
                            "value": "value",
                        },
                        {
                            "name": "name",
                            "owner_id": "ownerId",
                            "value": "value",
                        },
                        {
                            "name": "name",
                            "owner_id": "ownerId",
                            "value": "value",
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
                            "name": "name",
                            "owner_id": "ownerId",
                            "value": "value",
                        },
                        {
                            "name": "name",
                            "owner_id": "ownerId",
                            "value": "value",
                        },
                        {
                            "name": "name",
                            "owner_id": "ownerId",
                            "value": "value",
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
                            "name": "name",
                            "owner_id": "ownerId",
                            "value": "value",
                        },
                        {
                            "name": "name",
                            "owner_id": "ownerId",
                            "value": "value",
                        },
                        {
                            "name": "name",
                            "owner_id": "ownerId",
                            "value": "value",
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
                    "amount": "amount",
                    "class_id": "classId",
                    "custom_fields": [
                        {
                            "name": "name",
                            "owner_id": "ownerId",
                            "value": "value",
                        },
                        {
                            "name": "name",
                            "owner_id": "ownerId",
                            "value": "value",
                        },
                        {
                            "name": "name",
                            "owner_id": "ownerId",
                            "value": "value",
                        },
                    ],
                    "description": "description",
                    "inventory_site_id": "inventorySiteId",
                    "inventory_site_location_id": "inventorySiteLocationId",
                    "item_id": "itemId",
                    "link_to_transaction_line_item": {
                        "transaction_id": "transactionId",
                        "transaction_line_id": "transactionLineId",
                    },
                    "lot_number": "lotNumber",
                    "other_field1": "otherField1",
                    "other_field2": "otherField2",
                    "override_item_account_id": "overrideItemAccountId",
                    "price_level_id": "priceLevelId",
                    "price_rule_conflict_behavior": "base_price",
                    "quantity": 0,
                    "rate": "rate",
                    "rate_percent": "ratePercent",
                    "sales_tax_code_id": "salesTaxCodeId",
                    "serial_number": "serialNumber",
                    "service_date": "serviceDate",
                    "unit_of_measure": "unitOfMeasure",
                },
                {
                    "amount": "amount",
                    "class_id": "classId",
                    "custom_fields": [
                        {
                            "name": "name",
                            "owner_id": "ownerId",
                            "value": "value",
                        },
                        {
                            "name": "name",
                            "owner_id": "ownerId",
                            "value": "value",
                        },
                        {
                            "name": "name",
                            "owner_id": "ownerId",
                            "value": "value",
                        },
                    ],
                    "description": "description",
                    "inventory_site_id": "inventorySiteId",
                    "inventory_site_location_id": "inventorySiteLocationId",
                    "item_id": "itemId",
                    "link_to_transaction_line_item": {
                        "transaction_id": "transactionId",
                        "transaction_line_id": "transactionLineId",
                    },
                    "lot_number": "lotNumber",
                    "other_field1": "otherField1",
                    "other_field2": "otherField2",
                    "override_item_account_id": "overrideItemAccountId",
                    "price_level_id": "priceLevelId",
                    "price_rule_conflict_behavior": "base_price",
                    "quantity": 0,
                    "rate": "rate",
                    "rate_percent": "ratePercent",
                    "sales_tax_code_id": "salesTaxCodeId",
                    "serial_number": "serialNumber",
                    "service_date": "serviceDate",
                    "unit_of_measure": "unitOfMeasure",
                },
                {
                    "amount": "amount",
                    "class_id": "classId",
                    "custom_fields": [
                        {
                            "name": "name",
                            "owner_id": "ownerId",
                            "value": "value",
                        },
                        {
                            "name": "name",
                            "owner_id": "ownerId",
                            "value": "value",
                        },
                        {
                            "name": "name",
                            "owner_id": "ownerId",
                            "value": "value",
                        },
                    ],
                    "description": "description",
                    "inventory_site_id": "inventorySiteId",
                    "inventory_site_location_id": "inventorySiteLocationId",
                    "item_id": "itemId",
                    "link_to_transaction_line_item": {
                        "transaction_id": "transactionId",
                        "transaction_line_id": "transactionLineId",
                    },
                    "lot_number": "lotNumber",
                    "other_field1": "otherField1",
                    "other_field2": "otherField2",
                    "override_item_account_id": "overrideItemAccountId",
                    "price_level_id": "priceLevelId",
                    "price_rule_conflict_behavior": "base_price",
                    "quantity": 0,
                    "rate": "rate",
                    "rate_percent": "ratePercent",
                    "sales_tax_code_id": "salesTaxCodeId",
                    "serial_number": "serialNumber",
                    "service_date": "serviceDate",
                    "unit_of_measure": "unitOfMeasure",
                },
            ],
            is_finance_charge=True,
            is_pending=True,
            is_tax_included=True,
            is_to_be_emailed=True,
            is_to_be_printed=True,
            item_sales_tax_id="itemSalesTaxId",
            link_to_transaction_ids=["string", "string", "string"],
            memo="memo",
            other_field="otherField",
            purchase_order_number="purchaseOrderNumber",
            ref_number="CHARGE-1234",
            sales_representative_id="salesRepresentativeId",
            set_credit=[
                {
                    "applied_amount": "100.00",
                    "credit_id": "ABCDEF-1234567890",
                    "override": True,
                },
                {
                    "applied_amount": "100.00",
                    "credit_id": "ABCDEF-1234567890",
                    "override": True,
                },
                {
                    "applied_amount": "100.00",
                    "credit_id": "ABCDEF-1234567890",
                    "override": True,
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
            shipping_date="shippingDate",
            shipping_method_id="shippingMethodId",
            shipping_origin="shippingOrigin",
            template_id="templateId",
            terms_id="termsId",
            transaction_date="transactionDate",
        )
        assert_matches_type(QbdInvoice, invoice, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Conductor) -> None:
        response = client.qbd.invoices.with_raw_response.create(
            customer_id="customerId",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(QbdInvoice, invoice, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Conductor) -> None:
        with client.qbd.invoices.with_streaming_response.create(
            customer_id="customerId",
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
            transaction_date_from="transactionDateFrom",
            transaction_date_to="transactionDateTo",
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
            customer_id="customerId",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(QbdInvoice, invoice, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncConductor) -> None:
        invoice = await async_client.qbd.invoices.create(
            customer_id="customerId",
            conductor_end_user_id="end_usr_1234567abcdefg",
            accounts_receivable_account_id="accountsReceivableAccountId",
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
            customer_message_id="customerMessageId",
            customer_sales_tax_code_id="customerSalesTaxCodeId",
            due_date="dueDate",
            exchange_rate=0,
            external_id="12345678-abcd-1234-abcd-1234567890ab",
            invoice_line_groups=[
                {
                    "item_group_id": "itemGroupId",
                    "custom_fields": [
                        {
                            "name": "name",
                            "owner_id": "ownerId",
                            "value": "value",
                        },
                        {
                            "name": "name",
                            "owner_id": "ownerId",
                            "value": "value",
                        },
                        {
                            "name": "name",
                            "owner_id": "ownerId",
                            "value": "value",
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
                            "name": "name",
                            "owner_id": "ownerId",
                            "value": "value",
                        },
                        {
                            "name": "name",
                            "owner_id": "ownerId",
                            "value": "value",
                        },
                        {
                            "name": "name",
                            "owner_id": "ownerId",
                            "value": "value",
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
                            "name": "name",
                            "owner_id": "ownerId",
                            "value": "value",
                        },
                        {
                            "name": "name",
                            "owner_id": "ownerId",
                            "value": "value",
                        },
                        {
                            "name": "name",
                            "owner_id": "ownerId",
                            "value": "value",
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
                    "amount": "amount",
                    "class_id": "classId",
                    "custom_fields": [
                        {
                            "name": "name",
                            "owner_id": "ownerId",
                            "value": "value",
                        },
                        {
                            "name": "name",
                            "owner_id": "ownerId",
                            "value": "value",
                        },
                        {
                            "name": "name",
                            "owner_id": "ownerId",
                            "value": "value",
                        },
                    ],
                    "description": "description",
                    "inventory_site_id": "inventorySiteId",
                    "inventory_site_location_id": "inventorySiteLocationId",
                    "item_id": "itemId",
                    "link_to_transaction_line_item": {
                        "transaction_id": "transactionId",
                        "transaction_line_id": "transactionLineId",
                    },
                    "lot_number": "lotNumber",
                    "other_field1": "otherField1",
                    "other_field2": "otherField2",
                    "override_item_account_id": "overrideItemAccountId",
                    "price_level_id": "priceLevelId",
                    "price_rule_conflict_behavior": "base_price",
                    "quantity": 0,
                    "rate": "rate",
                    "rate_percent": "ratePercent",
                    "sales_tax_code_id": "salesTaxCodeId",
                    "serial_number": "serialNumber",
                    "service_date": "serviceDate",
                    "unit_of_measure": "unitOfMeasure",
                },
                {
                    "amount": "amount",
                    "class_id": "classId",
                    "custom_fields": [
                        {
                            "name": "name",
                            "owner_id": "ownerId",
                            "value": "value",
                        },
                        {
                            "name": "name",
                            "owner_id": "ownerId",
                            "value": "value",
                        },
                        {
                            "name": "name",
                            "owner_id": "ownerId",
                            "value": "value",
                        },
                    ],
                    "description": "description",
                    "inventory_site_id": "inventorySiteId",
                    "inventory_site_location_id": "inventorySiteLocationId",
                    "item_id": "itemId",
                    "link_to_transaction_line_item": {
                        "transaction_id": "transactionId",
                        "transaction_line_id": "transactionLineId",
                    },
                    "lot_number": "lotNumber",
                    "other_field1": "otherField1",
                    "other_field2": "otherField2",
                    "override_item_account_id": "overrideItemAccountId",
                    "price_level_id": "priceLevelId",
                    "price_rule_conflict_behavior": "base_price",
                    "quantity": 0,
                    "rate": "rate",
                    "rate_percent": "ratePercent",
                    "sales_tax_code_id": "salesTaxCodeId",
                    "serial_number": "serialNumber",
                    "service_date": "serviceDate",
                    "unit_of_measure": "unitOfMeasure",
                },
                {
                    "amount": "amount",
                    "class_id": "classId",
                    "custom_fields": [
                        {
                            "name": "name",
                            "owner_id": "ownerId",
                            "value": "value",
                        },
                        {
                            "name": "name",
                            "owner_id": "ownerId",
                            "value": "value",
                        },
                        {
                            "name": "name",
                            "owner_id": "ownerId",
                            "value": "value",
                        },
                    ],
                    "description": "description",
                    "inventory_site_id": "inventorySiteId",
                    "inventory_site_location_id": "inventorySiteLocationId",
                    "item_id": "itemId",
                    "link_to_transaction_line_item": {
                        "transaction_id": "transactionId",
                        "transaction_line_id": "transactionLineId",
                    },
                    "lot_number": "lotNumber",
                    "other_field1": "otherField1",
                    "other_field2": "otherField2",
                    "override_item_account_id": "overrideItemAccountId",
                    "price_level_id": "priceLevelId",
                    "price_rule_conflict_behavior": "base_price",
                    "quantity": 0,
                    "rate": "rate",
                    "rate_percent": "ratePercent",
                    "sales_tax_code_id": "salesTaxCodeId",
                    "serial_number": "serialNumber",
                    "service_date": "serviceDate",
                    "unit_of_measure": "unitOfMeasure",
                },
            ],
            is_finance_charge=True,
            is_pending=True,
            is_tax_included=True,
            is_to_be_emailed=True,
            is_to_be_printed=True,
            item_sales_tax_id="itemSalesTaxId",
            link_to_transaction_ids=["string", "string", "string"],
            memo="memo",
            other_field="otherField",
            purchase_order_number="purchaseOrderNumber",
            ref_number="CHARGE-1234",
            sales_representative_id="salesRepresentativeId",
            set_credit=[
                {
                    "applied_amount": "100.00",
                    "credit_id": "ABCDEF-1234567890",
                    "override": True,
                },
                {
                    "applied_amount": "100.00",
                    "credit_id": "ABCDEF-1234567890",
                    "override": True,
                },
                {
                    "applied_amount": "100.00",
                    "credit_id": "ABCDEF-1234567890",
                    "override": True,
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
            shipping_date="shippingDate",
            shipping_method_id="shippingMethodId",
            shipping_origin="shippingOrigin",
            template_id="templateId",
            terms_id="termsId",
            transaction_date="transactionDate",
        )
        assert_matches_type(QbdInvoice, invoice, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.invoices.with_raw_response.create(
            customer_id="customerId",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(QbdInvoice, invoice, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.invoices.with_streaming_response.create(
            customer_id="customerId",
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
            transaction_date_from="transactionDateFrom",
            transaction_date_to="transactionDateTo",
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
