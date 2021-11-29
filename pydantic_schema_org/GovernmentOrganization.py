from pydantic import Field
from pydantic_schema_org.Organization import Organization


class GovernmentOrganization(Organization):
    """A governmental organization or agency.

    See https://schema.org/GovernmentOrganization.

    """

    locals().update({"@type": Field("GovernmentOrganization", const=True)})


GovernmentOrganization.update_forward_refs()
