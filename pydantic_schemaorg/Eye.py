from pydantic import Field
from pydantic_schemaorg.PhysicalExam import PhysicalExam


class Eye(PhysicalExam):
    """Eye or ophtalmological function assessment with clinical examination.

    See https://schema.org/Eye.

    """
    type_: str = Field("Eye", const=True, alias='@type')
    

Eye.update_forward_refs()
