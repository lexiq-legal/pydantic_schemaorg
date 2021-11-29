from pydantic import Field
from pydantic_schema_org.CreateAction import CreateAction


class PaintAction(CreateAction):
    """The act of producing a painting, typically with paint and canvas as instruments.

    See https://schema.org/PaintAction.

    """

    locals().update({"@type": Field("PaintAction", const=True)})


PaintAction.update_forward_refs()
