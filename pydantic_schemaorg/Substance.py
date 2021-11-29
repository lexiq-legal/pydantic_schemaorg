from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.MedicalEntity import MedicalEntity


class Substance(MedicalEntity):
    """Any matter of defined composition that has discrete existence, whose origin may be biological,"
     "mineral or chemical.

    See https://schema.org/Substance.

    """

    activeIngredient: Optional[Union[List[str], str]] = Field(
        None,
        description="An active ingredient, typically chemical compounds and/or biologic substances.",
    )
    maximumIntake: Any = Field(
        None,
        description="Recommended intake of this supplement for a given population as defined by a specific"
     "recommending authority.",
    )
    locals().update({"@type": Field("Substance", const=True)})


Substance.update_forward_refs()
