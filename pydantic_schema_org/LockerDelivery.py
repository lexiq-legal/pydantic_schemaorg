from pydantic import Field
from pydantic_schema_org.DeliveryMethod import DeliveryMethod


class LockerDelivery(DeliveryMethod):
    """A DeliveryMethod in which an item is made available via locker.

    See https://schema.org/LockerDelivery.

    """

    locals().update({"@type": Field("LockerDelivery", const=True)})


LockerDelivery.update_forward_refs()
