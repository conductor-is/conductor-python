# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EndUser"]


class EndUser(BaseModel):
    id: str
    """The unique identifier for this EndUser.

    You must save this value to your database because it is how you identify which
    of your users to receive your API requests.
    """

    company_name: str = FieldInfo(alias="companyName")
    """Your end-user's company name that will be shown elsewhere in Conductor."""

    created_at: str = FieldInfo(alias="createdAt")
    """The time at which the object was created."""

    email: str
    """Your end-user's email address for identification purposes."""

    object_type: Literal["end_user"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"end_user"`."""

    source_id: str = FieldInfo(alias="sourceId")
    """Your end-user's unique ID from your system.

    Maps users between your database and Conductor.
    """
