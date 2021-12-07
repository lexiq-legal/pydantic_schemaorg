from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class PublicToilet(CivicStructure):
    """A public toilet is a room or small building containing one or more toilets (and possibly"
     "also urinals) which is available for use by the general public, or by customers or employees"
     "of certain businesses.

    See https://schema.org/PublicToilet.

    """
    type_: str = Field("PublicToilet", const=True, alias='@type')
    

PublicToilet.update_forward_refs()
