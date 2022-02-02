from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Action import Action


class AssessAction(Action):
    """The act of forming one's opinion, reaction or sentiment.

    See: https://schema.org/AssessAction
    Model depth: 3
    """
    type_: str = Field("AssessAction", alias='@type')
    

