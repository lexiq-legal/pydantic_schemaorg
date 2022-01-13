from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.MedicalBusiness import MedicalBusiness

from pydantic_schemaorg.MedicalOrganization import MedicalOrganization


class MedicalClinic(MedicalBusiness, MedicalOrganization):
    """A facility, often associated with a hospital or medical school, that is devoted to the"
     "specific diagnosis and/or healthcare. Previously limited to outpatients but with"
     "evolution it may be open to inpatients as well.

    See: https://schema.org/MedicalClinic
    Model depth: 4
    """

    type_: str = Field("MedicalClinic", const=True, alias="@type")
    medicalSpecialty: "Optional[Union[List[Union[MedicalSpecialty, str]], Union[MedicalSpecialty, str]]]" = Field(
        None,
        description="A medical specialty of the provider.",
    )
    availableService: "Optional[Union[List[Union[MedicalTherapy, MedicalProcedure, MedicalTest, str]], Union[MedicalTherapy, MedicalProcedure, MedicalTest, str]]]" = Field(
        None,
        description="A medical service available from this provider.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty

    from pydantic_schemaorg.MedicalTherapy import MedicalTherapy

    from pydantic_schemaorg.MedicalProcedure import MedicalProcedure

    from pydantic_schemaorg.MedicalTest import MedicalTest

    MedicalClinic.update_forward_refs()
