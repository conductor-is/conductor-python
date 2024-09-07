# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["QbdClass", "Parent"]


class Parent(BaseModel):
    id: Optional[str] = None
    """The QuickBooks-assigned unique identifier for this object.

    This ID is not unique across _all_ object types in QuickBooks, but it is unique
    for each particular object type. This ID is automatically generated when the
    object is created in QuickBooks.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """
    The hierarchical name of this object, including its full path in the QuickBooks
    list structure. Names are separated by colons (e.g., "Parent:Child:Grandchild").
    This field is case-insensitive.
    """


class QbdClass(BaseModel):
    id: str
    """The QuickBooks-assigned identifier for this class, unique across all classes."""

    created_at: str = FieldInfo(alias="createdAt")
    """
    The date and time when the object was created, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """

    full_name: str = FieldInfo(alias="fullName")

    is_active: bool = FieldInfo(alias="isActive")
    """Whether this class is active.

    QuickBooks hides inactive objects from most views and reports in the UI.
    """

    name: str
    """The case-insensitive name of the class.

    Does not include the names of its accentors like `fullName` does.
    """

    object_type: Literal["qbd_class"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_class"`."""

    parent: Optional[Parent] = None

    sublevel: float
    """The nesting level of this class within the class hierarchy.

    A top-level class has a `sublevel` of 0, a direct sub-class has a `sublevel` of
    1, and so on. For example, a class with a `fullName` of
    "Corporate:Sales:Marketing" and a `name` of "Marketing" would have a `sublevel`
    of 2.
    """

    updated_at: str = FieldInfo(alias="updatedAt")
    """
    The date and time when the object was last updated, in ISO 8601 format
    (YYYY-MM-DDThh:mm:ss±hh:mm). The time zone is the same as the user's time zone
    in QuickBooks.
    """

    version: str
    """The current version identifier of the object that changes with each
    modification.

    Provide this value when updating the object to verify you are working with the
    latest version; mismatched values will fail.
    """
