from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.ConsumeAction import ConsumeAction


class EatAction(ConsumeAction):
    """The act of swallowing solid objects.

    See: https://schema.org/EatAction
    Model depth: 4
    """

    type_: str = Field("EatAction", const=True, alias="@type")


if TYPE_CHECKING:

    EatAction.update_forward_refs()
