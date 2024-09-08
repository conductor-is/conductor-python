# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from conductor import Conductor, AsyncConductor
from tests.utils import assert_matches_type
from conductor.types.qbd import QbdCreditCardCharge
from conductor.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCreditCardCharges:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Conductor) -> None:
        credit_card_charge = client.qbd.credit_card_charges.create(
            account_id="accountId",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(QbdCreditCardCharge, credit_card_charge, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Conductor) -> None:
        credit_card_charge = client.qbd.credit_card_charges.create(
            account_id="accountId",
            conductor_end_user_id="end_usr_1234567abcdefg",
            exchange_rate=0,
            expense_lines=[
                {
                    "account_id": "accountId",
                    "amount": "amount",
                    "billable_status": "billable",
                    "class_id": "80000001-1234567890",
                    "customer_id": "customerId",
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
                    "memo": "memo",
                    "sales_representative_id": "salesRepresentativeId",
                    "sales_tax_code_id": "salesTaxCodeId",
                },
                {
                    "account_id": "accountId",
                    "amount": "amount",
                    "billable_status": "billable",
                    "class_id": "80000001-1234567890",
                    "customer_id": "customerId",
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
                    "memo": "memo",
                    "sales_representative_id": "salesRepresentativeId",
                    "sales_tax_code_id": "salesTaxCodeId",
                },
                {
                    "account_id": "accountId",
                    "amount": "amount",
                    "billable_status": "billable",
                    "class_id": "80000001-1234567890",
                    "customer_id": "customerId",
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
                    "memo": "memo",
                    "sales_representative_id": "salesRepresentativeId",
                    "sales_tax_code_id": "salesTaxCodeId",
                },
            ],
            external_id="12345678-abcd-1234-abcd-1234567890ab",
            item_group_lines=[
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
            item_lines=[
                {
                    "amount": "amount",
                    "billable_status": "billable",
                    "class_id": "80000001-1234567890",
                    "cost": "cost",
                    "customer_id": "customerId",
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
                    "expiration_date": "expirationDate",
                    "inventory_site_id": "inventorySiteId",
                    "inventory_site_location_id": "inventorySiteLocationId",
                    "item_id": "itemId",
                    "link_to_transaction_line_item": {
                        "transaction_id": "transactionId",
                        "transaction_line_id": "transactionLineId",
                    },
                    "lot_number": "lotNumber",
                    "override_item_account_id": "overrideItemAccountId",
                    "quantity": 0,
                    "sales_representative_id": "salesRepresentativeId",
                    "sales_tax_code_id": "salesTaxCodeId",
                    "serial_number": "serialNumber",
                    "unit_of_measure": "unitOfMeasure",
                },
                {
                    "amount": "amount",
                    "billable_status": "billable",
                    "class_id": "80000001-1234567890",
                    "cost": "cost",
                    "customer_id": "customerId",
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
                    "expiration_date": "expirationDate",
                    "inventory_site_id": "inventorySiteId",
                    "inventory_site_location_id": "inventorySiteLocationId",
                    "item_id": "itemId",
                    "link_to_transaction_line_item": {
                        "transaction_id": "transactionId",
                        "transaction_line_id": "transactionLineId",
                    },
                    "lot_number": "lotNumber",
                    "override_item_account_id": "overrideItemAccountId",
                    "quantity": 0,
                    "sales_representative_id": "salesRepresentativeId",
                    "sales_tax_code_id": "salesTaxCodeId",
                    "serial_number": "serialNumber",
                    "unit_of_measure": "unitOfMeasure",
                },
                {
                    "amount": "amount",
                    "billable_status": "billable",
                    "class_id": "80000001-1234567890",
                    "cost": "cost",
                    "customer_id": "customerId",
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
                    "expiration_date": "expirationDate",
                    "inventory_site_id": "inventorySiteId",
                    "inventory_site_location_id": "inventorySiteLocationId",
                    "item_id": "itemId",
                    "link_to_transaction_line_item": {
                        "transaction_id": "transactionId",
                        "transaction_line_id": "transactionLineId",
                    },
                    "lot_number": "lotNumber",
                    "override_item_account_id": "overrideItemAccountId",
                    "quantity": 0,
                    "sales_representative_id": "salesRepresentativeId",
                    "sales_tax_code_id": "salesTaxCodeId",
                    "serial_number": "serialNumber",
                    "unit_of_measure": "unitOfMeasure",
                },
            ],
            memo="memo",
            payee_id="payeeId",
            ref_number="CHARGE-1234",
            sales_tax_code_id="salesTaxCodeId",
            transaction_date="transactionDate",
        )
        assert_matches_type(QbdCreditCardCharge, credit_card_charge, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Conductor) -> None:
        response = client.qbd.credit_card_charges.with_raw_response.create(
            account_id="accountId",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_card_charge = response.parse()
        assert_matches_type(QbdCreditCardCharge, credit_card_charge, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Conductor) -> None:
        with client.qbd.credit_card_charges.with_streaming_response.create(
            account_id="accountId",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_card_charge = response.parse()
            assert_matches_type(QbdCreditCardCharge, credit_card_charge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Conductor) -> None:
        credit_card_charge = client.qbd.credit_card_charges.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(QbdCreditCardCharge, credit_card_charge, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Conductor) -> None:
        response = client.qbd.credit_card_charges.with_raw_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_card_charge = response.parse()
        assert_matches_type(QbdCreditCardCharge, credit_card_charge, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Conductor) -> None:
        with client.qbd.credit_card_charges.with_streaming_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_card_charge = response.parse()
            assert_matches_type(QbdCreditCardCharge, credit_card_charge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.credit_card_charges.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    def test_method_list(self, client: Conductor) -> None:
        credit_card_charge = client.qbd.credit_card_charges.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(SyncCursorPage[QbdCreditCardCharge], credit_card_charge, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Conductor) -> None:
        credit_card_charge = client.qbd.credit_card_charges.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_ids="80000001-1234567890",
            currency_ids="80000001-1234567890",
            cursor="12345678-abcd-abcd-example-1234567890ab",
            ids="123ABC-1234567890",
            include_line_items=True,
            limit=1,
            payee_ids="80000001-1234567890",
            ref_number_contains="CHARGE",
            ref_number_ends_with="1234",
            ref_number_from="CHARGE-0001",
            ref_numbers="CREDIT CARD CHARGE-1234",
            ref_number_starts_with="SALE",
            ref_number_to="CHARGE-9999",
            transaction_date_from="transactionDateFrom",
            transaction_date_to="transactionDateTo",
            updated_after="updatedAfter",
            updated_before="updatedBefore",
        )
        assert_matches_type(SyncCursorPage[QbdCreditCardCharge], credit_card_charge, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Conductor) -> None:
        response = client.qbd.credit_card_charges.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_card_charge = response.parse()
        assert_matches_type(SyncCursorPage[QbdCreditCardCharge], credit_card_charge, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Conductor) -> None:
        with client.qbd.credit_card_charges.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_card_charge = response.parse()
            assert_matches_type(SyncCursorPage[QbdCreditCardCharge], credit_card_charge, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCreditCardCharges:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncConductor) -> None:
        credit_card_charge = await async_client.qbd.credit_card_charges.create(
            account_id="accountId",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(QbdCreditCardCharge, credit_card_charge, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncConductor) -> None:
        credit_card_charge = await async_client.qbd.credit_card_charges.create(
            account_id="accountId",
            conductor_end_user_id="end_usr_1234567abcdefg",
            exchange_rate=0,
            expense_lines=[
                {
                    "account_id": "accountId",
                    "amount": "amount",
                    "billable_status": "billable",
                    "class_id": "80000001-1234567890",
                    "customer_id": "customerId",
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
                    "memo": "memo",
                    "sales_representative_id": "salesRepresentativeId",
                    "sales_tax_code_id": "salesTaxCodeId",
                },
                {
                    "account_id": "accountId",
                    "amount": "amount",
                    "billable_status": "billable",
                    "class_id": "80000001-1234567890",
                    "customer_id": "customerId",
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
                    "memo": "memo",
                    "sales_representative_id": "salesRepresentativeId",
                    "sales_tax_code_id": "salesTaxCodeId",
                },
                {
                    "account_id": "accountId",
                    "amount": "amount",
                    "billable_status": "billable",
                    "class_id": "80000001-1234567890",
                    "customer_id": "customerId",
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
                    "memo": "memo",
                    "sales_representative_id": "salesRepresentativeId",
                    "sales_tax_code_id": "salesTaxCodeId",
                },
            ],
            external_id="12345678-abcd-1234-abcd-1234567890ab",
            item_group_lines=[
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
            item_lines=[
                {
                    "amount": "amount",
                    "billable_status": "billable",
                    "class_id": "80000001-1234567890",
                    "cost": "cost",
                    "customer_id": "customerId",
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
                    "expiration_date": "expirationDate",
                    "inventory_site_id": "inventorySiteId",
                    "inventory_site_location_id": "inventorySiteLocationId",
                    "item_id": "itemId",
                    "link_to_transaction_line_item": {
                        "transaction_id": "transactionId",
                        "transaction_line_id": "transactionLineId",
                    },
                    "lot_number": "lotNumber",
                    "override_item_account_id": "overrideItemAccountId",
                    "quantity": 0,
                    "sales_representative_id": "salesRepresentativeId",
                    "sales_tax_code_id": "salesTaxCodeId",
                    "serial_number": "serialNumber",
                    "unit_of_measure": "unitOfMeasure",
                },
                {
                    "amount": "amount",
                    "billable_status": "billable",
                    "class_id": "80000001-1234567890",
                    "cost": "cost",
                    "customer_id": "customerId",
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
                    "expiration_date": "expirationDate",
                    "inventory_site_id": "inventorySiteId",
                    "inventory_site_location_id": "inventorySiteLocationId",
                    "item_id": "itemId",
                    "link_to_transaction_line_item": {
                        "transaction_id": "transactionId",
                        "transaction_line_id": "transactionLineId",
                    },
                    "lot_number": "lotNumber",
                    "override_item_account_id": "overrideItemAccountId",
                    "quantity": 0,
                    "sales_representative_id": "salesRepresentativeId",
                    "sales_tax_code_id": "salesTaxCodeId",
                    "serial_number": "serialNumber",
                    "unit_of_measure": "unitOfMeasure",
                },
                {
                    "amount": "amount",
                    "billable_status": "billable",
                    "class_id": "80000001-1234567890",
                    "cost": "cost",
                    "customer_id": "customerId",
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
                    "expiration_date": "expirationDate",
                    "inventory_site_id": "inventorySiteId",
                    "inventory_site_location_id": "inventorySiteLocationId",
                    "item_id": "itemId",
                    "link_to_transaction_line_item": {
                        "transaction_id": "transactionId",
                        "transaction_line_id": "transactionLineId",
                    },
                    "lot_number": "lotNumber",
                    "override_item_account_id": "overrideItemAccountId",
                    "quantity": 0,
                    "sales_representative_id": "salesRepresentativeId",
                    "sales_tax_code_id": "salesTaxCodeId",
                    "serial_number": "serialNumber",
                    "unit_of_measure": "unitOfMeasure",
                },
            ],
            memo="memo",
            payee_id="payeeId",
            ref_number="CHARGE-1234",
            sales_tax_code_id="salesTaxCodeId",
            transaction_date="transactionDate",
        )
        assert_matches_type(QbdCreditCardCharge, credit_card_charge, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.credit_card_charges.with_raw_response.create(
            account_id="accountId",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_card_charge = await response.parse()
        assert_matches_type(QbdCreditCardCharge, credit_card_charge, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.credit_card_charges.with_streaming_response.create(
            account_id="accountId",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_card_charge = await response.parse()
            assert_matches_type(QbdCreditCardCharge, credit_card_charge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncConductor) -> None:
        credit_card_charge = await async_client.qbd.credit_card_charges.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(QbdCreditCardCharge, credit_card_charge, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.credit_card_charges.with_raw_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_card_charge = await response.parse()
        assert_matches_type(QbdCreditCardCharge, credit_card_charge, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.credit_card_charges.with_streaming_response.retrieve(
            id="123ABC-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_card_charge = await response.parse()
            assert_matches_type(QbdCreditCardCharge, credit_card_charge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.credit_card_charges.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncConductor) -> None:
        credit_card_charge = await async_client.qbd.credit_card_charges.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(AsyncCursorPage[QbdCreditCardCharge], credit_card_charge, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncConductor) -> None:
        credit_card_charge = await async_client.qbd.credit_card_charges.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_ids="80000001-1234567890",
            currency_ids="80000001-1234567890",
            cursor="12345678-abcd-abcd-example-1234567890ab",
            ids="123ABC-1234567890",
            include_line_items=True,
            limit=1,
            payee_ids="80000001-1234567890",
            ref_number_contains="CHARGE",
            ref_number_ends_with="1234",
            ref_number_from="CHARGE-0001",
            ref_numbers="CREDIT CARD CHARGE-1234",
            ref_number_starts_with="SALE",
            ref_number_to="CHARGE-9999",
            transaction_date_from="transactionDateFrom",
            transaction_date_to="transactionDateTo",
            updated_after="updatedAfter",
            updated_before="updatedBefore",
        )
        assert_matches_type(AsyncCursorPage[QbdCreditCardCharge], credit_card_charge, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.credit_card_charges.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_card_charge = await response.parse()
        assert_matches_type(AsyncCursorPage[QbdCreditCardCharge], credit_card_charge, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.credit_card_charges.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_card_charge = await response.parse()
            assert_matches_type(AsyncCursorPage[QbdCreditCardCharge], credit_card_charge, path=["response"])

        assert cast(Any, response.is_closed) is True
