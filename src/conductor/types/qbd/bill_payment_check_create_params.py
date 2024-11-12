# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BillPaymentCheckCreateParams", "ApplyToTransaction", "ApplyToTransactionApplyCredit"]


class BillPaymentCheckCreateParams(TypedDict, total=False):
    bank_account_id: Required[Annotated[str, PropertyInfo(alias="bankAccountId")]]
    """
    The bank account from which the funds are being drawn for this bill payment
    check; e.g., Checking or Savings. This bill payment check will decrease the
    balance of this account.
    """

    transaction_date: Required[Annotated[Union[str, date], PropertyInfo(alias="transactionDate", format="iso8601")]]
    """The date of this bill payment check, in ISO 8601 format (YYYY-MM-DD)."""

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    apply_to_transactions: Annotated[Iterable[ApplyToTransaction], PropertyInfo(alias="applyToTransactions")]
    """Transactions to be paid by this bill payment check.

    This will create a link between this bill payment check and the specified
    transactions.

    NOTE: By default, QuickBooks will not return any information about the linked
    transactions in this endpoint's response even when this request is successful.
    To see the transactions linked via this field, refetch the bill payment check
    and check the `linkedTransactions` response field. If fetching a list of bill
    payment checks, you must also specify the parameter `includeLinkedTransactions`
    to see the `linkedTransactions` response field.
    """

    exchange_rate: Annotated[float, PropertyInfo(alias="exchangeRate")]
    """
    The market exchange rate between this bill payment check's currency and the home
    currency in QuickBooks at the time of this transaction. Represented as a decimal
    value (e.g., 1.2345 for 1 EUR = 1.2345 USD if USD is the home currency).
    """

    external_id: Annotated[str, PropertyInfo(alias="externalId")]
    """
    A globally unique identifier (GUID) you can provide for tracking this object in
    your external system. Must be formatted as a valid GUID; otherwise, QuickBooks
    will return an error. This field is immutable and can only be set during object
    creation.
    """

    is_queued_for_print: Annotated[bool, PropertyInfo(alias="isQueuedForPrint")]
    """
    Indicates whether this bill payment check is included in the queue of documents
    for QuickBooks to print.
    """

    memo: str
    """A memo or note for this bill payment check, as entered by the user."""

    payables_account_id: Annotated[str, PropertyInfo(alias="payablesAccountId")]
    """
    The Accounts-Payable (A/P) account to which this bill payment check is assigned,
    used to track the amount owed. If not specified, the default Accounts-Payable
    account in QuickBooks is used.
    """

    payee_id: Annotated[str, PropertyInfo(alias="payeeId")]
    """The person or company who sent this bill payment check."""

    ref_number: Annotated[str, PropertyInfo(alias="refNumber")]
    """
    The case-sensitive user-defined reference number for this bill payment check,
    which can be used to identify the transaction in QuickBooks. This value is not
    required to be unique and can be arbitrarily changed by the QuickBooks user.
    """


class ApplyToTransactionApplyCredit(TypedDict, total=False):
    applied_amount: Required[Annotated[str, PropertyInfo(alias="appliedAmount")]]
    """The amount of credit applied to this transaction.

    This could include customer deposits, payments, or credits. Represented as a
    decimal string.
    """

    credit_memo_id: Required[Annotated[str, PropertyInfo(alias="creditMemoId")]]
    """The unique identifier of the credit memo to apply to this transaction."""

    override_credit_application: Annotated[bool, PropertyInfo(alias="overrideCreditApplication")]
    """Indicates whether to override the credit."""


class ApplyToTransaction(TypedDict, total=False):
    id: Required[str]
    """The ID of the receivable transaction to which this payment is applied."""

    apply_credits: Annotated[Iterable[ApplyToTransactionApplyCredit], PropertyInfo(alias="applyCredits")]
    """Credit memos to apply to this receivable transaction, reducing its balance.

    This creates a link between this receivable transaction and the specified credit
    memos.

    NOTE: By default, QuickBooks will not return any information about the linked
    transactions in this endpoint's response even when this request is successful.
    To see the transactions linked via this field, refetch the receivable
    transaction and check the `linkedTransactions` response field. If fetching a
    list of receivable transactions, you must also specify the parameter
    `includeLinkedTransactions` to see the `linkedTransactions` response field.
    """

    discount_account_id: Annotated[str, PropertyInfo(alias="discountAccountId")]
    """The financial account used to track this receivable transaction's discount."""

    discount_amount: Annotated[str, PropertyInfo(alias="discountAmount")]
    """
    The monetary amount by which to reduce the receivable transaction's receivable
    amount, represented as a decimal string.
    """

    discount_class_id: Annotated[str, PropertyInfo(alias="discountClassId")]
    """The class used to track this receivable transaction's discount."""

    payment_amount: Annotated[str, PropertyInfo(alias="paymentAmount")]
    """
    The monetary amount to apply to the receivable transaction, represented as a
    decimal string.
    """
