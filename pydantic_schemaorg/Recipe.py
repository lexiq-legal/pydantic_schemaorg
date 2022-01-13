from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional, Any

from pydantic_schemaorg.HowTo import HowTo


class Recipe(HowTo):
    """A recipe. For dietary restrictions covered by the recipe, a few common restrictions"
     "are enumerated via [[suitableForDiet]]. The [[keywords]] property can also be used"
     "to add more detail.

    See: https://schema.org/Recipe
    Model depth: 4
    """

    type_: str = Field("Recipe", const=True, alias="@type")
    recipeInstructions: "Optional[Union[List[Union[str, ItemList, CreativeWork]], Union[str, ItemList, CreativeWork]]]" = Field(
        None,
        description="A step in making the recipe, in the form of a single item (document, video, etc.) or an ordered"
        "list with HowToStep and/or HowToSection items.",
    )
    cookTime: "Optional[Union[List[Union[Duration, str]], Union[Duration, str]]]" = Field(
        None,
        description="The time it takes to actually cook the dish, in [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601).",
    )
    ingredients: "Optional[Union[List[str], str]]" = Field(
        None,
        description="A single ingredient used in the recipe, e.g. sugar, flour or garlic.",
    )
    recipeCuisine: "Optional[Union[List[str], str]]" = Field(
        None,
        description="The cuisine of the recipe (for example, French or Ethiopian).",
    )
    nutrition: "Optional[Union[List[Union[NutritionInformation, str]], Union[NutritionInformation, str]]]" = Field(
        None,
        description="Nutrition information about the recipe or menu item.",
    )
    recipeIngredient: "Optional[Union[List[str], str]]" = Field(
        None,
        description="A single ingredient used in the recipe, e.g. sugar, flour or garlic.",
    )
    recipeCategory: "Optional[Union[List[str], str]]" = Field(
        None,
        description="The category of the recipe—for example, appetizer, entree, etc.",
    )
    suitableForDiet: "Optional[Union[List[Union[RestrictedDiet, str]], Union[RestrictedDiet, str]]]" = Field(
        None,
        description="Indicates a dietary restriction or guideline for which this recipe or menu item is suitable,"
        "e.g. diabetic, halal etc.",
    )
    recipeYield: "Optional[Union[List[Union[str, QuantitativeValue]], Union[str, QuantitativeValue]]]" = Field(
        None,
        description="The quantity produced by the recipe (for example, number of people served, number of"
        "servings, etc).",
    )
    cookingMethod: "Optional[Union[List[str], str]]" = Field(
        None,
        description="The method of cooking, such as Frying, Steaming, ...",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.ItemList import ItemList

    from pydantic_schemaorg.CreativeWork import CreativeWork

    from pydantic_schemaorg.Duration import Duration

    from pydantic_schemaorg.NutritionInformation import NutritionInformation

    from pydantic_schemaorg.RestrictedDiet import RestrictedDiet

    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue

    Recipe.update_forward_refs()
