from pydantic import Field
from pydantic_schemaorg.PhysicalExam import PhysicalExam


class Genitourinary(PhysicalExam):
    """Genitourinary system function assessment with clinical examination.

    See https://schema.org/Genitourinary.

    """
    type_: str = Field("Genitourinary", const=True, alias='@type')
    

Genitourinary.update_forward_refs()
