from pydantic import Field
from pydantic_schemaorg.GenderType import GenderType
from typing import Any, Union, List, Optional
from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
from decimal import Decimal
from pydantic_schemaorg.MedicalCondition import MedicalCondition
from pydantic_schemaorg.Audience import Audience


class PeopleAudience(Audience):
    """A set of characteristics belonging to people, e.g. who compose an item's target audience.

    See https://schema.org/PeopleAudience.

    """

    suggestedGender: Optional[Union[List[Union[str, GenderType]], Union[str, GenderType]]] = Field(
        None,
        description="The suggested gender of the intended person or audience, for example \"male\", \"female\","
     "or \"unisex\".",
    )
    requiredMaxAge: Optional[Union[List[int], int]] = Field(
        None,
        description="Audiences defined by a person's maximum age.",
    )
    suggestedAge: Optional[Union[List[QuantitativeValue], QuantitativeValue]] = Field(
        None,
        description="The age or age range for the intended audience or person, for example 3-12 months for infants,"
     "1-5 years for toddlers.",
    )
    suggestedMaxAge: Optional[Union[List[Decimal], Decimal]] = Field(
        None,
        description="Maximum recommended age in years for the audience or user.",
    )
    suggestedMinAge: Optional[Union[List[Decimal], Decimal]] = Field(
        None,
        description="Minimum recommended age in years for the audience or user.",
    )
    suggestedMeasurement: Optional[Union[List[QuantitativeValue], QuantitativeValue]] = Field(
        None,
        description="A suggested range of body measurements for the intended audience or person, for example"
     "inseam between 32 and 34 inches or height between 170 and 190 cm. Typically found on a size"
     "chart for wearable products.",
    )
    requiredGender: Optional[Union[List[str], str]] = Field(
        None,
        description="Audiences defined by a person's gender.",
    )
    healthCondition: Optional[Union[List[MedicalCondition], MedicalCondition]] = Field(
        None,
        description="Specifying the health condition(s) of a patient, medical study, or other target audience.",
    )
    requiredMinAge: Optional[Union[List[int], int]] = Field(
        None,
        description="Audiences defined by a person's minimum age.",
    )
    locals().update({"@type": Field("PeopleAudience", const=True)})


PeopleAudience.update_forward_refs()
