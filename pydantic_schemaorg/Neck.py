from pydantic import Field
from pydantic_schemaorg.PhysicalExam import PhysicalExam


class Neck(PhysicalExam):
    """Neck assessment with clinical examination.

    See https://schema.org/Neck.

    """
    type_: str = Field("Neck", const=True, alias='@type')
    

Neck.update_forward_refs()
