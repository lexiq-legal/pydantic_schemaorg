from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.LocalBusiness import LocalBusiness


class EmergencyService(LocalBusiness):
    """An emergency service, such as a fire station or ER.

    See: https://schema.org/EmergencyService
    Model depth: 4
    """

    type_: str = Field("EmergencyService", const=True, alias="@type")


if TYPE_CHECKING:

    EmergencyService.update_forward_refs()
