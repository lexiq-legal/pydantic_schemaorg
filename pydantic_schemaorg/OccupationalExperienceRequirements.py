from pydantic import Field
from decimal import Decimal
from typing import Any, Optional, Union, List
from pydantic_schemaorg.Intangible import Intangible


class OccupationalExperienceRequirements(Intangible):
    """Indicates employment-related experience requirements, e.g. [[monthsOfExperience]].

    See https://schema.org/OccupationalExperienceRequirements.

    """
    type_: str = Field("OccupationalExperienceRequirements", const=True, alias='@type')
    monthsOfExperience: Optional[Union[List[Decimal], Decimal]] = Field(
        None,
        description="Indicates the minimal number of months of experience required for a position.",
    )
    

OccupationalExperienceRequirements.update_forward_refs()
