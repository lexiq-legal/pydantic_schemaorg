from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional, Any

from pydantic_schemaorg.LifestyleModification import LifestyleModification

from pydantic_schemaorg.CreativeWork import CreativeWork


class Diet(LifestyleModification, CreativeWork):
    """A strategy of regulating the intake of food to achieve or maintain a specific health-related"
     "goal.

    See: https://schema.org/Diet
    Model depth: 3
    """

    type_: str = Field("Diet", const=True, alias="@type")
    risks: "Optional[Union[List[str], str]]" = Field(
        None,
        description="Specific physiologic risks associated to the diet plan.",
    )
    endorsers: "Optional[Union[List[Union[Person, Organization, str]], Union[Person, Organization, str]]]" = Field(
        None,
        description="People or organizations that endorse the plan.",
    )
    expertConsiderations: "Optional[Union[List[str], str]]" = Field(
        None,
        description="Medical expert advice related to the plan.",
    )
    physiologicalBenefits: "Optional[Union[List[str], str]]" = Field(
        None,
        description="Specific physiologic benefits associated to the plan.",
    )
    dietFeatures: "Optional[Union[List[str], str]]" = Field(
        None,
        description="Nutritional information specific to the dietary plan. May include dietary recommendations"
        "on what foods to avoid, what foods to consume, and specific alterations/deviations"
        "from the USDA or other regulatory body's approved dietary guidelines.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.Person import Person

    from pydantic_schemaorg.Organization import Organization

    Diet.update_forward_refs()
