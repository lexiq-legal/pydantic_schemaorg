from pydantic import Field
from typing import List, Optional, Any, Union
from pydantic_schemaorg.CategoryCode import CategoryCode
from pydantic_schemaorg.MedicalIntangible import MedicalIntangible


class MedicalCode(CategoryCode, MedicalIntangible):
    """A code for a medical entity.

    See https://schema.org/MedicalCode.

    """
    type_: str = Field("MedicalCode", const=True, alias='@type')
    codeValue: Optional[Union[List[str], str]] = Field(
        None,
        description="A short textual code that uniquely identifies the value.",
    )
    codingSystem: Optional[Union[List[str], str]] = Field(
        None,
        description="The coding system, e.g. 'ICD-10'.",
    )
    

MedicalCode.update_forward_refs()
