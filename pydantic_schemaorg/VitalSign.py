from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalSign import MedicalSign


class VitalSign(MedicalSign):
    """Vital signs are measures of various physiological functions in order to assess the most"
     "basic body functions.

    See: https://schema.org/VitalSign
    Model depth: 6
    """
    type_: str = Field("VitalSign", alias='@type')
    

