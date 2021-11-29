from pydantic import Field
from pydantic_schemaorg.InfectiousAgentClass import InfectiousAgentClass


class Virus(InfectiousAgentClass):
    """Pathogenic virus that causes viral infection.

    See https://schema.org/Virus.

    """

    locals().update({"@type": Field("Virus", const=True)})


Virus.update_forward_refs()
