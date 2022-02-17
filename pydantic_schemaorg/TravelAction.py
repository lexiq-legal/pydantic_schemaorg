from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.MoveAction import MoveAction


class TravelAction(MoveAction):
    """The act of traveling from an fromLocation to a destination by a specified mode of transport,"
     "optionally with participants.

    See: https://schema.org/TravelAction
    Model depth: 4
    """
    type_: str = Field(default="TravelAction", alias='@type')
    distance: Optional[Union[List[Union['Distance', str]], 'Distance', str]] = Field(
        default=None,
        description="The distance travelled, e.g. exercising or travelling.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Distance import Distance
