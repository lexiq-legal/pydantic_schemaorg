from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Organization import Organization


class Consortium(Organization):
    """A Consortium is a membership [[Organization]] whose members are typically Organizations.

    See: https://schema.org/Consortium
    Model depth: 3
    """

    type_: str = Field("Consortium", const=True, alias="@type")


if TYPE_CHECKING:

    Consortium.update_forward_refs()
