from pydantic import Field
from decimal import Decimal
from typing import List, Optional, Union
from pydantic_schemaorg.Intangible import Intangible


class OccupationalExperienceRequirements(Intangible):
    """Indicates employment-related experience requirements, e.g. [[monthsOfExperience]].

    See https://schema.org/OccupationalExperienceRequirements.

    """
    type_: str = Field("OccupationalExperienceRequirements", const=True, alias='@type')
    monthsOfExperience: Optional[Union[List[Union[Decimal, str]], Union[Decimal, str]]] = Field(
        None,
        description="Indicates the minimal number of months of experience required for a position.",
    )
    

OccupationalExperienceRequirements.update_forward_refs()
