from pydantic import Field
from pydantic_schemaorg.MedicalImagingTechnique import MedicalImagingTechnique


class CT(MedicalImagingTechnique):
    """X-ray computed tomography imaging.

    See https://schema.org/CT.

    """
    type_: str = Field("CT", const=True, alias='@type')
    

CT.update_forward_refs()
