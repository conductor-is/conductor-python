# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["QbdClass", "Parent"]


class Parent(BaseModel):
    id: Optional[str] = None
    """The unique identifier assigned by QuickBooks for this object.

    This ID is unique among all objects of the same type, but not across different
    QuickBooks object types.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The fully-qualified unique name for this object, formed by combining the names
    of its parent objects with its own `name`, separated by colons. Not
    case-sensitive.
    """


class QbdClass(BaseModel):
    id: str
    """The unique identifier assigned by QuickBooks for this class.

    This ID is unique among all classes but not across different QuickBooks object
    types.
    """

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when this class was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """

    full_name: str = FieldInfo(alias="fullName")
    """
    The fully-qualified unique name for this class, formed by combining the names of
    its parent objects with its own `name`, separated by colons. For example, if a
    class is under "Corporate:Sales" and has the `name` "Marketing", its `fullName`
    would be "Corporate:Sales:Marketing". Unlike `name`, `fullName` is guaranteed to
    be unique across all class objects. Not case-sensitive.
    """

    is_active: bool = FieldInfo(alias="isActive")
    """Indicates whether this class is active.

    Inactive objects are typically hidden from views and reports in QuickBooks.
    """

    name: str
    """The case-insensitive name of this class.

    Not guaranteed to be unique because it does not include the names of its parent
    objects like `fullName` does. For example, two classes could both have the
    `name` "Marketing", but they could have unique `fullName` values, such as
    "Corporate:Marketing" and "Internal:Marketing".
    """

    object_type: Literal["qbd_class"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_class"`."""

    parent: Optional[Parent] = None
    """The parent class one level above this one in the hierarchy.

    For example, if this class has a `fullName` of "Corporate:Sales:Marketing", its
    parent has a `fullName` of "Corporate:Sales". If this class is at the top level,
    `parent` will be `null`.
    """

    sublevel: float
    """The depth level of this class in the hierarchy.

    A top-level class has a `sublevel` of 0; each subsequent sublevel increases this
    number by 1. For example, a class with a `fullName` of
    "Corporate:Sales:Marketing" would have a `sublevel` of 2.
    """

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when this class was last updated, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """

    version: str
    """
    The current version identifier for this class, which changes each time the
    object is modified. When updating this object, you must provide the most recent
    `version` to ensure you're working with the latest data; otherwise, the update
    will fail. This value is opaque and should not be interpreted.
    """
