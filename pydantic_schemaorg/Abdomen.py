from pydantic import Field
from pydantic_schemaorg.PhysicalExam import PhysicalExam


class Abdomen(PhysicalExam):
    """Abdomen clinical examination.

    See https://schema.org/Abdomen.

    """

    locals().update({"@type": Field("Abdomen", const=True)})


Abdomen.update_forward_refs()
