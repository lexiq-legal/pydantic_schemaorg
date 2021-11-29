from pydantic import Field
from pydantic_schemaorg.MedicineSystem import MedicineSystem
from typing import Any, Union, List, Optional
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration
from pydantic_schemaorg.Thing import Thing


class MedicalEntity(Thing):
    """The most generic type of entity related to health and the practice of medicine.

    See https://schema.org/MedicalEntity.

    """

    medicineSystem: Optional[Union[List[MedicineSystem], MedicineSystem]] = Field(
        None,
        description="The system of medicine that includes this MedicalEntity, for example 'evidence-based',"
     "'homeopathic', 'chiropractic', etc.",
    )
    guideline: Any = Field(
        None,
        description="A medical guideline related to this entity.",
    )
    study: Any = Field(
        None,
        description="A medical study or trial related to this entity.",
    )
    relevantSpecialty: Optional[Union[List[MedicalSpecialty], MedicalSpecialty]] = Field(
        None,
        description="If applicable, a medical specialty in which this entity is relevant.",
    )
    recognizingAuthority: Optional[Union[List[Organization], Organization]] = Field(
        None,
        description="If applicable, the organization that officially recognizes this entity as part of its"
     "endorsed system of medicine.",
    )
    code: Any = Field(
        None,
        description="A medical code for the entity, taken from a controlled vocabulary or ontology such as"
     "ICD-9, DiseasesDB, MeSH, SNOMED-CT, RxNorm, etc.",
    )
    legalStatus: Union[List[Union[str, MedicalEnumeration, Any]], Union[str, MedicalEnumeration, Any]] = Field(
        None,
        description="The drug or supplement's legal status, including any controlled substance schedules"
     "that apply.",
    )
    locals().update({"@type": Field("MedicalEntity", const=True)})


MedicalEntity.update_forward_refs()
