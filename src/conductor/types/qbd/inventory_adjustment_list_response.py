# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .inventory_adjustment import InventoryAdjustment

__all__ = ["InventoryAdjustmentListResponse"]


class InventoryAdjustmentListResponse(BaseModel):
    data: List[InventoryAdjustment]
    """The array of inventory adjustments."""

    object_type: Literal["list"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"list"`."""

    url: str
    """The endpoint URL where this list can be accessed."""
