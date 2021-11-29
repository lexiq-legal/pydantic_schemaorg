from pydantic import Field
from pydantic_schema_org.Store import Store


class HobbyShop(Store):
    """A store that sells materials useful or necessary for various hobbies.

    See https://schema.org/HobbyShop.

    """

    locals().update({"@type": Field("HobbyShop", const=True)})


HobbyShop.update_forward_refs()
