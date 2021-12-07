from pydantic import Field
from pydantic_schemaorg.SportsActivityLocation import SportsActivityLocation


class GolfCourse(SportsActivityLocation):
    """A golf course.

    See https://schema.org/GolfCourse.

    """
    type_: str = Field("GolfCourse", const=True, alias='@type')
    

GolfCourse.update_forward_refs()
