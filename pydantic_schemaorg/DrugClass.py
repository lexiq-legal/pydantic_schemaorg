from pydantic import Field
from pydantic_schemaorg.Drug import Drug
from typing import Any, Optional, Union, List
from pydantic_schemaorg.MedicalEntity import MedicalEntity


class DrugClass(MedicalEntity):
    """A class of medical drugs, e.g., statins. Classes can represent general pharmacological"
     "class, common mechanisms of action, common physiological effects, etc.

    See https://schema.org/DrugClass.

    """
    type_: str = Field("DrugClass", const=True, alias='@type')
    drug: Optional[Union[List[Drug], Drug]] = Field(
        None,
        description="Specifying a drug or medicine used in a medication procedure.",
    )
    

DrugClass.update_forward_refs()
