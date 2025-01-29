# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from conductor import Conductor, AsyncConductor
from tests.utils import assert_matches_type
from conductor._utils import parse_date
from conductor.types.qbd import Employee
from conductor.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEmployees:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Conductor) -> None:
        employee = client.qbd.employees.create(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(Employee, employee, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Conductor) -> None:
        employee = client.qbd.employees.create(
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_number="1010",
            additional_notes=[{"note": "This is a fun note."}],
            address={
                "city": "San Francisco",
                "country": "United States",
                "line1": "Conductor Labs Inc.",
                "line2": "540 Market St.",
                "line3": "Suite 100",
                "line4": "",
                "line5": "",
                "postal_code": "94110",
                "state": "none",
            },
            adjusted_service_date=parse_date("2019-12-27"),
            alternate_phone="+1-555-987-6543",
            billing_rate_id="80000001-1234567890",
            birth_date=parse_date("2019-12-27"),
            custom_contact_fields=[
                {
                    "name": "Main Phone",
                    "value": "555-123-4567",
                }
            ],
            department="Sales",
            description="This employee is a key employee.",
            disability_description="Cerebral Palsy",
            disability_status="disabled",
            email="employee@example.com",
            emergency_contact={
                "primary_contact": {
                    "name": "Main Phone",
                    "value": "555-123-4567",
                    "relation": "brother",
                },
                "secondary_contact": {
                    "name": "Main Phone",
                    "value": "555-123-4567",
                    "relation": "brother",
                },
            },
            employee_payroll={
                "class_id": "80000001-1234567890",
                "earnings": [
                    {
                        "payroll_wage_item_id": "80000001-1234567890",
                        "rate": "10.00",
                        "rate_percent": "10.5",
                    }
                ],
                "pay_period": "biweekly",
                "sick_hours": {
                    "accrual_period": "accrues_annually",
                    "accrual_start_date": parse_date("2019-12-27"),
                    "hours_accrued_per_period": "8",
                    "hours_available": "40",
                    "hours_used": "24",
                    "maximum_hours": "160",
                    "resets_hours_each_year": False,
                },
                "use_time_data_to_create_paychecks": "does_not_use_time_data",
                "vacation_hours": {
                    "accrual_period": "accrues_annually",
                    "accrual_start_date": parse_date("2019-12-27"),
                    "hours_accrued_per_period": "8",
                    "hours_available": "40",
                    "hours_used": "24",
                    "maximum_hours": "160",
                    "resets_hours_each_year": False,
                },
            },
            employee_type="officer",
            employment_status="full_time",
            ethnicity="american_indian",
            external_id="12345678-abcd-1234-abcd-1234567890ab",
            fax="+1-555-555-1212",
            first_name="John",
            gender="male",
            hired_date=parse_date("2019-12-27"),
            i9_on_file_status="on_file",
            is_active=True,
            job_title="Purchasing Manager",
            key_employee_status="key_employee",
            last_name="Doe",
            middle_name="A.",
            military_status="active",
            mobile="+1-555-555-1212",
            note="This employee is a key employee.",
            original_hire_date=parse_date("2019-12-27"),
            overtime_exempt_status="exempt",
            pager="+1-555-555-1212",
            pager_pin="1234",
            phone="+1-555-123-4567",
            print_as="John Doe",
            salutation="Dr.",
            ssn="123-45-6789",
            supervisor_id="80000001-1234567890",
            target_bonus="10000.00",
            termination_date=parse_date("2019-12-27"),
            us_citizenship_status="citizen",
            us_veteran_status="veteran",
            work_authorization_expiration_date=parse_date("2019-12-27"),
        )
        assert_matches_type(Employee, employee, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Conductor) -> None:
        response = client.qbd.employees.with_raw_response.create(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employee = response.parse()
        assert_matches_type(Employee, employee, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Conductor) -> None:
        with client.qbd.employees.with_streaming_response.create(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employee = response.parse()
            assert_matches_type(Employee, employee, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Conductor) -> None:
        employee = client.qbd.employees.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(Employee, employee, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Conductor) -> None:
        response = client.qbd.employees.with_raw_response.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employee = response.parse()
        assert_matches_type(Employee, employee, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Conductor) -> None:
        with client.qbd.employees.with_streaming_response.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employee = response.parse()
            assert_matches_type(Employee, employee, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.employees.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    def test_method_update(self, client: Conductor) -> None:
        employee = client.qbd.employees.update(
            id="80000001-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(Employee, employee, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Conductor) -> None:
        employee = client.qbd.employees.update(
            id="80000001-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_number="1010",
            additional_notes=[
                {
                    "id": 1,
                    "note": "This is a fun note.",
                }
            ],
            address={
                "city": "San Francisco",
                "country": "United States",
                "line1": "Conductor Labs Inc.",
                "line2": "540 Market St.",
                "line3": "Suite 100",
                "line4": "",
                "line5": "",
                "postal_code": "94110",
                "state": "none",
            },
            adjusted_service_date=parse_date("2019-12-27"),
            alternate_phone="+1-555-987-6543",
            billing_rate_id="80000001-1234567890",
            birth_date=parse_date("2019-12-27"),
            custom_contact_fields=[
                {
                    "name": "Main Phone",
                    "value": "555-123-4567",
                }
            ],
            department="Sales",
            description="This employee is a key employee.",
            disability_description="Cerebral Palsy",
            disability_status="disabled",
            email="employee@example.com",
            emergency_contact={
                "primary_contact": {
                    "name": "Main Phone",
                    "value": "555-123-4567",
                    "relation": "brother",
                },
                "secondary_contact": {
                    "name": "Main Phone",
                    "value": "555-123-4567",
                    "relation": "brother",
                },
            },
            employee_payroll={
                "class_id": "80000001-1234567890",
                "earnings": [
                    {
                        "payroll_wage_item_id": "80000001-1234567890",
                        "rate": "10.00",
                        "rate_percent": "10.5",
                    }
                ],
                "pay_period": "biweekly",
                "sick_hours": {
                    "accrual_period": "accrues_annually",
                    "accrual_start_date": parse_date("2019-12-27"),
                    "hours_accrued_per_period": "8",
                    "hours_available": "40",
                    "hours_used": "24",
                    "maximum_hours": "160",
                    "resets_hours_each_year": False,
                },
                "use_time_data_to_create_paychecks": "does_not_use_time_data",
                "vacation_hours": {
                    "accrual_period": "accrues_annually",
                    "accrual_start_date": parse_date("2019-12-27"),
                    "hours_accrued_per_period": "8",
                    "hours_available": "40",
                    "hours_used": "24",
                    "maximum_hours": "160",
                    "resets_hours_each_year": False,
                },
            },
            employee_type="officer",
            employment_status="full_time",
            ethnicity="american_indian",
            fax="+1-555-555-1212",
            first_name="John",
            hired_date=parse_date("2019-12-27"),
            i9_on_file_status="on_file",
            is_active=True,
            job_title="Purchasing Manager",
            key_employee_status="key_employee",
            last_name="Doe",
            middle_name="A.",
            military_status="active",
            mobile="+1-555-555-1212",
            note="This employee is a key employee.",
            original_hire_date=parse_date("2019-12-27"),
            overtime_exempt_status="exempt",
            pager="+1-555-555-1212",
            pager_pin="1234",
            phone="+1-555-123-4567",
            print_as="John Doe",
            salutation="Dr.",
            supervisor_id="80000001-1234567890",
            target_bonus="10000.00",
            termination_date=parse_date("2019-12-27"),
            us_citizenship_status="citizen",
            us_veteran_status="veteran",
            work_authorization_expiration_date=parse_date("2019-12-27"),
        )
        assert_matches_type(Employee, employee, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Conductor) -> None:
        response = client.qbd.employees.with_raw_response.update(
            id="80000001-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employee = response.parse()
        assert_matches_type(Employee, employee, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Conductor) -> None:
        with client.qbd.employees.with_streaming_response.update(
            id="80000001-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employee = response.parse()
            assert_matches_type(Employee, employee, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Conductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.qbd.employees.with_raw_response.update(
                id="",
                revision_number="1721172183",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    def test_method_list(self, client: Conductor) -> None:
        employee = client.qbd.employees.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(SyncCursorPage[Employee], employee, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Conductor) -> None:
        employee = client.qbd.employees.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            cursor="12345678-abcd-abcd-example-1234567890ab",
            ids=["80000001-1234567890"],
            limit=150,
            name_contains="ABC",
            name_ends_with="ABC",
            name_from="A",
            names=["John Doe"],
            name_starts_with="ABC",
            name_to="Z",
            status="active",
            updated_after="updatedAfter",
            updated_before="updatedBefore",
        )
        assert_matches_type(SyncCursorPage[Employee], employee, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Conductor) -> None:
        response = client.qbd.employees.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employee = response.parse()
        assert_matches_type(SyncCursorPage[Employee], employee, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Conductor) -> None:
        with client.qbd.employees.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employee = response.parse()
            assert_matches_type(SyncCursorPage[Employee], employee, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEmployees:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncConductor) -> None:
        employee = await async_client.qbd.employees.create(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(Employee, employee, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncConductor) -> None:
        employee = await async_client.qbd.employees.create(
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_number="1010",
            additional_notes=[{"note": "This is a fun note."}],
            address={
                "city": "San Francisco",
                "country": "United States",
                "line1": "Conductor Labs Inc.",
                "line2": "540 Market St.",
                "line3": "Suite 100",
                "line4": "",
                "line5": "",
                "postal_code": "94110",
                "state": "none",
            },
            adjusted_service_date=parse_date("2019-12-27"),
            alternate_phone="+1-555-987-6543",
            billing_rate_id="80000001-1234567890",
            birth_date=parse_date("2019-12-27"),
            custom_contact_fields=[
                {
                    "name": "Main Phone",
                    "value": "555-123-4567",
                }
            ],
            department="Sales",
            description="This employee is a key employee.",
            disability_description="Cerebral Palsy",
            disability_status="disabled",
            email="employee@example.com",
            emergency_contact={
                "primary_contact": {
                    "name": "Main Phone",
                    "value": "555-123-4567",
                    "relation": "brother",
                },
                "secondary_contact": {
                    "name": "Main Phone",
                    "value": "555-123-4567",
                    "relation": "brother",
                },
            },
            employee_payroll={
                "class_id": "80000001-1234567890",
                "earnings": [
                    {
                        "payroll_wage_item_id": "80000001-1234567890",
                        "rate": "10.00",
                        "rate_percent": "10.5",
                    }
                ],
                "pay_period": "biweekly",
                "sick_hours": {
                    "accrual_period": "accrues_annually",
                    "accrual_start_date": parse_date("2019-12-27"),
                    "hours_accrued_per_period": "8",
                    "hours_available": "40",
                    "hours_used": "24",
                    "maximum_hours": "160",
                    "resets_hours_each_year": False,
                },
                "use_time_data_to_create_paychecks": "does_not_use_time_data",
                "vacation_hours": {
                    "accrual_period": "accrues_annually",
                    "accrual_start_date": parse_date("2019-12-27"),
                    "hours_accrued_per_period": "8",
                    "hours_available": "40",
                    "hours_used": "24",
                    "maximum_hours": "160",
                    "resets_hours_each_year": False,
                },
            },
            employee_type="officer",
            employment_status="full_time",
            ethnicity="american_indian",
            external_id="12345678-abcd-1234-abcd-1234567890ab",
            fax="+1-555-555-1212",
            first_name="John",
            gender="male",
            hired_date=parse_date("2019-12-27"),
            i9_on_file_status="on_file",
            is_active=True,
            job_title="Purchasing Manager",
            key_employee_status="key_employee",
            last_name="Doe",
            middle_name="A.",
            military_status="active",
            mobile="+1-555-555-1212",
            note="This employee is a key employee.",
            original_hire_date=parse_date("2019-12-27"),
            overtime_exempt_status="exempt",
            pager="+1-555-555-1212",
            pager_pin="1234",
            phone="+1-555-123-4567",
            print_as="John Doe",
            salutation="Dr.",
            ssn="123-45-6789",
            supervisor_id="80000001-1234567890",
            target_bonus="10000.00",
            termination_date=parse_date("2019-12-27"),
            us_citizenship_status="citizen",
            us_veteran_status="veteran",
            work_authorization_expiration_date=parse_date("2019-12-27"),
        )
        assert_matches_type(Employee, employee, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.employees.with_raw_response.create(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employee = await response.parse()
        assert_matches_type(Employee, employee, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.employees.with_streaming_response.create(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employee = await response.parse()
            assert_matches_type(Employee, employee, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncConductor) -> None:
        employee = await async_client.qbd.employees.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(Employee, employee, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.employees.with_raw_response.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employee = await response.parse()
        assert_matches_type(Employee, employee, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.employees.with_streaming_response.retrieve(
            id="80000001-1234567890",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employee = await response.parse()
            assert_matches_type(Employee, employee, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.employees.with_raw_response.retrieve(
                id="",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncConductor) -> None:
        employee = await async_client.qbd.employees.update(
            id="80000001-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(Employee, employee, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncConductor) -> None:
        employee = await async_client.qbd.employees.update(
            id="80000001-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
            account_number="1010",
            additional_notes=[
                {
                    "id": 1,
                    "note": "This is a fun note.",
                }
            ],
            address={
                "city": "San Francisco",
                "country": "United States",
                "line1": "Conductor Labs Inc.",
                "line2": "540 Market St.",
                "line3": "Suite 100",
                "line4": "",
                "line5": "",
                "postal_code": "94110",
                "state": "none",
            },
            adjusted_service_date=parse_date("2019-12-27"),
            alternate_phone="+1-555-987-6543",
            billing_rate_id="80000001-1234567890",
            birth_date=parse_date("2019-12-27"),
            custom_contact_fields=[
                {
                    "name": "Main Phone",
                    "value": "555-123-4567",
                }
            ],
            department="Sales",
            description="This employee is a key employee.",
            disability_description="Cerebral Palsy",
            disability_status="disabled",
            email="employee@example.com",
            emergency_contact={
                "primary_contact": {
                    "name": "Main Phone",
                    "value": "555-123-4567",
                    "relation": "brother",
                },
                "secondary_contact": {
                    "name": "Main Phone",
                    "value": "555-123-4567",
                    "relation": "brother",
                },
            },
            employee_payroll={
                "class_id": "80000001-1234567890",
                "earnings": [
                    {
                        "payroll_wage_item_id": "80000001-1234567890",
                        "rate": "10.00",
                        "rate_percent": "10.5",
                    }
                ],
                "pay_period": "biweekly",
                "sick_hours": {
                    "accrual_period": "accrues_annually",
                    "accrual_start_date": parse_date("2019-12-27"),
                    "hours_accrued_per_period": "8",
                    "hours_available": "40",
                    "hours_used": "24",
                    "maximum_hours": "160",
                    "resets_hours_each_year": False,
                },
                "use_time_data_to_create_paychecks": "does_not_use_time_data",
                "vacation_hours": {
                    "accrual_period": "accrues_annually",
                    "accrual_start_date": parse_date("2019-12-27"),
                    "hours_accrued_per_period": "8",
                    "hours_available": "40",
                    "hours_used": "24",
                    "maximum_hours": "160",
                    "resets_hours_each_year": False,
                },
            },
            employee_type="officer",
            employment_status="full_time",
            ethnicity="american_indian",
            fax="+1-555-555-1212",
            first_name="John",
            hired_date=parse_date("2019-12-27"),
            i9_on_file_status="on_file",
            is_active=True,
            job_title="Purchasing Manager",
            key_employee_status="key_employee",
            last_name="Doe",
            middle_name="A.",
            military_status="active",
            mobile="+1-555-555-1212",
            note="This employee is a key employee.",
            original_hire_date=parse_date("2019-12-27"),
            overtime_exempt_status="exempt",
            pager="+1-555-555-1212",
            pager_pin="1234",
            phone="+1-555-123-4567",
            print_as="John Doe",
            salutation="Dr.",
            supervisor_id="80000001-1234567890",
            target_bonus="10000.00",
            termination_date=parse_date("2019-12-27"),
            us_citizenship_status="citizen",
            us_veteran_status="veteran",
            work_authorization_expiration_date=parse_date("2019-12-27"),
        )
        assert_matches_type(Employee, employee, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.employees.with_raw_response.update(
            id="80000001-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employee = await response.parse()
        assert_matches_type(Employee, employee, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.employees.with_streaming_response.update(
            id="80000001-1234567890",
            revision_number="1721172183",
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employee = await response.parse()
            assert_matches_type(Employee, employee, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncConductor) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.qbd.employees.with_raw_response.update(
                id="",
                revision_number="1721172183",
                conductor_end_user_id="end_usr_1234567abcdefg",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncConductor) -> None:
        employee = await async_client.qbd.employees.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )
        assert_matches_type(AsyncCursorPage[Employee], employee, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncConductor) -> None:
        employee = await async_client.qbd.employees.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
            cursor="12345678-abcd-abcd-example-1234567890ab",
            ids=["80000001-1234567890"],
            limit=150,
            name_contains="ABC",
            name_ends_with="ABC",
            name_from="A",
            names=["John Doe"],
            name_starts_with="ABC",
            name_to="Z",
            status="active",
            updated_after="updatedAfter",
            updated_before="updatedBefore",
        )
        assert_matches_type(AsyncCursorPage[Employee], employee, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncConductor) -> None:
        response = await async_client.qbd.employees.with_raw_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employee = await response.parse()
        assert_matches_type(AsyncCursorPage[Employee], employee, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncConductor) -> None:
        async with async_client.qbd.employees.with_streaming_response.list(
            conductor_end_user_id="end_usr_1234567abcdefg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employee = await response.parse()
            assert_matches_type(AsyncCursorPage[Employee], employee, path=["response"])

        assert cast(Any, response.is_closed) is True
