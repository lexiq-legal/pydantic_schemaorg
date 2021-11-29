from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.MedicalEvidenceLevel import MedicalEvidenceLevel
from datetime import date
from pydantic_schemaorg.MedicalEntity import MedicalEntity


class MedicalGuideline(MedicalEntity):
    """Any recommendation made by a standard society (e.g. ACC/AHA) or consensus statement"
     "that denotes how to diagnose and treat a particular condition. Note: this type should"
     "be used to tag the actual guideline recommendation; if the guideline recommendation"
     "occurs in a larger scholarly article, use MedicalScholarlyArticle to tag the overall"
     "article, not this type. Note also: the organization making the recommendation should"
     "be captured in the recognizingAuthority base property of MedicalEntity.

    See https://schema.org/MedicalGuideline.

    """

    evidenceOrigin: Optional[Union[List[str], str]] = Field(
        None,
        description="Source of the data used to formulate the guidance, e.g. RCT, consensus opinion, etc.",
    )
    evidenceLevel: Optional[Union[List[MedicalEvidenceLevel], MedicalEvidenceLevel]] = Field(
        None,
        description="Strength of evidence of the data used to formulate the guideline (enumerated).",
    )
    guidelineDate: Optional[Union[List[date], date]] = Field(
        None,
        description="Date on which this guideline's recommendation was made.",
    )
    guidelineSubject: Optional[Union[List[MedicalEntity], MedicalEntity]] = Field(
        None,
        description="The medical conditions, treatments, etc. that are the subject of the guideline.",
    )
    locals().update({"@type": Field("MedicalGuideline", const=True)})


MedicalGuideline.update_forward_refs()
