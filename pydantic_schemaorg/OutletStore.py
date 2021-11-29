from pydantic import Field
from pydantic_schemaorg.Store import Store


class OutletStore(Store):
    """An outlet store.

    See https://schema.org/OutletStore.

    """

    locals().update({"@type": Field("OutletStore", const=True)})


OutletStore.update_forward_refs()
