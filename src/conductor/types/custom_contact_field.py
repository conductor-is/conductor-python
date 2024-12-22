# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel

__all__ = ["CustomContactField"]


class CustomContactField(BaseModel):
    name: str
    """The name of the custom contact field (e.g., "old address", "secondary phone")."""

    value: str
    """The value of the custom contact field."""
