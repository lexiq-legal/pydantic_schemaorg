from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.FindAction import FindAction


class DiscoverAction(FindAction):
    """The act of discovering/finding an object.

    See: https://schema.org/DiscoverAction
    Model depth: 4
    """

    type_: str = Field("DiscoverAction", const=True, alias="@type")


if TYPE_CHECKING:

    DiscoverAction.update_forward_refs()
