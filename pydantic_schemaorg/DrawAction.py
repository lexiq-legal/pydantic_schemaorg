from pydantic import Field
from pydantic_schemaorg.CreateAction import CreateAction


class DrawAction(CreateAction):
    """The act of producing a visual/graphical representation of an object, typically with"
     "a pen/pencil and paper as instruments.

    See https://schema.org/DrawAction.

    """
    type_: str = Field("DrawAction", const=True, alias='@type')
    

DrawAction.update_forward_refs()
