from pydantic import Field
from pydantic_schema_org.MedicalTrialDesign import MedicalTrialDesign


class MultiCenterTrial(MedicalTrialDesign):
    """A trial that takes place at multiple centers.

    See https://schema.org/MultiCenterTrial.

    """

    locals().update({"@type": Field("MultiCenterTrial", const=True)})


MultiCenterTrial.update_forward_refs()
