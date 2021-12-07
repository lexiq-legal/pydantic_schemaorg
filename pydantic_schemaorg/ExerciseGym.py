from pydantic import Field
from pydantic_schemaorg.SportsActivityLocation import SportsActivityLocation


class ExerciseGym(SportsActivityLocation):
    """A gym.

    See https://schema.org/ExerciseGym.

    """
    type_: str = Field("ExerciseGym", const=True, alias='@type')
    

ExerciseGym.update_forward_refs()
