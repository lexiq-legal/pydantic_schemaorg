from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.AssessAction import AssessAction


class IgnoreAction(AssessAction):
    """The act of intentionally disregarding the object. An agent ignores an object.

    See: https://schema.org/IgnoreAction
    Model depth: 4
    """
    type_: str = Field("IgnoreAction", alias='@type')
    

