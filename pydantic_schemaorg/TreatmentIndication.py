from pydantic import Field
from pydantic_schemaorg.MedicalIndication import MedicalIndication


class TreatmentIndication(MedicalIndication):
    """An indication for treating an underlying condition, symptom, etc.

    See https://schema.org/TreatmentIndication.

    """
    type_: str = Field("TreatmentIndication", const=True, alias='@type')
    

TreatmentIndication.update_forward_refs()
