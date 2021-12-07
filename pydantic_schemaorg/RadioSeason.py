from pydantic import Field
from pydantic_schemaorg.CreativeWorkSeason import CreativeWorkSeason


class RadioSeason(CreativeWorkSeason):
    """Season dedicated to radio broadcast and associated online delivery.

    See https://schema.org/RadioSeason.

    """
    type_: str = Field("RadioSeason", const=True, alias='@type')
    

RadioSeason.update_forward_refs()
