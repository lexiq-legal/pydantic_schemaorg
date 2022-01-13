from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.InsertAction import InsertAction


class PrependAction(InsertAction):
    """The act of inserting at the beginning if an ordered collection.

    See: https://schema.org/PrependAction
    Model depth: 6
    """

    type_: str = Field("PrependAction", const=True, alias="@type")


if TYPE_CHECKING:

    PrependAction.update_forward_refs()
