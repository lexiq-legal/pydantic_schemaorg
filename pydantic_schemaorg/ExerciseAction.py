from pydantic import Field
from pydantic_schemaorg.ExercisePlan import ExercisePlan
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Person import Person
from pydantic_schemaorg.Place import Place
from pydantic_schemaorg.SportsActivityLocation import SportsActivityLocation
from pydantic_schemaorg.PlayAction import PlayAction


class ExerciseAction(PlayAction):
    """The act of participating in exertive activity for the purposes of improving health and"
     "fitness.

    See https://schema.org/ExerciseAction.

    """

    exercisePlan: Optional[Union[List[ExercisePlan], ExercisePlan]] = Field(
        None,
        description="A sub property of instrument. The exercise plan used on this action.",
    )
    distance: Any = Field(
        None,
        description="The distance travelled, e.g. exercising or travelling.",
    )
    diet: Any = Field(
        None,
        description="A sub property of instrument. The diet used in this action.",
    )
    opponent: Optional[Union[List[Person], Person]] = Field(
        None,
        description="A sub property of participant. The opponent on this action.",
    )
    fromLocation: Optional[Union[List[Place], Place]] = Field(
        None,
        description="A sub property of location. The original location of the object or the agent before the"
     "action.",
    )
    sportsActivityLocation: Optional[Union[List[SportsActivityLocation], SportsActivityLocation]] = Field(
        None,
        description="A sub property of location. The sports activity location where this action occurred.",
    )
    exerciseRelatedDiet: Any = Field(
        None,
        description="A sub property of instrument. The diet used in this action.",
    )
    exerciseType: Optional[Union[List[str], str]] = Field(
        None,
        description="Type(s) of exercise or activity, such as strength training, flexibility training,"
     "aerobics, cardiac rehabilitation, etc.",
    )
    toLocation: Optional[Union[List[Place], Place]] = Field(
        None,
        description="A sub property of location. The final location of the object or the agent after the action.",
    )
    sportsEvent: Any = Field(
        None,
        description="A sub property of location. The sports event where this action occurred.",
    )
    course: Optional[Union[List[Place], Place]] = Field(
        None,
        description="A sub property of location. The course where this action was taken.",
    )
    exerciseCourse: Optional[Union[List[Place], Place]] = Field(
        None,
        description="A sub property of location. The course where this action was taken.",
    )
    sportsTeam: Any = Field(
        None,
        description="A sub property of participant. The sports team that participated on this action.",
    )
    locals().update({"@type": Field("ExerciseAction", const=True)})


ExerciseAction.update_forward_refs()
