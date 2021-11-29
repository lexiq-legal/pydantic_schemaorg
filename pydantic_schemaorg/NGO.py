from pydantic import Field
from pydantic_schemaorg.Organization import Organization


class NGO(Organization):
    """Organization: Non-governmental Organization.

    See https://schema.org/NGO.

    """

    locals().update({"@type": Field("NGO", const=True)})


NGO.update_forward_refs()
