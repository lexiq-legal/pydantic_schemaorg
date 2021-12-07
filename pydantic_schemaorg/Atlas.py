from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class Atlas(CreativeWork):
    """A collection or bound volume of maps, charts, plates or tables, physical or in media form"
     "illustrating any subject.

    See https://schema.org/Atlas.

    """
    type_: str = Field("Atlas", const=True, alias='@type')
    

Atlas.update_forward_refs()
