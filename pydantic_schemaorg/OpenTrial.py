from pydantic import Field
from pydantic_schemaorg.MedicalTrialDesign import MedicalTrialDesign


class OpenTrial(MedicalTrialDesign):
    """A trial design in which the researcher knows the full details of the treatment, and so"
     "does the patient.

    See https://schema.org/OpenTrial.

    """

    locals().update({"@type": Field("OpenTrial", const=True)})


OpenTrial.update_forward_refs()
