from pydantic import Field
from pydantic_schemaorg.AutomotiveBusiness import AutomotiveBusiness


class AutoBodyShop(AutomotiveBusiness):
    """Auto body shop.

    See https://schema.org/AutoBodyShop.

    """
    type_: str = Field("AutoBodyShop", const=True, alias='@type')
    

AutoBodyShop.update_forward_refs()
