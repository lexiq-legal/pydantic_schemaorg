from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.ReactAction import ReactAction


class WantAction(ReactAction):
    """The act of expressing a desire about the object. An agent wants an object.

    See: https://schema.org/WantAction
    Model depth: 5
    """

    type_: str = Field("WantAction", const=True, alias="@type")


if TYPE_CHECKING:

    WantAction.update_forward_refs()
