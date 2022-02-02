from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Audience import Audience


class Researcher(Audience):
    """Researchers.

    See: https://schema.org/Researcher
    Model depth: 4
    """
    type_: str = Field("Researcher", alias='@type')
    

