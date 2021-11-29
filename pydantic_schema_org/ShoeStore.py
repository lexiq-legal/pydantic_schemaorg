from pydantic import Field
from pydantic_schema_org.Store import Store


class ShoeStore(Store):
    """A shoe store.

    See https://schema.org/ShoeStore.

    """

    locals().update({"@type": Field("ShoeStore", const=True)})


ShoeStore.update_forward_refs()
