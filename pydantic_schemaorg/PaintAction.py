from pydantic import Field
from pydantic_schemaorg.CreateAction import CreateAction


class PaintAction(CreateAction):
    """The act of producing a painting, typically with paint and canvas as instruments.

    See https://schema.org/PaintAction.

    """
    type_: str = Field("PaintAction", const=True, alias='@type')
    

PaintAction.update_forward_refs()
