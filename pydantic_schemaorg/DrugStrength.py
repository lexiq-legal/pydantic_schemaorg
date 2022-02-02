from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List
from decimal import Decimal


from pydantic import Field
from pydantic_schemaorg.MedicalIntangible import MedicalIntangible


class DrugStrength(MedicalIntangible):
    """A specific strength in which a medical drug is available in a specific country.

    See: https://schema.org/DrugStrength
    Model depth: 4
    """
    type_: str = Field("DrugStrength", alias='@type')
    activeIngredient: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="An active ingredient, typically chemical compounds and/or biologic substances.",
    )
    availableIn: Optional[Union[List[Union['AdministrativeArea', str]], 'AdministrativeArea', str]] = Field(
        None,
        description="The location in which the strength is available.",
    )
    strengthUnit: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The units of an active ingredient's strength, e.g. mg.",
    )
    strengthValue: Optional[Union[List[Union[Decimal, 'Number', str]], Decimal, 'Number', str]] = Field(
        None,
        description="The value of an active ingredient's strength, e.g. 325.",
    )
    maximumIntake: Optional[Union[List[Union['MaximumDoseSchedule', str]], 'MaximumDoseSchedule', str]] = Field(
        None,
        description="Recommended intake of this supplement for a given population as defined by a specific"
     "recommending authority.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.AdministrativeArea import AdministrativeArea
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.MaximumDoseSchedule import MaximumDoseSchedule
