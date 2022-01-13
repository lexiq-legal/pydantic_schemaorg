from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Action import Action


class AssessAction(Action):
    """The act of forming one's opinion, reaction or sentiment.

    See: https://schema.org/AssessAction
    Model depth: 3
    """

    type_: str = Field("AssessAction", const=True, alias="@type")


if TYPE_CHECKING:

    AssessAction.update_forward_refs()
