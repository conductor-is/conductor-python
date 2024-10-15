# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EndUserCreateParams"]


class EndUserCreateParams(TypedDict, total=False):
    company_name: Required[Annotated[str, PropertyInfo(alias="companyName")]]
    """The end-user's company name that will be shown elsewhere in Conductor."""

    email: Required[str]
    """The end-user's email address for identification purposes.

    Setting this field will not cause any emails to be sent.
    """

    source_id: Required[Annotated[str, PropertyInfo(alias="sourceId")]]
    """The end-user's unique identifier from your system.

    Maps users between your database and Conductor. Must be unique for each user. If
    you have only one user, you may use any string value.
    """
