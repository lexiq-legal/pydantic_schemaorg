from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty
from typing import List, Optional, Union, Any
from pydantic_schemaorg.MedicalTest import MedicalTest
from pydantic_schemaorg.MedicalProcedure import MedicalProcedure
from pydantic_schemaorg.MedicalTherapy import MedicalTherapy
from pydantic_schemaorg.MedicalBusiness import MedicalBusiness
from pydantic_schemaorg.MedicalOrganization import MedicalOrganization


class Physician(MedicalBusiness, MedicalOrganization):
    """A doctor's office.

    See https://schema.org/Physician.

    """

    medicalSpecialty: Optional[Union[List[MedicalSpecialty], MedicalSpecialty]] = Field(
        None,
        description="A medical specialty of the provider.",
    )
    hospitalAffiliation: Any = Field(
        None,
        description="A hospital with which the physician or office is affiliated.",
    )
    availableService: Optional[Union[List[Union[MedicalTest, MedicalProcedure, MedicalTherapy]], Union[MedicalTest, MedicalProcedure, MedicalTherapy]]] = Field(
        None,
        description="A medical service available from this provider.",
    )
    locals().update({"@type": Field("Physician", const=True)})


Physician.update_forward_refs()
