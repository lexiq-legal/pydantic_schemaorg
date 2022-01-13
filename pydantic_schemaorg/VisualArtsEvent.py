from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Event import Event


class VisualArtsEvent(Event):
    """Event type: Visual arts event.

    See: https://schema.org/VisualArtsEvent
    Model depth: 3
    """

    type_: str = Field("VisualArtsEvent", const=True, alias="@type")


if TYPE_CHECKING:

    VisualArtsEvent.update_forward_refs()
