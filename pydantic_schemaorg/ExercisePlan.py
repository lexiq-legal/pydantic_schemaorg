from pydantic import Field
from decimal import Decimal
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Energy import Energy
from pydantic_schemaorg.CreativeWork import CreativeWork
from pydantic_schemaorg.PhysicalActivity import PhysicalActivity


class ExercisePlan(CreativeWork, PhysicalActivity):
    """Fitness-related activity designed for a specific health-related purpose, including"
     "defined exercise routines as well as activity prescribed by a clinician.

    See https://schema.org/ExercisePlan.

    """

    repetitions: Union[List[Union[Decimal, Any]], Union[Decimal, Any]] = Field(
        None,
        description="Number of times one should repeat the activity.",
    )
    restPeriods: Union[List[Union[str, Any]], Union[str, Any]] = Field(
        None,
        description="How often one should break from the activity.",
    )
    intensity: Union[List[Union[str, Any]], Union[str, Any]] = Field(
        None,
        description="Quantitative measure gauging the degree of force involved in the exercise, for example,"
     "heartbeats per minute. May include the velocity of the movement.",
    )
    workload: Union[List[Union[Energy, Any]], Union[Energy, Any]] = Field(
        None,
        description="Quantitative measure of the physiologic output of the exercise; also referred to as"
     "energy expenditure.",
    )
    additionalVariable: Optional[Union[List[str], str]] = Field(
        None,
        description="Any additional component of the exercise prescription that may need to be articulated"
     "to the patient. This may include the order of exercises, the number of repetitions of"
     "movement, quantitative distance, progressions over time, etc.",
    )
    exerciseType: Optional[Union[List[str], str]] = Field(
        None,
        description="Type(s) of exercise or activity, such as strength training, flexibility training,"
     "aerobics, cardiac rehabilitation, etc.",
    )
    activityDuration: Any = Field(
        None,
        description="Length of time to engage in the activity.",
    )
    activityFrequency: Union[List[Union[str, Any]], Union[str, Any]] = Field(
        None,
        description="How often one should engage in the activity.",
    )
    locals().update({"@type": Field("ExercisePlan", const=True)})


ExercisePlan.update_forward_refs()
