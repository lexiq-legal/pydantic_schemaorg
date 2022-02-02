from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.CategoryCode import CategoryCode
from pydantic_schemaorg.MedicalIntangible import MedicalIntangible


class MedicalCode(CategoryCode, MedicalIntangible):
    """A code for a medical entity.

    See: https://schema.org/MedicalCode
    Model depth: 4
    """
    type_: str = Field("MedicalCode", alias='@type')
    codeValue: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="A short textual code that uniquely identifies the value.",
    )
    codingSystem: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The coding system, e.g. 'ICD-10'.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
