from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Project import Project


class ResearchProject(Project):
    """A Research project.

    See: https://schema.org/ResearchProject
    Model depth: 4
    """
    type_: str = Field("ResearchProject", alias='@type')
    

