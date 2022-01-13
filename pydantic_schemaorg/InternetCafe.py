from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.LocalBusiness import LocalBusiness


class InternetCafe(LocalBusiness):
    """An internet cafe.

    See: https://schema.org/InternetCafe
    Model depth: 4
    """

    type_: str = Field("InternetCafe", const=True, alias="@type")


if TYPE_CHECKING:

    InternetCafe.update_forward_refs()
