# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ClassCreateParams"]


class ClassCreateParams(TypedDict, total=False):
    name: Required[str]
    """The case-insensitive name of the class.

    Does not include the names of its accentors like `fullName` does.
    """

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]
    """Whether this class is active.

    QuickBooks hides inactive objects from most views and reports in the UI.
    """

    parent_id: Annotated[str, PropertyInfo(alias="parentId")]
