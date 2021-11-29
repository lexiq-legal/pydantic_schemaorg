from pydantic import Field
from typing import Any, Union, List, Optional
from datetime import datetime
from pydantic_schemaorg.DeliveryMethod import DeliveryMethod
from pydantic_schemaorg.Event import Event


class DeliveryEvent(Event):
    """An event involving the delivery of an item.

    See https://schema.org/DeliveryEvent.

    """

    accessCode: Optional[Union[List[str], str]] = Field(
        None,
        description="Password, PIN, or access code needed for delivery (e.g. from a locker).",
    )
    availableThrough: Optional[Union[List[datetime], datetime]] = Field(
        None,
        description="After this date, the item will no longer be available for pickup.",
    )
    hasDeliveryMethod: Optional[Union[List[DeliveryMethod], DeliveryMethod]] = Field(
        None,
        description="Method used for delivery or shipping.",
    )
    availableFrom: Optional[Union[List[datetime], datetime]] = Field(
        None,
        description="When the item is available for pickup from the store, locker, etc.",
    )
    locals().update({"@type": Field("DeliveryEvent", const=True)})


DeliveryEvent.update_forward_refs()
