from pydantic import Field
from pydantic_schemaorg.PlaceOfWorship import PlaceOfWorship


class Church(PlaceOfWorship):
    """A church.

    See https://schema.org/Church.

    """
    type_: str = Field("Church", const=True, alias='@type')
    

Church.update_forward_refs()
