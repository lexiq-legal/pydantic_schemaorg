from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.ConsumeAction import ConsumeAction


class ViewAction(ConsumeAction):
    """The act of consuming static visual content.

    See: https://schema.org/ViewAction
    Model depth: 4
    """

    type_: str = Field("ViewAction", const=True, alias="@type")


if TYPE_CHECKING:

    ViewAction.update_forward_refs()
