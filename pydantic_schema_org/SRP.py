from pydantic import Field
from pydantic_schema_org.PriceTypeEnumeration import PriceTypeEnumeration


class SRP(PriceTypeEnumeration):
    """Represents the suggested retail price (\"SRP\") of an offered product.

    See https://schema.org/SRP.

    """

    locals().update({"@type": Field("SRP", const=True)})


SRP.update_forward_refs()
