from pydantic import Field
from pydantic_schemaorg.PhysicalExam import PhysicalExam


class Ear(PhysicalExam):
    """Ear function assessment with clinical examination.

    See https://schema.org/Ear.

    """
    type_: str = Field("Ear", const=True, alias='@type')
    

Ear.update_forward_refs()
