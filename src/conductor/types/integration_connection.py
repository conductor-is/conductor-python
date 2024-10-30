# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["IntegrationConnection"]


class IntegrationConnection(BaseModel):
    id: str
    """The unique identifier for this IntegrationConnection."""

    created_at: str = FieldInfo(alias="createdAt")
    """The date and time when this IntegrationConnection was created."""

    integration_slug: Literal["quickbooks_desktop"] = FieldInfo(alias="integrationSlug")
    """The identifier of the third-party platform to integrate."""

    last_request_at: Optional[str] = FieldInfo(alias="lastRequestAt", default=None)
    """The date and time of your last API request to this IntegrationConnection."""

    object_type: Literal["integration_connection"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"integration_connection"`."""
