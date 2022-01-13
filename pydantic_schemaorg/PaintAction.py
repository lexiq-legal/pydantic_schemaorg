from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.CreateAction import CreateAction


class PaintAction(CreateAction):
    """The act of producing a painting, typically with paint and canvas as instruments.

    See: https://schema.org/PaintAction
    Model depth: 4
    """

    type_: str = Field("PaintAction", const=True, alias="@type")


if TYPE_CHECKING:

    PaintAction.update_forward_refs()
