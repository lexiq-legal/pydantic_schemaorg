from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.MoveAction import MoveAction


class TravelAction(MoveAction):
    """The act of traveling from an fromLocation to a destination by a specified mode of transport,"
     "optionally with participants.

    See: https://schema.org/TravelAction
    Model depth: 4
    """

    type_: str = Field("TravelAction", const=True, alias="@type")
    distance: "Optional[Union[List[Union[Distance, str]], Union[Distance, str]]]" = (
        Field(
            None,
            description="The distance travelled, e.g. exercising or travelling.",
        )
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.Distance import Distance

    TravelAction.update_forward_refs()
