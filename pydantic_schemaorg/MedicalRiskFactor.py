from pydantic import Field
from pydantic_schemaorg.MedicalEntity import MedicalEntity
from typing import Any, Union, List, Optional


class MedicalRiskFactor(MedicalEntity):
    """A risk factor is anything that increases a person's likelihood of developing or contracting"
     "a disease, medical condition, or complication.

    See https://schema.org/MedicalRiskFactor.

    """

    increasesRiskOf: Optional[Union[List[MedicalEntity], MedicalEntity]] = Field(
        None,
        description="The condition, complication, etc. influenced by this factor.",
    )
    locals().update({"@type": Field("MedicalRiskFactor", const=True)})


MedicalRiskFactor.update_forward_refs()
