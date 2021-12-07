from pydantic import Field
from pydantic_schemaorg.MedicalTrialDesign import MedicalTrialDesign


class MultiCenterTrial(MedicalTrialDesign):
    """A trial that takes place at multiple centers.

    See https://schema.org/MultiCenterTrial.

    """
    type_: str = Field("MultiCenterTrial", const=True, alias='@type')
    

MultiCenterTrial.update_forward_refs()
