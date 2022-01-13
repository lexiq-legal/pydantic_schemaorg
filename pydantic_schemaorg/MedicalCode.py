from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional, Any

from pydantic_schemaorg.CategoryCode import CategoryCode

from pydantic_schemaorg.MedicalIntangible import MedicalIntangible


class MedicalCode(CategoryCode, MedicalIntangible):
    """A code for a medical entity.

    See: https://schema.org/MedicalCode
    Model depth: 4
    """

    type_: str = Field("MedicalCode", const=True, alias="@type")
    codeValue: "Optional[Union[List[str], str]]" = Field(
        None,
        description="A short textual code that uniquely identifies the value.",
    )
    codingSystem: "Optional[Union[List[str], str]]" = Field(
        None,
        description="The coding system, e.g. 'ICD-10'.",
    )


if TYPE_CHECKING:

    MedicalCode.update_forward_refs()
