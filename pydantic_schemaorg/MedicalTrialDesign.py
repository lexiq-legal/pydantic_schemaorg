from pydantic import Field
from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration


class MedicalTrialDesign(MedicalEnumeration):
    """Design models for medical trials. Enumerated type.

    See https://schema.org/MedicalTrialDesign.

    """

    locals().update({"@type": Field("MedicalTrialDesign", const=True)})


MedicalTrialDesign.update_forward_refs()
