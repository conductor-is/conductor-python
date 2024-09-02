# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["QbdAccount", "Currency", "CustomField", "Parent", "SalesTaxCode", "TaxLineInfo"]


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


class TaxLineInfo(BaseModel):
    tax_line_id: str = FieldInfo(alias="taxLineId")

    tax_line_name: Optional[str] = FieldInfo(alias="taxLineName", default=None)


class QbdAccount(BaseModel):
    id: str
    """
    The QuickBooks-assigned identifier for this account, unique across all accounts.
    """

    account_number: Optional[str] = FieldInfo(alias="accountNumber", default=None)

    account_type: Literal[
        "accounts_payable",
        "accounts_receivable",
        "bank",
        "cost_of_goods_sold",
        "credit_card",
        "equity",
        "expense",
        "fixed_asset",
        "income",
        "long_term_liability",
        "non_posting",
        "other_asset",
        "other_current_asset",
        "other_current_liability",
        "other_expense",
        "other_income",
    ] = FieldInfo(alias="accountType")
    """The type of QuickBooks account."""

    balance: Optional[str] = None

    bank_number: Optional[str] = FieldInfo(alias="bankNumber", default=None)

    cash_flow_classification: Optional[Literal["financing", "investing", "none", "not_applicable", "operating"]] = (
        FieldInfo(alias="cashFlowClassification", default=None)
    )
    """The account's classification for cash flow reporting."""

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when the object was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """

    currency: Optional[Currency] = None
    """The account's currency."""

    custom_fields: List[CustomField] = FieldInfo(alias="customFields")
    """The custom fields added by the user to QuickBooks object as a data extension.

    These fields are not part of the standard QuickBooks object.
    """

    description: Optional[str] = None

    full_name: str = FieldInfo(alias="fullName")

    is_active: bool = FieldInfo(alias="isActive")
    """Whether this account is active.

    QuickBooks hides inactive objects from most views and reports in the UI.
    """

    is_tax_account: Optional[bool] = FieldInfo(alias="isTaxAccount", default=None)
    """Whether this account is used for tax."""

    name: str

    object_type: Literal["qbd_account"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_account"`."""

    parent: Optional[Parent] = None

    sales_tax_code: Optional[SalesTaxCode] = FieldInfo(alias="salesTaxCode", default=None)
    """The sales tax code, indicating whether related items are taxable or non-taxable.

    Two default codes are 'Non' (non-taxable) and 'Tax' (taxable). If QuickBooks is
    not set up to charge sales tax, it will assign the default non-taxable code to
    all sales.
    """

    special_account_type: Optional[
        Literal[
            "accounts_payable",
            "accounts_receivable",
            "condense_item_adjustment_expenses",
            "cost_of_goods_sold",
            "direct_deposit_liabilities",
            "estimates",
            "exchange_gain_loss",
            "inventory_assets",
            "item_receipt_account",
            "opening_balance_equity",
            "payroll_expenses",
            "payroll_liabilities",
            "petty_cash",
            "purchase_orders",
            "reconciliation_differences",
            "retained_earnings",
            "sales_orders",
            "sales_tax_payable",
            "uncategorized_expenses",
            "uncategorized_income",
            "undeposited_funds",
        ]
    ] = FieldInfo(alias="specialAccountType", default=None)
    """
    If specified, then QuickBooks automatically created this account when it was
    needed. Some special accounts cannot be overridden, because QuickBooks uses them
    exclusively for special purposes.
    """

    sublevel: float

    tax_line_info: Optional[TaxLineInfo] = FieldInfo(alias="taxLineInfo", default=None)

    total_balance: Optional[str] = FieldInfo(alias="totalBalance", default=None)

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
