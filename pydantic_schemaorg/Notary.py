from pydantic import Field
from pydantic_schemaorg.LegalService import LegalService


class Notary(LegalService):
    """A notary.

    See https://schema.org/Notary.

    """
    type_: str = Field("Notary", const=True, alias='@type')
    

Notary.update_forward_refs()
