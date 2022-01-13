from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.DayOfWeek import DayOfWeek


class Monday(DayOfWeek):
    """The day of the week between Sunday and Tuesday.

    See: https://schema.org/Monday
    Model depth: 5
    """

    type_: str = Field("Monday", const=True, alias="@type")


if TYPE_CHECKING:

    Monday.update_forward_refs()
