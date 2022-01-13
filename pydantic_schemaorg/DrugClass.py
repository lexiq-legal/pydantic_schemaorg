from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.MedicalEntity import MedicalEntity


class DrugClass(MedicalEntity):
    """A class of medical drugs, e.g., statins. Classes can represent general pharmacological"
     "class, common mechanisms of action, common physiological effects, etc.

    See: https://schema.org/DrugClass
    Model depth: 3
    """

    type_: str = Field("DrugClass", const=True, alias="@type")
    drug: "Optional[Union[List[Union[Drug, str]], Union[Drug, str]]]" = Field(
        None,
        description="Specifying a drug or medicine used in a medication procedure.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.Drug import Drug

    DrugClass.update_forward_refs()
