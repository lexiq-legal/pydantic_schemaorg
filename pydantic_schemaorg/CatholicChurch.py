from pydantic import Field
from pydantic_schemaorg.Church import Church


class CatholicChurch(Church):
    """A Catholic church.

    See https://schema.org/CatholicChurch.

    """
    type_: str = Field("CatholicChurch", const=True, alias='@type')
    

CatholicChurch.update_forward_refs()
