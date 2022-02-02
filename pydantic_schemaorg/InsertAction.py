from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, List, Optional


from pydantic import Field
from pydantic_schemaorg.AddAction import AddAction


class InsertAction(AddAction):
    """The act of adding at a specific location in an ordered collection.

    See: https://schema.org/InsertAction
    Model depth: 5
    """
    type_: str = Field("InsertAction", alias='@type')
    toLocation: Optional[Union[List[Union['Place', str]], 'Place', str]] = Field(
        None,
        description="A sub property of location. The final location of the object or the agent after the action.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Place import Place
