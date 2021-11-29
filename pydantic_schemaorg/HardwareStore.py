from pydantic import Field
from pydantic_schemaorg.Store import Store


class HardwareStore(Store):
    """A hardware store.

    See https://schema.org/HardwareStore.

    """

    locals().update({"@type": Field("HardwareStore", const=True)})


HardwareStore.update_forward_refs()
