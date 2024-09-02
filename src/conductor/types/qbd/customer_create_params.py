# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "CustomerCreateParams",
    "AdditionalContact",
    "AdditionalContactCustomContactField",
    "BillingAddress",
    "CreditCard",
    "CustomContactField",
    "ShippingAddress",
    "ShipToAddress",
]


class CustomerCreateParams(TypedDict, total=False):
    name: Required[str]
    """The customer's case-insensitive unique name, unique across all customers."""

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    account_number: Annotated[str, PropertyInfo(alias="accountNumber")]
    """
    The customer's account number, which appears in the QuickBooks chart of
    accounts, account fields, reports, and graphs.
    """

    additional_contacts: Annotated[Iterable[AdditionalContact], PropertyInfo(alias="additionalContacts")]
    """Additional contacts."""

    additional_notes: Annotated[List[str], PropertyInfo(alias="additionalNotes")]
    """Additional information about this customer."""

    alternate_contact: Annotated[str, PropertyInfo(alias="alternateContact")]
    """The customer's alternate contact name."""

    alternate_phone: Annotated[str, PropertyInfo(alias="alternatePhone")]
    """The customer's alternate phone number."""

    billing_address: Annotated[BillingAddress, PropertyInfo(alias="billingAddress")]
    """The customer's billing address."""

    cc: str
    """The customer's CC email address."""

    class_id: Annotated[str, PropertyInfo(alias="classId")]
    """The class associated with this object.

    Classes can be used to categorize objects or transactions by department,
    location, or other meaningful segments.
    """

    company_name: Annotated[str, PropertyInfo(alias="companyName")]
    """The name of the customer's business.

    This is used on invoices, checks, and other forms.
    """

    contact: str
    """The customer's contact name."""

    credit_card: Annotated[CreditCard, PropertyInfo(alias="creditCard")]
    """The customer's credit card information."""

    credit_limit: Annotated[str, PropertyInfo(alias="creditLimit")]
    """The customer's credit limit.

    This is the maximum amount of money that the customer can spend before being
    billed. If undefined, there is no credit limit.
    """

    currency_id: Annotated[str, PropertyInfo(alias="currencyId")]
    """The ID of the customer's currency."""

    custom_contact_fields: Annotated[Iterable[CustomContactField], PropertyInfo(alias="customContactFields")]
    """Additional custom contact fields."""

    customer_type_id: Annotated[str, PropertyInfo(alias="customerTypeId")]
    """
    The ID of the customer type, used for categorizing customers (e.g., by industry
    or region).
    """

    email: str
    """The customer's email address."""

    external_id: Annotated[str, PropertyInfo(alias="externalId")]
    """
    An arbitrary globally unique identifier (GUID) the developer can provide to
    track this object in their own system. This value must be formatted as a GUID;
    otherwise, QuickBooks will return an error.
    """

    fax: str
    """The customer's fax number."""

    first_name: Annotated[str, PropertyInfo(alias="firstName")]
    """The customer's first name."""

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]
    """Whether this customer is active.

    QuickBooks hides inactive objects from most views and reports in the UI.
    """

    item_sales_tax_id: Annotated[str, PropertyInfo(alias="itemSalesTaxId")]
    """
    The ID of the item sales tax, used to calculate a single sales tax that is
    collected at a specified rate and paid to a single agency.
    """

    job_description: Annotated[str, PropertyInfo(alias="jobDescription")]
    """The description of the job, if this is a job (i.e., sub-customer)."""

    job_end_date: Annotated[str, PropertyInfo(alias="jobEndDate")]
    """The actual end date of the job, if applicable."""

    job_projected_end_date: Annotated[str, PropertyInfo(alias="jobProjectedEndDate")]
    """The projected end date of the job, if applicable."""

    job_start_date: Annotated[str, PropertyInfo(alias="jobStartDate")]
    """The start date of the job, if applicable."""

    job_status: Annotated[
        Literal["Awarded", "Closed", "InProgress", "None", "NotAwarded", "Pending"], PropertyInfo(alias="jobStatus")
    ]

    job_title: Annotated[str, PropertyInfo(alias="jobTitle")]
    """The customer's job title."""

    job_type_id: Annotated[str, PropertyInfo(alias="jobTypeId")]
    """The ID of the job type, if this is a job (i.e., sub-customer)."""

    last_name: Annotated[str, PropertyInfo(alias="lastName")]
    """The customer's last name."""

    middle_name: Annotated[str, PropertyInfo(alias="middleName")]
    """The customer's middle name."""

    open_balance: Annotated[str, PropertyInfo(alias="openBalance")]
    """The opening balance of this customer's account."""

    open_balance_date: Annotated[str, PropertyInfo(alias="openBalanceDate")]
    """The date of the opening balance for this customer."""

    parent_id: Annotated[str, PropertyInfo(alias="parentId")]
    """The ID of the parent customer or job."""

    phone: str
    """The customer's phone number."""

    preferred_delivery_method: Annotated[Literal["Email", "Fax", "None"], PropertyInfo(alias="preferredDeliveryMethod")]

    preferred_payment_method_id: Annotated[str, PropertyInfo(alias="preferredPaymentMethodId")]
    """The ID of the customer's preferred payment method, if they have one."""

    price_level_id: Annotated[str, PropertyInfo(alias="priceLevelId")]
    """The ID of the custom price level for this customer.

    QuickBooks will automatically use the custom price in new invoices, sales
    receipts, sales orders, or credit memos for that customer. You can override this
    automatic feature, however, when you create the invoices, sales receipts, etc.
    Notice that the affected sales transactions do not list the price level, but
    instead list the rate for the item, which was set using the price level.
    """

    resale_number: Annotated[str, PropertyInfo(alias="resaleNumber")]
    """The customer's resale number, if they have one.

    This number will not affect reports or sales tax calculations.
    """

    sales_representative_id: Annotated[str, PropertyInfo(alias="salesRepresentativeId")]
    """The ID of the customer's sales representative."""

    sales_tax_code_id: Annotated[str, PropertyInfo(alias="salesTaxCodeId")]
    """
    The ID of the sales tax code, indicating whether related items are taxable or
    non-taxable.
    """

    sales_tax_country: Annotated[Literal["Australia", "Canada", "UK", "US"], PropertyInfo(alias="salesTaxCountry")]

    salutation: str
    """The customer's formal salutation that precedes their name."""

    shipping_address: Annotated[ShippingAddress, PropertyInfo(alias="shippingAddress")]
    """The customer's shipping address."""

    ship_to_addresses: Annotated[Iterable[ShipToAddress], PropertyInfo(alias="shipToAddresses")]
    """The customer's ship-to addresses."""

    tax_registration_number: Annotated[str, PropertyInfo(alias="taxRegistrationNumber")]
    """
    The tax registration number associated with this customer, for use in Canada or
    the UK.
    """

    terms_id: Annotated[str, PropertyInfo(alias="termsId")]
    """The ID of the customer's payment terms."""


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


class CreditCard(TypedDict, total=False):
    address: Required[Optional[str]]
    """The card's billing address."""

    address_zip: Required[Annotated[Optional[str], PropertyInfo(alias="addressZip")]]
    """The card's billing address ZIP or postal code."""

    expiration_month: Required[Annotated[Optional[float], PropertyInfo(alias="expirationMonth")]]
    """The month when the credit card expires."""

    expiration_year: Required[Annotated[Optional[float], PropertyInfo(alias="expirationYear")]]
    """The year when the credit card expires."""

    name: Required[Optional[str]]
    """The cardholder's name on the card."""

    number: Required[Optional[str]]
    """The credit card number. Must be masked with lower case “x” and no dashes."""


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


class ShipToAddress(TypedDict, total=False):
    name: Required[str]
    """The ship-to address's unique name."""

    city: str
    """The city, district, suburb, town, or village name of the address."""

    country: str
    """The country name of the address."""

    default_ship_to: Annotated[bool, PropertyInfo(alias="defaultShipTo")]
    """Whether this address is the default ship-to address."""

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
