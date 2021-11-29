from pydantic import Field
from pydantic_schemaorg.Store import Store


class LiquorStore(Store):
    """A shop that sells alcoholic drinks such as wine, beer, whisky and other spirits.

    See https://schema.org/LiquorStore.

    """

    locals().update({"@type": Field("LiquorStore", const=True)})


LiquorStore.update_forward_refs()
