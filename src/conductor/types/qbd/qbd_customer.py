# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "QbdCustomer",
    "AdditionalContact",
    "AdditionalContactCustomContactField",
    "AdditionalNote",
    "AlternateShippingAddress",
    "BillingAddress",
    "Class",
    "CreditCard",
    "Currency",
    "CustomContactField",
    "CustomerType",
    "CustomField",
    "ItemSalesTax",
    "JobType",
    "Parent",
    "PreferredPaymentMethod",
    "PriceLevel",
    "SalesRepresentative",
    "SalesTaxCode",
    "ShippingAddress",
    "Terms",
]


class AdditionalContactCustomContactField(BaseModel):
    name: str
    """The name of the custom contact field (e.g., phone number, email address)."""

    value: str
    """The value of the custom contact field."""


class AdditionalContact(BaseModel):
    id: str
    """
    The QuickBooks-assigned identifier for this contact, unique across all contacts.
    """

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when the object was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """

    custom_contact_fields: List[AdditionalContactCustomContactField] = FieldInfo(alias="customContactFields")
    """Additional custom contact fields, such as phone numbers or email addresses."""

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)
    """The contact's first name."""

    job_title: Optional[str] = FieldInfo(alias="jobTitle", default=None)
    """The contact's job title."""

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)
    """The contact's last name."""

    middle_name: Optional[str] = FieldInfo(alias="middleName", default=None)
    """The contact's middle name."""

    name: Optional[str] = None
    """The contact's full name."""

    object_type: Literal["qbd_contact"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_contact"`."""

    salutation: Optional[str] = None
    """The contact's formal salutation that precedes their name."""

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when the object was last updated, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """

    version: str
    """The current version identifier of the object that changes with each
    modification.

    Provide this value when updating the object to verify you are working with the
    latest version; mismatched values will fail.
    """


class AdditionalNote(BaseModel):
    id: float
    """An auto-incrementing ID for the note."""

    date: str
    """The date the note was last updated, in ISO 8601 format (YYYY-MM-DD)."""

    note: str
    """The text of the note."""


class AlternateShippingAddress(BaseModel):
    city: Optional[str] = None
    """The city, district, suburb, town, or village name of the address."""

    country: Optional[str] = None
    """The country name of the address."""

    default_ship_to: Optional[bool] = FieldInfo(alias="defaultShipTo", default=None)
    """Whether this address is the default ship-to address."""

    line1: Optional[str] = None
    """The first line of the address (e.g., street, PO Box, or company name)."""

    line2: Optional[str] = None
    """
    The second line of the address, if needed (e.g., apartment, suite, unit, or
    building).
    """

    line3: Optional[str] = None
    """The third line of the address, if needed."""

    line4: Optional[str] = None
    """The fourth line of the address, if needed."""

    line5: Optional[str] = None
    """The fifth line of the address, if needed."""

    name: str
    """The ship-to address's unique name."""

    note: Optional[str] = None
    """A note about the address for additional context."""

    postal_code: Optional[str] = FieldInfo(alias="postalCode", default=None)
    """The postal code or ZIP code of the address."""

    state: Optional[str] = None
    """The state, county, province, or region name of the address."""


class BillingAddress(BaseModel):
    city: Optional[str] = None
    """The city, district, suburb, town, or village name of the address."""

    country: Optional[str] = None
    """The country name of the address."""

    line1: Optional[str] = None
    """The first line of the address (e.g., street, PO Box, or company name)."""

    line2: Optional[str] = None
    """
    The second line of the address, if needed (e.g., apartment, suite, unit, or
    building).
    """

    line3: Optional[str] = None
    """The third line of the address, if needed."""

    line4: Optional[str] = None
    """The fourth line of the address, if needed."""

    line5: Optional[str] = None
    """The fifth line of the address, if needed."""

    note: Optional[str] = None
    """A note about the address for additional context."""

    postal_code: Optional[str] = FieldInfo(alias="postalCode", default=None)
    """The postal code or ZIP code of the address."""

    state: Optional[str] = None
    """The state, county, province, or region name of the address."""


class Class(BaseModel):
    id: Optional[str] = None
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical, case-insensitive name of this object, including its full path
    in the QuickBooks list structure. Names are separated by colons (e.g.,
    "Parent:Child:Grandchild").
    """


class CreditCard(BaseModel):
    address: Optional[str] = None
    """The card's billing address."""

    address_zip: Optional[str] = FieldInfo(alias="addressZip", default=None)
    """The card's billing address ZIP or postal code."""

    expiration_month: Optional[float] = FieldInfo(alias="expirationMonth", default=None)
    """The month when the credit card expires."""

    expiration_year: Optional[float] = FieldInfo(alias="expirationYear", default=None)
    """The year when the credit card expires."""

    name: Optional[str] = None
    """The cardholder's name on the card."""

    number: Optional[str] = None
    """The credit card number. Must be masked with lower case “x” and no dashes."""


class Currency(BaseModel):
    id: Optional[str] = None
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical, case-insensitive name of this object, including its full path
    in the QuickBooks list structure. Names are separated by colons (e.g.,
    "Parent:Child:Grandchild").
    """


class CustomContactField(BaseModel):
    name: str
    """The name of the custom contact field (e.g., phone number, email address)."""

    value: str
    """The value of the custom contact field."""


class CustomerType(BaseModel):
    id: Optional[str] = None
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical, case-insensitive name of this object, including its full path
    in the QuickBooks list structure. Names are separated by colons (e.g.,
    "Parent:Child:Grandchild").
    """


class CustomField(BaseModel):
    name: str

    owner_id: Optional[str] = FieldInfo(alias="ownerId", default=None)

    type: Literal[
        "amount_type",
        "date_time_type",
        "integer_type",
        "percent_type",
        "price_type",
        "quantity_type",
        "string_1024_type",
        "string_255_type",
    ]
    """The custom field's data type, which corresponds to a QuickBooks data type."""

    value: str


class ItemSalesTax(BaseModel):
    id: Optional[str] = None
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical, case-insensitive name of this object, including its full path
    in the QuickBooks list structure. Names are separated by colons (e.g.,
    "Parent:Child:Grandchild").
    """


class JobType(BaseModel):
    id: Optional[str] = None
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical, case-insensitive name of this object, including its full path
    in the QuickBooks list structure. Names are separated by colons (e.g.,
    "Parent:Child:Grandchild").
    """


class Parent(BaseModel):
    id: Optional[str] = None
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical, case-insensitive name of this object, including its full path
    in the QuickBooks list structure. Names are separated by colons (e.g.,
    "Parent:Child:Grandchild").
    """


class PreferredPaymentMethod(BaseModel):
    id: Optional[str] = None
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical, case-insensitive name of this object, including its full path
    in the QuickBooks list structure. Names are separated by colons (e.g.,
    "Parent:Child:Grandchild").
    """


class PriceLevel(BaseModel):
    id: Optional[str] = None
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical, case-insensitive name of this object, including its full path
    in the QuickBooks list structure. Names are separated by colons (e.g.,
    "Parent:Child:Grandchild").
    """


class SalesRepresentative(BaseModel):
    id: Optional[str] = None
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical, case-insensitive name of this object, including its full path
    in the QuickBooks list structure. Names are separated by colons (e.g.,
    "Parent:Child:Grandchild").
    """


class SalesTaxCode(BaseModel):
    id: Optional[str] = None
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical, case-insensitive name of this object, including its full path
    in the QuickBooks list structure. Names are separated by colons (e.g.,
    "Parent:Child:Grandchild").
    """


class ShippingAddress(BaseModel):
    city: Optional[str] = None
    """The city, district, suburb, town, or village name of the address."""

    country: Optional[str] = None
    """The country name of the address."""

    line1: Optional[str] = None
    """The first line of the address (e.g., street, PO Box, or company name)."""

    line2: Optional[str] = None
    """
    The second line of the address, if needed (e.g., apartment, suite, unit, or
    building).
    """

    line3: Optional[str] = None
    """The third line of the address, if needed."""

    line4: Optional[str] = None
    """The fourth line of the address, if needed."""

    line5: Optional[str] = None
    """The fifth line of the address, if needed."""

    note: Optional[str] = None
    """A note about the address for additional context."""

    postal_code: Optional[str] = FieldInfo(alias="postalCode", default=None)
    """The postal code or ZIP code of the address."""

    state: Optional[str] = None
    """The state, county, province, or region name of the address."""


class Terms(BaseModel):
    id: Optional[str] = None
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical, case-insensitive name of this object, including its full path
    in the QuickBooks list structure. Names are separated by colons (e.g.,
    "Parent:Child:Grandchild").
    """


class QbdCustomer(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks for this customer.

    This ID is unique among all customers but not across different object types.
    """

    account_number: Optional[str] = FieldInfo(alias="accountNumber", default=None)
    """The account number assigned to this customer in QuickBooks.

    Account numbers appear in the chart of accounts, reports, and graphs. Note that
    if the "Use Account Numbers" preference is turned off in QuickBooks, the account
    number may not be visible in the user interface, but it can still be set and
    retrieved through the API.
    """

    additional_contacts: List[AdditionalContact] = FieldInfo(alias="additionalContacts")
    """Additional alternate contacts for this customer."""

    additional_notes: List[AdditionalNote] = FieldInfo(alias="additionalNotes")
    """Additional notes about this customer."""

    alternate_contact: Optional[str] = FieldInfo(alias="alternateContact", default=None)
    """The name of an alternate contact person for this customer."""

    alternate_phone: Optional[str] = FieldInfo(alias="alternatePhone", default=None)
    """The customer's alternate telephone number."""

    alternate_shipping_addresses: List[AlternateShippingAddress] = FieldInfo(alias="alternateShippingAddresses")
    """
    A list of additional shipping addresses for this customer, useful when the
    customer has multiple shipping locations.
    """

    balance: Optional[str] = None
    """The current balance owed by this customer, represented as a decimal string.

    Compare with `totalBalance`. A positive number indicates money that the customer
    owes.
    """

    billing_address: Optional[BillingAddress] = FieldInfo(alias="billingAddress", default=None)
    """The customer's billing address."""

    cc_email: Optional[str] = FieldInfo(alias="ccEmail", default=None)
    """An email address to carbon copy (CC) on communications with this customer."""

    class_: Optional[Class] = FieldInfo(alias="class", default=None)
    """
    The customer's class, used for categorization (e.g., by department, location, or
    type of work).
    """

    company_name: Optional[str] = FieldInfo(alias="companyName", default=None)
    """
    The name of the company associated with this customer, as specified in
    QuickBooks. This name is used on invoices, checks, and other forms.
    """

    contact: Optional[str] = None
    """The name of the primary contact person for this customer."""

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when this customer was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """

    credit_card: Optional[CreditCard] = FieldInfo(alias="creditCard", default=None)
    """
    The customer's credit card information, including card type, number, and
    expiration date, used for processing credit card payments.
    """

    credit_limit: Optional[str] = FieldInfo(alias="creditLimit", default=None)
    """The customer's credit limit, represented as a decimal string.

    This is the maximum amount of money that can be spent before being billed. If
    `null`, there is no credit limit.
    """

    currency: Optional[Currency] = None
    """The customer's currency.

    For built-in currencies, the name and code are standard international values.
    For user-defined currencies, all values are editable.
    """

    custom_contact_fields: List[CustomContactField] = FieldInfo(alias="customContactFields")
    """Additional custom contact fields for this customer."""

    customer_type: Optional[CustomerType] = FieldInfo(alias="customerType", default=None)
    """
    The category or type assigned to this customer, allowing for meaningful grouping
    and segmentation (e.g., by industry or region).
    """

    custom_fields: List[CustomField] = FieldInfo(alias="customFields")
    """The custom fields added by the user to this customer object as a data extension.

    These fields are not part of the standard QuickBooks object.
    """

    email: Optional[str] = None
    """The customer's email address."""

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """
    A developer-assigned globally unique identifier (GUID) for tracking this object
    in external systems. Must be formatted as a valid GUID; otherwise, QuickBooks
    will return an error.
    """

    fax: Optional[str] = None
    """The customer's fax number."""

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)
    """The first name of the contact person for this customer."""

    full_name: str = FieldInfo(alias="fullName")
    """
    The fully-qualified unique name for this customer, formed by combining the names
    of its parent objects with its own `name`, separated by colons. For example, if
    a customer is under 'Jones' and has the `name` 'Kitchen-Renovation', its
    `fullName` would be 'Jones:Kitchen-Renovation'. Unlike `name`, `fullName` is
    guaranteed to be unique across all customer objects. If this object is a job
    (i.e., a sub-customer), this value would likely be the job's `name` prefixed by
    the customer's `name`.
    """

    is_active: bool = FieldInfo(alias="isActive")
    """Indicates whether this customer is active.

    Inactive objects are typically hidden from views and reports in QuickBooks
    Desktop.
    """

    item_sales_tax: Optional[ItemSalesTax] = FieldInfo(alias="itemSalesTax", default=None)
    """The sales tax item for items associated with this customer.

    A sales-tax item represents a single sales tax that is collected at a specified
    rate and paid to a single agency. For complex tax situations, a zero percent tax
    item named "Tax Calculated On Invoice" may be used, indicating that taxes are
    applied manually on the invoice.
    """

    job_description: Optional[str] = FieldInfo(alias="jobDescription", default=None)
    """
    A brief description of this customer's job, if this object is a job (i.e.,
    sub-customer).
    """

    job_end_date: Optional[date] = FieldInfo(alias="jobEndDate", default=None)
    """
    The actual completion date of this customer's job, if applicable, in ISO 8601
    format (YYYY-MM-DD).
    """

    job_projected_end_date: Optional[date] = FieldInfo(alias="jobProjectedEndDate", default=None)
    """
    The projected completion date for this customer's job, if applicable, in ISO
    8601 format (YYYY-MM-DD).
    """

    job_start_date: Optional[date] = FieldInfo(alias="jobStartDate", default=None)
    """
    The date when work on this customer's job began, if applicable, in ISO 8601
    format (YYYY-MM-DD).
    """

    job_status: Optional[Literal["awarded", "closed", "in_progress", "none", "not_awarded", "pending"]] = FieldInfo(
        alias="jobStatus", default=None
    )
    """
    The status of this customer's job, if this object is a job (i.e., sub-customer).
    """

    job_title: Optional[str] = FieldInfo(alias="jobTitle", default=None)
    """The job title of the contact person for this customer."""

    job_type: Optional[JobType] = FieldInfo(alias="jobType", default=None)
    """
    The type or category of this customer's job, if this object is a job (i.e.,
    sub-customer). Useful for classifying into meaningful segments (e.g., repair,
    installation, consulting).
    """

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)
    """The last name of the contact person for this customer."""

    middle_name: Optional[str] = FieldInfo(alias="middleName", default=None)
    """The middle name of the contact person for this customer."""

    name: str
    """The case-insensitive name of this customer.

    Not guaranteed to be unique because it does not include the names of its parent
    objects like `fullName` does. For example, two objects could both have the
    `name` "Kitchen-Renovation", but they could have unique `fullName` values, such
    as "Jones:Kitchen-Renovation" and "Baker:Kitchen-Renovation".
    """

    note: Optional[str] = None
    """Additional notes or comments about this customer."""

    object_type: Literal["qbd_customer"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_customer"`."""

    parent: Optional[Parent] = None
    """The parent customer one level above this one in the hierarchy.

    For example, if this customer has a `fullName` of "Jones:Kitchen-Renovation",
    its parent has a `fullName` of "Jones". If this customer is at the top level,
    `parent` will be `null`.
    """

    phone: Optional[str] = None
    """The customer's primary telephone number."""

    preferred_delivery_method: Optional[Literal["email", "fax", "none"]] = FieldInfo(
        alias="preferredDeliveryMethod", default=None
    )
    """
    The preferred method for delivering invoices and other documents to this
    customer.
    """

    preferred_payment_method: Optional[PreferredPaymentMethod] = FieldInfo(alias="preferredPaymentMethod", default=None)
    """The customer's preferred payment method (e.g., cash, check, credit card)."""

    price_level: Optional[PriceLevel] = FieldInfo(alias="priceLevel", default=None)
    """
    The custom price level assigned to this customer, used to apply custom pricing
    in invoices, sales receipts, sales orders, or credit memos for that customer.
    Notice that the affected sales transactions do not list the price level, but
    instead list the rate for the item, which was set using the price level.
    """

    resale_number: Optional[str] = FieldInfo(alias="resaleNumber", default=None)
    """
    The customer's resale number, used if the customer is purchasing items for
    resale. This number does not affect sales tax calculations or reports in
    QuickBooks.
    """

    sales_representative: Optional[SalesRepresentative] = FieldInfo(alias="salesRepresentative", default=None)
    """The customer's sales representative.

    Sales representatives can be employees, vendors, or other names in QuickBooks.
    """

    sales_tax_code: Optional[SalesTaxCode] = FieldInfo(alias="salesTaxCode", default=None)
    """
    The sales tax code associated with this customer, indicating whether it is
    taxable or non-taxable. Default codes include 'NON' (non-taxable) and 'TAX'
    (taxable). If QuickBooks is not set up to charge sales tax, it will assign the
    default non-taxable code to all sales.
    """

    sales_tax_country: Optional[Literal["australia", "canada", "uk", "us"]] = FieldInfo(
        alias="salesTaxCountry", default=None
    )
    """The country for which sales tax is collected by this customer."""

    salutation: Optional[str] = None
    """
    The formal salutation title that precedes the name of the contact person for
    this customer, such as 'Mr.', 'Ms.', or 'Dr.'.
    """

    shipping_address: Optional[ShippingAddress] = FieldInfo(alias="shippingAddress", default=None)
    """The customer's shipping address."""

    sublevel: float
    """The depth level of this customer in the hierarchy.

    A top-level customer has a `sublevel` of 0; each subsequent sublevel increases
    this number by 1. For example, a customer with a `fullName` of
    "Jones:Kitchen-Renovation" would have a `sublevel` of 1. When `sublevel` is 0,
    this object is a customer; when `sublevel` is greater than 0, this object is
    typically a job (i.e., a sub-customer).
    """

    tax_registration_number: Optional[str] = FieldInfo(alias="taxRegistrationNumber", default=None)
    """The customer's tax registration number, for use in Canada and the UK."""

    terms: Optional[Terms] = None
    """
    The customer's payment terms, defining when payment is due and any applicable
    discounts.
    """

    total_balance: Optional[str] = FieldInfo(alias="totalBalance", default=None)
    """
    The combined balance of this customer and all of this customer's jobs (i.e.,
    sub-customers), represented as a decimal string. If there are no sub-customers,
    `totalBalance` and `balance` are equal. A positive number indicates money that
    the customer owes.
    """

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when this customer was last updated, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """

    version: str
    """
    The current version identifier for this customer, which changes each time the
    object is modified. When updating this object, you must provide the most recent
    `version` to ensure you're working with the latest data; otherwise, the update
    will fail. This value is opaque and should not be interpreted.
    """
