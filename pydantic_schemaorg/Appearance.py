from pydantic import Field
from pydantic_schemaorg.PhysicalExam import PhysicalExam


class Appearance(PhysicalExam):
    """Appearance assessment with clinical examination.

    See https://schema.org/Appearance.

    """
    type_: str = Field("Appearance", const=True, alias='@type')
    

Appearance.update_forward_refs()
