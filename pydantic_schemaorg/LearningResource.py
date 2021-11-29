from pydantic import Field, AnyUrl
from pydantic_schemaorg.AlignmentObject import AlignmentObject
from typing import Any, Union, List, Optional
from pydantic_schemaorg.DefinedTerm import DefinedTerm
from pydantic_schemaorg.CreativeWork import CreativeWork


class LearningResource(CreativeWork):
    """The LearningResource type can be used to indicate [[CreativeWork]]s (whether physical"
     "or digital) that have a particular and explicit orientation towards learning, education,"
     "skill acquisition, and other educational purposes. [[LearningResource]] is expected"
     "to be used as an addition to a primary type such as [[Book]], [[VideoObject]], [[Product]]"
     "etc. [[EducationEvent]] serves a similar purpose for event-like things (e.g. a [[Trip]])."
     "A [[LearningResource]] may be created as a result of an [[EducationEvent]], for example"
     "by recording one.

    See https://schema.org/LearningResource.

    """

    educationalAlignment: Optional[Union[List[AlignmentObject], AlignmentObject]] = Field(
        None,
        description="An alignment to an established educational framework. This property should not be used"
     "where the nature of the alignment can be described using a simple property, for example"
     "to express that a resource [[teaches]] or [[assesses]] a competency.",
    )
    teaches: Optional[Union[List[Union[str, DefinedTerm]], Union[str, DefinedTerm]]] = Field(
        None,
        description="The item being described is intended to help a person learn the competency or learning"
     "outcome defined by the referenced term.",
    )
    competencyRequired: Optional[Union[List[Union[AnyUrl, str, DefinedTerm]], Union[AnyUrl, str, DefinedTerm]]] = Field(
        None,
        description="Knowledge, skill, ability or personal attribute that must be demonstrated by a person"
     "or other entity in order to do something such as earn an Educational Occupational Credential"
     "or understand a LearningResource.",
    )
    educationalLevel: Optional[Union[List[Union[AnyUrl, str, DefinedTerm]], Union[AnyUrl, str, DefinedTerm]]] = Field(
        None,
        description="The level in terms of progression through an educational or training context. Examples"
     "of educational levels include 'beginner', 'intermediate' or 'advanced', and formal"
     "sets of level indicators.",
    )
    assesses: Optional[Union[List[Union[str, DefinedTerm]], Union[str, DefinedTerm]]] = Field(
        None,
        description="The item being described is intended to assess the competency or learning outcome defined"
     "by the referenced term.",
    )
    educationalUse: Optional[Union[List[Union[str, DefinedTerm]], Union[str, DefinedTerm]]] = Field(
        None,
        description="The purpose of a work in the context of education; for example, 'assignment', 'group"
     "work'.",
    )
    learningResourceType: Optional[Union[List[Union[str, DefinedTerm]], Union[str, DefinedTerm]]] = Field(
        None,
        description="The predominant type or kind characterizing the learning resource. For example, 'presentation',"
     "'handout'.",
    )
    locals().update({"@type": Field("LearningResource", const=True)})


LearningResource.update_forward_refs()
