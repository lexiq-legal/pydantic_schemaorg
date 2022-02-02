from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class Poster(CreativeWork):
    """A large, usually printed placard, bill, or announcement, often illustrated, that is"
     "posted to advertise or publicize something.

    See: https://schema.org/Poster
    Model depth: 3
    """
    type_: str = Field("Poster", alias='@type')
    

