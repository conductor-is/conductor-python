# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "QbdCustomer",
    "AdditionalContact",
    "AdditionalContactCustomContactField",
    "AdditionalNote",
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
    "ShipToAddress",
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
    The hierarchical name of this object, including its full path in the QuickBooks
    list structure. Names are separated by colons (e.g., "Parent:Child:Grandchild").
    This field is case-insensitive.
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
    The hierarchical name of this object, including its full path in the QuickBooks
    list structure. Names are separated by colons (e.g., "Parent:Child:Grandchild").
    This field is case-insensitive.
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
    The hierarchical name of this object, including its full path in the QuickBooks
    list structure. Names are separated by colons (e.g., "Parent:Child:Grandchild").
    This field is case-insensitive.
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
    The hierarchical name of this object, including its full path in the QuickBooks
    list structure. Names are separated by colons (e.g., "Parent:Child:Grandchild").
    This field is case-insensitive.
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
    The hierarchical name of this object, including its full path in the QuickBooks
    list structure. Names are separated by colons (e.g., "Parent:Child:Grandchild").
    This field is case-insensitive.
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
    The hierarchical name of this object, including its full path in the QuickBooks
    list structure. Names are separated by colons (e.g., "Parent:Child:Grandchild").
    This field is case-insensitive.
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
    The hierarchical name of this object, including its full path in the QuickBooks
    list structure. Names are separated by colons (e.g., "Parent:Child:Grandchild").
    This field is case-insensitive.
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
    The hierarchical name of this object, including its full path in the QuickBooks
    list structure. Names are separated by colons (e.g., "Parent:Child:Grandchild").
    This field is case-insensitive.
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
    The hierarchical name of this object, including its full path in the QuickBooks
    list structure. Names are separated by colons (e.g., "Parent:Child:Grandchild").
    This field is case-insensitive.
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
    The hierarchical name of this object, including its full path in the QuickBooks
    list structure. Names are separated by colons (e.g., "Parent:Child:Grandchild").
    This field is case-insensitive.
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


class ShipToAddress(BaseModel):
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


class Terms(BaseModel):
    id: Optional[str] = None
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical name of this object, including its full path in the QuickBooks
    list structure. Names are separated by colons (e.g., "Parent:Child:Grandchild").
    This field is case-insensitive.
    """


class QbdCustomer(BaseModel):
    id: str
    """
    The QuickBooks-assigned identifier for this customer, unique across all
    customers.
    """

    account_number: Optional[str] = FieldInfo(alias="accountNumber", default=None)
    """
    The customer's account number, which appears in the QuickBooks chart of
    accounts, account fields, reports, and graphs.
    """

    additional_contacts: List[AdditionalContact] = FieldInfo(alias="additionalContacts")
    """Additional contacts."""

    additional_notes: List[AdditionalNote] = FieldInfo(alias="additionalNotes")
    """Additional notes about this customer."""

    alternate_contact: Optional[str] = FieldInfo(alias="alternateContact", default=None)
    """The customer's alternate contact name."""

    alternate_phone: Optional[str] = FieldInfo(alias="alternatePhone", default=None)
    """The customer's alternate phone number."""

    balance: Optional[str] = None
    """The current balance owed by the customer."""

    billing_address: Optional[BillingAddress] = FieldInfo(alias="billingAddress", default=None)
    """The customer's billing address."""

    cc: Optional[str] = None
    """The customer's CC email address."""

    class_: Optional[Class] = FieldInfo(alias="class", default=None)
    """The class associated with this object.

    Classes can be used to categorize objects or transactions by department,
    location, or other meaningful segments.
    """

    company_name: Optional[str] = FieldInfo(alias="companyName", default=None)
    """The name of the customer's business.

    This is used on invoices, checks, and other forms.
    """

    contact: Optional[str] = None
    """The customer's contact name."""

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when the object was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """

    credit_card: Optional[CreditCard] = FieldInfo(alias="creditCard", default=None)
    """The customer's credit card information."""

    credit_limit: Optional[str] = FieldInfo(alias="creditLimit", default=None)
    """The customer's credit limit.

    This is the maximum amount of money that the customer can spend before being
    billed. If undefined, there is no credit limit.
    """

    currency: Optional[Currency] = None
    """The customer's currency."""

    custom_contact_fields: List[CustomContactField] = FieldInfo(alias="customContactFields")
    """Additional custom contact fields."""

    customer_type: Optional[CustomerType] = FieldInfo(alias="customerType", default=None)
    """
    The customer's type, used for categorizing customers (e.g., by industry or
    region).
    """

    custom_fields: List[CustomField] = FieldInfo(alias="customFields")
    """The custom fields added by the user to QuickBooks object as a data extension.

    These fields are not part of the standard QuickBooks object.
    """

    email: Optional[str] = None
    """The customer's email address."""

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """
    An arbitrary globally unique identifier (GUID) the developer can provide to
    track this object in their own system. This value must be formatted as a GUID;
    otherwise, QuickBooks will return an error.
    """

    fax: Optional[str] = None
    """The customer's fax number."""

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)
    """The customer's first name."""

    full_name: str = FieldInfo(alias="fullName")
    """The customer's or job's case-insensitive full name.

    If this is a job, it will be the job's name prefixed by the customer's name.
    """

    is_active: bool = FieldInfo(alias="isActive")
    """Whether this customer is active.

    QuickBooks hides inactive objects from most views and reports in the UI.
    """

    item_sales_tax: Optional[ItemSalesTax] = FieldInfo(alias="itemSalesTax", default=None)
    """The sales tax item for items associated with this customer.

    This is used to calculate a single sales tax collected at a specified rate and
    paid to a single agency. For complex tax situations, a zero percent tax item
    named "Tax Calculated On Invoice" may be used, indicating that taxes are applied
    manually on the invoice.
    """

    job_description: Optional[str] = FieldInfo(alias="jobDescription", default=None)
    """The description of the job, if this is a job (i.e., sub-customer)."""

    job_end_date: Optional[str] = FieldInfo(alias="jobEndDate", default=None)
    """The actual end date of the job, if applicable."""

    job_projected_end_date: Optional[str] = FieldInfo(alias="jobProjectedEndDate", default=None)
    """The projected end date of the job, if applicable."""

    job_start_date: Optional[str] = FieldInfo(alias="jobStartDate", default=None)
    """The start date of the job, if applicable."""

    job_status: Optional[Literal["awarded", "closed", "in_progress", "none", "not_awarded", "pending"]] = FieldInfo(
        alias="jobStatus", default=None
    )
    """The status of the job, if this is a job (i.e, sub-customer)."""

    job_title: Optional[str] = FieldInfo(alias="jobTitle", default=None)
    """The customer's job title."""

    job_type: Optional[JobType] = FieldInfo(alias="jobType", default=None)
    """The type of job, if this is a job (i.e., sub-customer)."""

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)
    """The customer's last name."""

    middle_name: Optional[str] = FieldInfo(alias="middleName", default=None)
    """The customer's middle name."""

    name: str
    """The customer's case-insensitive unique name, unique across all customers."""

    note: Optional[str] = None
    """Additional information about this customer."""

    object_type: Literal["qbd_customer"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_customer"`."""

    parent: Optional[Parent] = None
    """The parent customer or job."""

    phone: Optional[str] = None
    """The customer's phone number."""

    preferred_delivery_method: Optional[Literal["email", "fax", "none"]] = FieldInfo(
        alias="preferredDeliveryMethod", default=None
    )
    """The preferred method for receiving invoices."""

    preferred_payment_method: Optional[PreferredPaymentMethod] = FieldInfo(alias="preferredPaymentMethod", default=None)
    """The customer's preferred payment method."""

    price_level: Optional[PriceLevel] = FieldInfo(alias="priceLevel", default=None)
    """The custom price level for this customer.

    QuickBooks will automatically use the custom price in new invoices, sales
    receipts, sales orders, or credit memos for that customer. You can override this
    automatic feature, however, when you create the invoices, sales receipts, etc.
    Notice that the affected sales transactions do not list the price level, but
    instead list the rate for the item, which was set using the price level.
    """

    resale_number: Optional[str] = FieldInfo(alias="resaleNumber", default=None)
    """The customer's resale number, if they have one.

    This number will not affect reports or sales tax calculations.
    """

    sales_representative: Optional[SalesRepresentative] = FieldInfo(alias="salesRepresentative", default=None)
    """The customer's sales representative."""

    sales_tax_code: Optional[SalesTaxCode] = FieldInfo(alias="salesTaxCode", default=None)
    """The sales tax code, indicating whether related items are taxable or non-taxable.

    Two default codes are 'Non' (non-taxable) and 'Tax' (taxable). If QuickBooks is
    not set up to charge sales tax, it will assign the default non-taxable code to
    all sales.
    """

    sales_tax_country: Optional[Literal["australia", "canada", "uk", "us"]] = FieldInfo(
        alias="salesTaxCountry", default=None
    )
    """The country for which sales tax is collected."""

    salutation: Optional[str] = None
    """The customer's formal salutation that precedes their name."""

    shipping_address: Optional[ShippingAddress] = FieldInfo(alias="shippingAddress", default=None)
    """The customer's shipping address."""

    ship_to_addresses: List[ShipToAddress] = FieldInfo(alias="shipToAddresses")
    """The customer's ship-to addresses."""

    sublevel: float
    """The nesting level of this customer-job within the customer hierarchy.

    A top-level customer has a `sublevel` of 0, a direct sub-customer, which is
    usually a job, has a `sublevel` of 1, and so on. Hence, when `sublevel` is 0,
    you can assume it is a customer, and when `sublevel` is greater than 0, you can
    assume it is a job. For example, a customer-job with a `fullName` of
    `Jones:Kitchen:Carpets` and `name` of `Kitchen` would have a `sublevel` of 2.
    """

    tax_registration_number: Optional[str] = FieldInfo(alias="taxRegistrationNumber", default=None)
    """
    The tax registration number associated with this customer, for use in Canada or
    the UK.
    """

    terms: Optional[Terms] = None
    """The customer's payment terms."""

    total_balance: Optional[str] = FieldInfo(alias="totalBalance", default=None)
    """
    The total balance owed by this customer, including all jobs (i.e.,
    sub-customers).
    """

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
