from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.MedicalEntity import MedicalEntity
from pydantic_schemaorg.MedicalStudyStatus import MedicalStudyStatus
from pydantic_schemaorg.EventStatusType import EventStatusType
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.Person import Person
from pydantic_schemaorg.MedicalCondition import MedicalCondition


class MedicalStudy(MedicalEntity):
    """A medical study is an umbrella type covering all kinds of research studies relating to"
     "human medicine or health, including observational studies and interventional trials"
     "and registries, randomized, controlled or not. When the specific type of study is known,"
     "use one of the extensions of this type, such as MedicalTrial or MedicalObservationalStudy."
     "Also, note that this type should be used to mark up data that describes the study itself;"
     "to tag an article that publishes the results of a study, use MedicalScholarlyArticle."
     "Note: use the code property of MedicalEntity to store study IDs, e.g. clinicaltrials.gov"
     "ID.

    See https://schema.org/MedicalStudy.

    """

    studyLocation: Any = Field(
        None,
        description="The location in which the study is taking/took place.",
    )
    studySubject: Optional[Union[List[MedicalEntity], MedicalEntity]] = Field(
        None,
        description="A subject of the study, i.e. one of the medical conditions, therapies, devices, drugs,"
     "etc. investigated by the study.",
    )
    status: Optional[Union[List[Union[str, MedicalStudyStatus, EventStatusType]], Union[str, MedicalStudyStatus, EventStatusType]]] = Field(
        None,
        description="The status of the study (enumerated).",
    )
    sponsor: Optional[Union[List[Union[Organization, Person]], Union[Organization, Person]]] = Field(
        None,
        description="A person or organization that supports a thing through a pledge, promise, or financial"
     "contribution. e.g. a sponsor of a Medical Study or a corporate sponsor of an event.",
    )
    healthCondition: Optional[Union[List[MedicalCondition], MedicalCondition]] = Field(
        None,
        description="Specifying the health condition(s) of a patient, medical study, or other target audience.",
    )
    locals().update({"@type": Field("MedicalStudy", const=True)})


MedicalStudy.update_forward_refs()
