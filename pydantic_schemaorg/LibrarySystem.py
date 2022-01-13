from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Organization import Organization


class LibrarySystem(Organization):
    """A [[LibrarySystem]] is a collaborative system amongst several libraries.

    See: https://schema.org/LibrarySystem
    Model depth: 3
    """

    type_: str = Field("LibrarySystem", const=True, alias="@type")


if TYPE_CHECKING:

    LibrarySystem.update_forward_refs()
