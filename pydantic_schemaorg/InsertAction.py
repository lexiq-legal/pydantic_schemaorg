from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.AddAction import AddAction


class InsertAction(AddAction):
    """The act of adding at a specific location in an ordered collection.

    See: https://schema.org/InsertAction
    Model depth: 5
    """

    type_: str = Field("InsertAction", const=True, alias="@type")
    toLocation: "Optional[Union[List[Union[Place, str]], Union[Place, str]]]" = Field(
        None,
        description="A sub property of location. The final location of the object or the agent after the action.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.Place import Place

    InsertAction.update_forward_refs()
