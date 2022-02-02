from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.Thing import Thing


class MedicalEntity(Thing):
    """The most generic type of entity related to health and the practice of medicine.

    See: https://schema.org/MedicalEntity
    Model depth: 2
    """
    type_: str = Field("MedicalEntity", alias='@type')
    medicineSystem: Optional[Union[List[Union['MedicineSystem', str]], 'MedicineSystem', str]] = Field(
        None,
        description="The system of medicine that includes this MedicalEntity, for example 'evidence-based',"
     "'homeopathic', 'chiropractic', etc.",
    )
    guideline: Optional[Union[List[Union['MedicalGuideline', str]], 'MedicalGuideline', str]] = Field(
        None,
        description="A medical guideline related to this entity.",
    )
    study: Optional[Union[List[Union['MedicalStudy', str]], 'MedicalStudy', str]] = Field(
        None,
        description="A medical study or trial related to this entity.",
    )
    relevantSpecialty: Optional[Union[List[Union['MedicalSpecialty', str]], 'MedicalSpecialty', str]] = Field(
        None,
        description="If applicable, a medical specialty in which this entity is relevant.",
    )
    recognizingAuthority: Optional[Union[List[Union['Organization', str]], 'Organization', str]] = Field(
        None,
        description="If applicable, the organization that officially recognizes this entity as part of its"
     "endorsed system of medicine.",
    )
    code: Optional[Union[List[Union['MedicalCode', str]], 'MedicalCode', str]] = Field(
        None,
        description="A medical code for the entity, taken from a controlled vocabulary or ontology such as"
     "ICD-9, DiseasesDB, MeSH, SNOMED-CT, RxNorm, etc.",
    )
    legalStatus: Optional[Union[List[Union[str, 'Text', 'MedicalEnumeration', 'DrugLegalStatus']], str, 'Text', 'MedicalEnumeration', 'DrugLegalStatus']] = Field(
        None,
        description="The drug or supplement's legal status, including any controlled substance schedules"
     "that apply.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.MedicineSystem import MedicineSystem
    from pydantic_schemaorg.MedicalGuideline import MedicalGuideline
    from pydantic_schemaorg.MedicalStudy import MedicalStudy
    from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.MedicalCode import MedicalCode
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration
    from pydantic_schemaorg.DrugLegalStatus import DrugLegalStatus
