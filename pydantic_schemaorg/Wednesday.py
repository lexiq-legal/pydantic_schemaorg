from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.DayOfWeek import DayOfWeek


class Wednesday(DayOfWeek):
    """The day of the week between Tuesday and Thursday.

    See: https://schema.org/Wednesday
    Model depth: 5
    """

    type_: str = Field("Wednesday", const=True, alias="@type")


if TYPE_CHECKING:

    Wednesday.update_forward_refs()
