from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.LocalBusiness import LocalBusiness


class Library(LocalBusiness):
    """A library.

    See: https://schema.org/Library
    Model depth: 4
    """

    type_: str = Field("Library", const=True, alias="@type")


if TYPE_CHECKING:

    Library.update_forward_refs()
