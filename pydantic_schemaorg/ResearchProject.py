from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Project import Project


class ResearchProject(Project):
    """A Research project.

    See: https://schema.org/ResearchProject
    Model depth: 4
    """

    type_: str = Field("ResearchProject", const=True, alias="@type")


if TYPE_CHECKING:

    ResearchProject.update_forward_refs()
