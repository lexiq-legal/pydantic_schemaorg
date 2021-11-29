from pydantic import Field
from pydantic_schemaorg.PhysicalExam import PhysicalExam


class Nose(PhysicalExam):
    """Nose function assessment with clinical examination.

    See https://schema.org/Nose.

    """

    locals().update({"@type": Field("Nose", const=True)})


Nose.update_forward_refs()
