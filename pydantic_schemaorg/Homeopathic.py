from pydantic import Field
from pydantic_schemaorg.MedicineSystem import MedicineSystem


class Homeopathic(MedicineSystem):
    """A system of medicine based on the principle that a disease can be cured by a substance that"
     "produces similar symptoms in healthy people.

    See https://schema.org/Homeopathic.

    """
    type_: str = Field("Homeopathic", const=True, alias='@type')
    

Homeopathic.update_forward_refs()
