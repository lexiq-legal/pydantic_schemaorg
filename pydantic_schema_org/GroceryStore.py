from pydantic import Field
from pydantic_schema_org.Store import Store


class GroceryStore(Store):
    """A grocery store.

    See https://schema.org/GroceryStore.

    """

    locals().update({"@type": Field("GroceryStore", const=True)})


GroceryStore.update_forward_refs()
