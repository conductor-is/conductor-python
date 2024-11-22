# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "VendorUpdateParams",
    "AdditionalContact",
    "AdditionalContactCustomContactField",
    "AdditionalNote",
    "BillingAddress",
    "CustomContactField",
    "ShippingAddress",
]


class VendorUpdateParams(TypedDict, total=False):
    revision_number: Required[Annotated[str, PropertyInfo(alias="revisionNumber")]]
    """
    The current revision number of the vendor object you are updating, which you can
    get by fetching the object first. Provide the most recent `revisionNumber` to
    ensure you're working with the latest data; otherwise, the update will return an
    error.
    """

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    account_number: Annotated[str, PropertyInfo(alias="accountNumber")]
    """
    The vendor's account number, which appears in the QuickBooks chart of accounts,
    reports, and graphs. Note that if the "Use Account Numbers" preference is turned
    off in QuickBooks, the account number may not be visible in the user interface,
    but it can still be set and retrieved through the API.
    """

    additional_contacts: Annotated[Iterable[AdditionalContact], PropertyInfo(alias="additionalContacts")]
    """Additional alternate contacts for this vendor."""

    additional_notes: Annotated[Iterable[AdditionalNote], PropertyInfo(alias="additionalNotes")]
    """Additional notes about this vendor."""

    alternate_contact: Annotated[str, PropertyInfo(alias="alternateContact")]
    """The name of a alternate contact person for this vendor."""

    alternate_phone: Annotated[str, PropertyInfo(alias="alternatePhone")]
    """The vendor's alternate telephone number."""

    billing_address: Annotated[BillingAddress, PropertyInfo(alias="billingAddress")]
    """The vendor's billing address."""

    billing_rate_id: Annotated[str, PropertyInfo(alias="billingRateId")]
    """
    The vendor's billing rate, used to override service item rates in time tracking
    transactions.
    """

    cc_email: Annotated[str, PropertyInfo(alias="ccEmail")]
    """An email address to carbon copy (CC) on communications with this vendor."""

    class_id: Annotated[str, PropertyInfo(alias="classId")]
    """The vendor's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default.
    """

    company_name: Annotated[str, PropertyInfo(alias="companyName")]
    """The name of the company associated with this vendor.

    This name is used on invoices, checks, and other forms.
    """

    contact: str
    """The name of the primary contact person for this vendor."""

    credit_limit: Annotated[str, PropertyInfo(alias="creditLimit")]
    """The vendor's credit limit, represented as a decimal string.

    This is the maximum amount of money that can be spent being before billed by
    this vendor. If `null`, there is no credit limit.
    """

    currency_id: Annotated[str, PropertyInfo(alias="currencyId")]
    """The vendor's currency.

    For built-in currencies, the name and code are standard international values.
    For user-defined currencies, all values are editable.
    """

    custom_contact_fields: Annotated[Iterable[CustomContactField], PropertyInfo(alias="customContactFields")]
    """
    Additional custom contact fields for this vendor, such as phone numbers or email
    addresses.
    """

    default_expense_account_ids: Annotated[List[str], PropertyInfo(alias="defaultExpenseAccountIds")]
    """The expense accounts to prefill when entering bills for this vendor."""

    email: str
    """The vendor's email address."""

    fax: str
    """The vendor's fax number."""

    first_name: Annotated[str, PropertyInfo(alias="firstName")]
    """The first name of the contact person for this vendor."""

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]
    """Indicates whether this vendor is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    """

    is_compounding_tax: Annotated[bool, PropertyInfo(alias="isCompoundingTax")]
    """
    Indicates whether tax is charged on top of tax for this vendor, for use in
    Canada or the UK.
    """

    is_eligible_for1099: Annotated[bool, PropertyInfo(alias="isEligibleFor1099")]
    """
    Indicates whether this vendor is eligible to receive a 1099 form for tax
    reporting purposes. If `true`, then the fields `taxId` and `billingAddress` are
    required.
    """

    is_sales_tax_agency: Annotated[bool, PropertyInfo(alias="isSalesTaxAgency")]
    """Indicates whether this vendor is a sales tax agency."""

    is_tracking_purchase_tax: Annotated[bool, PropertyInfo(alias="isTrackingPurchaseTax")]
    """
    Indicates whether tax is tracked on purchases for this vendor, for use in Canada
    or the UK.
    """

    is_tracking_sales_tax: Annotated[bool, PropertyInfo(alias="isTrackingSalesTax")]
    """
    Indicates whether tax is tracked on sales for this vendor, for use in Canada or
    the UK.
    """

    job_title: Annotated[str, PropertyInfo(alias="jobTitle")]
    """The job title of the contact person for this vendor."""

    last_name: Annotated[str, PropertyInfo(alias="lastName")]
    """The last name of the contact person for this vendor."""

    middle_name: Annotated[str, PropertyInfo(alias="middleName")]
    """The middle name of the contact person for this vendor."""

    name: str
    """The case-insensitive unique name of this vendor, unique across all vendors.

    **NOTE**: Vendors do not have a `fullName` field because they are not
    hierarchical objects, which is why `name` is unique for them but not for objects
    that have parents. Maximum length: 41 characters.
    """

    name_on_check: Annotated[str, PropertyInfo(alias="nameOnCheck")]
    """The vendor's name as it should appear on checks issued to this vendor."""

    note: str
    """Additional notes or comments about this vendor."""

    phone: str
    """The vendor's primary telephone number."""

    purchase_tax_account_id: Annotated[str, PropertyInfo(alias="purchaseTaxAccountId")]
    """
    The account used for tracking taxes on purchases for this vendor, for use in
    Canada or the UK.
    """

    reporting_period: Annotated[Literal["monthly", "quarterly"], PropertyInfo(alias="reportingPeriod")]
    """The vendor's tax reporting period, for use in Canada or the UK."""

    sales_tax_account_id: Annotated[str, PropertyInfo(alias="salesTaxAccountId")]
    """
    The account used for tracking taxes on sales for this vendor, for use in Canada
    or the UK.
    """

    sales_tax_code_id: Annotated[str, PropertyInfo(alias="salesTaxCodeId")]
    """
    The sales-tax code associated with this vendor, determining whether items bought
    from this vendor are taxable or non-taxable. It's used to assign a default tax
    status to all transactions for this vendor. Default codes include "Non"
    (non-taxable) and "Tax" (taxable), but custom codes can also be created in
    QuickBooks. If QuickBooks is not set up to charge sales tax (via the "Do You
    Charge Sales Tax?" preference), it will assign the default non-taxable code to
    all sales.
    """

    sales_tax_country: Annotated[Literal["australia", "canada", "uk", "us"], PropertyInfo(alias="salesTaxCountry")]
    """The country for which sales tax is collected for this vendor."""

    sales_tax_return_id: Annotated[str, PropertyInfo(alias="salesTaxReturnId")]
    """
    The vendor's sales tax return information, used for tracking and reporting sales
    tax liabilities.
    """

    salutation: str
    """
    The formal salutation title that precedes the name of the contact person for
    this vendor, such as "Mr.", "Ms.", or "Dr.".
    """

    shipping_address: Annotated[ShippingAddress, PropertyInfo(alias="shippingAddress")]
    """The vendor's shipping address."""

    tax_identification_number: Annotated[str, PropertyInfo(alias="taxIdentificationNumber")]
    """The vendor's tax identification number (e.g., EIN or SSN)."""

    tax_registration_number: Annotated[str, PropertyInfo(alias="taxRegistrationNumber")]
    """The vendor's tax registration number, for use in Canada or the UK."""

    terms_id: Annotated[str, PropertyInfo(alias="termsId")]
    """
    The vendor's payment terms, defining when payment is due and any applicable
    discounts.
    """

    vendor_type_id: Annotated[str, PropertyInfo(alias="vendorTypeId")]
    """
    The vendor's type, used for categorizing vendors into meaningful segments, such
    as industry or region.
    """


class AdditionalContactCustomContactField(TypedDict, total=False):
    name: Required[str]
    """The name of the custom contact field (e.g., "old address", "secondary phone")."""

    value: Required[str]
    """The value of the custom contact field."""


class AdditionalContact(TypedDict, total=False):
    id: Required[str]
    """The QuickBooks-assigned unique identifier of the contact to update."""

    first_name: Required[Annotated[str, PropertyInfo(alias="firstName")]]
    """The contact's first name."""

    revision_number: Required[Annotated[str, PropertyInfo(alias="revisionNumber")]]
    """
    The current revision number of the contact object you are updating, which you
    can get by fetching the object first. Provide the most recent `revisionNumber`
    to ensure you're working with the latest data; otherwise, the update will return
    an error.
    """

    custom_contact_fields: Annotated[
        Iterable[AdditionalContactCustomContactField], PropertyInfo(alias="customContactFields")
    ]
    """
    Additional custom contact fields for this contact, such as phone numbers or
    email addresses.
    """

    job_title: Annotated[str, PropertyInfo(alias="jobTitle")]
    """The contact's job title."""

    last_name: Annotated[str, PropertyInfo(alias="lastName")]
    """The contact's last name."""

    middle_name: Annotated[str, PropertyInfo(alias="middleName")]
    """The contact's middle name."""

    salutation: str
    """
    The contact's formal salutation title that precedes their name, such as "Mr.",
    "Ms.", or "Dr.".
    """


class AdditionalNote(TypedDict, total=False):
    id: Required[float]
    """The ID of the note to update."""

    note: Required[str]
    """The text of this note."""


class BillingAddress(TypedDict, total=False):
    city: str
    """The city, district, suburb, town, or village name of the address."""

    country: str
    """The country name of the address."""

    line1: str
    """The first line of the address (e.g., street, PO Box, or company name)."""

    line2: str
    """
    The second line of the address, if needed (e.g., apartment, suite, unit, or
    building).
    """

    line3: str
    """The third line of the address, if needed."""

    line4: str
    """The fourth line of the address, if needed."""

    line5: str
    """The fifth line of the address, if needed."""

    note: str
    """
    A note written at the bottom of the address in the form in which it appears,
    such as the invoice form.
    """

    postal_code: Annotated[str, PropertyInfo(alias="postalCode")]
    """The postal code or ZIP code of the address."""

    state: str
    """The state, county, province, or region name of the address."""


class CustomContactField(TypedDict, total=False):
    name: Required[str]
    """The name of the custom contact field (e.g., "old address", "secondary phone")."""

    value: Required[str]
    """The value of the custom contact field."""


class ShippingAddress(TypedDict, total=False):
    city: str
    """The city, district, suburb, town, or village name of the address."""

    country: str
    """The country name of the address."""

    line1: str
    """The first line of the address (e.g., street, PO Box, or company name)."""

    line2: str
    """
    The second line of the address, if needed (e.g., apartment, suite, unit, or
    building).
    """

    line3: str
    """The third line of the address, if needed."""

    line4: str
    """The fourth line of the address, if needed."""

    line5: str
    """The fifth line of the address, if needed."""

    note: str
    """
    A note written at the bottom of the address in the form in which it appears,
    such as the invoice form.
    """

    postal_code: Annotated[str, PropertyInfo(alias="postalCode")]
    """The postal code or ZIP code of the address."""

    state: str
    """The state, county, province, or region name of the address."""
