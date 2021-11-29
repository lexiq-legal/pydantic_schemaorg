from pydantic import Field
from pydantic_schemaorg.PriceTypeEnumeration import PriceTypeEnumeration


class MSRP(PriceTypeEnumeration):
    """Represents the manufacturer suggested retail price (\"MSRP\") of an offered product.

    See https://schema.org/MSRP.

    """

    locals().update({"@type": Field("MSRP", const=True)})


MSRP.update_forward_refs()
