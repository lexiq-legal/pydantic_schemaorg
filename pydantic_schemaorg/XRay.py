from pydantic import Field
from pydantic_schemaorg.MedicalImagingTechnique import MedicalImagingTechnique


class XRay(MedicalImagingTechnique):
    """X-ray imaging.

    See https://schema.org/XRay.

    """
    type_: str = Field("XRay", const=True, alias='@type')
    

XRay.update_forward_refs()
