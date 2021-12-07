from pydantic import Field
from pydantic_schemaorg.PhysicalExam import PhysicalExam


class Abdomen(PhysicalExam):
    """Abdomen clinical examination.

    See https://schema.org/Abdomen.

    """
    type_: str = Field("Abdomen", const=True, alias='@type')
    

Abdomen.update_forward_refs()
