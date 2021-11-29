from pydantic import Field
from pydantic_schema_org.SportsActivityLocation import SportsActivityLocation


class GolfCourse(SportsActivityLocation):
    """A golf course.

    See https://schema.org/GolfCourse.

    """

    locals().update({"@type": Field("GolfCourse", const=True)})


GolfCourse.update_forward_refs()
