from pydantic import Field
from pydantic_schemaorg.Store import Store


class DepartmentStore(Store):
    """A department store.

    See https://schema.org/DepartmentStore.

    """

    locals().update({"@type": Field("DepartmentStore", const=True)})


DepartmentStore.update_forward_refs()
