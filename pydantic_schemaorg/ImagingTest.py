from pydantic import Field
from pydantic_schemaorg.MedicalImagingTechnique import MedicalImagingTechnique
from typing import List, Optional, Union, Any
from pydantic_schemaorg.MedicalTest import MedicalTest


class ImagingTest(MedicalTest):
    """Any medical imaging modality typically used for diagnostic purposes.

    See https://schema.org/ImagingTest.

    """

    imagingTechnique: Optional[Union[List[MedicalImagingTechnique], MedicalImagingTechnique]] = Field(
        None,
        description="Imaging technique used.",
    )
    locals().update({"@type": Field("ImagingTest", const=True)})


ImagingTest.update_forward_refs()
