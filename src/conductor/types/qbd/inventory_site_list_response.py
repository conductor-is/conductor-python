# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .qbd_inventory_site import QbdInventorySite

__all__ = ["InventorySiteListResponse"]


class InventorySiteListResponse(BaseModel):
    data: List[QbdInventorySite]
    """The array of inventory sites."""

    object_type: Literal["list"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"list"`."""

    url: str
    """The endpoint URL where this list can be accessed."""
