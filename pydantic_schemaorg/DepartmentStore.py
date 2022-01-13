from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Store import Store


class DepartmentStore(Store):
    """A department store.

    See: https://schema.org/DepartmentStore
    Model depth: 5
    """

    type_: str = Field("DepartmentStore", const=True, alias="@type")


if TYPE_CHECKING:

    DepartmentStore.update_forward_refs()
