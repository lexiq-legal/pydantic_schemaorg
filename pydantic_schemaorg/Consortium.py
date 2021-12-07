from pydantic import Field
from pydantic_schemaorg.Organization import Organization


class Consortium(Organization):
    """A Consortium is a membership [[Organization]] whose members are typically Organizations.

    See https://schema.org/Consortium.

    """
    type_: str = Field("Consortium", const=True, alias='@type')
    

Consortium.update_forward_refs()
