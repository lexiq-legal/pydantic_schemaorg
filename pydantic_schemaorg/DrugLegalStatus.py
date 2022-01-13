from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.MedicalIntangible import MedicalIntangible


class DrugLegalStatus(MedicalIntangible):
    """The legal availability status of a medical drug.

    See: https://schema.org/DrugLegalStatus
    Model depth: 4
    """

    type_: str = Field("DrugLegalStatus", const=True, alias="@type")
    applicableLocation: "Optional[Union[List[Union[AdministrativeArea, str]], Union[AdministrativeArea, str]]]" = Field(
        None,
        description="The location in which the status applies.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.AdministrativeArea import AdministrativeArea

    DrugLegalStatus.update_forward_refs()
