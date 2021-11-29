from pydantic import Field
from pydantic_schemaorg.Store import Store


class WholesaleStore(Store):
    """A wholesale store.

    See https://schema.org/WholesaleStore.

    """

    locals().update({"@type": Field("WholesaleStore", const=True)})


WholesaleStore.update_forward_refs()
