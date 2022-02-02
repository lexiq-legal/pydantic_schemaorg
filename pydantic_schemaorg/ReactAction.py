from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.AssessAction import AssessAction


class ReactAction(AssessAction):
    """The act of responding instinctively and emotionally to an object, expressing a sentiment.

    See: https://schema.org/ReactAction
    Model depth: 4
    """
    type_: str = Field("ReactAction", alias='@type')
    

