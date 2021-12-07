from pydantic import Field
from pydantic_schemaorg.AdministrativeArea import AdministrativeArea
from typing import Any, Optional, Union, List
from pydantic_schemaorg.MedicalIntangible import MedicalIntangible


class DrugLegalStatus(MedicalIntangible):
    """The legal availability status of a medical drug.

    See https://schema.org/DrugLegalStatus.

    """
    type_: str = Field("DrugLegalStatus", const=True, alias='@type')
    applicableLocation: Optional[Union[List[AdministrativeArea], AdministrativeArea]] = Field(
        None,
        description="The location in which the status applies.",
    )
    

DrugLegalStatus.update_forward_refs()
