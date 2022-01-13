from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.AllocateAction import AllocateAction


class AssignAction(AllocateAction):
    """The act of allocating an action/event/task to some destination (someone or something).

    See: https://schema.org/AssignAction
    Model depth: 5
    """

    type_: str = Field("AssignAction", const=True, alias="@type")


if TYPE_CHECKING:

    AssignAction.update_forward_refs()
