from pydantic import Field
from pydantic_schemaorg.MedicalEntity import MedicalEntity
from typing import List, Optional, Union


class MedicalRiskFactor(MedicalEntity):
    """A risk factor is anything that increases a person's likelihood of developing or contracting"
     "a disease, medical condition, or complication.

    See https://schema.org/MedicalRiskFactor.

    """
    type_: str = Field("MedicalRiskFactor", const=True, alias='@type')
    increasesRiskOf: Optional[Union[List[Union[MedicalEntity, str]], Union[MedicalEntity, str]]] = Field(
        None,
        description="The condition, complication, etc. influenced by this factor.",
    )
    

MedicalRiskFactor.update_forward_refs()
