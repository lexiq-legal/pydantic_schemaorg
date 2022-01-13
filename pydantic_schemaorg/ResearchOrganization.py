from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Organization import Organization


class ResearchOrganization(Organization):
    """A Research Organization (e.g. scientific institute, research company).

    See: https://schema.org/ResearchOrganization
    Model depth: 3
    """

    type_: str = Field("ResearchOrganization", const=True, alias="@type")


if TYPE_CHECKING:

    ResearchOrganization.update_forward_refs()
