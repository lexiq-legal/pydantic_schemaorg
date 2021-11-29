from pydantic import Field
from pydantic_schemaorg.Project import Project


class ResearchProject(Project):
    """A Research project.

    See https://schema.org/ResearchProject.

    """

    locals().update({"@type": Field("ResearchProject", const=True)})


ResearchProject.update_forward_refs()
