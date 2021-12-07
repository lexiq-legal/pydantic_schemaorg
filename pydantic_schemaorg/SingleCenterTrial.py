from pydantic import Field
from pydantic_schemaorg.MedicalTrialDesign import MedicalTrialDesign


class SingleCenterTrial(MedicalTrialDesign):
    """A trial that takes place at a single center.

    See https://schema.org/SingleCenterTrial.

    """
    type_: str = Field("SingleCenterTrial", const=True, alias='@type')
    

SingleCenterTrial.update_forward_refs()
