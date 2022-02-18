from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.MedicalIntangible import MedicalIntangible


class DrugLegalStatus(MedicalIntangible):
    """The legal availability status of a medical drug.

    See: https://schema.org/DrugLegalStatus
    Model depth: 4
    """
    type_: str = Field(default="DrugLegalStatus", alias='@type', const=True)
    applicableLocation: Optional[Union[List[Union['AdministrativeArea', str]], 'AdministrativeArea', str]] = Field(
        default=None,
        description="The location in which the status applies.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.AdministrativeArea import AdministrativeArea
