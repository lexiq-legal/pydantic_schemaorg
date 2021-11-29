from pydantic import Field
from pydantic_schema_org.PhysicalExam import PhysicalExam


class Eye(PhysicalExam):
    """Eye or ophtalmological function assessment with clinical examination.

    See https://schema.org/Eye.

    """

    locals().update({"@type": Field("Eye", const=True)})


Eye.update_forward_refs()
