from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class Poster(CreativeWork):
    """A large, usually printed placard, bill, or announcement, often illustrated, that is"
     "posted to advertise or publicize something.

    See https://schema.org/Poster.

    """
    type_: str = Field("Poster", const=True, alias='@type')
    

Poster.update_forward_refs()
