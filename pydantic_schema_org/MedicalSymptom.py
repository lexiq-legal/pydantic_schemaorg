from pydantic import Field
from pydantic_schema_org.MedicalSignOrSymptom import MedicalSignOrSymptom


class MedicalSymptom(MedicalSignOrSymptom):
    """Any complaint sensed and expressed by the patient (therefore defined as subjective)"
     "like stomachache, lower-back pain, or fatigue.

    See https://schema.org/MedicalSymptom.

    """

    locals().update({"@type": Field("MedicalSymptom", const=True)})


MedicalSymptom.update_forward_refs()
