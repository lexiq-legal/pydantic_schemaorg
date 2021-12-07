from pydantic import Field
from pydantic_schemaorg.PhysicalExam import PhysicalExam


class Nose(PhysicalExam):
    """Nose function assessment with clinical examination.

    See https://schema.org/Nose.

    """
    type_: str = Field("Nose", const=True, alias='@type')
    

Nose.update_forward_refs()
