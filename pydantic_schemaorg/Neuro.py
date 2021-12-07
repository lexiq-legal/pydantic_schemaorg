from pydantic import Field
from pydantic_schemaorg.PhysicalExam import PhysicalExam


class Neuro(PhysicalExam):
    """Neurological system clinical examination.

    See https://schema.org/Neuro.

    """
    type_: str = Field("Neuro", const=True, alias='@type')
    

Neuro.update_forward_refs()
