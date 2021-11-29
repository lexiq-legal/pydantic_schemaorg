from pydantic import Field
from pydantic_schemaorg.PhysicalExam import PhysicalExam


class Neck(PhysicalExam):
    """Neck assessment with clinical examination.

    See https://schema.org/Neck.

    """

    locals().update({"@type": Field("Neck", const=True)})


Neck.update_forward_refs()
