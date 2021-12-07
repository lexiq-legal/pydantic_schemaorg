from pydantic import Field
from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration


class MedicalImagingTechnique(MedicalEnumeration):
    """Any medical imaging modality typically used for diagnostic purposes. Enumerated type.

    See https://schema.org/MedicalImagingTechnique.

    """
    type_: str = Field("MedicalImagingTechnique", const=True, alias='@type')
    

MedicalImagingTechnique.update_forward_refs()
