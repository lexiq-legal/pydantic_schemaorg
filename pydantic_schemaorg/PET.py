from pydantic import Field
from pydantic_schemaorg.MedicalImagingTechnique import MedicalImagingTechnique


class PET(MedicalImagingTechnique):
    """Positron emission tomography imaging.

    See https://schema.org/PET.

    """
    type_: str = Field("PET", const=True, alias='@type')
    

PET.update_forward_refs()
