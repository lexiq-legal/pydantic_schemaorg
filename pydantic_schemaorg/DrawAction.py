from pydantic import Field
from pydantic_schemaorg.CreateAction import CreateAction


class DrawAction(CreateAction):
    """The act of producing a visual/graphical representation of an object, typically with"
     "a pen/pencil and paper as instruments.

    See https://schema.org/DrawAction.

    """

    locals().update({"@type": Field("DrawAction", const=True)})


DrawAction.update_forward_refs()
