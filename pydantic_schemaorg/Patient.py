from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.MedicalAudience import MedicalAudience
from pydantic_schemaorg.Person import Person


class Patient(MedicalAudience, Person):
    """A patient is any person recipient of health care services.

    See: https://schema.org/Patient
    Model depth: 3
    """
    type_: str = Field("Patient", alias='@type')
    diagnosis: Optional[Union[List[Union['MedicalCondition', str]], 'MedicalCondition', str]] = Field(
        None,
        description="One or more alternative conditions considered in the differential diagnosis process"
     "as output of a diagnosis process.",
    )
    healthCondition: Optional[Union[List[Union['MedicalCondition', str]], 'MedicalCondition', str]] = Field(
        None,
        description="Specifying the health condition(s) of a patient, medical study, or other target audience.",
    )
    drug: Optional[Union[List[Union['Drug', str]], 'Drug', str]] = Field(
        None,
        description="Specifying a drug or medicine used in a medication procedure.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.MedicalCondition import MedicalCondition
    from pydantic_schemaorg.Drug import Drug
