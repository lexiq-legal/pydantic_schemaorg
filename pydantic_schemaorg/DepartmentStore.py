from pydantic import Field
from pydantic_schemaorg.Store import Store


class DepartmentStore(Store):
    """A department store.

    See https://schema.org/DepartmentStore.

    """
    type_: str = Field("DepartmentStore", const=True, alias='@type')
    

DepartmentStore.update_forward_refs()
