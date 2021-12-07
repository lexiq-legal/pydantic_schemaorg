from pydantic import Field
from pydantic_schemaorg.DeliveryMethod import DeliveryMethod


class LockerDelivery(DeliveryMethod):
    """A DeliveryMethod in which an item is made available via locker.

    See https://schema.org/LockerDelivery.

    """
    type_: str = Field("LockerDelivery", const=True, alias='@type')
    

LockerDelivery.update_forward_refs()
