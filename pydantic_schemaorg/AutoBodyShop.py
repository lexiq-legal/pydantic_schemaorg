from pydantic import Field
from pydantic_schemaorg.AutomotiveBusiness import AutomotiveBusiness


class AutoBodyShop(AutomotiveBusiness):
    """Auto body shop.

    See https://schema.org/AutoBodyShop.

    """

    locals().update({"@type": Field("AutoBodyShop", const=True)})


AutoBodyShop.update_forward_refs()
