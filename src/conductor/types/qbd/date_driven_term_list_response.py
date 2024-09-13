# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .date_driven_term import DateDrivenTerm

__all__ = ["DateDrivenTermListResponse"]


class DateDrivenTermListResponse(BaseModel):
    data: List[DateDrivenTerm]
    """The array of date-driven-terms."""

    has_more: bool = FieldInfo(alias="hasMore")
    """Indicates whether there are more objects to be fetched."""

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
    """
    The pagination token to use with the `cursor` request parameter to fetch the
    next set of results. This value is only returned when using the `limit`
    parameter.
    """

    object_type: Literal["list"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"list"`."""

    remaining_count: Optional[float] = FieldInfo(alias="remainingCount", default=None)
    """The number of objects remaining to be fetched."""

    url: str
    """The endpoint URL where this list can be accessed."""
