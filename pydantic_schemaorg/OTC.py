from pydantic import Field
from pydantic_schemaorg.DrugPrescriptionStatus import DrugPrescriptionStatus


class OTC(DrugPrescriptionStatus):
    """The character of a medical substance, typically a medicine, of being available over"
     "the counter or not.

    See https://schema.org/OTC.

    """

    locals().update({"@type": Field("OTC", const=True)})


OTC.update_forward_refs()
