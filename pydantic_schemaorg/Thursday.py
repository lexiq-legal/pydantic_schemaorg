from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.DayOfWeek import DayOfWeek


class Thursday(DayOfWeek):
    """The day of the week between Wednesday and Friday.

    See: https://schema.org/Thursday
    Model depth: 5
    """

    type_: str = Field("Thursday", const=True, alias="@type")


if TYPE_CHECKING:

    Thursday.update_forward_refs()
