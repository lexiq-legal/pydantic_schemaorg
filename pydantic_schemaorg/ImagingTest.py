from pydantic import Field
from pydantic_schemaorg.MedicalImagingTechnique import MedicalImagingTechnique
from typing import Any, Optional, Union, List
from pydantic_schemaorg.MedicalTest import MedicalTest


class ImagingTest(MedicalTest):
    """Any medical imaging modality typically used for diagnostic purposes.

    See https://schema.org/ImagingTest.

    """
    type_: str = Field("ImagingTest", const=True, alias='@type')
    imagingTechnique: Optional[Union[List[MedicalImagingTechnique], MedicalImagingTechnique]] = Field(
        None,
        description="Imaging technique used.",
    )
    

ImagingTest.update_forward_refs()
