from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.AdministrativeArea import AdministrativeArea


class City(AdministrativeArea):
    """A city or town.

    See: https://schema.org/City
    Model depth: 4
    """

    type_: str = Field("City", const=True, alias="@type")


if TYPE_CHECKING:

    City.update_forward_refs()
