# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["InventoryAssemblyItemUpdateParams", "Barcode", "ItemLine"]


class InventoryAssemblyItemUpdateParams(TypedDict, total=False):
    revision_number: Required[Annotated[str, PropertyInfo(alias="revisionNumber")]]
    """
    The current revision number of the inventory assembly item object you are
    updating, which you can get by fetching the object first. Provide the most
    recent `revisionNumber` to ensure you're working with the latest data;
    otherwise, the update will return an error.
    """

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    asset_account_id: Annotated[str, PropertyInfo(alias="assetAccountId")]
    """
    The asset account used to track the current value of this inventory assembly
    item in inventory.
    """

    barcode: Barcode
    """The inventory assembly item's barcode."""

    build_notification_threshold: Annotated[float, PropertyInfo(alias="buildNotificationThreshold")]
    """
    The inventory assembly item's minimum quantity threshold that triggers a build
    notification in QuickBooks. When the sum of `quantityOnHand` (current inventory)
    and `quantityOnOrder` (pending purchase orders) drops below this threshold,
    QuickBooks will notify users that more units need to be built or assembled. This
    helps ensure adequate inventory levels for inventory assembly items.
    """

    class_id: Annotated[str, PropertyInfo(alias="classId")]
    """The inventory assembly item's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default.
    """

    clear_item_lines: Annotated[bool, PropertyInfo(alias="clearItemLines")]
    """
    When `true`, removes all existing item lines associated with this inventory
    assembly item. To modify or add individual item lines, use the field `itemLines`
    instead.
    """

    cogs_account_id: Annotated[str, PropertyInfo(alias="cogsAccountId")]
    """
    The Cost of Goods Sold (COGS) account for this inventory assembly item, tracking
    the original direct costs of producing goods sold.
    """

    force_unit_of_measure_change: Annotated[bool, PropertyInfo(alias="forceUnitOfMeasureChange")]
    """
    Indicates whether to allow changing the inventory assembly item's
    unit-of-measure set (using the `unitOfMeasureSetId` field) when the base unit of
    the new unit-of-measure set does not match that of the currently assigned set.
    Without setting this field to `true` in this scenario, the request will fail
    with an error; hence, this field is equivalent to accepting the warning prompt
    in the QuickBooks UI.

    NOTE: Changing the base unit requires you to update the item's
    quantities-on-hand and cost to reflect the new unit; otherwise, these values
    will be inaccurate. Alternatively, consider creating a new item with the desired
    unit-of-measure set and deactivating the old item.
    """

    income_account_id: Annotated[str, PropertyInfo(alias="incomeAccountId")]
    """
    The income account used to track revenue from sales of this inventory assembly
    item.
    """

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]
    """Indicates whether this inventory assembly item is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    """

    item_lines: Annotated[Iterable[ItemLine], PropertyInfo(alias="itemLines")]
    """The inventory assembly item's lines."""

    maximum_quantity_on_hand: Annotated[float, PropertyInfo(alias="maximumQuantityOnHand")]
    """The maximum quantity of this inventory assembly item desired in inventory."""

    name: str
    """The case-insensitive name of this inventory assembly item.

    Not guaranteed to be unique because it does not include the names of its parent
    objects like `fullName` does. For example, two inventory assembly items could
    both have the `name` "Deluxe Kit", but they could have unique `fullName` values,
    such as "Assemblies:Deluxe Kit" and "Inventory:Deluxe Kit". Maximum length: 31
    characters.
    """

    parent_id: Annotated[str, PropertyInfo(alias="parentId")]
    """The parent inventory assembly item one level above this one in the hierarchy.

    For example, if this inventory assembly item has a `fullName` of
    "Assemblies:Kitchen:Cabinets", its parent has a `fullName` of
    "Assemblies:Kitchen". If this inventory assembly item is at the top level, this
    field will be `null`.
    """

    preferred_vendor_id: Annotated[str, PropertyInfo(alias="preferredVendorId")]
    """
    The preferred vendor from whom this inventory assembly item is typically
    purchased.
    """

    purchase_cost: Annotated[str, PropertyInfo(alias="purchaseCost")]
    """
    The cost at which this inventory assembly item is purchased from vendors,
    represented as a decimal string.
    """

    purchase_description: Annotated[str, PropertyInfo(alias="purchaseDescription")]
    """
    The description of this inventory assembly item that appears on purchase forms
    (e.g., checks, bills, item receipts) when it is ordered or bought from vendors.
    """

    purchase_tax_code_id: Annotated[str, PropertyInfo(alias="purchaseTaxCodeId")]
    """The tax code applied to purchases of this inventory assembly item.

    Applicable in regions where purchase taxes are used, such as Canada or the UK.
    """

    sales_description: Annotated[str, PropertyInfo(alias="salesDescription")]
    """
    The description of this inventory assembly item that appears on sales forms
    (e.g., invoices, sales receipts) when sold to customers.
    """

    sales_price: Annotated[str, PropertyInfo(alias="salesPrice")]
    """
    The price at which this inventory assembly item is sold to customers,
    represented as a decimal string.
    """

    sales_tax_code_id: Annotated[str, PropertyInfo(alias="salesTaxCodeId")]
    """
    The sales-tax code associated with this inventory assembly item, determining
    whether it is taxable or non-taxable. It's used to assign a default tax status
    to all transactions for this inventory assembly item. Default codes include
    "Non" (non-taxable) and "Tax" (taxable), but custom codes can also be created in
    QuickBooks. If QuickBooks is not set up to charge sales tax (via the "Do You
    Charge Sales Tax?" preference), it will assign the default non-taxable code to
    all sales.
    """

    sku: str
    """
    The inventory assembly item's stock keeping unit (SKU), which is sometimes the
    manufacturer's part number.
    """

    unit_of_measure_set_id: Annotated[str, PropertyInfo(alias="unitOfMeasureSetId")]
    """
    The unit-of-measure set associated with this inventory assembly item, which
    consists of a base unit and related units.
    """

    update_existing_transactions_income_account: Annotated[
        bool, PropertyInfo(alias="updateExistingTransactionsIncomeAccount")
    ]
    """
    When `true`, applies the new income account (specified by the `incomeAccountId`
    field) to all existing transactions that use this inventory assembly item. If
    `true`, the income account will be updated in all historical transactions where
    this inventory assembly item appears. Be cautious with this setting as it
    modifies historical data. The update will fail if any affected transactions fall
    within a closed accounting period. If not specified, QuickBooks will prompt the
    user to make this choice.
    """


class Barcode(TypedDict, total=False):
    allow_override: Annotated[bool, PropertyInfo(alias="allowOverride")]
    """Indicates whether to allow the barcode to be overridden."""

    assign_even_if_used: Annotated[bool, PropertyInfo(alias="assignEvenIfUsed")]
    """Indicates whether to assign the barcode even if it is already used."""

    value: str
    """The item's barcode value."""


class ItemLine(TypedDict, total=False):
    inventory_item_id: Annotated[str, PropertyInfo(alias="inventoryItemId")]
    """The inventory item associated with this inventory assembly item line."""

    quantity: float
    """The quantity of the item associated with this inventory assembly item line."""
