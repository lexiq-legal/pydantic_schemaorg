from pydantic import Field
from pydantic_schemaorg.MedicalEntity import MedicalEntity


class MedicalIndication(MedicalEntity):
    """A condition or factor that indicates use of a medical therapy, including signs, symptoms,"
     "risk factors, anatomical states, etc.

    See https://schema.org/MedicalIndication.

    """

    locals().update({"@type": Field("MedicalIndication", const=True)})


MedicalIndication.update_forward_refs()
