from pydantic import Field
from pydantic_schemaorg.MedicalTrialDesign import MedicalTrialDesign


class PlaceboControlledTrial(MedicalTrialDesign):
    """A placebo-controlled trial design.

    See https://schema.org/PlaceboControlledTrial.

    """
    type_: str = Field("PlaceboControlledTrial", const=True, alias='@type')
    

PlaceboControlledTrial.update_forward_refs()
