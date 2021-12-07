from pydantic import Field
from pydantic_schemaorg.Organization import Organization


class NGO(Organization):
    """Organization: Non-governmental Organization.

    See https://schema.org/NGO.

    """
    type_: str = Field("NGO", const=True, alias='@type')
    

NGO.update_forward_refs()
