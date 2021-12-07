from pydantic import Field
from pydantic_schemaorg.MedicalImagingTechnique import MedicalImagingTechnique


class MRI(MedicalImagingTechnique):
    """Magnetic resonance imaging.

    See https://schema.org/MRI.

    """
    type_: str = Field("MRI", const=True, alias='@type')
    

MRI.update_forward_refs()
