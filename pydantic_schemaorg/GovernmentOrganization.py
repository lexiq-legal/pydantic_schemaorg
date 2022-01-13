from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Organization import Organization


class GovernmentOrganization(Organization):
    """A governmental organization or agency.

    See: https://schema.org/GovernmentOrganization
    Model depth: 3
    """

    type_: str = Field("GovernmentOrganization", const=True, alias="@type")


if TYPE_CHECKING:

    GovernmentOrganization.update_forward_refs()
