from pydantic import Field
from pydantic_schemaorg.PhysicalExam import PhysicalExam


class Head(PhysicalExam):
    """Head assessment with clinical examination.

    See https://schema.org/Head.

    """
    type_: str = Field("Head", const=True, alias='@type')
    

Head.update_forward_refs()
