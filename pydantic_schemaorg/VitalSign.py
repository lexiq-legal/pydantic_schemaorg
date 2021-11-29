from pydantic import Field
from pydantic_schemaorg.MedicalSign import MedicalSign


class VitalSign(MedicalSign):
    """Vital signs are measures of various physiological functions in order to assess the most"
     "basic body functions.

    See https://schema.org/VitalSign.

    """

    locals().update({"@type": Field("VitalSign", const=True)})


VitalSign.update_forward_refs()
