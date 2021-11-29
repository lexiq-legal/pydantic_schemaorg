from pydantic import Field
from pydantic_schemaorg.Drug import Drug
from typing import Any, Union, List, Optional
from pydantic_schemaorg.MedicalEntity import MedicalEntity


class DrugClass(MedicalEntity):
    """A class of medical drugs, e.g., statins. Classes can represent general pharmacological"
     "class, common mechanisms of action, common physiological effects, etc.

    See https://schema.org/DrugClass.

    """

    drug: Optional[Union[List[Drug], Drug]] = Field(
        None,
        description="Specifying a drug or medicine used in a medication procedure.",
    )
    locals().update({"@type": Field("DrugClass", const=True)})


DrugClass.update_forward_refs()
