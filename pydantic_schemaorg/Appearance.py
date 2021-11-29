from pydantic import Field
from pydantic_schemaorg.PhysicalExam import PhysicalExam


class Appearance(PhysicalExam):
    """Appearance assessment with clinical examination.

    See https://schema.org/Appearance.

    """

    locals().update({"@type": Field("Appearance", const=True)})


Appearance.update_forward_refs()
