# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ClassUpdateParams"]


class ClassUpdateParams(TypedDict, total=False):
    revision_number: Required[Annotated[str, PropertyInfo(alias="revisionNumber")]]
    """
    The current revision number of the class object you are updating, which you can
    get by fetching the object first. Provide the most recent `revisionNumber` to
    ensure you're working with the latest data; otherwise, the update will return an
    error.
    """

    conductor_end_user_id: Required[Annotated[str, PropertyInfo(alias="Conductor-End-User-Id")]]
    """
    The ID of the EndUser to receive this request (e.g.,
    `"Conductor-End-User-Id: {{END_USER_ID}}"`).
    """

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]
    """Indicates whether this class is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    """

    name: str
    """The case-insensitive name of this class.

    Not guaranteed to be unique because it does not include the names of its
    hierarchical parent objects like `fullName` does. For example, two classes could
    both have the `name` "Marketing", but they could have unique `fullName` values,
    such as "Department:Marketing" and "Internal:Marketing". Maximum length: 31
    characters.
    """

    parent_id: Annotated[str, PropertyInfo(alias="parentId")]
    """The parent class one level above this one in the hierarchy.

    For example, if this class has a `fullName` of "Department:Marketing", its
    parent has a `fullName` of "Department". If this class is at the top level, this
    field will be `null`.
    """
