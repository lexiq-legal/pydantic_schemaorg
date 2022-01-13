from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.Intangible import Intangible


class OccupationalExperienceRequirements(Intangible):
    """Indicates employment-related experience requirements, e.g. [[monthsOfExperience]].

    See: https://schema.org/OccupationalExperienceRequirements
    Model depth: 3
    """

    type_: str = Field("OccupationalExperienceRequirements", const=True, alias="@type")
    monthsOfExperience: "Optional[Union[List[Union[Decimal, str]], Union[Decimal, str]]]" = Field(
        None,
        description="Indicates the minimal number of months of experience required for a position.",
    )


if TYPE_CHECKING:

    from decimal import Decimal

    OccupationalExperienceRequirements.update_forward_refs()
