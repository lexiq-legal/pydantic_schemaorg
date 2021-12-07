from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class Play(CreativeWork):
    """A play is a form of literature, usually consisting of dialogue between characters, intended"
     "for theatrical performance rather than just reading. Note: A performance of a Play would"
     "be a [[TheaterEvent]] or [[BroadcastEvent]] - the *Play* being the [[workPerformed]].

    See https://schema.org/Play.

    """
    type_: str = Field("Play", const=True, alias='@type')
    

Play.update_forward_refs()
