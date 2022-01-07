from pydantic import Field
from pydantic_schemaorg.AdministrativeArea import AdministrativeArea
from typing import List, Optional, Union
from pydantic_schemaorg.MedicalIntangible import MedicalIntangible


class DrugLegalStatus(MedicalIntangible):
    """The legal availability status of a medical drug.

    See https://schema.org/DrugLegalStatus.

    """
    type_: str = Field("DrugLegalStatus", const=True, alias='@type')
    applicableLocation: Optional[Union[List[Union[AdministrativeArea, str]], Union[AdministrativeArea, str]]] = Field(
        None,
        description="The location in which the status applies.",
    )
    

DrugLegalStatus.update_forward_refs()
