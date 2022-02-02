from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from datetime import time


from pydantic import Field
from pydantic_schemaorg.StructuredValue import StructuredValue


class InteractionCounter(StructuredValue):
    """A summary of how users have interacted with this CreativeWork. In most cases, authors"
     "will use a subtype to specify the specific type of interaction.

    See: https://schema.org/InteractionCounter
    Model depth: 4
    """
    type_: str = Field("InteractionCounter", alias='@type')
    userInteractionCount: Optional[Union[List[Union[int, 'Integer', str]], int, 'Integer', str]] = Field(
        None,
        description="The number of interactions for the CreativeWork using the WebSite or SoftwareApplication.",
    )
    interactionType: Optional[Union[List[Union['Action', str]], 'Action', str]] = Field(
        None,
        description="The Action representing the type of interaction. For up votes, +1s, etc. use [[LikeAction]]."
     "For down votes use [[DislikeAction]]. Otherwise, use the most specific Action.",
    )
    location: Optional[Union[List[Union[str, 'Text', 'PostalAddress', 'Place', 'VirtualLocation']], str, 'Text', 'PostalAddress', 'Place', 'VirtualLocation']] = Field(
        None,
        description="The location of, for example, where an event is happening, where an organization is located,"
     "or where an action takes place.",
    )
    endTime: Optional[Union[List[Union[ISO8601Date, 'DateTime', time, 'Time', str]], ISO8601Date, 'DateTime', time, 'Time', str]] = Field(
        None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation),"
     "the time that it is expected to end. For actions that span a period of time, when the action"
     "was performed. e.g. John wrote a book from January to *December*. For media, including"
     "audio and video, it's the time offset of the end of a clip within a larger file. Note that"
     "Event uses startDate/endDate instead of startTime/endTime, even when describing"
     "dates with times. This situation may be clarified in future revisions.",
    )
    interactionService: Optional[Union[List[Union['SoftwareApplication', 'WebSite', str]], 'SoftwareApplication', 'WebSite', str]] = Field(
        None,
        description="The WebSite or SoftwareApplication where the interactions took place.",
    )
    startTime: Optional[Union[List[Union[ISO8601Date, 'DateTime', time, 'Time', str]], ISO8601Date, 'DateTime', time, 'Time', str]] = Field(
        None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation),"
     "the time that it is expected to start. For actions that span a period of time, when the action"
     "was performed. e.g. John wrote a book from *January* to December. For media, including"
     "audio and video, it's the time offset of the start of a clip within a larger file. Note that"
     "Event uses startDate/endDate instead of startTime/endTime, even when describing"
     "dates with times. This situation may be clarified in future revisions.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Integer import Integer
    from pydantic_schemaorg.Action import Action
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.PostalAddress import PostalAddress
    from pydantic_schemaorg.Place import Place
    from pydantic_schemaorg.VirtualLocation import VirtualLocation
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Time import Time
    from pydantic_schemaorg.SoftwareApplication import SoftwareApplication
    from pydantic_schemaorg.WebSite import WebSite
