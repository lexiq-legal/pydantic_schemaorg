from pydantic import Field
from pydantic_schemaorg.Drug import Drug
from typing import List, Optional, Union
from pydantic_schemaorg.MedicalEntity import MedicalEntity


class DrugClass(MedicalEntity):
    """A class of medical drugs, e.g., statins. Classes can represent general pharmacological"
     "class, common mechanisms of action, common physiological effects, etc.

    See https://schema.org/DrugClass.

    """
    type_: str = Field("DrugClass", const=True, alias='@type')
    drug: Optional[Union[List[Union[Drug, str]], Union[Drug, str]]] = Field(
        None,
        description="Specifying a drug or medicine used in a medication procedure.",
    )
    

DrugClass.update_forward_refs()
