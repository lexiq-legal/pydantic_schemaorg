from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.LocalBusiness import LocalBusiness


class EntertainmentBusiness(LocalBusiness):
    """A business providing entertainment.

    See: https://schema.org/EntertainmentBusiness
    Model depth: 4
    """

    type_: str = Field("EntertainmentBusiness", const=True, alias="@type")


if TYPE_CHECKING:

    EntertainmentBusiness.update_forward_refs()
