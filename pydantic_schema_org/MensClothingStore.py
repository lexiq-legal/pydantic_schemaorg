from pydantic import Field
from pydantic_schema_org.Store import Store


class MensClothingStore(Store):
    """A men's clothing store.

    See https://schema.org/MensClothingStore.

    """

    locals().update({"@type": Field("MensClothingStore", const=True)})


MensClothingStore.update_forward_refs()
