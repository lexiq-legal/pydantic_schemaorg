from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.SportsActivityLocation import SportsActivityLocation


class GolfCourse(SportsActivityLocation):
    """A golf course.

    See: https://schema.org/GolfCourse
    Model depth: 5
    """

    type_: str = Field("GolfCourse", const=True, alias="@type")


if TYPE_CHECKING:

    GolfCourse.update_forward_refs()
