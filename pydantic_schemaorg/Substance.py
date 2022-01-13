from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional, Any

from pydantic_schemaorg.MedicalEntity import MedicalEntity


class Substance(MedicalEntity):
    """Any matter of defined composition that has discrete existence, whose origin may be biological,"
     "mineral or chemical.

    See: https://schema.org/Substance
    Model depth: 3
    """

    type_: str = Field("Substance", const=True, alias="@type")
    activeIngredient: "Optional[Union[List[str], str]]" = Field(
        None,
        description="An active ingredient, typically chemical compounds and/or biologic substances.",
    )
    maximumIntake: "Optional[Union[List[Union[MaximumDoseSchedule, str]], Union[MaximumDoseSchedule, str]]]" = Field(
        None,
        description="Recommended intake of this supplement for a given population as defined by a specific"
        "recommending authority.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.MaximumDoseSchedule import MaximumDoseSchedule

    Substance.update_forward_refs()
