# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["EndUserRequestParams"]


class EndUserRequestParams(TypedDict, total=False):
    id: Required[str]
    """The ID of the EndUser who owns the integration connection."""

    body: Required[Dict[str, object]]
    """The request body to send to the integration connection."""
