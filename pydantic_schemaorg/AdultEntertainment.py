from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.EntertainmentBusiness import EntertainmentBusiness


class AdultEntertainment(EntertainmentBusiness):
    """An adult entertainment establishment.

    See: https://schema.org/AdultEntertainment
    Model depth: 5
    """

    type_: str = Field("AdultEntertainment", const=True, alias="@type")


if TYPE_CHECKING:

    AdultEntertainment.update_forward_refs()
