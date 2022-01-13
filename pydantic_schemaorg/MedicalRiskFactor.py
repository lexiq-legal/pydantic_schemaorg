from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.MedicalEntity import MedicalEntity


class MedicalRiskFactor(MedicalEntity):
    """A risk factor is anything that increases a person's likelihood of developing or contracting"
     "a disease, medical condition, or complication.

    See: https://schema.org/MedicalRiskFactor
    Model depth: 3
    """

    type_: str = Field("MedicalRiskFactor", const=True, alias="@type")
    increasesRiskOf: "Optional[Union[List[Union[MedicalEntity, str]], Union[MedicalEntity, str]]]" = Field(
        None,
        description="The condition, complication, etc. influenced by this factor.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.MedicalEntity import MedicalEntity

    MedicalRiskFactor.update_forward_refs()
