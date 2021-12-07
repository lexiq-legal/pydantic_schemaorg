from pydantic import Field
from pydantic_schemaorg.PriceTypeEnumeration import PriceTypeEnumeration


class SRP(PriceTypeEnumeration):
    """Represents the suggested retail price (\"SRP\") of an offered product.

    See https://schema.org/SRP.

    """
    type_: str = Field("SRP", const=True, alias='@type')
    

SRP.update_forward_refs()
