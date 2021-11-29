from pydantic import Field
from pydantic_schemaorg.Store import Store


class GardenStore(Store):
    """A garden store.

    See https://schema.org/GardenStore.

    """

    locals().update({"@type": Field("GardenStore", const=True)})


GardenStore.update_forward_refs()
