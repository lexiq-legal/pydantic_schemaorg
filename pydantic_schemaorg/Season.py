from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class Season(CreativeWork):
    """A media season e.g. tv, radio, video game etc.

    See https://schema.org/Season.

    """
    type_: str = Field("Season", const=True, alias='@type')
    

Season.update_forward_refs()
