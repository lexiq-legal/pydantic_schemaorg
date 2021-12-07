from pydantic import Field
from pydantic_schemaorg.DrugPrescriptionStatus import DrugPrescriptionStatus


class PrescriptionOnly(DrugPrescriptionStatus):
    """Available by prescription only.

    See https://schema.org/PrescriptionOnly.

    """
    type_: str = Field("PrescriptionOnly", const=True, alias='@type')
    

PrescriptionOnly.update_forward_refs()
