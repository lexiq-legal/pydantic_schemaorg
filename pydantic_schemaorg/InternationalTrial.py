from pydantic import Field
from pydantic_schemaorg.MedicalTrialDesign import MedicalTrialDesign


class InternationalTrial(MedicalTrialDesign):
    """An international trial.

    See https://schema.org/InternationalTrial.

    """
    type_: str = Field("InternationalTrial", const=True, alias='@type')
    

InternationalTrial.update_forward_refs()
