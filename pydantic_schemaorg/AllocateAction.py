from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.OrganizeAction import OrganizeAction


class AllocateAction(OrganizeAction):
    """The act of organizing tasks/objects/events by associating resources to it.

    See: https://schema.org/AllocateAction
    Model depth: 4
    """

    type_: str = Field("AllocateAction", const=True, alias="@type")


if TYPE_CHECKING:

    AllocateAction.update_forward_refs()
