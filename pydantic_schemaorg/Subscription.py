from pydantic import Field
from pydantic_schemaorg.PriceComponentTypeEnumeration import PriceComponentTypeEnumeration


class Subscription(PriceComponentTypeEnumeration):
    """Represents the subscription pricing component of the total price for an offered product.

    See https://schema.org/Subscription.

    """

    locals().update({"@type": Field("Subscription", const=True)})


Subscription.update_forward_refs()
