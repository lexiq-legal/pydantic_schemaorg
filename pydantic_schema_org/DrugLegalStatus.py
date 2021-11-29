from pydantic import Field
from pydantic_schema_org.AdministrativeArea import AdministrativeArea
from typing import Any, Optional, Union, List
from pydantic_schema_org.MedicalIntangible import MedicalIntangible


class DrugLegalStatus(MedicalIntangible):
    """The legal availability status of a medical drug.

    See https://schema.org/DrugLegalStatus.

    """

    applicableLocation: Optional[Union[List[AdministrativeArea], AdministrativeArea]] = Field(
        None,
        description="The location in which the status applies.",
    )
    locals().update({"@type": Field("DrugLegalStatus", const=True)})


DrugLegalStatus.update_forward_refs()
