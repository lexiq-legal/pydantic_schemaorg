from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.DoseSchedule import DoseSchedule


class RecommendedDoseSchedule(DoseSchedule):
    """A recommended dosing schedule for a drug or supplement as prescribed or recommended"
     "by an authority or by the drug/supplement's manufacturer. Capture the recommending"
     "authority in the recognizingAuthority property of MedicalEntity.

    See: https://schema.org/RecommendedDoseSchedule
    Model depth: 5
    """
    type_: str = Field("RecommendedDoseSchedule", alias='@type')
    

