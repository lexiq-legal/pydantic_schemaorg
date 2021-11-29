from pydantic import Field
from pydantic_schema_org.MedicalImagingTechnique import MedicalImagingTechnique
from typing import Any, Optional, Union, List
from pydantic_schema_org.MedicalTest import MedicalTest


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
