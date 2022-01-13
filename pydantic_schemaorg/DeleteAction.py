from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.UpdateAction import UpdateAction


class DeleteAction(UpdateAction):
    """The act of editing a recipient by removing one of its objects.

    See: https://schema.org/DeleteAction
    Model depth: 4
    """

    type_: str = Field("DeleteAction", const=True, alias="@type")


if TYPE_CHECKING:

    DeleteAction.update_forward_refs()
