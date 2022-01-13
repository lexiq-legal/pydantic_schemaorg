from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.UpdateAction import UpdateAction


class AddAction(UpdateAction):
    """The act of editing by adding an object to a collection.

    See: https://schema.org/AddAction
    Model depth: 4
    """

    type_: str = Field("AddAction", const=True, alias="@type")


if TYPE_CHECKING:

    AddAction.update_forward_refs()
