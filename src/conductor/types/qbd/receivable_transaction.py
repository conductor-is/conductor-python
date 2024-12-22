# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .linked_transaction import LinkedTransaction

__all__ = ["ReceivableTransaction", "DiscountAccount", "DiscountClass"]


class DiscountAccount(BaseModel):
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


class DiscountClass(BaseModel):
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


class ReceivableTransaction(BaseModel):
    amount: Optional[str] = None
    """
    The monetary amount of this receivable transaction, represented as a decimal
    string.
    """

    balance_remaining: Optional[str] = FieldInfo(alias="balanceRemaining", default=None)
    """
    The outstanding balance of this receivable transaction after applying any
    credits or payments. Represented as a decimal string.
    """

    discount_account: Optional[DiscountAccount] = FieldInfo(alias="discountAccount", default=None)
    """The financial account used to track this receivable transaction's discount."""

    discount_amount: Optional[str] = FieldInfo(alias="discountAmount", default=None)
    """
    The monetary amount by which to reduce the receivable transaction's receivable
    amount, represented as a decimal string.
    """

    discount_class: Optional[DiscountClass] = FieldInfo(alias="discountClass", default=None)
    """The class used to track this receivable transaction's discount."""

    linked_transactions: List[LinkedTransaction] = FieldInfo(alias="linkedTransactions")
    """
    The receivable transaction's linked transactions, such as payments applied,
    credits used, or associated purchase orders.

    **IMPORTANT**: You must specify the parameter `includeLinkedTransactions` when
    fetching a list of receivable transactions to receive this field because it is
    not returned by default.
    """

    ref_number: Optional[str] = FieldInfo(alias="refNumber", default=None)
    """
    The case-sensitive user-defined reference number for this receivable
    transaction, which can be used to identify the transaction in QuickBooks. This
    value is not required to be unique and can be arbitrarily changed by the
    QuickBooks user.
    """

    transaction_date: date = FieldInfo(alias="transactionDate")
    """The date of this receivable transaction, in ISO 8601 format (YYYY-MM-DD)."""

    transaction_id: str = FieldInfo(alias="transactionId")
    """The ID of the receivable transaction to which this payment is applied."""

    transaction_type: Literal[
        "ar_refund_credit_card",
        "bill",
        "bill_payment_check",
        "bill_payment_credit_card",
        "build_assembly",
        "charge",
        "check",
        "credit_card_charge",
        "credit_card_credit",
        "credit_memo",
        "deposit",
        "estimate",
        "inventory_adjustment",
        "invoice",
        "item_receipt",
        "journal_entry",
        "liability_adjustment",
        "paycheck",
        "payroll_liability_check",
        "purchase_order",
        "receive_payment",
        "sales_order",
        "sales_receipt",
        "sales_tax_payment_check",
        "transfer",
        "vendor_credit",
        "ytd_adjustment",
    ] = FieldInfo(alias="transactionType")
    """The type of transaction for this receivable transaction."""
