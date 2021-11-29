from pydantic import Field
from pydantic_schema_org.PhysicalExam import PhysicalExam


class Ear(PhysicalExam):
    """Ear function assessment with clinical examination.

    See https://schema.org/Ear.

    """

    locals().update({"@type": Field("Ear", const=True)})


Ear.update_forward_refs()
