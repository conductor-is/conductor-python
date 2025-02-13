# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ServiceItemUpdateParams", "Barcode", "SalesAndPurchaseDetails", "SalesOrPurchaseDetails"]


class ServiceItemUpdateParams(TypedDict, total=False):
    revision_number: Required[Annotated[str, PropertyInfo(alias="revisionNumber")]]
    """
    The current QuickBooks-assigned revision number of the service item object you
    are updating, which you can get by fetching the object first. Provide the most
    recent `revisionNumber` to ensure you're working with the latest data;
    otherwise, the update will return an error.
    """

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    barcode: Barcode
    """The service item's barcode."""

    class_id: Annotated[str, PropertyInfo(alias="classId")]
    """The service item's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default.
    """

    force_unit_of_measure_change: Annotated[bool, PropertyInfo(alias="forceUnitOfMeasureChange")]
    """
    Indicates whether to allow changing the service item's unit-of-measure set
    (using the `unitOfMeasureSetId` field) when the base unit of the new
    unit-of-measure set does not match that of the currently assigned set. Without
    setting this field to `true` in this scenario, the request will fail with an
    error; hence, this field is equivalent to accepting the warning prompt in the
    QuickBooks UI.

    NOTE: Changing the base unit requires you to update the item's
    quantities-on-hand and cost to reflect the new unit; otherwise, these values
    will be inaccurate. Alternatively, consider creating a new item with the desired
    unit-of-measure set and deactivating the old item.
    """

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]
    """Indicates whether this service item is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    Defaults to `true`.
    """

    name: str
    """The case-insensitive name of this service item.

    Not guaranteed to be unique because it does not include the names of its
    hierarchical parent objects like `fullName` does. For example, two service items
    could both have the `name` "Web-Design", but they could have unique `fullName`
    values, such as "Consulting:Web-Design" and "Contracting:Web-Design".

    Maximum length: 31 characters.
    """

    parent_id: Annotated[str, PropertyInfo(alias="parentId")]
    """The parent service item one level above this one in the hierarchy.

    For example, if this service item has a `fullName` of "Consulting:Web-Design",
    its parent has a `fullName` of "Consulting". If this service item is at the top
    level, this field will be `null`.
    """

    sales_and_purchase_details: Annotated[SalesAndPurchaseDetails, PropertyInfo(alias="salesAndPurchaseDetails")]
    """
    Details for service items that are both purchased and sold, such as reimbursable
    expenses or inventory items that are bought from vendors and sold to customers.

    **IMPORTANT**: You cannot specify both `salesAndPurchaseDetails` and
    `salesOrPurchaseDetails` when modifying a service item because an item cannot
    have both configurations.
    """

    sales_or_purchase_details: Annotated[SalesOrPurchaseDetails, PropertyInfo(alias="salesOrPurchaseDetails")]
    """
    Details for service items that are exclusively sold or exclusively purchased,
    but not both. This typically applies to non-inventory items (like a purchased
    office supply that isn't resold) or service items (like consulting services that
    are sold but not purchased).

    **IMPORTANT**: You cannot specify both `salesOrPurchaseDetails` and
    `salesAndPurchaseDetails` when modifying a service item because an item cannot
    have both configurations.
    """

    sales_tax_code_id: Annotated[str, PropertyInfo(alias="salesTaxCodeId")]
    """
    The default sales-tax code for this service item, determining whether it is
    taxable or non-taxable. This can be overridden at the transaction-line level.

    Default codes include "Non" (non-taxable) and "Tax" (taxable), but custom codes
    can also be created in QuickBooks. If QuickBooks is not set up to charge sales
    tax (via the "Do You Charge Sales Tax?" preference), it will assign the default
    non-taxable code to all sales.
    """

    unit_of_measure_set_id: Annotated[str, PropertyInfo(alias="unitOfMeasureSetId")]
    """
    The unit-of-measure set associated with this service item, which consists of a
    base unit and related units.
    """


class Barcode(TypedDict, total=False):
    allow_override: Annotated[bool, PropertyInfo(alias="allowOverride")]
    """Indicates whether to allow the barcode to be overridden."""

    assign_even_if_used: Annotated[bool, PropertyInfo(alias="assignEvenIfUsed")]
    """Indicates whether to assign the barcode even if it is already used."""

    value: str
    """The item's barcode value."""


class SalesAndPurchaseDetails(TypedDict, total=False):
    expense_account_id: Annotated[str, PropertyInfo(alias="expenseAccountId")]
    """The expense account used to track costs from purchases of this item."""

    income_account_id: Annotated[str, PropertyInfo(alias="incomeAccountId")]
    """The income account used to track revenue from sales of this item."""

    preferred_vendor_id: Annotated[str, PropertyInfo(alias="preferredVendorId")]
    """The preferred vendor from whom this item is typically purchased."""

    purchase_cost: Annotated[str, PropertyInfo(alias="purchaseCost")]
    """
    The cost at which this item is purchased from vendors, represented as a decimal
    string.
    """

    purchase_description: Annotated[str, PropertyInfo(alias="purchaseDescription")]
    """
    The description of this item that appears on purchase forms (e.g., checks,
    bills, item receipts) when it is ordered or bought from vendors.
    """

    purchase_tax_code_id: Annotated[str, PropertyInfo(alias="purchaseTaxCodeId")]
    """The tax code applied to purchases of this item.

    Applicable in regions where purchase taxes are used, such as Canada or the UK.
    """

    sales_description: Annotated[str, PropertyInfo(alias="salesDescription")]
    """
    The description of this item that appears on sales forms (e.g., invoices, sales
    receipts) when sold to customers.
    """

    sales_price: Annotated[str, PropertyInfo(alias="salesPrice")]
    """
    The price at which this item is sold to customers, represented as a decimal
    string.
    """

    update_existing_transactions_expense_account: Annotated[
        bool, PropertyInfo(alias="updateExistingTransactionsExpenseAccount")
    ]
    """
    When `true`, applies the new expense account (specified by the
    `expenseAccountId` field) to all existing transactions that use this item. This
    updates historical data and should be used with caution. The update will fail if
    any affected transaction falls within a closed accounting period. If this
    parameter is not specified, QuickBooks will prompt the user before making any
    changes.
    """

    update_existing_transactions_income_account: Annotated[
        bool, PropertyInfo(alias="updateExistingTransactionsIncomeAccount")
    ]
    """
    When `true`, applies the new income account (specified by the `incomeAccountId`
    field) to all existing transactions that use this item. This updates historical
    data and should be used with caution. The update will fail if any affected
    transaction falls within a closed accounting period. If this parameter is not
    specified, QuickBooks will prompt the user before making any changes.
    """


class SalesOrPurchaseDetails(TypedDict, total=False):
    description: str
    """A description of this item."""

    posting_account_id: Annotated[str, PropertyInfo(alias="postingAccountId")]
    """The posting account to which transactions involving this item are posted.

    This could be an income account when selling or an expense account when
    purchasing.
    """

    price: str
    """
    The price at which this item is purchased or sold, represented as a decimal
    string.
    """

    price_percentage: Annotated[str, PropertyInfo(alias="pricePercentage")]
    """
    The price of this item expressed as a percentage, used instead of `price` when
    the item's cost is calculated as a percentage of another amount. For example, a
    service item that costs a percentage of another item's price.
    """

    update_existing_transactions_account: Annotated[bool, PropertyInfo(alias="updateExistingTransactionsAccount")]
    """
    When `true`, applies the new account (specified by the `accountId` field) to all
    existing transactions associated with this item. This updates historical data
    and should be used with caution. The update will fail if any affected
    transaction falls within a closed accounting period. If this parameter is not
    specified, QuickBooks will prompt the user before making any changes.
    """
