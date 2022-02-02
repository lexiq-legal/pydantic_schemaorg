from __future__ import annotations
from typing import TYPE_CHECKING

from decimal import Decimal
from typing import Union, List, Optional


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class OccupationalExperienceRequirements(Intangible):
    """Indicates employment-related experience requirements, e.g. [[monthsOfExperience]].

    See: https://schema.org/OccupationalExperienceRequirements
    Model depth: 3
    """
    type_: str = Field("OccupationalExperienceRequirements", alias='@type')
    monthsOfExperience: Optional[Union[List[Union[Decimal, 'Number', str]], Decimal, 'Number', str]] = Field(
        None,
        description="Indicates the minimal number of months of experience required for a position.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Number import Number
