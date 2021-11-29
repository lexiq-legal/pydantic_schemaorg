from pydantic import Field
from pydantic_schemaorg.MenuSection import MenuSection
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Offer import Offer
from pydantic_schemaorg.Demand import Demand
from pydantic_schemaorg.NutritionInformation import NutritionInformation
from pydantic_schemaorg.RestrictedDiet import RestrictedDiet
from pydantic_schemaorg.Intangible import Intangible


class MenuItem(Intangible):
    """A food or drink item listed in a menu or menu section.

    See https://schema.org/MenuItem.

    """

    menuAddOn: Union[List[Union[MenuSection, Any]], Union[MenuSection, Any]] = Field(
        None,
        description="Additional menu item(s) such as a side dish of salad or side order of fries that can be added"
     "to this menu item. Additionally it can be a menu section containing allowed add-on menu"
     "items for this menu item.",
    )
    offers: Optional[Union[List[Union[Offer, Demand]], Union[Offer, Demand]]] = Field(
        None,
        description="An offer to provide this item&#x2014;for example, an offer to sell a product, rent the"
     "DVD of a movie, perform a service, or give away tickets to an event. Use [[businessFunction]]"
     "to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can"
     "also be used to describe a [[Demand]]. While this property is listed as expected on a number"
     "of common types, it can be used in others. In that case, using a second type, such as Product"
     "or a subtype of Product, can clarify the nature of the offer.",
    )
    nutrition: Optional[Union[List[NutritionInformation], NutritionInformation]] = Field(
        None,
        description="Nutrition information about the recipe or menu item.",
    )
    suitableForDiet: Optional[Union[List[RestrictedDiet], RestrictedDiet]] = Field(
        None,
        description="Indicates a dietary restriction or guideline for which this recipe or menu item is suitable,"
     "e.g. diabetic, halal etc.",
    )
    locals().update({"@type": Field("MenuItem", const=True)})


MenuItem.update_forward_refs()
