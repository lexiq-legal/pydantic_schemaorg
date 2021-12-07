from pydantic import Field
from pydantic_schemaorg.Project import Project


class ResearchProject(Project):
    """A Research project.

    See https://schema.org/ResearchProject.

    """
    type_: str = Field("ResearchProject", const=True, alias='@type')
    

ResearchProject.update_forward_refs()
