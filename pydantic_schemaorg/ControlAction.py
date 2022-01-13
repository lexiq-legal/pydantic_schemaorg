from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Action import Action


class ControlAction(Action):
    """An agent controls a device or application.

    See: https://schema.org/ControlAction
    Model depth: 3
    """

    type_: str = Field("ControlAction", const=True, alias="@type")


if TYPE_CHECKING:

    ControlAction.update_forward_refs()
