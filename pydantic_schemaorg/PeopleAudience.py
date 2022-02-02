from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List
from decimal import Decimal


from pydantic import Field
from pydantic_schemaorg.Audience import Audience


class PeopleAudience(Audience):
    """A set of characteristics belonging to people, e.g. who compose an item's target audience.

    See: https://schema.org/PeopleAudience
    Model depth: 4
    """
    type_: str = Field("PeopleAudience", alias='@type')
    suggestedGender: Optional[Union[List[Union[str, 'Text', 'GenderType']], str, 'Text', 'GenderType']] = Field(
        None,
        description="The suggested gender of the intended person or audience, for example \"male\", \"female\","
     "or \"unisex\".",
    )
    requiredMaxAge: Optional[Union[List[Union[int, 'Integer', str]], int, 'Integer', str]] = Field(
        None,
        description="Audiences defined by a person's maximum age.",
    )
    suggestedAge: Optional[Union[List[Union['QuantitativeValue', str]], 'QuantitativeValue', str]] = Field(
        None,
        description="The age or age range for the intended audience or person, for example 3-12 months for infants,"
     "1-5 years for toddlers.",
    )
    suggestedMaxAge: Optional[Union[List[Union[Decimal, 'Number', str]], Decimal, 'Number', str]] = Field(
        None,
        description="Maximum recommended age in years for the audience or user.",
    )
    suggestedMinAge: Optional[Union[List[Union[Decimal, 'Number', str]], Decimal, 'Number', str]] = Field(
        None,
        description="Minimum recommended age in years for the audience or user.",
    )
    suggestedMeasurement: Optional[Union[List[Union['QuantitativeValue', str]], 'QuantitativeValue', str]] = Field(
        None,
        description="A suggested range of body measurements for the intended audience or person, for example"
     "inseam between 32 and 34 inches or height between 170 and 190 cm. Typically found on a size"
     "chart for wearable products.",
    )
    requiredGender: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Audiences defined by a person's gender.",
    )
    healthCondition: Optional[Union[List[Union['MedicalCondition', str]], 'MedicalCondition', str]] = Field(
        None,
        description="Specifying the health condition(s) of a patient, medical study, or other target audience.",
    )
    requiredMinAge: Optional[Union[List[Union[int, 'Integer', str]], int, 'Integer', str]] = Field(
        None,
        description="Audiences defined by a person's minimum age.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.GenderType import GenderType
    from pydantic_schemaorg.Integer import Integer
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.MedicalCondition import MedicalCondition
