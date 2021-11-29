from pydantic import Field
from pydantic_schemaorg.InfectiousAgentClass import InfectiousAgentClass


class MulticellularParasite(InfectiousAgentClass):
    """Multicellular parasite that causes an infection.

    See https://schema.org/MulticellularParasite.

    """

    locals().update({"@type": Field("MulticellularParasite", const=True)})


MulticellularParasite.update_forward_refs()
