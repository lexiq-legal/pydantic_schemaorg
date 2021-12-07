from pydantic import Field
from pydantic_schemaorg.Episode import Episode


class RadioEpisode(Episode):
    """A radio episode which can be part of a series or season.

    See https://schema.org/RadioEpisode.

    """
    type_: str = Field("RadioEpisode", const=True, alias='@type')
    

RadioEpisode.update_forward_refs()
