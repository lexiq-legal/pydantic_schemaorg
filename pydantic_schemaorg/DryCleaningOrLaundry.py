from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.LocalBusiness import LocalBusiness


class DryCleaningOrLaundry(LocalBusiness):
    """A dry-cleaning business.

    See: https://schema.org/DryCleaningOrLaundry
    Model depth: 4
    """

    type_: str = Field("DryCleaningOrLaundry", const=True, alias="@type")


if TYPE_CHECKING:

    DryCleaningOrLaundry.update_forward_refs()
