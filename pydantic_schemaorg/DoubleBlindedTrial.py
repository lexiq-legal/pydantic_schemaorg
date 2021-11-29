from pydantic import Field
from pydantic_schemaorg.MedicalTrialDesign import MedicalTrialDesign


class DoubleBlindedTrial(MedicalTrialDesign):
    """A trial design in which neither the researcher nor the patient knows the details of the"
     "treatment the patient was randomly assigned to.

    See https://schema.org/DoubleBlindedTrial.

    """

    locals().update({"@type": Field("DoubleBlindedTrial", const=True)})


DoubleBlindedTrial.update_forward_refs()
