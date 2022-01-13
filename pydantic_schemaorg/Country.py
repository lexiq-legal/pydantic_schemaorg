from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.AdministrativeArea import AdministrativeArea


class Country(AdministrativeArea):
    """A country.

    See: https://schema.org/Country
    Model depth: 4
    """

    type_: str = Field("Country", const=True, alias="@type")


if TYPE_CHECKING:

    Country.update_forward_refs()
