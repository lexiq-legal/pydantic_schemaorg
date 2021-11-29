from pydantic import Field
from typing import Any, Optional, Union, List
from pydantic_schema_org.Person import Person
from pydantic_schema_org.Organization import Organization
from pydantic_schema_org.CreativeWork import CreativeWork
from pydantic_schema_org.LifestyleModification import LifestyleModification


class Diet(CreativeWork, LifestyleModification):
    """A strategy of regulating the intake of food to achieve or maintain a specific health-related"
     "goal.

    See https://schema.org/Diet.

    """

    risks: Optional[Union[List[str], str]] = Field(
        None,
        description="Specific physiologic risks associated to the diet plan.",
    )
    endorsers: Optional[Union[List[Union[Person, Organization]], Union[Person, Organization]]] = Field(
        None,
        description="People or organizations that endorse the plan.",
    )
    expertConsiderations: Optional[Union[List[str], str]] = Field(
        None,
        description="Medical expert advice related to the plan.",
    )
    physiologicalBenefits: Optional[Union[List[str], str]] = Field(
        None,
        description="Specific physiologic benefits associated to the plan.",
    )
    dietFeatures: Optional[Union[List[str], str]] = Field(
        None,
        description="Nutritional information specific to the dietary plan. May include dietary recommendations"
     "on what foods to avoid, what foods to consume, and specific alterations/deviations"
     "from the USDA or other regulatory body's approved dietary guidelines.",
    )
    locals().update({"@type": Field("Diet", const=True)})


Diet.update_forward_refs()
