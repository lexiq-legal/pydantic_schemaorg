from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.MedicalGuideline import MedicalGuideline


class MedicalGuidelineRecommendation(MedicalGuideline):
    """A guideline recommendation that is regarded as efficacious and where quality of the"
     "data supporting the recommendation is sound.

    See https://schema.org/MedicalGuidelineRecommendation.

    """

    recommendationStrength: Optional[Union[List[str], str]] = Field(
        None,
        description="Strength of the guideline's recommendation (e.g. 'class I').",
    )
    locals().update({"@type": Field("MedicalGuidelineRecommendation", const=True)})


MedicalGuidelineRecommendation.update_forward_refs()
