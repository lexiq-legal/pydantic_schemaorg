from pydantic import Field
from pydantic_schemaorg.PhysicalExam import PhysicalExam


class Neuro(PhysicalExam):
    """Neurological system clinical examination.

    See https://schema.org/Neuro.

    """

    locals().update({"@type": Field("Neuro", const=True)})


Neuro.update_forward_refs()
