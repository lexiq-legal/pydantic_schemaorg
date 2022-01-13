from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.DayOfWeek import DayOfWeek


class Friday(DayOfWeek):
    """The day of the week between Thursday and Saturday.

    See: https://schema.org/Friday
    Model depth: 5
    """

    type_: str = Field("Friday", const=True, alias="@type")


if TYPE_CHECKING:

    Friday.update_forward_refs()
