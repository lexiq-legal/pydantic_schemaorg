from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.MoveAction import MoveAction


class TravelAction(MoveAction):
    """The act of traveling from an fromLocation to a destination by a specified mode of transport,"
     "optionally with participants.

    See https://schema.org/TravelAction.

    """

    distance: Any = Field(
        None,
        description="The distance travelled, e.g. exercising or travelling.",
    )
    locals().update({"@type": Field("TravelAction", const=True)})


TravelAction.update_forward_refs()
