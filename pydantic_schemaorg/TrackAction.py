from pydantic import Field
from pydantic_schemaorg.DeliveryMethod import DeliveryMethod
from typing import List, Optional, Union
from pydantic_schemaorg.FindAction import FindAction


class TrackAction(FindAction):
    """An agent tracks an object for updates. Related actions: * [[FollowAction]]: Unlike"
     "FollowAction, TrackAction refers to the interest on the location of innanimates objects."
     "* [[SubscribeAction]]: Unlike SubscribeAction, TrackAction refers to the interest"
     "on the location of innanimate objects.

    See https://schema.org/TrackAction.

    """
    type_: str = Field("TrackAction", const=True, alias='@type')
    deliveryMethod: Optional[Union[List[Union[DeliveryMethod, str]], Union[DeliveryMethod, str]]] = Field(
        None,
        description="A sub property of instrument. The method of delivery.",
    )
    

TrackAction.update_forward_refs()
