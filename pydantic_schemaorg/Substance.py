from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.MedicalEntity import MedicalEntity


class Substance(MedicalEntity):
    """Any matter of defined composition that has discrete existence, whose origin may be biological,"
     "mineral or chemical.

    See: https://schema.org/Substance
    Model depth: 3
    """
    type_: str = Field("Substance", alias='@type')
    activeIngredient: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="An active ingredient, typically chemical compounds and/or biologic substances.",
    )
    maximumIntake: Optional[Union[List[Union['MaximumDoseSchedule', str]], 'MaximumDoseSchedule', str]] = Field(
        None,
        description="Recommended intake of this supplement for a given population as defined by a specific"
     "recommending authority.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.MaximumDoseSchedule import MaximumDoseSchedule
