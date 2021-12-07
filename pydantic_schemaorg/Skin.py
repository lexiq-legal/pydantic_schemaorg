from pydantic import Field
from pydantic_schemaorg.PhysicalExam import PhysicalExam


class Skin(PhysicalExam):
    """Skin assessment with clinical examination.

    See https://schema.org/Skin.

    """
    type_: str = Field("Skin", const=True, alias='@type')
    

Skin.update_forward_refs()
