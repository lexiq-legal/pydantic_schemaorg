from pydantic import Field
from pydantic_schemaorg.Store import Store


class ClothingStore(Store):
    """A clothing store.

    See https://schema.org/ClothingStore.

    """

    locals().update({"@type": Field("ClothingStore", const=True)})


ClothingStore.update_forward_refs()
