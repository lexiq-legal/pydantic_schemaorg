from pydantic import Field
from typing import List, Optional, Union
from pydantic_schemaorg.MaximumDoseSchedule import MaximumDoseSchedule
from pydantic_schemaorg.MedicalEntity import MedicalEntity


class Substance(MedicalEntity):
    """Any matter of defined composition that has discrete existence, whose origin may be biological,"
     "mineral or chemical.

    See https://schema.org/Substance.

    """
    type_: str = Field("Substance", const=True, alias='@type')
    activeIngredient: Optional[Union[List[str], str]] = Field(
        None,
        description="An active ingredient, typically chemical compounds and/or biologic substances.",
    )
    maximumIntake: Optional[Union[List[Union[MaximumDoseSchedule, str]], Union[MaximumDoseSchedule, str]]] = Field(
        None,
        description="Recommended intake of this supplement for a given population as defined by a specific"
     "recommending authority.",
    )
    

Substance.update_forward_refs()
