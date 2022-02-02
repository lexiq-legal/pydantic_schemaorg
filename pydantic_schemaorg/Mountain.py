from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Landform import Landform


class Mountain(Landform):
    """A mountain, like Mount Whitney or Mount Everest.

    See: https://schema.org/Mountain
    Model depth: 4
    """
    type_: str = Field("Mountain", alias='@type')
    

