from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.StructuredValue import StructuredValue


class NutritionInformation(StructuredValue):
    """Nutritional information about the recipe.

    See: https://schema.org/NutritionInformation
    Model depth: 4
    """
    type_: str = Field("NutritionInformation", alias='@type')
    calories: Optional[Union[List[Union['Energy', str]], 'Energy', str]] = Field(
        None,
        description="The number of calories.",
    )
    cholesterolContent: Optional[Union[List[Union['Mass', str]], 'Mass', str]] = Field(
        None,
        description="The number of milligrams of cholesterol.",
    )
    fatContent: Optional[Union[List[Union['Mass', str]], 'Mass', str]] = Field(
        None,
        description="The number of grams of fat.",
    )
    transFatContent: Optional[Union[List[Union['Mass', str]], 'Mass', str]] = Field(
        None,
        description="The number of grams of trans fat.",
    )
    servingSize: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The serving size, in terms of the number of volume or mass.",
    )
    unsaturatedFatContent: Optional[Union[List[Union['Mass', str]], 'Mass', str]] = Field(
        None,
        description="The number of grams of unsaturated fat.",
    )
    saturatedFatContent: Optional[Union[List[Union['Mass', str]], 'Mass', str]] = Field(
        None,
        description="The number of grams of saturated fat.",
    )
    carbohydrateContent: Optional[Union[List[Union['Mass', str]], 'Mass', str]] = Field(
        None,
        description="The number of grams of carbohydrates.",
    )
    proteinContent: Optional[Union[List[Union['Mass', str]], 'Mass', str]] = Field(
        None,
        description="The number of grams of protein.",
    )
    sodiumContent: Optional[Union[List[Union['Mass', str]], 'Mass', str]] = Field(
        None,
        description="The number of milligrams of sodium.",
    )
    fiberContent: Optional[Union[List[Union['Mass', str]], 'Mass', str]] = Field(
        None,
        description="The number of grams of fiber.",
    )
    sugarContent: Optional[Union[List[Union['Mass', str]], 'Mass', str]] = Field(
        None,
        description="The number of grams of sugar.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Energy import Energy
    from pydantic_schemaorg.Mass import Mass
    from pydantic_schemaorg.Text import Text
