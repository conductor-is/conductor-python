# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BillUpdateParams", "ExpenseLine", "ItemGroupLine", "ItemGroupLineItemLine", "ItemLine", "VendorAddress"]


class BillUpdateParams(TypedDict, total=False):
    version: Required[str]
    """
    The current version identifier of the bill you are updating, which you can get
    by fetching the object first. Provide the most recent `version` to ensure you're
    working with the latest data; otherwise, the update will fail.
    """

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    accounts_payable_account_id: Annotated[str, PropertyInfo(alias="accountsPayableAccountId")]
    """
    The Accounts Payable account to which this bill is assigned, used to track the
    amount owed. If not specified, the default Accounts Payable account in
    QuickBooks is used.
    """

    clear_expense_lines: Annotated[bool, PropertyInfo(alias="clearExpenseLines")]
    """Indicates whether to clear all the expense lines of this bill.

    To modify individual lines, use the field `expenseLines`.
    """

    clear_item_lines: Annotated[bool, PropertyInfo(alias="clearItemLines")]
    """Indicates whether to clear all the item lines of this bill.

    To modify individual lines, use the field `itemLines`.
    """

    due_date: Annotated[Union[str, date], PropertyInfo(alias="dueDate", format="iso8601")]
    """The date by which this bill must be paid, in ISO 8601 format (YYYY-MM-DD)."""

    exchange_rate: Annotated[float, PropertyInfo(alias="exchangeRate")]
    """
    The market exchange rate between this bill's currency and the home currency in
    QuickBooks at the time of this transaction. Represented as a decimal value
    (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).
    """

    expense_lines: Annotated[Iterable[ExpenseLine], PropertyInfo(alias="expenseLines")]
    """The bill's expense lines, each representing one line in this expense.

    IMPORTANT: When updating a bill's expense lines, this array completely REPLACES
    all existing expense lines for that bill. To retain any current expense lines,
    include them in this array, even if they have not changed. Any expense lines not
    included will be removed. To add a new expense line, include it with its `id`
    set to `-1`. If you do not wish to modify the expense lines, you can omit this
    field entirely to keep them unchanged.
    """

    item_group_lines: Annotated[Iterable[ItemGroupLine], PropertyInfo(alias="itemGroupLines")]
    """
    The bill's item group lines, each representing a predefined set of items bundled
    together because they are commonly purchased together or grouped for faster
    entry.

    IMPORTANT: When updating a bill's item group lines, this array completely
    REPLACES all existing item group lines for that bill. To retain any current item
    group lines, include them in this array, even if they have not changed. Any item
    group lines not included will be removed. To add a new item group line, include
    it with its `id` set to `-1`. If you do not wish to modify the item group lines,
    you can omit this field entirely to keep them unchanged.
    """

    item_lines: Annotated[Iterable[ItemLine], PropertyInfo(alias="itemLines")]
    """
    The bill's item lines, each representing the purchase of a specific item or
    service.

    IMPORTANT: When updating a bill's item lines, this array completely REPLACES all
    existing item lines for that bill. To retain any current item lines, include
    them in this array, even if they have not changed. Any item lines not included
    will be removed. To add a new item line, include it with its `id` set to `-1`.
    If you do not wish to modify the item lines, you can omit this field entirely to
    keep them unchanged.
    """

    memo: str
    """A memo or note for this bill, as entered by the user.

    Appears in the Accounts Payable register and relevant reports.
    """

    ref_number: Annotated[str, PropertyInfo(alias="refNumber")]
    """
    The case-sensitive user-defined reference number for this bill, which can be
    used to identify the transaction in QuickBooks. This value is not required to be
    unique and can be arbitrarily changed by the QuickBooks user.
    """

    sales_tax_code_id: Annotated[str, PropertyInfo(alias="salesTaxCodeId")]
    """
    The sales-tax code associated with this bill, determining whether it is taxable
    or non-taxable. It's used to assign a default tax status to all transactions for
    this bill. Default codes include "Non" (non-taxable) and "Tax" (taxable), but
    custom codes can also be created in QuickBooks. If QuickBooks is not set up to
    charge sales tax (via the "Do You Charge Sales Tax?" preference), it will assign
    the default non-taxable code to all sales.
    """

    terms_id: Annotated[str, PropertyInfo(alias="termsId")]
    """
    The bill's payment terms, defining when payment is due and any applicable
    discounts.
    """

    transaction_date: Annotated[Union[str, date], PropertyInfo(alias="transactionDate", format="iso8601")]
    """The date of this bill, in ISO 8601 format (YYYY-MM-DD)."""

    vendor_address: Annotated[VendorAddress, PropertyInfo(alias="vendorAddress")]
    """The address of the vendor who sent this bill."""

    vendor_id: Annotated[str, PropertyInfo(alias="vendorId")]
    """The vendor who sent this bill for goods or services purchased."""


class ExpenseLine(TypedDict, total=False):
    id: Required[str]
    """
    The QuickBooks-assigned unique identifier of an existing expense line you wish
    to retain or update. Set this field to `-1` for new expense lines you wish to
    add.
    """

    account_id: Annotated[str, PropertyInfo(alias="accountId")]
    """The expense account being debited (increased).

    The corresponding account being credited is usually a liability account (e.g.,
    Accounts Payable) or an asset account (e.g., Cash), depending on the transaction
    type.
    """

    amount: str
    """The monetary amount of this expense line, represented as a decimal string."""

    billing_status: Annotated[
        Literal["billable", "has_been_billed", "not_billable"], PropertyInfo(alias="billingStatus")
    ]
    """The billing status of this expense line."""

    class_id: Annotated[str, PropertyInfo(alias="classId")]
    """The expense line's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default. If a class is specified for the entire parent transaction, it is
    automatically applied to all expense lines unless overridden here, at the
    transaction line level.
    """

    memo: str
    """A memo or note for this expense line, as entered by the user."""

    payee_id: Annotated[str, PropertyInfo(alias="payeeId")]
    """
    If `account` refers to an Accounts Payable (A/P) account, `payee` refers to the
    expense's vendor (not the customer). If `account` refers to any other type of
    account, `payee` refers to the expense's customer (not the vendor).
    """

    sales_representative_id: Annotated[str, PropertyInfo(alias="salesRepresentativeId")]
    """The expense line's sales representative.

    Sales representatives can be employees, vendors, or other names in QuickBooks.
    """

    sales_tax_code_id: Annotated[str, PropertyInfo(alias="salesTaxCodeId")]
    """
    The sales-tax code associated with this expense line, determining whether it is
    taxable or non-taxable. It's used to assign a default tax status to all
    transactions for this expense line. Default codes include "Non" (non-taxable)
    and "Tax" (taxable), but custom codes can also be created in QuickBooks. If
    QuickBooks is not set up to charge sales tax (via the "Do You Charge Sales Tax?"
    preference), it will assign the default non-taxable code to all sales.
    """


class ItemGroupLineItemLine(TypedDict, total=False):
    id: Required[str]
    """
    The QuickBooks-assigned unique identifier of an existing item line you wish to
    retain or update. Set this field to `-1` for new item lines you wish to add.
    """

    amount: str
    """The monetary amount of this item line, represented as a decimal string.

    If both `quantity` and `cost` are specified but not `amount`, QuickBooks will
    use them to calculate `amount`. If `amount`, `cost`, and `quantity` are all
    unspecified, then QuickBooks will calculate `amount` based on a `quantity` of
    `1` and the suggested `cost`.
    """

    billing_status: Annotated[
        Literal["billable", "has_been_billed", "not_billable"], PropertyInfo(alias="billingStatus")
    ]
    """The billing status of this item line."""

    class_id: Annotated[str, PropertyInfo(alias="classId")]
    """The item line's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default. If a class is specified for the entire parent transaction, it is
    automatically applied to all item lines unless overridden here, at the
    transaction line level.
    """

    cost: str
    """The cost of this item line, represented as a decimal string.

    If both `quantity` and `amount` are specified but not `cost`, QuickBooks will
    use them to calculate `cost`.
    """

    customer_id: Annotated[str, PropertyInfo(alias="customerId")]
    """The customer or customer-job associated with this item line."""

    description: str
    """A description of this item line."""

    expiration_date: Annotated[Union[str, date], PropertyInfo(alias="expirationDate", format="iso8601")]
    """
    The expiration date for the serial number or lot number of the item associated
    with this item line, in ISO 8601 format (YYYY-MM-DD). This is particularly
    relevant for perishable or time-sensitive inventory items. Note that this field
    is only supported on QuickBooks Desktop 2023 or later.
    """

    inventory_site_id: Annotated[str, PropertyInfo(alias="inventorySiteId")]
    """
    The site location where inventory for the item associated with this item line is
    stored.
    """

    inventory_site_location_id: Annotated[str, PropertyInfo(alias="inventorySiteLocationId")]
    """
    The specific location (e.g., bin or shelf) within the inventory site where the
    item associated with this item line is stored.
    """

    item_id: Annotated[str, PropertyInfo(alias="itemId")]
    """The item associated with this item line.

    This can refer to any good or service that the business buys or sells, including
    item types such as a service item, inventory item, or special calculation item
    like a discount item or sales-tax item.
    """

    lot_number: Annotated[str, PropertyInfo(alias="lotNumber")]
    """The lot number of the item associated with this item line.

    Used for tracking groups of inventory items that are purchased or manufactured
    together.
    """

    override_item_account_id: Annotated[str, PropertyInfo(alias="overrideItemAccountId")]
    """
    The account to use for this item line, overriding the default account associated
    with the item.
    """

    override_unit_of_measure_set_id: Annotated[str, PropertyInfo(alias="overrideUnitOfMeasureSetId")]
    """Specifies an alternative unit of measure set for this specific item line.

    This does not change the item's default unit of measure set (which is set on the
    item itself rather than a transaction line), but allows selecting from a
    different set of units for this particular line. For example, an item typically
    measured in volume units could be sold using weight units in a specific
    transaction. The actual unit selection (e.g., "pound" or "kilogram") is made
    separately via the `unitOfMeasure` field.
    """

    quantity: float
    """The quantity of the item associated with this item line."""

    sales_representative_id: Annotated[str, PropertyInfo(alias="salesRepresentativeId")]
    """The item line's sales representative.

    Sales representatives can be employees, vendors, or other names in QuickBooks.
    """

    sales_tax_code_id: Annotated[str, PropertyInfo(alias="salesTaxCodeId")]
    """
    The sales-tax code associated with this item line, determining whether it is
    taxable or non-taxable. It's used to assign a default tax status to all
    transactions for this item line. Default codes include "Non" (non-taxable) and
    "Tax" (taxable), but custom codes can also be created in QuickBooks. If
    QuickBooks is not set up to charge sales tax (via the "Do You Charge Sales Tax?"
    preference), it will assign the default non-taxable code to all sales.
    """

    serial_number: Annotated[str, PropertyInfo(alias="serialNumber")]
    """The serial number of the item associated with this item line.

    This is used for tracking individual units of serialized inventory items.
    """

    unit_of_measure: Annotated[str, PropertyInfo(alias="unitOfMeasure")]
    """The unit of measure used for the `quantity` in this item line.

    Must be a valid unit within the item's available units of measure.
    """


class ItemGroupLine(TypedDict, total=False):
    id: Required[str]
    """
    The QuickBooks-assigned unique identifier of an existing item group line you
    wish to retain or update. Set this field to `-1` for new item group lines you
    wish to add.
    """

    item_group_id: Annotated[str, PropertyInfo(alias="itemGroupId")]
    """
    The item group line's item group, representing a predefined set of items bundled
    because they are commonly purchased together or grouped for faster entry.
    """

    item_lines: Annotated[Iterable[ItemGroupLineItemLine], PropertyInfo(alias="itemLines")]
    """
    The item group line's item lines, each representing the purchase of a specific
    item or service.

    IMPORTANT: When updating an item group line's item lines, this array completely
    REPLACES all existing item lines for that item group line. To retain any current
    item lines, include them in this array, even if they have not changed. Any item
    lines not included will be removed. To add a new item line, include it with its
    `id` set to `-1`. If you do not wish to modify the item lines, you can omit this
    field entirely to keep them unchanged.
    """

    override_unit_of_measure_set_id: Annotated[str, PropertyInfo(alias="overrideUnitOfMeasureSetId")]
    """Specifies an alternative unit of measure set for this specific item group line.

    This does not change the item's default unit of measure set (which is set on the
    item itself rather than a transaction line), but allows selecting from a
    different set of units for this particular line. For example, an item typically
    measured in volume units could be sold using weight units in a specific
    transaction. The actual unit selection (e.g., "pound" or "kilogram") is made
    separately via the `unitOfMeasure` field.
    """

    quantity: float
    """The quantity of the item group associated with this item group line."""

    unit_of_measure: Annotated[str, PropertyInfo(alias="unitOfMeasure")]
    """The unit of measure used for the `quantity` in this item group line.

    Must be a valid unit within the item's available units of measure.
    """


class ItemLine(TypedDict, total=False):
    id: Required[str]
    """
    The QuickBooks-assigned unique identifier of an existing item line you wish to
    retain or update. Set this field to `-1` for new item lines you wish to add.
    """

    amount: str
    """The monetary amount of this item line, represented as a decimal string.

    If both `quantity` and `cost` are specified but not `amount`, QuickBooks will
    use them to calculate `amount`. If `amount`, `cost`, and `quantity` are all
    unspecified, then QuickBooks will calculate `amount` based on a `quantity` of
    `1` and the suggested `cost`.
    """

    billing_status: Annotated[
        Literal["billable", "has_been_billed", "not_billable"], PropertyInfo(alias="billingStatus")
    ]
    """The billing status of this item line."""

    class_id: Annotated[str, PropertyInfo(alias="classId")]
    """The item line's class.

    Classes can be used to categorize objects into meaningful segments, such as
    department, location, or type of work. In QuickBooks, class tracking is off by
    default. If a class is specified for the entire parent transaction, it is
    automatically applied to all item lines unless overridden here, at the
    transaction line level.
    """

    cost: str
    """The cost of this item line, represented as a decimal string.

    If both `quantity` and `amount` are specified but not `cost`, QuickBooks will
    use them to calculate `cost`.
    """

    customer_id: Annotated[str, PropertyInfo(alias="customerId")]
    """The customer or customer-job associated with this item line."""

    description: str
    """A description of this item line."""

    expiration_date: Annotated[Union[str, date], PropertyInfo(alias="expirationDate", format="iso8601")]
    """
    The expiration date for the serial number or lot number of the item associated
    with this item line, in ISO 8601 format (YYYY-MM-DD). This is particularly
    relevant for perishable or time-sensitive inventory items. Note that this field
    is only supported on QuickBooks Desktop 2023 or later.
    """

    inventory_site_id: Annotated[str, PropertyInfo(alias="inventorySiteId")]
    """
    The site location where inventory for the item associated with this item line is
    stored.
    """

    inventory_site_location_id: Annotated[str, PropertyInfo(alias="inventorySiteLocationId")]
    """
    The specific location (e.g., bin or shelf) within the inventory site where the
    item associated with this item line is stored.
    """

    item_id: Annotated[str, PropertyInfo(alias="itemId")]
    """The item associated with this item line.

    This can refer to any good or service that the business buys or sells, including
    item types such as a service item, inventory item, or special calculation item
    like a discount item or sales-tax item.
    """

    lot_number: Annotated[str, PropertyInfo(alias="lotNumber")]
    """The lot number of the item associated with this item line.

    Used for tracking groups of inventory items that are purchased or manufactured
    together.
    """

    override_item_account_id: Annotated[str, PropertyInfo(alias="overrideItemAccountId")]
    """
    The account to use for this item line, overriding the default account associated
    with the item.
    """

    override_unit_of_measure_set_id: Annotated[str, PropertyInfo(alias="overrideUnitOfMeasureSetId")]
    """Specifies an alternative unit of measure set for this specific item line.

    This does not change the item's default unit of measure set (which is set on the
    item itself rather than a transaction line), but allows selecting from a
    different set of units for this particular line. For example, an item typically
    measured in volume units could be sold using weight units in a specific
    transaction. The actual unit selection (e.g., "pound" or "kilogram") is made
    separately via the `unitOfMeasure` field.
    """

    quantity: float
    """The quantity of the item associated with this item line."""

    sales_representative_id: Annotated[str, PropertyInfo(alias="salesRepresentativeId")]
    """The item line's sales representative.

    Sales representatives can be employees, vendors, or other names in QuickBooks.
    """

    sales_tax_code_id: Annotated[str, PropertyInfo(alias="salesTaxCodeId")]
    """
    The sales-tax code associated with this item line, determining whether it is
    taxable or non-taxable. It's used to assign a default tax status to all
    transactions for this item line. Default codes include "Non" (non-taxable) and
    "Tax" (taxable), but custom codes can also be created in QuickBooks. If
    QuickBooks is not set up to charge sales tax (via the "Do You Charge Sales Tax?"
    preference), it will assign the default non-taxable code to all sales.
    """

    serial_number: Annotated[str, PropertyInfo(alias="serialNumber")]
    """The serial number of the item associated with this item line.

    This is used for tracking individual units of serialized inventory items.
    """

    unit_of_measure: Annotated[str, PropertyInfo(alias="unitOfMeasure")]
    """The unit of measure used for the `quantity` in this item line.

    Must be a valid unit within the item's available units of measure.
    """


class VendorAddress(TypedDict, total=False):
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
    """
    A note written at the bottom of the address in the form in which it appears,
    such as the invoice form.
    """

    postal_code: Annotated[str, PropertyInfo(alias="postalCode")]
    """The postal code or ZIP code of the address."""

    state: str
    """The state, county, province, or region name of the address."""
