from pydantic import Field
from pydantic_schemaorg.Organization import Organization


class ResearchOrganization(Organization):
    """A Research Organization (e.g. scientific institute, research company).

    See https://schema.org/ResearchOrganization.

    """

    locals().update({"@type": Field("ResearchOrganization", const=True)})


ResearchOrganization.update_forward_refs()
