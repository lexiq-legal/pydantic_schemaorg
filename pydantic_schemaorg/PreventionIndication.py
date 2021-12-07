from pydantic import Field
from pydantic_schemaorg.MedicalIndication import MedicalIndication


class PreventionIndication(MedicalIndication):
    """An indication for preventing an underlying condition, symptom, etc.

    See https://schema.org/PreventionIndication.

    """
    type_: str = Field("PreventionIndication", const=True, alias='@type')
    

PreventionIndication.update_forward_refs()
