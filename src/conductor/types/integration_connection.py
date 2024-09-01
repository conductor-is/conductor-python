# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["IntegrationConnection"]


class IntegrationConnection(BaseModel):
    id: str
    """The unique identifier for this IntegrationConnection."""

    created_at: str = FieldInfo(alias="createdAt")
    """The time at which the object was created."""

    end_user_id: str = FieldInfo(alias="endUserId")
    """The ID of the EndUser who owns this IntegrationConnection."""

    integration_slug: Literal["quickbooks_desktop"] = FieldInfo(alias="integrationSlug")
    """The identifier of the third-party platform to integrate."""

    object_type: Literal["integration_connection"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"integration_connection"`."""
