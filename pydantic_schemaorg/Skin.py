from pydantic import Field
from pydantic_schemaorg.PhysicalExam import PhysicalExam


class Skin(PhysicalExam):
    """Skin assessment with clinical examination.

    See https://schema.org/Skin.

    """

    locals().update({"@type": Field("Skin", const=True)})


Skin.update_forward_refs()
