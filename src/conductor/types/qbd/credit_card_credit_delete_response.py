# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CreditCardCreditDeleteResponse"]


class CreditCardCreditDeleteResponse(BaseModel):
    id: str
    """The QuickBooks-assigned unique identifier of the deleted credit card credit."""

    deleted: bool
    """Indicates whether the credit card credit was deleted."""

    object_type: Literal["qbd_credit_card_credit"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_credit_card_credit"`."""

    ref_number: Optional[str] = FieldInfo(alias="refNumber", default=None)
    """
    The case-sensitive user-defined reference number of the deleted credit card
    credit.
    """
