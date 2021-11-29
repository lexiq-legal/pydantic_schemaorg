from pydantic import Field
from pydantic_schemaorg.AdministrativeArea import AdministrativeArea
from typing import Any, Union, List, Optional
from pydantic_schemaorg.MedicalIntangible import MedicalIntangible


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
