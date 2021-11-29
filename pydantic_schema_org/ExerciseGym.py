from pydantic import Field
from pydantic_schema_org.SportsActivityLocation import SportsActivityLocation


class ExerciseGym(SportsActivityLocation):
    """A gym.

    See https://schema.org/ExerciseGym.

    """

    locals().update({"@type": Field("ExerciseGym", const=True)})


ExerciseGym.update_forward_refs()
