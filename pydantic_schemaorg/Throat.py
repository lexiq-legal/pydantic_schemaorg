from pydantic import Field
from pydantic_schemaorg.PhysicalExam import PhysicalExam


class Throat(PhysicalExam):
    """Throat assessment with clinical examination.

    See https://schema.org/Throat.

    """
    type_: str = Field("Throat", const=True, alias='@type')
    

Throat.update_forward_refs()
