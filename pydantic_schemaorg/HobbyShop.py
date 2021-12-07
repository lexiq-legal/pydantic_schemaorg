from pydantic import Field
from pydantic_schemaorg.Store import Store


class HobbyShop(Store):
    """A store that sells materials useful or necessary for various hobbies.

    See https://schema.org/HobbyShop.

    """
    type_: str = Field("HobbyShop", const=True, alias='@type')
    

HobbyShop.update_forward_refs()
