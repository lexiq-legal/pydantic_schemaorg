from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.UseAction import UseAction


class WearAction(UseAction):
    """The act of dressing oneself in clothing.

    See: https://schema.org/WearAction
    Model depth: 5
    """
    type_: str = Field("WearAction", alias='@type')
    

