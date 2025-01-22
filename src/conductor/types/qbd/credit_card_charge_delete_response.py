# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CreditCardChargeDeleteResponse"]


class CreditCardChargeDeleteResponse(BaseModel):
    id: str
    """The QuickBooks-assigned unique identifier of the deleted credit card charge."""

    deleted: bool
    """Indicates whether the credit card charge was deleted."""

    object_type: Literal["qbd_credit_card_charge"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_credit_card_charge"`."""

    ref_number: Optional[str] = FieldInfo(alias="refNumber", default=None)
    """
    The case-sensitive user-defined reference number of the deleted credit card
    charge.
    """
