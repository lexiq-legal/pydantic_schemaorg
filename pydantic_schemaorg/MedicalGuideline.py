from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional, Any

from pydantic_schemaorg.MedicalEntity import MedicalEntity


class MedicalGuideline(MedicalEntity):
    """Any recommendation made by a standard society (e.g. ACC/AHA) or consensus statement"
     "that denotes how to diagnose and treat a particular condition. Note: this type should"
     "be used to tag the actual guideline recommendation; if the guideline recommendation"
     "occurs in a larger scholarly article, use MedicalScholarlyArticle to tag the overall"
     "article, not this type. Note also: the organization making the recommendation should"
     "be captured in the recognizingAuthority base property of MedicalEntity.

    See: https://schema.org/MedicalGuideline
    Model depth: 3
    """

    type_: str = Field("MedicalGuideline", const=True, alias="@type")
    evidenceOrigin: "Optional[Union[List[str], str]]" = Field(
        None,
        description="Source of the data used to formulate the guidance, e.g. RCT, consensus opinion, etc.",
    )
    evidenceLevel: "Optional[Union[List[Union[MedicalEvidenceLevel, str]], Union[MedicalEvidenceLevel, str]]]" = Field(
        None,
        description="Strength of evidence of the data used to formulate the guideline (enumerated).",
    )
    guidelineDate: "Optional[Union[List[Union[date, str]], Union[date, str]]]" = Field(
        None,
        description="Date on which this guideline's recommendation was made.",
    )
    guidelineSubject: "Optional[Union[List[Union[MedicalEntity, str]], Union[MedicalEntity, str]]]" = Field(
        None,
        description="The medical conditions, treatments, etc. that are the subject of the guideline.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.MedicalEvidenceLevel import MedicalEvidenceLevel

    from datetime import date

    from pydantic_schemaorg.MedicalEntity import MedicalEntity

    MedicalGuideline.update_forward_refs()
