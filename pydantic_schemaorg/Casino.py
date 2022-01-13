from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.EntertainmentBusiness import EntertainmentBusiness


class Casino(EntertainmentBusiness):
    """A casino.

    See: https://schema.org/Casino
    Model depth: 5
    """

    type_: str = Field("Casino", const=True, alias="@type")


if TYPE_CHECKING:

    Casino.update_forward_refs()
