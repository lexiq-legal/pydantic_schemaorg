from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.CreateAction import CreateAction


class DrawAction(CreateAction):
    """The act of producing a visual/graphical representation of an object, typically with"
     "a pen/pencil and paper as instruments.

    See: https://schema.org/DrawAction
    Model depth: 4
    """
    type_: str = Field("DrawAction", alias='@type')
    

