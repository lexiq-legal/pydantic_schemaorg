from pydantic import Field
from pydantic_schemaorg.PhysicalExam import PhysicalExam


class Genitourinary(PhysicalExam):
    """Genitourinary system function assessment with clinical examination.

    See https://schema.org/Genitourinary.

    """

    locals().update({"@type": Field("Genitourinary", const=True)})


Genitourinary.update_forward_refs()
