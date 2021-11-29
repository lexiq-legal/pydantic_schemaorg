from pydantic import Field
from pydantic_schemaorg.PhysicalExam import PhysicalExam


class Throat(PhysicalExam):
    """Throat assessment with clinical examination.

    See https://schema.org/Throat.

    """

    locals().update({"@type": Field("Throat", const=True)})


Throat.update_forward_refs()
