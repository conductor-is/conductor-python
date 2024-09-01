# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "VendorCreateParams",
    "AdditionalContact",
    "AdditionalContactCustomContactField",
    "BillingAddress",
    "CustomContactField",
    "ShippingAddress",
]


class VendorCreateParams(TypedDict, total=False):
    name: Required[str]
    """The vendor's case-insensitive unique name, unique across all vendors."""

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    account_number: Annotated[str, PropertyInfo(alias="accountNumber")]
    """The vendor's account number."""

    additional_contacts: Annotated[Iterable[AdditionalContact], PropertyInfo(alias="additionalContacts")]
    """Additional contacts."""

    additional_notes: Annotated[List[str], PropertyInfo(alias="additionalNotes")]
    """Additional notes about this vendor."""

    alternate_contact: Annotated[str, PropertyInfo(alias="alternateContact")]
    """The vendor's alternate contact name."""

    alternate_phone: Annotated[str, PropertyInfo(alias="alternatePhone")]
    """The vendor's alternate phone number."""

    billing_address: Annotated[BillingAddress, PropertyInfo(alias="billingAddress")]
    """The vendor's billing address."""

    billing_rate_id: Annotated[str, PropertyInfo(alias="billingRateId")]
    """The ID of the billing rate associated with this vendor.

    Use this rate to override a service-item's rate when recording a time-tracking
    transaction for this vendor.
    """

    cc: str
    """The vendor's CC email address."""

    check_name: Annotated[str, PropertyInfo(alias="checkName")]
    """The vendor's name as it will appear on checks sent to the vendor."""

    class_id: Annotated[str, PropertyInfo(alias="classId")]
    """The class associated with this object.

    Classes can be used to categorize objects or transactions by department,
    location, or other meaningful segments.
    """

    company_name: Annotated[str, PropertyInfo(alias="companyName")]
    """The name of the vendor's business.

    This is used on invoices, checks, and other forms.
    """

    contact: str
    """The vendor's contact name."""

    credit_limit: Annotated[str, PropertyInfo(alias="creditLimit")]
    """The vendor's credit limit."""

    currency_id: Annotated[str, PropertyInfo(alias="currencyId")]
    """The ID of the currency associated with this vendor."""

    custom_contact_fields: Annotated[Iterable[CustomContactField], PropertyInfo(alias="customContactFields")]
    """Additional custom contact fields."""

    email: str
    """The vendor's email address."""

    external_id: Annotated[str, PropertyInfo(alias="externalId")]
    """
    An arbitrary globally unique identifier (GUID) the developer can provide to
    track this object in their own system. This value must be formatted as a GUID;
    otherwise, QuickBooks will return an error.
    """

    fax: str
    """The vendor's fax number."""

    first_name: Annotated[str, PropertyInfo(alias="firstName")]
    """The vendor's first name."""

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]
    """Whether this vendor is active.

    QuickBooks hides inactive objects from most views and reports in the UI.
    """

    is_eligible_for1099: Annotated[bool, PropertyInfo(alias="isEligibleFor1099")]
    """Whether the vendor is eligible for 1099.

    If `true`, then the fields `taxId` and `billingAddress` are required.
    """

    is_sales_tax_agency: Annotated[bool, PropertyInfo(alias="isSalesTaxAgency")]
    """Whether this vendor is a sales tax agency.

    If true, the vendor is responsible for collecting and remitting sales tax.
    """

    is_tax_on_tax: Annotated[bool, PropertyInfo(alias="isTaxOnTax")]
    """Whether tax is charged on top of tax in Canada or the UK for this vendor."""

    is_tax_tracked_on_purchases: Annotated[bool, PropertyInfo(alias="isTaxTrackedOnPurchases")]
    """Whether tax is tracked on purchases in Canada or the UK for this vendor."""

    is_tax_tracked_on_sales: Annotated[bool, PropertyInfo(alias="isTaxTrackedOnSales")]
    """Whether tax is tracked on sales in Canada or the UK for this vendor."""

    job_title: Annotated[str, PropertyInfo(alias="jobTitle")]
    """The vendor's job title."""

    last_name: Annotated[str, PropertyInfo(alias="lastName")]
    """The vendor's last name."""

    middle_name: Annotated[str, PropertyInfo(alias="middleName")]
    """The vendor's middle name."""

    note: str
    """Additional information about this vendor."""

    open_balance: Annotated[str, PropertyInfo(alias="openBalance")]
    """The opening balance of this vendor's account.

    A positive number indicates money owed to this vendor.
    """

    open_balance_date: Annotated[str, PropertyInfo(alias="openBalanceDate")]
    """
    The date of the opening balance for this vendor, in ISO 8601 format
    (YYYY-MM-DD).
    """

    phone: str
    """The vendor's phone number."""

    prefill_account_ids: Annotated[List[str], PropertyInfo(alias="prefillAccountIds")]
    """The IDs of the accounts to prefill when entering bills for this vendor."""

    reporting_period: Annotated[Literal["Monthly", "Quarterly"], PropertyInfo(alias="reportingPeriod")]

    sales_tax_code_id: Annotated[str, PropertyInfo(alias="salesTaxCodeId")]
    """The ID of the sales tax code associated with this vendor.

    Sales tax codes indicate whether items are taxable or non-taxable. Two default
    codes are 'Non' (non-taxable) and 'Tax' (taxable). This code determines how
    sales tax is applied to items related to this vendor. If QuickBooks is not set
    up to charge sales tax, it will assign the default non-taxable code to all
    sales.
    """

    sales_tax_country: Annotated[Literal["australia", "canada", "uk", "us"], PropertyInfo(alias="salesTaxCountry")]
    """The country for which sales tax is collected."""

    sales_tax_return_id: Annotated[str, PropertyInfo(alias="salesTaxReturnId")]
    """The ID of the sales tax return associated with this vendor.

    This is used to track sales tax returns for this vendor.
    """

    salutation: str
    """The vendor's formal salutation that precedes their name."""

    shipping_address: Annotated[ShippingAddress, PropertyInfo(alias="shippingAddress")]
    """The vendor's shipping address."""

    tax_id: Annotated[str, PropertyInfo(alias="taxId")]
    """The vendor's tax ID."""

    tax_on_purchases_account_id: Annotated[str, PropertyInfo(alias="taxOnPurchasesAccountId")]
    """
    The ID of the account used for taxes on purchases in Canada or the UK for this
    vendor.
    """

    tax_on_sales_account_id: Annotated[str, PropertyInfo(alias="taxOnSalesAccountId")]
    """
    The ID of the account used for taxes on sales in Canada or the UK for this
    vendor.
    """

    tax_registration_number: Annotated[str, PropertyInfo(alias="taxRegistrationNumber")]
    """The tax registration number associated with this vendor."""

    terms_id: Annotated[str, PropertyInfo(alias="termsId")]
    """The ID of the vendor's payment terms, which define how the vendor is paid."""

    vendor_type_id: Annotated[str, PropertyInfo(alias="vendorTypeId")]
    """The ID of the vendor's type, used for categorization.

    This can represent industry, location, or other business-specific
    classifications.
    """


class AdditionalContactCustomContactField(TypedDict, total=False):
    name: Required[str]
    """The name of the custom contact field (e.g., phone number, email address)."""

    value: Required[str]
    """The value of the custom contact field."""


class AdditionalContact(TypedDict, total=False):
    first_name: Required[Annotated[str, PropertyInfo(alias="firstName")]]
    """The contact's first name."""

    custom_contact_fields: Annotated[
        Iterable[AdditionalContactCustomContactField], PropertyInfo(alias="customContactFields")
    ]
    """Additional custom contact fields, such as phone numbers or email addresses."""

    job_title: Annotated[str, PropertyInfo(alias="jobTitle")]
    """The contact's job title."""

    last_name: Annotated[str, PropertyInfo(alias="lastName")]
    """The contact's last name."""

    middle_name: Annotated[str, PropertyInfo(alias="middleName")]
    """The contact's middle name."""

    salutation: str
    """The contact's formal salutation that precedes their name."""


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
    """A note about the address for additional context."""

    postal_code: Annotated[str, PropertyInfo(alias="postalCode")]
    """The postal code or ZIP code of the address."""

    state: str
    """The state, county, province, or region name of the address."""


class CustomContactField(TypedDict, total=False):
    name: Required[str]
    """The name of the custom contact field (e.g., phone number, email address)."""

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
    """A note about the address for additional context."""

    postal_code: Annotated[str, PropertyInfo(alias="postalCode")]
    """The postal code or ZIP code of the address."""

    state: str
    """The state, county, province, or region name of the address."""
