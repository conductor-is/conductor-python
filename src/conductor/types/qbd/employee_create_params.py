# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "EmployeeCreateParams",
    "AdditionalNote",
    "Address",
    "CustomContactField",
    "EmergencyContact",
    "EmergencyContactPrimaryContact",
    "EmergencyContactSecondaryContact",
    "EmployeePayrollInfo",
    "EmployeePayrollInfoEarning",
    "EmployeePayrollInfoSickHours",
    "EmployeePayrollInfoVacationHours",
]


class EmployeeCreateParams(TypedDict, total=False):
    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    account_number: Annotated[str, PropertyInfo(alias="accountNumber")]
    """
    The employee's account number, which appears in the QuickBooks chart of
    accounts, reports, and graphs.

    Note that if the "Use Account Numbers" preference is turned off in QuickBooks,
    the account number may not be visible in the user interface, but it can still be
    set and retrieved through the API.
    """

    additional_notes: Annotated[Iterable[AdditionalNote], PropertyInfo(alias="additionalNotes")]
    """Additional notes about this employee."""

    address: Address
    """The employee's address."""

    adjusted_service_date: Annotated[Union[str, date], PropertyInfo(alias="adjustedServiceDate", format="iso8601")]
    """The adjusted service date for this employee.

    This date accounts for previous employment periods or leaves that affect
    seniority.
    """

    alternate_phone: Annotated[str, PropertyInfo(alias="alternatePhone")]
    """The employee's alternate telephone number."""

    billing_rate_id: Annotated[str, PropertyInfo(alias="billingRateId")]
    """
    The employee's billing rate, used to override service item rates in time
    tracking transactions.
    """

    birth_date: Annotated[Union[str, date], PropertyInfo(alias="birthDate", format="iso8601")]
    """This employee's date of birth."""

    custom_contact_fields: Annotated[Iterable[CustomContactField], PropertyInfo(alias="customContactFields")]
    """
    Additional custom contact fields for this employee, such as phone numbers or
    email addresses.
    """

    department: str
    """The employee's department.

    Found in the "employment job details" section of the employee's record in
    QuickBooks.
    """

    description: str
    """A description of this employee.

    Found in the "employment job details" section of the employee's record in
    QuickBooks.
    """

    disability_description: Annotated[str, PropertyInfo(alias="disabilityDescription")]
    """A description of this employee's disability."""

    disability_status: Annotated[Literal["disabled", "non_disabled"], PropertyInfo(alias="disabilityStatus")]
    """Indicates whether this employee is disabled."""

    email: str
    """The employee's email address."""

    emergency_contact: Annotated[EmergencyContact, PropertyInfo(alias="emergencyContact")]
    """The employee's emergency contacts."""

    employee_payroll_info: Annotated[EmployeePayrollInfo, PropertyInfo(alias="employeePayrollInfo")]
    """The employee's payroll information."""

    employee_type: Annotated[Literal["officer", "owner", "regular", "statutory"], PropertyInfo(alias="employeeType")]
    """The employee type.

    This affects payroll taxes - a statutory employee is defined as an employee by
    statute. Note that owners/partners are typically on the "Other Names" list in
    QuickBooks, but if listed as an employee their type will be `owner`.
    """

    employment_status: Annotated[Literal["full_time", "part_time"], PropertyInfo(alias="employmentStatus")]
    """Indicates whether this employee is a part-time or full-time employee."""

    ethnicity: Literal["american_indian", "asian", "black", "hawaiian", "hispanic", "white", "two_or_more_races"]
    """This employee's ethnicity."""

    external_id: Annotated[str, PropertyInfo(alias="externalId")]
    """
    A globally unique identifier (GUID) you, the developer, can provide for tracking
    this object in your external system.

    **IMPORTANT**: Must be formatted as a valid GUID; otherwise, QuickBooks will
    return an error. This field is immutable and can only be set during object
    creation.
    """

    fax: str
    """The employee's fax number."""

    first_name: Annotated[str, PropertyInfo(alias="firstName")]
    """The employee's first name."""

    gender: Literal["male", "female"]
    """This employee's gender."""

    hired_date: Annotated[Union[str, date], PropertyInfo(alias="hiredDate", format="iso8601")]
    """The date this employee was hired."""

    i9_on_file_status: Annotated[Literal["on_file", "not_on_file"], PropertyInfo(alias="i9OnFileStatus")]
    """Indicates whether this employee's I-9 is on file."""

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]
    """Indicates whether this employee is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    """

    job_title: Annotated[str, PropertyInfo(alias="jobTitle")]
    """The employee's job title."""

    key_employee_status: Annotated[Literal["key_employee", "non_key_employee"], PropertyInfo(alias="keyEmployeeStatus")]
    """Indicates whether this employee is a key employee."""

    last_name: Annotated[str, PropertyInfo(alias="lastName")]
    """The employee's last name."""

    middle_name: Annotated[str, PropertyInfo(alias="middleName")]
    """The employee's middle name."""

    military_status: Annotated[Literal["active", "reserve"], PropertyInfo(alias="militaryStatus")]
    """This employee's military status if they are a U.S. veteran."""

    mobile: str
    """The employee's mobile phone number."""

    note: str
    """A note or comment about this employee."""

    original_hire_date: Annotated[Union[str, date], PropertyInfo(alias="originalHireDate", format="iso8601")]
    """The original hire date for this employee."""

    overtime_exempt_status: Annotated[Literal["exempt", "non_exempt"], PropertyInfo(alias="overtimeExemptStatus")]
    """Indicates whether this employee is exempt from overtime pay.

    This classification is based on U.S. labor laws (FLSA).
    """

    pager: str
    """The employee's pager number."""

    pager_pin: Annotated[str, PropertyInfo(alias="pagerPin")]
    """The employee's pager PIN."""

    phone: str
    """The employee's primary telephone number."""

    print_as: Annotated[str, PropertyInfo(alias="printAs")]
    """The name to use when printing this employee from QuickBooks.

    By default, this is the same as the `name` field.
    """

    salutation: str
    """
    The employee's formal salutation title that precedes their name, such as "Mr.",
    "Ms.", or "Dr.".
    """

    ssn: str
    """The employee's Social Security Number.

    **NOTE**: This field cannot be changed after creation.
    """

    supervisor_id: Annotated[str, PropertyInfo(alias="supervisorId")]
    """The employee's supervisor.

    Found in the "employment job details" section of the employee's record in
    QuickBooks.
    """

    target_bonus: Annotated[str, PropertyInfo(alias="targetBonus")]
    """The target bonus for this employee, represented as a decimal string.

    Found in the "employment job details" section of the employee's record in
    QuickBooks.
    """

    termination_date: Annotated[Union[str, date], PropertyInfo(alias="terminationDate", format="iso8601")]
    """The date this employee's employment ended with the company.

    This is also known as the released date or separation date.
    """

    us_citizenship_status: Annotated[Literal["citizen", "non_citizen"], PropertyInfo(alias="usCitizenshipStatus")]
    """Indicates whether this employee is a U.S. citizen."""

    us_veteran_status: Annotated[Literal["veteran", "non_veteran"], PropertyInfo(alias="usVeteranStatus")]
    """Indicates whether this employee is a U.S. veteran."""

    work_authorization_expiration_date: Annotated[
        Union[str, date], PropertyInfo(alias="workAuthorizationExpirationDate", format="iso8601")
    ]
    """The date this employee's work authorization expires."""


class AdditionalNote(TypedDict, total=False):
    note: Required[str]
    """The text of this note."""


class Address(TypedDict, total=False):
    city: str
    """The city, district, suburb, town, or village name of the employee address."""

    line1: str
    """The first line of the employee address (e.g., street, PO Box, or company name)."""

    line2: str
    """
    The second line of the employee address, if needed (e.g., apartment, suite,
    unit, or building).
    """

    postal_code: Annotated[str, PropertyInfo(alias="postalCode")]
    """The postal code or ZIP code of the employee address."""

    state: Literal[
        "none",
        "armed_forces_americas",
        "armed_forces_europe",
        "armed_forces_pacific",
        "AK",
        "AL",
        "AR",
        "AZ",
        "CA",
        "CO",
        "CT",
        "DC",
        "DE",
        "FL",
        "GA",
        "HI",
        "IA",
        "ID",
        "IL",
        "IN",
        "KS",
        "KY",
        "LA",
        "MA",
        "MD",
        "ME",
        "MI",
        "MN",
        "MO",
        "MS",
        "MT",
        "NC",
        "ND",
        "NE",
        "NH",
        "NJ",
        "NM",
        "NV",
        "NY",
        "OH",
        "OK",
        "OR",
        "PA",
        "PR",
        "RI",
        "SC",
        "SD",
        "TN",
        "TX",
        "UT",
        "VA",
        "VT",
        "WA",
        "WI",
        "WV",
        "WY",
    ]
    """The U.S.

    state of the employee address. QuickBooks requires this field to be a U.S. state
    abbreviation (e.g., "CA" for California). See enum for all possible values.
    """


class CustomContactField(TypedDict, total=False):
    name: Required[str]
    """The name of the contact field (e.g., "old address", "secondary phone")."""

    value: Required[str]
    """The value of the contact field."""


class EmergencyContactPrimaryContact(TypedDict, total=False):
    name: Required[str]
    """The name of the contact field (e.g., "old address", "secondary phone")."""

    value: Required[str]
    """The value of the contact field."""

    relation: Literal[
        "brother", "daughter", "father", "friend", "mother", "other", "partner", "sister", "son", "spouse"
    ]
    """The relationship of the employee to the employee."""


class EmergencyContactSecondaryContact(TypedDict, total=False):
    name: Required[str]
    """The name of the contact field (e.g., "old address", "secondary phone")."""

    value: Required[str]
    """The value of the contact field."""

    relation: Literal[
        "brother", "daughter", "father", "friend", "mother", "other", "partner", "sister", "son", "spouse"
    ]
    """The relationship of the employee to the employee."""


class EmergencyContact(TypedDict, total=False):
    primary_contact: Annotated[EmergencyContactPrimaryContact, PropertyInfo(alias="primaryContact")]
    """The employee's primary emergency contact."""

    secondary_contact: Annotated[EmergencyContactSecondaryContact, PropertyInfo(alias="secondaryContact")]
    """The employee's secondary emergency contact."""


class EmployeePayrollInfoEarning(TypedDict, total=False):
    payroll_wage_item_id: Required[Annotated[str, PropertyInfo(alias="payrollWageItemId")]]
    """
    The payroll wage item that defines how this employee is paid (e.g., Regular Pay,
    Overtime Pay). This determines the payment scheme used for payroll calculations.
    """

    rate: str
    """The hourly rate for this employee, represented as a decimal string."""

    rate_percent: Annotated[str, PropertyInfo(alias="ratePercent")]
    """The hourly rate for this employee expressed as a percentage."""


class EmployeePayrollInfoSickHours(TypedDict, total=False):
    accrual_period: Annotated[
        Literal["accrues_annually", "accrues_hourly", "accrues_per_paycheck"], PropertyInfo(alias="accrualPeriod")
    ]
    """How frequently the employee's sick hours are accrued."""

    accrual_start_date: Annotated[Union[str, date], PropertyInfo(alias="accrualStartDate", format="iso8601")]
    """The date the employee's sick hours began to accrue."""

    hours_accrued_per_period: Annotated[str, PropertyInfo(alias="hoursAccruedPerPeriod")]
    """The number of sick hours the employee will accrue per accrual period."""

    hours_available: Annotated[str, PropertyInfo(alias="hoursAvailable")]
    """The total number of sick hours currently available for the employee to use.

    Defaults to 0.
    """

    hours_used: Annotated[str, PropertyInfo(alias="hoursUsed")]
    """The number of sick hours the employee has used."""

    is_resetting_hours_annually: Annotated[bool, PropertyInfo(alias="isResettingHoursAnnually")]
    """
    Indicates whether the employee's sick hours reset to zero at the beginning of
    the new year.
    """

    maximum_hours: Annotated[str, PropertyInfo(alias="maximumHours")]
    """The maximum number of sick hours the employee can accrue."""


class EmployeePayrollInfoVacationHours(TypedDict, total=False):
    accrual_period: Annotated[
        Literal["accrues_annually", "accrues_hourly", "accrues_per_paycheck"], PropertyInfo(alias="accrualPeriod")
    ]
    """How frequently the employee's vacation hours are accrued."""

    accrual_start_date: Annotated[Union[str, date], PropertyInfo(alias="accrualStartDate", format="iso8601")]
    """The date the employee's vacation hours began to accrue."""

    hours_accrued_per_period: Annotated[str, PropertyInfo(alias="hoursAccruedPerPeriod")]
    """The number of vacation hours the employee will accrue per accrual period."""

    hours_available: Annotated[str, PropertyInfo(alias="hoursAvailable")]
    """The total number of vacation hours currently available for the employee to use.

    Defaults to 0.
    """

    hours_used: Annotated[str, PropertyInfo(alias="hoursUsed")]
    """The number of vacation hours the employee has used."""

    is_resetting_hours_annually: Annotated[bool, PropertyInfo(alias="isResettingHoursAnnually")]
    """
    Indicates whether the employee's vacation hours reset to zero at the beginning
    of the new year.
    """

    maximum_hours: Annotated[str, PropertyInfo(alias="maximumHours")]
    """The maximum number of vacation hours the employee can accrue."""


class EmployeePayrollInfo(TypedDict, total=False):
    class_id: Annotated[str, PropertyInfo(alias="classId")]
    """The employee payroll's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default.
    """

    delete_all_earnings: Annotated[bool, PropertyInfo(alias="deleteAllEarnings")]
    """When `true`, deletes all earnings records for this employee payroll."""

    earnings: Iterable[EmployeePayrollInfoEarning]
    """The employee payroll's earnings."""

    is_using_time_data_to_create_paychecks: Annotated[bool, PropertyInfo(alias="isUsingTimeDataToCreatePaychecks")]
    """
    Indicates whether this employee payroll is using time-tracking data to create
    paychecks.
    """

    pay_period: Annotated[
        Literal["biweekly", "daily", "monthly", "quarterly", "semimonthly", "weekly", "yearly"],
        PropertyInfo(alias="payPeriod"),
    ]
    """How frequently this employee payroll is paid (e.g., weekly, biweekly, monthly).

    This determines the schedule for generating paychecks.
    """

    sick_hours: Annotated[EmployeePayrollInfoSickHours, PropertyInfo(alias="sickHours")]
    """
    The employee payroll's sick hours, including how sick time is accrued and the
    total hours accrued.
    """

    use_time_data_to_create_paychecks: Annotated[
        Literal["does_not_use_time_data", "not_set", "uses_time_data"],
        PropertyInfo(alias="useTimeDataToCreatePaychecks"),
    ]
    """
    Indicates whether this employee payroll is using time-tracking data to create
    paychecks.
    """

    vacation_hours: Annotated[EmployeePayrollInfoVacationHours, PropertyInfo(alias="vacationHours")]
    """
    The employee payroll's vacation hours, including how vacation time is accrued
    and the total hours accrued.
    """
