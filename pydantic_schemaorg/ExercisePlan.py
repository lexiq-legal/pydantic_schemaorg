from __future__ import annotations
from typing import TYPE_CHECKING

from decimal import Decimal
from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.PhysicalActivity import PhysicalActivity
from pydantic_schemaorg.CreativeWork import CreativeWork


class ExercisePlan(PhysicalActivity, CreativeWork):
    """Fitness-related activity designed for a specific health-related purpose, including"
     "defined exercise routines as well as activity prescribed by a clinician.

    See: https://schema.org/ExercisePlan
    Model depth: 3
    """
    type_: str = Field("ExercisePlan", alias='@type')
    repetitions: Optional[Union[List[Union[Decimal, 'Number', 'QuantitativeValue', str]], Decimal, 'Number', 'QuantitativeValue', str]] = Field(
        None,
        description="Number of times one should repeat the activity.",
    )
    restPeriods: Optional[Union[List[Union[str, 'Text', 'QuantitativeValue']], str, 'Text', 'QuantitativeValue']] = Field(
        None,
        description="How often one should break from the activity.",
    )
    intensity: Optional[Union[List[Union[str, 'Text', 'QuantitativeValue']], str, 'Text', 'QuantitativeValue']] = Field(
        None,
        description="Quantitative measure gauging the degree of force involved in the exercise, for example,"
     "heartbeats per minute. May include the velocity of the movement.",
    )
    workload: Optional[Union[List[Union['Energy', 'QuantitativeValue', str]], 'Energy', 'QuantitativeValue', str]] = Field(
        None,
        description="Quantitative measure of the physiologic output of the exercise; also referred to as"
     "energy expenditure.",
    )
    additionalVariable: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Any additional component of the exercise prescription that may need to be articulated"
     "to the patient. This may include the order of exercises, the number of repetitions of"
     "movement, quantitative distance, progressions over time, etc.",
    )
    exerciseType: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Type(s) of exercise or activity, such as strength training, flexibility training,"
     "aerobics, cardiac rehabilitation, etc.",
    )
    activityDuration: Optional[Union[List[Union['Duration', 'QuantitativeValue', str]], 'Duration', 'QuantitativeValue', str]] = Field(
        None,
        description="Length of time to engage in the activity.",
    )
    activityFrequency: Optional[Union[List[Union[str, 'Text', 'QuantitativeValue']], str, 'Text', 'QuantitativeValue']] = Field(
        None,
        description="How often one should engage in the activity.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Energy import Energy
    from pydantic_schemaorg.Duration import Duration
