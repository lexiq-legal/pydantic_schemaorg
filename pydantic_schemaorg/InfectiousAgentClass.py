from pydantic import Field
from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration


class InfectiousAgentClass(MedicalEnumeration):
    """Classes of agents or pathogens that transmit infectious diseases. Enumerated type.

    See https://schema.org/InfectiousAgentClass.

    """
    type_: str = Field("InfectiousAgentClass", const=True, alias='@type')
    

InfectiousAgentClass.update_forward_refs()
