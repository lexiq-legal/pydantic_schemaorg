from pydantic import Field
from pydantic_schemaorg.Organization import Organization


class GovernmentOrganization(Organization):
    """A governmental organization or agency.

    See https://schema.org/GovernmentOrganization.

    """
    type_: str = Field("GovernmentOrganization", const=True, alias='@type')
    

GovernmentOrganization.update_forward_refs()
