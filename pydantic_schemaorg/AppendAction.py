from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.InsertAction import InsertAction


class AppendAction(InsertAction):
    """The act of inserting at the end if an ordered collection.

    See: https://schema.org/AppendAction
    Model depth: 6
    """

    type_: str = Field("AppendAction", const=True, alias="@type")


if TYPE_CHECKING:

    AppendAction.update_forward_refs()
