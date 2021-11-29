from pydantic import Field
from pydantic_schemaorg.Store import Store


class BikeStore(Store):
    """A bike store.

    See https://schema.org/BikeStore.

    """

    locals().update({"@type": Field("BikeStore", const=True)})


BikeStore.update_forward_refs()
