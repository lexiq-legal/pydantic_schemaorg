from pydantic import Field
from decimal import Decimal
from typing import Any, Optional, Union, List
from pydantic_schema_org.Intangible import Intangible


class OccupationalExperienceRequirements(Intangible):
    """Indicates employment-related experience requirements, e.g. [[monthsOfExperience]].

    See https://schema.org/OccupationalExperienceRequirements.

    """

    monthsOfExperience: Optional[Union[List[Decimal], Decimal]] = Field(
        None,
        description="Indicates the minimal number of months of experience required for a position.",
    )
    locals().update({"@type": Field("OccupationalExperienceRequirements", const=True)})


OccupationalExperienceRequirements.update_forward_refs()
