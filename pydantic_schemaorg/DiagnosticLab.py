from pydantic import Field
from pydantic_schemaorg.MedicalTest import MedicalTest
from typing import Any, Optional, Union, List
from pydantic_schemaorg.MedicalOrganization import MedicalOrganization


class DiagnosticLab(MedicalOrganization):
    """A medical laboratory that offers on-site or off-site diagnostic services.

    See https://schema.org/DiagnosticLab.

    """
    type_: str = Field("DiagnosticLab", const=True, alias='@type')
    availableTest: Optional[Union[List[MedicalTest], MedicalTest]] = Field(
        None,
        description="A diagnostic test or procedure offered by this lab.",
    )
    

DiagnosticLab.update_forward_refs()
