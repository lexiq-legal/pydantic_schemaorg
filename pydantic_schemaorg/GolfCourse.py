from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.SportsActivityLocation import SportsActivityLocation


class GolfCourse(SportsActivityLocation):
    """A golf course.

    See: https://schema.org/GolfCourse
    Model depth: 5
    """
    type_: str = Field("GolfCourse", alias='@type')
    

