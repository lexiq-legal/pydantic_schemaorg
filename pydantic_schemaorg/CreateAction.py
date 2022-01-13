from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Action import Action


class CreateAction(Action):
    """The act of deliberately creating/producing/generating/building a result out of the"
     "agent.

    See: https://schema.org/CreateAction
    Model depth: 3
    """

    type_: str = Field("CreateAction", const=True, alias="@type")


if TYPE_CHECKING:

    CreateAction.update_forward_refs()
