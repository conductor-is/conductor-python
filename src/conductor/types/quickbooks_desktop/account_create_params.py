# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AccountCreateParams"]


class AccountCreateParams(TypedDict, total=False):
    account_type: Required[
        Annotated[
            Literal[
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
            ],
            PropertyInfo(alias="accountType"),
        ]
    ]
    """The type of QuickBooks account."""

    name: Required[str]

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    account_number: Annotated[str, PropertyInfo(alias="accountNumber")]

    bank_number: Annotated[str, PropertyInfo(alias="bankNumber")]

    currency_id: Annotated[str, PropertyInfo(alias="currencyId")]

    description: str

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]
    """Whether this account is active.

    QuickBooks hides inactive objects from most views and reports in the UI.
    """

    opening_balance: Annotated[str, PropertyInfo(alias="openingBalance")]

    opening_balance_date: Annotated[str, PropertyInfo(alias="openingBalanceDate")]

    parent_id: Annotated[str, PropertyInfo(alias="parentId")]

    sales_tax_code_id: Annotated[str, PropertyInfo(alias="salesTaxCodeId")]

    tax_line_id: Annotated[int, PropertyInfo(alias="taxLineId")]
