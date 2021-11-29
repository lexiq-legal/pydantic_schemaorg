from pydantic import Field
from pydantic_schema_org.Store import Store


class ElectronicsStore(Store):
    """An electronics store.

    See https://schema.org/ElectronicsStore.

    """

    locals().update({"@type": Field("ElectronicsStore", const=True)})


ElectronicsStore.update_forward_refs()
