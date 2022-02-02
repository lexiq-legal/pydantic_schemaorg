from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.SportsActivityLocation import SportsActivityLocation


class ExerciseGym(SportsActivityLocation):
    """A gym.

    See: https://schema.org/ExerciseGym
    Model depth: 5
    """
    type_: str = Field("ExerciseGym", alias='@type')
    

