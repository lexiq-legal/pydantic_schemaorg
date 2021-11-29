from pydantic import Field
from pydantic_schema_org.CivicStructure import CivicStructure


class Park(CivicStructure):
    """A park.

    See https://schema.org/Park.

    """

    locals().update({"@type": Field("Park", const=True)})


Park.update_forward_refs()
