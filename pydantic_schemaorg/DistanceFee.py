from pydantic import Field
from pydantic_schemaorg.PriceComponentTypeEnumeration import PriceComponentTypeEnumeration


class DistanceFee(PriceComponentTypeEnumeration):
    """Represents the distance fee (e.g., price per km or mile) part of the total price for an"
     "offered product, for example a car rental.

    See https://schema.org/DistanceFee.

    """

    locals().update({"@type": Field("DistanceFee", const=True)})


DistanceFee.update_forward_refs()
