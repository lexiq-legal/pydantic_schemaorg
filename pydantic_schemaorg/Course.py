from pydantic import Field, AnyUrl
from pydantic_schemaorg.StructuredValue import StructuredValue
from typing import Any, Union, List, Optional
from pydantic_schemaorg.EducationalOccupationalCredential import EducationalOccupationalCredential
from pydantic_schemaorg.AlignmentObject import AlignmentObject
from pydantic_schemaorg.CreativeWork import CreativeWork
from pydantic_schemaorg.LearningResource import LearningResource


class Course(CreativeWork, LearningResource):
    """A description of an educational course which may be offered as distinct instances at"
     "which take place at different times or take place at different locations, or be offered"
     "through different media or modes of study. An educational course is a sequence of one"
     "or more educational events and/or creative works which aims to build knowledge, competence"
     "or ability of learners.

    See https://schema.org/Course.

    """

    numberOfCredits: Optional[Union[List[Union[int, StructuredValue]], Union[int, StructuredValue]]] = Field(
        None,
        description="The number of credits or units awarded by a Course or required to complete an EducationalOccupationalProgram.",
    )
    educationalCredentialAwarded: Optional[Union[List[Union[AnyUrl, str, EducationalOccupationalCredential]], Union[AnyUrl, str, EducationalOccupationalCredential]]] = Field(
        None,
        description="A description of the qualification, award, certificate, diploma or other educational"
     "credential awarded as a consequence of successful completion of this course or program.",
    )
    courseCode: Optional[Union[List[str], str]] = Field(
        None,
        description="The identifier for the [[Course]] used by the course [[provider]] (e.g. CS101 or 6.001).",
    )
    hasCourseInstance: Any = Field(
        None,
        description="An offering of the course at a specific time and place or through specific media or mode"
     "of study or to a specific section of students.",
    )
    coursePrerequisites: Union[List[Union[str, AlignmentObject, Any]], Union[str, AlignmentObject, Any]] = Field(
        None,
        description="Requirements for taking the Course. May be completion of another [[Course]] or a textual"
     "description like \"permission of instructor\". Requirements may be a pre-requisite"
     "competency, referenced using [[AlignmentObject]].",
    )
    occupationalCredentialAwarded: Optional[Union[List[Union[AnyUrl, str, EducationalOccupationalCredential]], Union[AnyUrl, str, EducationalOccupationalCredential]]] = Field(
        None,
        description="A description of the qualification, award, certificate, diploma or other occupational"
     "credential awarded as a consequence of successful completion of this course or program.",
    )
    locals().update({"@type": Field("Course", const=True)})


Course.update_forward_refs()
