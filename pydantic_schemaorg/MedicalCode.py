from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.CategoryCode import CategoryCode
from pydantic_schemaorg.MedicalIntangible import MedicalIntangible


class MedicalCode(CategoryCode, MedicalIntangible):
    """A code for a medical entity.

    See: https://schema.org/MedicalCode
    Model depth: 4
    """
    type_: str = Field(default="MedicalCode", alias='@type', const=True)
    codeValue: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="A short textual code that uniquely identifies the value.",
    )
    codingSystem: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The coding system, e.g. 'ICD-10'.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
