from pydantic import Field
from pydantic_schemaorg.MedicalTrialDesign import MedicalTrialDesign


class RandomizedTrial(MedicalTrialDesign):
    """A randomized trial design.

    See https://schema.org/RandomizedTrial.

    """
    type_: str = Field("RandomizedTrial", const=True, alias='@type')
    

RandomizedTrial.update_forward_refs()
