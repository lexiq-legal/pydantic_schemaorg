from pydantic import Field
from pydantic_schemaorg.PriceTypeEnumeration import PriceTypeEnumeration


class MSRP(PriceTypeEnumeration):
    """Represents the manufacturer suggested retail price (\"MSRP\") of an offered product.

    See https://schema.org/MSRP.

    """
    type_: str = Field("MSRP", const=True, alias='@type')
    

MSRP.update_forward_refs()
