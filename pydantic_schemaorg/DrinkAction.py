from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.ConsumeAction import ConsumeAction


class DrinkAction(ConsumeAction):
    """The act of swallowing liquids.

    See: https://schema.org/DrinkAction
    Model depth: 4
    """
    type_: str = Field("DrinkAction", alias='@type')
    

