from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Action import Action


class AchieveAction(Action):
    """The act of accomplishing something via previous efforts. It is an instantaneous action"
     "rather than an ongoing process.

    See: https://schema.org/AchieveAction
    Model depth: 3
    """

    type_: str = Field("AchieveAction", const=True, alias="@type")


if TYPE_CHECKING:

    AchieveAction.update_forward_refs()
