from pydantic import Field
from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration


class InfectiousAgentClass(MedicalEnumeration):
    """Classes of agents or pathogens that transmit infectious diseases. Enumerated type.

    See https://schema.org/InfectiousAgentClass.

    """

    locals().update({"@type": Field("InfectiousAgentClass", const=True)})


InfectiousAgentClass.update_forward_refs()
