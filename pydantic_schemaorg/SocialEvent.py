from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Event import Event


class SocialEvent(Event):
    """Event type: Social event.

    See: https://schema.org/SocialEvent
    Model depth: 3
    """

    type_: str = Field("SocialEvent", const=True, alias="@type")


if TYPE_CHECKING:

    SocialEvent.update_forward_refs()
