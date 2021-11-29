from pydantic import Field
from pydantic_schemaorg.MedicalTrialDesign import MedicalTrialDesign


class PlaceboControlledTrial(MedicalTrialDesign):
    """A placebo-controlled trial design.

    See https://schema.org/PlaceboControlledTrial.

    """

    locals().update({"@type": Field("PlaceboControlledTrial", const=True)})


PlaceboControlledTrial.update_forward_refs()
