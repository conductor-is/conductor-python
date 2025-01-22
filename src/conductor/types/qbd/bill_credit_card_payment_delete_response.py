# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["BillCreditCardPaymentDeleteResponse"]


class BillCreditCardPaymentDeleteResponse(BaseModel):
    id: str
    """
    The QuickBooks-assigned unique identifier of the deleted bill credit card
    payment.
    """

    deleted: bool
    """Indicates whether the bill credit card payment was deleted."""

    object_type: Literal["qbd_bill_credit_card_payment"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_bill_credit_card_payment"`."""

    ref_number: Optional[str] = FieldInfo(alias="refNumber", default=None)
    """
    The case-sensitive user-defined reference number of the deleted bill credit card
    payment.
    """
