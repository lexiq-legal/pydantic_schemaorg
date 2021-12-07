from pydantic import Field
from pydantic_schemaorg.DoseSchedule import DoseSchedule


class MaximumDoseSchedule(DoseSchedule):
    """The maximum dosing schedule considered safe for a drug or supplement as recommended"
     "by an authority or by the drug/supplement's manufacturer. Capture the recommending"
     "authority in the recognizingAuthority property of MedicalEntity.

    See https://schema.org/MaximumDoseSchedule.

    """
    type_: str = Field("MaximumDoseSchedule", const=True, alias='@type')
    

MaximumDoseSchedule.update_forward_refs()
