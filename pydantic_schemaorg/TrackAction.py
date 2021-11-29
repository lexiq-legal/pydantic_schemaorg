from pydantic import Field
from pydantic_schemaorg.DeliveryMethod import DeliveryMethod
from typing import Any, Union, List, Optional
from pydantic_schemaorg.FindAction import FindAction


class TrackAction(FindAction):
    """An agent tracks an object for updates. Related actions: * [[FollowAction]]: Unlike"
     "FollowAction, TrackAction refers to the interest on the location of innanimates objects."
     "* [[SubscribeAction]]: Unlike SubscribeAction, TrackAction refers to the interest"
     "on the location of innanimate objects.

    See https://schema.org/TrackAction.

    """

    deliveryMethod: Optional[Union[List[DeliveryMethod], DeliveryMethod]] = Field(
        None,
        description="A sub property of instrument. The method of delivery.",
    )
    locals().update({"@type": Field("TrackAction", const=True)})


TrackAction.update_forward_refs()
