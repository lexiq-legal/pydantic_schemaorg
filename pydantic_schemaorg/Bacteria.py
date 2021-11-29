from pydantic import Field
from pydantic_schemaorg.InfectiousAgentClass import InfectiousAgentClass


class Bacteria(InfectiousAgentClass):
    """Pathogenic bacteria that cause bacterial infection.

    See https://schema.org/Bacteria.

    """

    locals().update({"@type": Field("Bacteria", const=True)})


Bacteria.update_forward_refs()
