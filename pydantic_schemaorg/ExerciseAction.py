from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.PlayAction import PlayAction


class ExerciseAction(PlayAction):
    """The act of participating in exertive activity for the purposes of improving health and"
     "fitness.

    See: https://schema.org/ExerciseAction
    Model depth: 4
    """
    type_: str = Field("ExerciseAction", alias='@type')
    exercisePlan: Optional[Union[List[Union['ExercisePlan', str]], 'ExercisePlan', str]] = Field(
        None,
        description="A sub property of instrument. The exercise plan used on this action.",
    )
    distance: Optional[Union[List[Union['Distance', str]], 'Distance', str]] = Field(
        None,
        description="The distance travelled, e.g. exercising or travelling.",
    )
    diet: Optional[Union[List[Union['Diet', str]], 'Diet', str]] = Field(
        None,
        description="A sub property of instrument. The diet used in this action.",
    )
    opponent: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        None,
        description="A sub property of participant. The opponent on this action.",
    )
    fromLocation: Optional[Union[List[Union['Place', str]], 'Place', str]] = Field(
        None,
        description="A sub property of location. The original location of the object or the agent before the"
     "action.",
    )
    sportsActivityLocation: Optional[Union[List[Union['SportsActivityLocation', str]], 'SportsActivityLocation', str]] = Field(
        None,
        description="A sub property of location. The sports activity location where this action occurred.",
    )
    exerciseRelatedDiet: Optional[Union[List[Union['Diet', str]], 'Diet', str]] = Field(
        None,
        description="A sub property of instrument. The diet used in this action.",
    )
    exerciseType: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Type(s) of exercise or activity, such as strength training, flexibility training,"
     "aerobics, cardiac rehabilitation, etc.",
    )
    toLocation: Optional[Union[List[Union['Place', str]], 'Place', str]] = Field(
        None,
        description="A sub property of location. The final location of the object or the agent after the action.",
    )
    sportsEvent: Optional[Union[List[Union['SportsEvent', str]], 'SportsEvent', str]] = Field(
        None,
        description="A sub property of location. The sports event where this action occurred.",
    )
    course: Optional[Union[List[Union['Place', str]], 'Place', str]] = Field(
        None,
        description="A sub property of location. The course where this action was taken.",
    )
    exerciseCourse: Optional[Union[List[Union['Place', str]], 'Place', str]] = Field(
        None,
        description="A sub property of location. The course where this action was taken.",
    )
    sportsTeam: Optional[Union[List[Union['SportsTeam', str]], 'SportsTeam', str]] = Field(
        None,
        description="A sub property of participant. The sports team that participated on this action.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.ExercisePlan import ExercisePlan
    from pydantic_schemaorg.Distance import Distance
    from pydantic_schemaorg.Diet import Diet
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Place import Place
    from pydantic_schemaorg.SportsActivityLocation import SportsActivityLocation
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.SportsEvent import SportsEvent
    from pydantic_schemaorg.SportsTeam import SportsTeam
