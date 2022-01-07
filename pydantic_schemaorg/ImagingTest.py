from pydantic import Field
from pydantic_schemaorg.MedicalImagingTechnique import MedicalImagingTechnique
from typing import List, Optional, Union
from pydantic_schemaorg.MedicalTest import MedicalTest


class ImagingTest(MedicalTest):
    """Any medical imaging modality typically used for diagnostic purposes.

    See https://schema.org/ImagingTest.

    """
    type_: str = Field("ImagingTest", const=True, alias='@type')
    imagingTechnique: Optional[Union[List[Union[MedicalImagingTechnique, str]], Union[MedicalImagingTechnique, str]]] = Field(
        None,
        description="Imaging technique used.",
    )
    

ImagingTest.update_forward_refs()
