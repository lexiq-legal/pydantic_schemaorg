from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic import StrictInt, StrictFloat
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class OccupationalExperienceRequirements(Intangible):
    """Indicates employment-related experience requirements, e.g. [[monthsOfExperience]].

    See: https://schema.org/OccupationalExperienceRequirements
    Model depth: 3
    """
    type_: str = Field(default="OccupationalExperienceRequirements", alias='@type', const=True)
    monthsOfExperience: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', str]], StrictInt, StrictFloat, 'Number', str]] = Field(
        default=None,
        description="Indicates the minimal number of months of experience required for a position.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Number import Number
