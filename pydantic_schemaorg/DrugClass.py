from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, List, Optional


from pydantic import Field
from pydantic_schemaorg.MedicalEntity import MedicalEntity


class DrugClass(MedicalEntity):
    """A class of medical drugs, e.g., statins. Classes can represent general pharmacological"
     "class, common mechanisms of action, common physiological effects, etc.

    See: https://schema.org/DrugClass
    Model depth: 3
    """
    type_: str = Field("DrugClass", alias='@type')
    drug: Optional[Union[List[Union['Drug', str]], 'Drug', str]] = Field(
        None,
        description="Specifying a drug or medicine used in a medication procedure.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Drug import Drug
