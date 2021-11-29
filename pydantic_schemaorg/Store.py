from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class Store(LocalBusiness):
    """A retail good store.

    See https://schema.org/Store.

    """

    locals().update({"@type": Field("Store", const=True)})


Store.update_forward_refs()
