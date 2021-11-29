from pydantic import Field
from pydantic_schema_org.Store import Store


class ComputerStore(Store):
    """A computer store.

    See https://schema.org/ComputerStore.

    """

    locals().update({"@type": Field("ComputerStore", const=True)})


ComputerStore.update_forward_refs()
