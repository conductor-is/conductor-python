# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["QbdAccount", "Currency", "CustomField", "Parent", "SalesTaxCode", "TaxLineDetails"]


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


class TaxLineDetails(BaseModel):
    tax_line_id: str = FieldInfo(alias="taxLineId")

    tax_line_name: Optional[str] = FieldInfo(alias="taxLineName", default=None)


class QbdAccount(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks for this account.

    This ID is unique among all accounts but not across different object types.
    """

    account_number: Optional[str] = FieldInfo(alias="accountNumber", default=None)
    """The account number assigned to this account in QuickBooks.

    Account numbers appear in the chart of accounts, reports, and graphs. Note that
    if the "Use Account Numbers" preference is turned off in QuickBooks, the account
    number may not be visible in the user interface, but it can still be set and
    retrieved through the API.
    """

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
    """
    The classification of this account, indicating its purpose within the chart of
    accounts.
    """

    balance: Optional[str] = None
    """
    The current balance of this account only, excluding balances from any
    subordinate accounts, represented as a decimal string. Compare with
    `totalBalance`. Note that income accounts and balance sheet accounts may not
    have balances.
    """

    bank_account_number: Optional[str] = FieldInfo(alias="bankAccountNumber", default=None)
    """The bank account number or identifying note for this account.

    Access to this field may be restricted based on permissions.
    """

    cash_flow_classification: Optional[Literal["financing", "investing", "none", "not_applicable", "operating"]] = (
        FieldInfo(alias="cashFlowClassification", default=None)
    )
    """Indicates how this account is classified for cash flow reporting.

    If `none`, the account has not been classified. If `not_applicable`, the account
    does not qualify to be classified (e.g., a bank account tracking cash
    transactions is not part of a cash flow report).
    """

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when this account was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """

    currency: Optional[Currency] = None
    """The account's currency.

    For built-in currencies, the name and code are standard international values.
    For user-defined currencies, all values are editable.
    """

    custom_fields: List[CustomField] = FieldInfo(alias="customFields")
    """The custom fields added by the user to this account object as a data extension.

    These fields are not part of the standard QuickBooks object.
    """

    description: Optional[str] = None
    """A longer explanation of the `name` of this account."""

    full_name: str = FieldInfo(alias="fullName")
    """
    The fully-qualified unique name for this account, formed by combining the names
    of its parent objects with its own `name`, separated by colons. For example, if
    an account is under 'Corporate' and has the `name` 'Accounts Payable', its
    `fullName` would be 'Corporate:Accounts Payable'. Unlike `name`, `fullName` is
    guaranteed to be unique across all account objects.
    """

    is_active: bool = FieldInfo(alias="isActive")
    """Indicates whether this account is active.

    Inactive objects are typically hidden from views and reports in QuickBooks
    Desktop.
    """

    is_tax_account: Optional[bool] = FieldInfo(alias="isTaxAccount", default=None)
    """Indicates whether this account is used for tracking taxes."""

    name: str
    """The case-insensitive name of this account.

    Not guaranteed to be unique because it does not include the names of its parent
    objects like `fullName` does. For example, two objects could both have the
    `name` "Accounts Payable", but they could have unique `fullName` values, such as
    "Corporate:Accounts Payable" and "Finance:Accounts Payable".
    """

    object_type: Literal["qbd_account"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_account"`."""

    parent: Optional[Parent] = None
    """The parent account one level above this one in the hierarchy.

    For example, if this account has a `fullName` of "Corporate:Accounts Payable",
    its parent has a `fullName` of "Corporate". If this account is at the top level,
    `parent` will be `null`.
    """

    sales_tax_code: Optional[SalesTaxCode] = FieldInfo(alias="salesTaxCode", default=None)
    """
    The sales tax code associated with this account, indicating whether it is
    taxable or non-taxable. Default codes include 'NON' (non-taxable) and 'TAX'
    (taxable). If QuickBooks is not set up to charge sales tax, it will assign the
    default non-taxable code to all sales.
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
    Indicates if this account is a special account automatically created by
    QuickBooks for specific purposes.
    """

    sublevel: float
    """The depth level of this account in the hierarchy.

    A top-level account has a `sublevel` of 0; each subsequent sublevel increases
    this number by 1. For example, a account with a `fullName` of
    "Corporate:Accounts Payable" would have a `sublevel` of 1.
    """

    tax_line_details: Optional[TaxLineDetails] = FieldInfo(alias="taxLineDetails", default=None)
    """
    The tax line information associated with this account, used for tax reporting
    purposes.
    """

    total_balance: Optional[str] = FieldInfo(alias="totalBalance", default=None)
    """
    The combined balance of this account and all its subordinate accounts,
    represented as a decimal string. For example, the `totalBalance` for XYZ Bank
    would be the total of the balances of all its sub-accounts (checking, savings,
    and so on). If XYZ Bank did not have any sub-accounts, `totalBalance` and
    `balance` would be the same.
    """

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when this account was last updated, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """

    version: str
    """
    The current version identifier for this account, which changes each time the
    object is modified. When updating this object, you must provide the most recent
    `version` to ensure you're working with the latest data; otherwise, the update
    will fail. This value is opaque and should not be interpreted.
    """
