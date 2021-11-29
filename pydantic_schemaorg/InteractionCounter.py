from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Action import Action
from pydantic_schemaorg.Place import Place
from datetime import datetime, time
from pydantic_schemaorg.SoftwareApplication import SoftwareApplication
from pydantic_schemaorg.StructuredValue import StructuredValue


class InteractionCounter(StructuredValue):
    """A summary of how users have interacted with this CreativeWork. In most cases, authors"
     "will use a subtype to specify the specific type of interaction.

    See https://schema.org/InteractionCounter.

    """

    userInteractionCount: Optional[Union[List[int], int]] = Field(
        None,
        description="The number of interactions for the CreativeWork using the WebSite or SoftwareApplication.",
    )
    interactionType: Optional[Union[List[Action], Action]] = Field(
        None,
        description="The Action representing the type of interaction. For up votes, +1s, etc. use [[LikeAction]]."
     "For down votes use [[DislikeAction]]. Otherwise, use the most specific Action.",
    )
    location: Union[List[Union[str, Place, Any]], Union[str, Place, Any]] = Field(
        None,
        description="The location of, for example, where an event is happening, where an organization is located,"
     "or where an action takes place.",
    )
    endTime: Optional[Union[List[Union[datetime, time]], Union[datetime, time]]] = Field(
        None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation),"
     "the time that it is expected to end. For actions that span a period of time, when the action"
     "was performed. e.g. John wrote a book from January to *December*. For media, including"
     "audio and video, it's the time offset of the end of a clip within a larger file. Note that"
     "Event uses startDate/endDate instead of startTime/endTime, even when describing"
     "dates with times. This situation may be clarified in future revisions.",
    )
    interactionService: Union[List[Union[SoftwareApplication, Any]], Union[SoftwareApplication, Any]] = Field(
        None,
        description="The WebSite or SoftwareApplication where the interactions took place.",
    )
    startTime: Optional[Union[List[Union[datetime, time]], Union[datetime, time]]] = Field(
        None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation),"
     "the time that it is expected to start. For actions that span a period of time, when the action"
     "was performed. e.g. John wrote a book from *January* to December. For media, including"
     "audio and video, it's the time offset of the start of a clip within a larger file. Note that"
     "Event uses startDate/endDate instead of startTime/endTime, even when describing"
     "dates with times. This situation may be clarified in future revisions.",
    )
    locals().update({"@type": Field("InteractionCounter", const=True)})


InteractionCounter.update_forward_refs()
