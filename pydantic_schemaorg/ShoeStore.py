from pydantic import Field
from pydantic_schemaorg.Store import Store


class ShoeStore(Store):
    """A shoe store.

    See https://schema.org/ShoeStore.

    """

    locals().update({"@type": Field("ShoeStore", const=True)})


ShoeStore.update_forward_refs()
