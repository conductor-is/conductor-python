# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

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


class BillingRate(BaseModel):
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


class PrefillAccount(BaseModel):
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


class SalesTaxReturn(BaseModel):
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


class TaxOnPurchasesAccount(BaseModel):
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


class TaxOnSalesAccount(BaseModel):
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


class VendorType(BaseModel):
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


class QbdVendor(BaseModel):
    id: str
    """The QuickBooks-assigned identifier for this vendor, unique across all vendors."""

    account_number: Optional[str] = FieldInfo(alias="accountNumber", default=None)
    """The vendor's account number."""

    additional_contacts: List[AdditionalContact] = FieldInfo(alias="additionalContacts")
    """Additional contacts."""

    additional_notes: List[AdditionalNote] = FieldInfo(alias="additionalNotes")
    """Additional notes about this vendor."""

    alternate_contact: Optional[str] = FieldInfo(alias="alternateContact", default=None)
    """The vendor's alternate contact name."""

    alternate_phone: Optional[str] = FieldInfo(alias="alternatePhone", default=None)
    """The vendor's alternate phone number."""

    balance: Optional[str] = None
    """The amount owed to this vendor."""

    billing_address: Optional[BillingAddress] = FieldInfo(alias="billingAddress", default=None)
    """The vendor's billing address."""

    billing_rate: Optional[BillingRate] = FieldInfo(alias="billingRate", default=None)
    """The billing rate associated with this vendor.

    Use this rate to override a service-item's rate when recording a time-tracking
    transaction for this vendor.
    """

    cc: Optional[str] = None
    """The vendor's CC email address."""

    check_name: Optional[str] = FieldInfo(alias="checkName", default=None)
    """The vendor's name as it will appear on checks sent to the vendor."""

    class_: Optional[Class] = FieldInfo(alias="class", default=None)
    """The class associated with this object.

    Classes can be used to categorize objects or transactions by department,
    location, or other meaningful segments.
    """

    company_name: Optional[str] = FieldInfo(alias="companyName", default=None)
    """The name of the vendor's business.

    This is used on invoices, checks, and other forms.
    """

    contact: Optional[str] = None
    """The vendor's contact name."""

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when the object was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """

    credit_limit: Optional[str] = FieldInfo(alias="creditLimit", default=None)
    """The vendor's credit limit."""

    currency: Optional[Currency] = None
    """The vendor's currency."""

    custom_contact_fields: List[CustomContactField] = FieldInfo(alias="customContactFields")
    """Additional custom contact fields."""

    custom_fields: List[CustomField] = FieldInfo(alias="customFields")
    """The custom fields added by the user to QuickBooks object as a data extension.

    These fields are not part of the standard QuickBooks object.
    """

    email: Optional[str] = None
    """The vendor's email address."""

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """
    An arbitrary globally unique identifier (GUID) the developer can provide to
    track this object in their own system. This value must be formatted as a GUID;
    otherwise, QuickBooks will return an error.
    """

    fax: Optional[str] = None
    """The vendor's fax number."""

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)
    """The vendor's first name."""

    is_active: bool = FieldInfo(alias="isActive")
    """Whether this vendor is active.

    QuickBooks hides inactive objects from most views and reports in the UI.
    """

    is_eligible_for1099: Optional[bool] = FieldInfo(alias="isEligibleFor1099", default=None)
    """Whether the vendor is eligible for 1099.

    If `true`, then the fields `taxId` and `billingAddress` are required.
    """

    is_sales_tax_agency: Optional[bool] = FieldInfo(alias="isSalesTaxAgency", default=None)
    """Whether this vendor is a sales tax agency."""

    is_tax_on_tax: Optional[bool] = FieldInfo(alias="isTaxOnTax", default=None)
    """Whether tax is charged on top of tax in Canada or the UK for this vendor."""

    is_tax_tracked_on_purchases: Optional[bool] = FieldInfo(alias="isTaxTrackedOnPurchases", default=None)
    """Whether tax is tracked on purchases in Canada or the UK for this vendor."""

    is_tax_tracked_on_sales: Optional[bool] = FieldInfo(alias="isTaxTrackedOnSales", default=None)
    """Whether tax is tracked on sales in Canada or the UK for this vendor."""

    job_title: Optional[str] = FieldInfo(alias="jobTitle", default=None)
    """The vendor's job title."""

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)
    """The vendor's last name."""

    middle_name: Optional[str] = FieldInfo(alias="middleName", default=None)
    """The vendor's middle name."""

    name: str
    """The vendor's case-insensitive unique name, unique across all vendors."""

    note: Optional[str] = None
    """Additional information about this vendor."""

    object_type: Literal["qbd_vendor"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_vendor"`."""

    phone: Optional[str] = None
    """The vendor's phone number."""

    prefill_account: List[PrefillAccount] = FieldInfo(alias="prefillAccount")
    """The expense account to prefill when entering bills for this vendor."""

    reporting_period: Optional[Literal["monthly", "quarterly"]] = FieldInfo(alias="reportingPeriod", default=None)
    """The reporting period associated with this vendor in Canada or the UK."""

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

    sales_tax_return: Optional[SalesTaxReturn] = FieldInfo(alias="salesTaxReturn", default=None)
    """The sales tax return associated with this vendor."""

    salutation: Optional[str] = None
    """The vendor's formal salutation that precedes their name."""

    shipping_address: Optional[ShippingAddress] = FieldInfo(alias="shippingAddress", default=None)
    """The vendor's shipping address."""

    tax_id: Optional[str] = FieldInfo(alias="taxId", default=None)
    """The vendor's tax ID."""

    tax_on_purchases_account: Optional[TaxOnPurchasesAccount] = FieldInfo(alias="taxOnPurchasesAccount", default=None)
    """The account used for taxes on purchases in Canada or the UK for this vendor."""

    tax_on_sales_account: Optional[TaxOnSalesAccount] = FieldInfo(alias="taxOnSalesAccount", default=None)
    """The account used for taxes on sales in Canada or the UK for this vendor."""

    tax_registration_number: Optional[str] = FieldInfo(alias="taxRegistrationNumber", default=None)
    """
    The tax registration number associated with this vendor, for use in Canada or
    the UK.
    """

    terms: Optional[Terms] = None
    """The vendor's payment terms."""

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when the object was last updated, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """

    vendor_type: Optional[VendorType] = FieldInfo(alias="vendorType", default=None)
    """The vendor's type, used for categorization.

    This can represent industry, location, or other business-specific
    classifications.
    """

    version: str
    """The current version identifier of the object that changes with each
    modification.

    Provide this value when updating the object to verify you are working with the
    latest version; mismatched values will fail.
    """
