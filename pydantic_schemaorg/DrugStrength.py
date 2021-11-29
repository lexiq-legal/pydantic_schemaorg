from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.AdministrativeArea import AdministrativeArea
from decimal import Decimal
from pydantic_schemaorg.MedicalIntangible import MedicalIntangible


class DrugStrength(MedicalIntangible):
    """A specific strength in which a medical drug is available in a specific country.

    See https://schema.org/DrugStrength.

    """

    activeIngredient: Optional[Union[List[str], str]] = Field(
        None,
        description="An active ingredient, typically chemical compounds and/or biologic substances.",
    )
    availableIn: Optional[Union[List[AdministrativeArea], AdministrativeArea]] = Field(
        None,
        description="The location in which the strength is available.",
    )
    strengthUnit: Optional[Union[List[str], str]] = Field(
        None,
        description="The units of an active ingredient's strength, e.g. mg.",
    )
    strengthValue: Optional[Union[List[Decimal], Decimal]] = Field(
        None,
        description="The value of an active ingredient's strength, e.g. 325.",
    )
    maximumIntake: Any = Field(
        None,
        description="Recommended intake of this supplement for a given population as defined by a specific"
     "recommending authority.",
    )
    locals().update({"@type": Field("DrugStrength", const=True)})


DrugStrength.update_forward_refs()
