from pydantic import Field
from pydantic_schemaorg.Energy import Energy
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Mass import Mass
from pydantic_schemaorg.StructuredValue import StructuredValue


class NutritionInformation(StructuredValue):
    """Nutritional information about the recipe.

    See https://schema.org/NutritionInformation.

    """

    calories: Optional[Union[List[Energy], Energy]] = Field(
        None,
        description="The number of calories.",
    )
    cholesterolContent: Optional[Union[List[Mass], Mass]] = Field(
        None,
        description="The number of milligrams of cholesterol.",
    )
    fatContent: Optional[Union[List[Mass], Mass]] = Field(
        None,
        description="The number of grams of fat.",
    )
    transFatContent: Optional[Union[List[Mass], Mass]] = Field(
        None,
        description="The number of grams of trans fat.",
    )
    servingSize: Optional[Union[List[str], str]] = Field(
        None,
        description="The serving size, in terms of the number of volume or mass.",
    )
    unsaturatedFatContent: Optional[Union[List[Mass], Mass]] = Field(
        None,
        description="The number of grams of unsaturated fat.",
    )
    saturatedFatContent: Optional[Union[List[Mass], Mass]] = Field(
        None,
        description="The number of grams of saturated fat.",
    )
    carbohydrateContent: Optional[Union[List[Mass], Mass]] = Field(
        None,
        description="The number of grams of carbohydrates.",
    )
    proteinContent: Optional[Union[List[Mass], Mass]] = Field(
        None,
        description="The number of grams of protein.",
    )
    sodiumContent: Optional[Union[List[Mass], Mass]] = Field(
        None,
        description="The number of milligrams of sodium.",
    )
    fiberContent: Optional[Union[List[Mass], Mass]] = Field(
        None,
        description="The number of grams of fiber.",
    )
    sugarContent: Optional[Union[List[Mass], Mass]] = Field(
        None,
        description="The number of grams of sugar.",
    )
    locals().update({"@type": Field("NutritionInformation", const=True)})


NutritionInformation.update_forward_refs()
