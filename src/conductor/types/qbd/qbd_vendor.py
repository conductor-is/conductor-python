# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "QbdVendor",
    "AdditionalContact",
    "AdditionalContactCustomContactField",
    "AdditionalNote",
    "BillingAddress",
    "BillingRate",
    "Class",
    "Currency",
    "CustomContactField",
    "CustomField",
    "PrefillAccount",
    "SalesTaxCode",
    "SalesTaxReturn",
    "ShippingAddress",
    "TaxOnPurchasesAccount",
    "TaxOnSalesAccount",
    "Terms",
    "VendorType",
]


class AdditionalContactCustomContactField(BaseModel):
    name: str
    """The name of the custom contact field (e.g., "old address", "secondary phone")."""

    value: str
    """The value of the custom contact field."""


class AdditionalContact(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks to this contact.

    This ID is unique across all contacts but not across different QuickBooks object
    types.
    """

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when this contact was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """

    custom_contact_fields: List[AdditionalContactCustomContactField] = FieldInfo(alias="customContactFields")
    """
    Additional custom contact fields for this contact, such as phone numbers or
    email addresses.
    """

    first_name: str = FieldInfo(alias="firstName")
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
    """
    The contact's formal salutation title that precedes their name, such as "Mr.",
    "Ms.", or "Dr.".
    """

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when this contact was last updated, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """

    version: str
    """
    The current version identifier for this contact, which changes each time the
    object is modified. When updating this object, you must provide the most recent
    `version` to ensure you're working with the latest data; otherwise, the update
    will fail. This value is opaque and should not be interpreted.
    """


class AdditionalNote(BaseModel):
    id: float
    """The auto-incrementing identifier assigned by QuickBooks to this note."""

    date: datetime.date
    """The date this note was last updated, in ISO 8601 format (YYYY-MM-DD)."""

    note: str
    """The text of this note."""


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
    """
    A note written at the bottom of the address in the form in which it appears,
    such as the invoice form.
    """

    postal_code: Optional[str] = FieldInfo(alias="postalCode", default=None)
    """The postal code or ZIP code of the address."""

    state: Optional[str] = None
    """The state, county, province, or region name of the address."""


class BillingRate(BaseModel):
    id: Optional[str] = None
    """The unique identifier assigned by QuickBooks to this object.

    This ID is unique across all objects of the same type, but not across different
    QuickBooks object types.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The fully-qualified unique name for this object, formed by combining the names
    of its parent objects with its own `name`, separated by colons. Not
    case-sensitive.
    """


class Class(BaseModel):
    id: Optional[str] = None
    """The unique identifier assigned by QuickBooks to this object.

    This ID is unique across all objects of the same type, but not across different
    QuickBooks object types.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The fully-qualified unique name for this object, formed by combining the names
    of its parent objects with its own `name`, separated by colons. Not
    case-sensitive.
    """


class Currency(BaseModel):
    id: Optional[str] = None
    """The unique identifier assigned by QuickBooks to this object.

    This ID is unique across all objects of the same type, but not across different
    QuickBooks object types.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The fully-qualified unique name for this object, formed by combining the names
    of its parent objects with its own `name`, separated by colons. Not
    case-sensitive.
    """


class CustomContactField(BaseModel):
    name: str
    """The name of the custom contact field (e.g., "old address", "secondary phone")."""

    value: str
    """The value of the custom contact field."""


class CustomField(BaseModel):
    name: str
    """The name of the custom field, unique for the specified `ownerId`.

    For public custom fields, this name is visible as a label in the QuickBooks UI.
    """

    owner_id: Optional[str] = FieldInfo(alias="ownerId", default=None)
    """
    The identifier of the owner of the custom field, which QuickBooks internally
    calls a "data extension". For public custom fields visible in the UI, such as
    those added by the QuickBooks user, this is always "0". For private custom
    fields that are only visible to the application that created them, this is a
    valid GUID identifying the owning application. Internally, Conductor always
    fetches all public custom fields (those with an `ownerId` of "0") for all
    objects.
    """

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
    """The data type of the custom field."""

    value: str
    """The value of the custom field.

    The maximum length depends on the field's data type.
    """


class PrefillAccount(BaseModel):
    id: Optional[str] = None
    """The unique identifier assigned by QuickBooks to this object.

    This ID is unique across all objects of the same type, but not across different
    QuickBooks object types.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The fully-qualified unique name for this object, formed by combining the names
    of its parent objects with its own `name`, separated by colons. Not
    case-sensitive.
    """


class SalesTaxCode(BaseModel):
    id: Optional[str] = None
    """The unique identifier assigned by QuickBooks to this object.

    This ID is unique across all objects of the same type, but not across different
    QuickBooks object types.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The fully-qualified unique name for this object, formed by combining the names
    of its parent objects with its own `name`, separated by colons. Not
    case-sensitive.
    """


class SalesTaxReturn(BaseModel):
    id: Optional[str] = None
    """The unique identifier assigned by QuickBooks to this object.

    This ID is unique across all objects of the same type, but not across different
    QuickBooks object types.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The fully-qualified unique name for this object, formed by combining the names
    of its parent objects with its own `name`, separated by colons. Not
    case-sensitive.
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
    """
    A note written at the bottom of the address in the form in which it appears,
    such as the invoice form.
    """

    postal_code: Optional[str] = FieldInfo(alias="postalCode", default=None)
    """The postal code or ZIP code of the address."""

    state: Optional[str] = None
    """The state, county, province, or region name of the address."""


class TaxOnPurchasesAccount(BaseModel):
    id: Optional[str] = None
    """The unique identifier assigned by QuickBooks to this object.

    This ID is unique across all objects of the same type, but not across different
    QuickBooks object types.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The fully-qualified unique name for this object, formed by combining the names
    of its parent objects with its own `name`, separated by colons. Not
    case-sensitive.
    """


class TaxOnSalesAccount(BaseModel):
    id: Optional[str] = None
    """The unique identifier assigned by QuickBooks to this object.

    This ID is unique across all objects of the same type, but not across different
    QuickBooks object types.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The fully-qualified unique name for this object, formed by combining the names
    of its parent objects with its own `name`, separated by colons. Not
    case-sensitive.
    """


class Terms(BaseModel):
    id: Optional[str] = None
    """The unique identifier assigned by QuickBooks to this object.

    This ID is unique across all objects of the same type, but not across different
    QuickBooks object types.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The fully-qualified unique name for this object, formed by combining the names
    of its parent objects with its own `name`, separated by colons. Not
    case-sensitive.
    """


class VendorType(BaseModel):
    id: Optional[str] = None
    """The unique identifier assigned by QuickBooks to this object.

    This ID is unique across all objects of the same type, but not across different
    QuickBooks object types.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The fully-qualified unique name for this object, formed by combining the names
    of its parent objects with its own `name`, separated by colons. Not
    case-sensitive.
    """


class QbdVendor(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks to this vendor.

    This ID is unique across all vendors but not across different QuickBooks object
    types.
    """

    account_number: Optional[str] = FieldInfo(alias="accountNumber", default=None)
    """
    The vendor's account number, which appears in the QuickBooks chart of accounts,
    reports, and graphs. Note that if the "Use Account Numbers" preference is turned
    off in QuickBooks, the account number may not be visible in the user interface,
    but it can still be set and retrieved through the API.
    """

    additional_contacts: List[AdditionalContact] = FieldInfo(alias="additionalContacts")
    """Additional alternate contacts for this vendor."""

    additional_notes: List[AdditionalNote] = FieldInfo(alias="additionalNotes")
    """Additional notes about this vendor."""

    alternate_contact: Optional[str] = FieldInfo(alias="alternateContact", default=None)
    """The name of an alternate contact person for this vendor."""

    alternate_phone: Optional[str] = FieldInfo(alias="alternatePhone", default=None)
    """The vendor's alternate telephone number."""

    balance: Optional[str] = None
    """The current balance owed to this vendor, represented as a decimal string.

    A positive number indicates money owed to the vendor.
    """

    billing_address: Optional[BillingAddress] = FieldInfo(alias="billingAddress", default=None)
    """The vendor's billing address."""

    billing_rate: Optional[BillingRate] = FieldInfo(alias="billingRate", default=None)
    """
    The vendor's billing rate, used to override service item rates in time tracking
    transactions.
    """

    cc_email: Optional[str] = FieldInfo(alias="ccEmail", default=None)
    """An email address to carbon copy (CC) on communications with this vendor."""

    class_: Optional[Class] = FieldInfo(alias="class", default=None)
    """The vendor's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default.
    """

    company_name: Optional[str] = FieldInfo(alias="companyName", default=None)
    """The name of the company associated with this vendor.

    This name is used on invoices, checks, and other forms.
    """

    contact: Optional[str] = None
    """The name of the primary contact person for this vendor."""

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when this vendor was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """

    credit_limit: Optional[str] = FieldInfo(alias="creditLimit", default=None)
    """The vendor's credit limit, represented as a decimal string.

    This is the maximum amount of money that can be spent being before billed by
    this vendor. If `null`, there is no credit limit.
    """

    currency: Optional[Currency] = None
    """The vendor's currency.

    For built-in currencies, the name and code are standard international values.
    For user-defined currencies, all values are editable.
    """

    custom_contact_fields: List[CustomContactField] = FieldInfo(alias="customContactFields")
    """
    Additional custom contact fields for this vendor, such as phone numbers or email
    addresses.
    """

    custom_fields: List[CustomField] = FieldInfo(alias="customFields")
    """
    The custom fields for the vendor object, added as user-defined data extensions,
    not included in the standard QuickBooks object.
    """

    email: Optional[str] = None
    """The vendor's email address."""

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """
    A globally unique identifier (GUID) you can provide for tracking this object in
    your external system. Must be formatted as a valid GUID; otherwise, QuickBooks
    will return an error. This field is immutable and can only be set during object
    creation.
    """

    fax: Optional[str] = None
    """The vendor's fax number."""

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)
    """The first name of the contact person for this vendor."""

    is_active: bool = FieldInfo(alias="isActive")
    """Indicates whether this vendor is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    """

    is_eligible_for1099: Optional[bool] = FieldInfo(alias="isEligibleFor1099", default=None)
    """
    Indicates whether this vendor is eligible to receive a 1099 form for tax
    reporting purposes. If `true`, then the fields `taxId` and `billingAddress` are
    required.
    """

    is_sales_tax_agency: Optional[bool] = FieldInfo(alias="isSalesTaxAgency", default=None)
    """Indicates whether this vendor is a sales tax agency."""

    is_tax_on_tax: Optional[bool] = FieldInfo(alias="isTaxOnTax", default=None)
    """
    Indicates whether tax is charged on top of tax for this vendor, for use in
    Canada or the UK.
    """

    is_tax_tracked_on_purchases: Optional[bool] = FieldInfo(alias="isTaxTrackedOnPurchases", default=None)
    """
    Indicates whether tax is tracked on purchases for this vendor, for use in Canada
    or the UK.
    """

    is_tax_tracked_on_sales: Optional[bool] = FieldInfo(alias="isTaxTrackedOnSales", default=None)
    """
    Indicates whether tax is tracked on sales for this vendor, for use in Canada or
    the UK.
    """

    job_title: Optional[str] = FieldInfo(alias="jobTitle", default=None)
    """The job title of the contact person for this vendor."""

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)
    """The last name of the contact person for this vendor."""

    middle_name: Optional[str] = FieldInfo(alias="middleName", default=None)
    """The middle name of the contact person for this vendor."""

    name: str
    """The case-insensitive unique name of this vendor, unique across all vendors."""

    name_on_check: Optional[str] = FieldInfo(alias="nameOnCheck", default=None)
    """The vendor's name as it should appear on checks issued to this vendor."""

    note: Optional[str] = None
    """Additional notes or comments about this vendor."""

    object_type: Literal["qbd_vendor"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_vendor"`."""

    phone: Optional[str] = None
    """The vendor's primary telephone number."""

    prefill_accounts: List[PrefillAccount] = FieldInfo(alias="prefillAccounts")
    """The expense accounts to prefill when entering bills for this vendor."""

    reporting_period: Optional[Literal["monthly", "quarterly"]] = FieldInfo(alias="reportingPeriod", default=None)
    """The vendor's tax reporting period, for use in Canada or the UK."""

    sales_tax_code: Optional[SalesTaxCode] = FieldInfo(alias="salesTaxCode", default=None)
    """
    The sales-tax code associated with this vendor, determining whether items bought
    from this vendor are taxable or non-taxable. It's used to assign a default tax
    status to all transactions for this vendor. Default codes include "Non"
    (non-taxable) and "Tax" (taxable), but custom codes can also be created in
    QuickBooks. If QuickBooks is not set up to charge sales tax (via the "Do You
    Charge Sales Tax?" preference), it will assign the default non-taxable code to
    all sales.
    """

    sales_tax_country: Optional[Literal["australia", "canada", "uk", "us"]] = FieldInfo(
        alias="salesTaxCountry", default=None
    )
    """The country for which sales tax is collected for this vendor."""

    sales_tax_return: Optional[SalesTaxReturn] = FieldInfo(alias="salesTaxReturn", default=None)
    """
    The vendor's sales tax return information, used for tracking and reporting sales
    tax liabilities.
    """

    salutation: Optional[str] = None
    """
    The formal salutation title that precedes the name of the contact person for
    this vendor, such as "Mr.", "Ms.", or "Dr.".
    """

    shipping_address: Optional[ShippingAddress] = FieldInfo(alias="shippingAddress", default=None)
    """The vendor's shipping address."""

    tax_identification_number: Optional[str] = FieldInfo(alias="taxIdentificationNumber", default=None)
    """The vendor's tax identification number (e.g., EIN or SSN)."""

    tax_on_purchases_account: Optional[TaxOnPurchasesAccount] = FieldInfo(alias="taxOnPurchasesAccount", default=None)
    """
    The account used for tracking taxes on purchases for this vendor, for use in
    Canada or the UK.
    """

    tax_on_sales_account: Optional[TaxOnSalesAccount] = FieldInfo(alias="taxOnSalesAccount", default=None)
    """
    The account used for tracking taxes on sales for this vendor, for use in Canada
    or the UK.
    """

    tax_registration_number: Optional[str] = FieldInfo(alias="taxRegistrationNumber", default=None)
    """The vendor's tax registration number, for use in Canada or the UK."""

    terms: Optional[Terms] = None
    """
    The vendor's payment terms, defining when payment is due and any applicable
    discounts.
    """

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when this vendor was last updated, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """

    vendor_type: Optional[VendorType] = FieldInfo(alias="vendorType", default=None)
    """
    The vendor's type, used for categorizing vendors into meaningful segments, such
    as industry or region.
    """

    version: str
    """
    The current version identifier for this vendor, which changes each time the
    object is modified. When updating this object, you must provide the most recent
    `version` to ensure you're working with the latest data; otherwise, the update
    will fail. This value is opaque and should not be interpreted.
    """
