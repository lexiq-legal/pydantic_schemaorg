from pydantic import Field
from pydantic_schemaorg.Distance import Distance
from typing import List, Optional, Union
from pydantic_schemaorg.MoveAction import MoveAction


class TravelAction(MoveAction):
    """The act of traveling from an fromLocation to a destination by a specified mode of transport,"
     "optionally with participants.

    See https://schema.org/TravelAction.

    """
    type_: str = Field("TravelAction", const=True, alias='@type')
    distance: Optional[Union[List[Union[Distance, str]], Union[Distance, str]]] = Field(
        None,
        description="The distance travelled, e.g. exercising or travelling.",
    )
    

TravelAction.update_forward_refs()
