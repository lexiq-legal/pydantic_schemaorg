from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty
from typing import Any, Union, List, Optional
from pydantic_schemaorg.MedicalProcedure import MedicalProcedure
from pydantic_schemaorg.MedicalTherapy import MedicalTherapy
from pydantic_schemaorg.MedicalTest import MedicalTest
from pydantic_schemaorg.MedicalBusiness import MedicalBusiness
from pydantic_schemaorg.MedicalOrganization import MedicalOrganization


class MedicalClinic(MedicalBusiness, MedicalOrganization):
    """A facility, often associated with a hospital or medical school, that is devoted to the"
     "specific diagnosis and/or healthcare. Previously limited to outpatients but with"
     "evolution it may be open to inpatients as well.

    See https://schema.org/MedicalClinic.

    """

    medicalSpecialty: Optional[Union[List[MedicalSpecialty], MedicalSpecialty]] = Field(
        None,
        description="A medical specialty of the provider.",
    )
    availableService: Optional[Union[List[Union[MedicalProcedure, MedicalTherapy, MedicalTest]], Union[MedicalProcedure, MedicalTherapy, MedicalTest]]] = Field(
        None,
        description="A medical service available from this provider.",
    )
    locals().update({"@type": Field("MedicalClinic", const=True)})


MedicalClinic.update_forward_refs()
