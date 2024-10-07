# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .sales_tax_code import SalesTaxCode

__all__ = ["SalesTaxCodeListResponse"]


class SalesTaxCodeListResponse(BaseModel):
    data: List[SalesTaxCode]
    """The array of sales tax codes."""

    object_type: Literal["list"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"list"`."""

    url: str
    """The endpoint URL where this list can be accessed."""
