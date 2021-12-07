from pydantic import Field
from pydantic_schemaorg.MedicalSign import MedicalSign


class VitalSign(MedicalSign):
    """Vital signs are measures of various physiological functions in order to assess the most"
     "basic body functions.

    See https://schema.org/VitalSign.

    """
    type_: str = Field("VitalSign", const=True, alias='@type')
    

VitalSign.update_forward_refs()
