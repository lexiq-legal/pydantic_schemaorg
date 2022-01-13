from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional, Any

from pydantic_schemaorg.Event import Event


class DeliveryEvent(Event):
    """An event involving the delivery of an item.

    See: https://schema.org/DeliveryEvent
    Model depth: 3
    """

    type_: str = Field("DeliveryEvent", const=True, alias="@type")
    accessCode: "Optional[Union[List[str], str]]" = Field(
        None,
        description="Password, PIN, or access code needed for delivery (e.g. from a locker).",
    )
    availableThrough: "Optional[Union[List[Union[datetime, str]], Union[datetime, str]]]" = Field(
        None,
        description="After this date, the item will no longer be available for pickup.",
    )
    hasDeliveryMethod: "Optional[Union[List[Union[DeliveryMethod, str]], Union[DeliveryMethod, str]]]" = Field(
        None,
        description="Method used for delivery or shipping.",
    )
    availableFrom: "Optional[Union[List[Union[datetime, str]], Union[datetime, str]]]" = Field(
        None,
        description="When the item is available for pickup from the store, locker, etc.",
    )


if TYPE_CHECKING:

    from datetime import datetime

    from pydantic_schemaorg.DeliveryMethod import DeliveryMethod

    DeliveryEvent.update_forward_refs()
