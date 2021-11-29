from pydantic import Field, AnyUrl
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Thing import Thing
from pydantic_schemaorg.PhysicalActivityCategory import PhysicalActivityCategory
from pydantic_schemaorg.AnatomicalStructure import AnatomicalStructure
from pydantic_schemaorg.LifestyleModification import LifestyleModification


class PhysicalActivity(LifestyleModification):
    """Any bodily activity that enhances or maintains physical fitness and overall health"
     "and wellness. Includes activity that is part of daily living and routine, structured"
     "exercise, and exercise prescribed as part of a medical treatment or recovery plan.

    See https://schema.org/PhysicalActivity.

    """

    epidemiology: Optional[Union[List[str], str]] = Field(
        None,
        description="The characteristics of associated patients, such as age, gender, race etc.",
    )
    category: Optional[Union[List[Union[AnyUrl, str, Thing, PhysicalActivityCategory]], Union[AnyUrl, str, Thing, PhysicalActivityCategory]]] = Field(
        None,
        description="A category for the item. Greater signs or slashes can be used to informally indicate a"
     "category hierarchy.",
    )
    pathophysiology: Optional[Union[List[str], str]] = Field(
        None,
        description="Changes in the normal mechanical, physical, and biochemical functions that are associated"
     "with this activity or condition.",
    )
    associatedAnatomy: Union[List[Union[AnatomicalStructure, Any]], Union[AnatomicalStructure, Any]] = Field(
        None,
        description="The anatomy of the underlying organ system or structures associated with this entity.",
    )
    locals().update({"@type": Field("PhysicalActivity", const=True)})


PhysicalActivity.update_forward_refs()
