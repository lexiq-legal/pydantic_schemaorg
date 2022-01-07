from pydantic import Field
from pydantic_schemaorg.Recipe import Recipe
from typing import List, Optional, Union
from pydantic_schemaorg.FoodEstablishment import FoodEstablishment
from pydantic_schemaorg.Place import Place
from pydantic_schemaorg.FoodEvent import FoodEvent
from pydantic_schemaorg.CreateAction import CreateAction


class CookAction(CreateAction):
    """The act of producing/preparing food.

    See https://schema.org/CookAction.

    """
    type_: str = Field("CookAction", const=True, alias='@type')
    recipe: Optional[Union[List[Union[Recipe, str]], Union[Recipe, str]]] = Field(
        None,
        description="A sub property of instrument. The recipe/instructions used to perform the action.",
    )
    foodEstablishment: Optional[Union[List[Union[FoodEstablishment, Place, str]], Union[FoodEstablishment, Place, str]]] = Field(
        None,
        description="A sub property of location. The specific food establishment where the action occurred.",
    )
    foodEvent: Optional[Union[List[Union[FoodEvent, str]], Union[FoodEvent, str]]] = Field(
        None,
        description="A sub property of location. The specific food event where the action occurred.",
    )
    

CookAction.update_forward_refs()
