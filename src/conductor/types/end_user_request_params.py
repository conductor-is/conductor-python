# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EndUserRequestParams"]


class EndUserRequestParams(TypedDict, total=False):
    id: Required[str]
    """The ID of the EndUser who owns the integration connection."""

    qbd_payload: Required[Annotated[Dict[str, object], PropertyInfo(alias="qbdPayload")]]
    """The request body to send to the integration connection."""
