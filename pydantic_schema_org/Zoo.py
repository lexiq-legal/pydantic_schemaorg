from pydantic import Field
from pydantic_schema_org.CivicStructure import CivicStructure


class Zoo(CivicStructure):
    """A zoo.

    See https://schema.org/Zoo.

    """

    locals().update({"@type": Field("Zoo", const=True)})


Zoo.update_forward_refs()
