from pydantic import Field
from pydantic_schemaorg.MedicalTherapy import MedicalTherapy


class RadiationTherapy(MedicalTherapy):
    """A process of care using radiation aimed at improving a health condition.

    See https://schema.org/RadiationTherapy.

    """
    type_: str = Field("RadiationTherapy", const=True, alias='@type')
    

RadiationTherapy.update_forward_refs()
