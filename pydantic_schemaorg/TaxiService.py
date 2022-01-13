from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Service import Service


class TaxiService(Service):
    """A service for a vehicle for hire with a driver for local travel. Fares are usually calculated"
     "based on distance traveled.

    See: https://schema.org/TaxiService
    Model depth: 4
    """

    type_: str = Field("TaxiService", const=True, alias="@type")


if TYPE_CHECKING:

    TaxiService.update_forward_refs()
