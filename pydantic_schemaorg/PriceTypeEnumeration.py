from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class PriceTypeEnumeration(Enumeration):
    """Enumerates different price types, for example list price, invoice price, and sale price.

    See https://schema.org/PriceTypeEnumeration.

    """

    locals().update({"@type": Field("PriceTypeEnumeration", const=True)})


PriceTypeEnumeration.update_forward_refs()
