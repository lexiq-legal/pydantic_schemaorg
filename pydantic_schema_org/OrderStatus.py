from pydantic import Field
from pydantic_schema_org.StatusEnumeration import StatusEnumeration


class OrderStatus(StatusEnumeration):
    """Enumerated status values for Order.

    See https://schema.org/OrderStatus.

    """

    locals().update({"@type": Field("OrderStatus", const=True)})


OrderStatus.update_forward_refs()
