from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.SportsActivityLocation import SportsActivityLocation


class ExerciseGym(SportsActivityLocation):
    """A gym.

    See: https://schema.org/ExerciseGym
    Model depth: 5
    """

    type_: str = Field("ExerciseGym", const=True, alias="@type")


if TYPE_CHECKING:

    ExerciseGym.update_forward_refs()
