from pydantic import Field
from pydantic_schemaorg.PhysicalExam import PhysicalExam


class Head(PhysicalExam):
    """Head assessment with clinical examination.

    See https://schema.org/Head.

    """

    locals().update({"@type": Field("Head", const=True)})


Head.update_forward_refs()
