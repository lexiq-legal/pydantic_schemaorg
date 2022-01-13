from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Place import Place


class AdministrativeArea(Place):
    """A geographical region, typically under the jurisdiction of a particular government.

    See: https://schema.org/AdministrativeArea
    Model depth: 3
    """

    type_: str = Field("AdministrativeArea", const=True, alias="@type")


if TYPE_CHECKING:

    AdministrativeArea.update_forward_refs()
