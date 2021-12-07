from pydantic import Field
from pydantic_schemaorg.InfectiousAgentClass import InfectiousAgentClass


class MulticellularParasite(InfectiousAgentClass):
    """Multicellular parasite that causes an infection.

    See https://schema.org/MulticellularParasite.

    """
    type_: str = Field("MulticellularParasite", const=True, alias='@type')
    

MulticellularParasite.update_forward_refs()
