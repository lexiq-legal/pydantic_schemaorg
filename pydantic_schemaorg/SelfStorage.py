from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.LocalBusiness import LocalBusiness


class SelfStorage(LocalBusiness):
    """A self-storage facility.

    See: https://schema.org/SelfStorage
    Model depth: 4
    """

    type_: str = Field("SelfStorage", const=True, alias="@type")


if TYPE_CHECKING:

    SelfStorage.update_forward_refs()
