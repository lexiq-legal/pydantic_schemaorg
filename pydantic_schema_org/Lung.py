from pydantic import Field
from pydantic_schema_org.PhysicalExam import PhysicalExam


class Lung(PhysicalExam):
    """Lung and respiratory system clinical examination.

    See https://schema.org/Lung.

    """

    locals().update({"@type": Field("Lung", const=True)})


Lung.update_forward_refs()
