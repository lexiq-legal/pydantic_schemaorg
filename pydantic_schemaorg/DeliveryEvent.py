from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date


from pydantic import Field
from pydantic_schemaorg.Event import Event


class DeliveryEvent(Event):
    """An event involving the delivery of an item.

    See: https://schema.org/DeliveryEvent
    Model depth: 3
    """
    type_: str = Field(default="DeliveryEvent", alias='@type', constant=True)
    accessCode: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Password, PIN, or access code needed for delivery (e.g. from a locker).",
    )
    availableThrough: Optional[Union[List[Union[ISO8601Date, 'DateTime', str]], ISO8601Date, 'DateTime', str]] = Field(
        default=None,
        description="After this date, the item will no longer be available for pickup.",
    )
    hasDeliveryMethod: Optional[Union[List[Union['DeliveryMethod', str]], 'DeliveryMethod', str]] = Field(
        default=None,
        description="Method used for delivery or shipping.",
    )
    availableFrom: Optional[Union[List[Union[ISO8601Date, 'DateTime', str]], ISO8601Date, 'DateTime', str]] = Field(
        default=None,
        description="When the item is available for pickup from the store, locker, etc.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.DeliveryMethod import DeliveryMethod
