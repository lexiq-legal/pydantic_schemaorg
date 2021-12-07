from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class ShoppingCenter(LocalBusiness):
    """A shopping center or mall.

    See https://schema.org/ShoppingCenter.

    """
    type_: str = Field("ShoppingCenter", const=True, alias='@type')
    

ShoppingCenter.update_forward_refs()
