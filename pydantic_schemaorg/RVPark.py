from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class RVPark(CivicStructure):
    """A place offering space for \"Recreational Vehicles\", Caravans, mobile homes and the"
     "like.

    See https://schema.org/RVPark.

    """

    locals().update({"@type": Field("RVPark", const=True)})


RVPark.update_forward_refs()
