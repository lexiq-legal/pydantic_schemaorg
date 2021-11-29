from pydantic import Field
from pydantic_schemaorg.InfectiousAgentClass import InfectiousAgentClass


class Prion(InfectiousAgentClass):
    """A prion is an infectious agent composed of protein in a misfolded form.

    See https://schema.org/Prion.

    """

    locals().update({"@type": Field("Prion", const=True)})


Prion.update_forward_refs()
