from pydantic import Field
from pydantic_schemaorg.PriceComponentTypeEnumeration import PriceComponentTypeEnumeration


class ActivationFee(PriceComponentTypeEnumeration):
    """Represents the activation fee part of the total price for an offered product, for example"
     "a cellphone contract.

    See https://schema.org/ActivationFee.

    """

    locals().update({"@type": Field("ActivationFee", const=True)})


ActivationFee.update_forward_refs()
