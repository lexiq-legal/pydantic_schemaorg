from pydantic import Field
from pydantic_schemaorg.Organization import Organization


class ResearchOrganization(Organization):
    """A Research Organization (e.g. scientific institute, research company).

    See https://schema.org/ResearchOrganization.

    """
    type_: str = Field("ResearchOrganization", const=True, alias='@type')
    

ResearchOrganization.update_forward_refs()
