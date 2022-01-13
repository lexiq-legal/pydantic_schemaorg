from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.MedicalOrganization import MedicalOrganization


class DiagnosticLab(MedicalOrganization):
    """A medical laboratory that offers on-site or off-site diagnostic services.

    See: https://schema.org/DiagnosticLab
    Model depth: 4
    """

    type_: str = Field("DiagnosticLab", const=True, alias="@type")
    availableTest: "Optional[Union[List[Union[MedicalTest, str]], Union[MedicalTest, str]]]" = Field(
        None,
        description="A diagnostic test or procedure offered by this lab.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.MedicalTest import MedicalTest

    DiagnosticLab.update_forward_refs()
