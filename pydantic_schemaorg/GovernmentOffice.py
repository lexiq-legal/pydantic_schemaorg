from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.LocalBusiness import LocalBusiness


class GovernmentOffice(LocalBusiness):
    """A government office&#x2014;for example, an IRS or DMV office.

    See: https://schema.org/GovernmentOffice
    Model depth: 4
    """

    type_: str = Field("GovernmentOffice", const=True, alias="@type")


if TYPE_CHECKING:

    GovernmentOffice.update_forward_refs()
