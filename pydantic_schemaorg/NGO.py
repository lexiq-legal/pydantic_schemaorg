from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Organization import Organization


class NGO(Organization):
    """Organization: Non-governmental Organization.

    See: https://schema.org/NGO
    Model depth: 3
    """

    type_: str = Field("NGO", const=True, alias="@type")


if TYPE_CHECKING:

    NGO.update_forward_refs()
