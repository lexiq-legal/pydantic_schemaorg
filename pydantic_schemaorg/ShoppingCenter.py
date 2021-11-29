from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class ShoppingCenter(LocalBusiness):
    """A shopping center or mall.

    See https://schema.org/ShoppingCenter.

    """

    locals().update({"@type": Field("ShoppingCenter", const=True)})


ShoppingCenter.update_forward_refs()
