from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.Event import Event


class EducationEvent(Event):
    """Event type: Education event.

    See: https://schema.org/EducationEvent
    Model depth: 3
    """

    type_: str = Field("EducationEvent", const=True, alias="@type")
    teaches: "Optional[Union[List[Union[str, DefinedTerm]], Union[str, DefinedTerm]]]" = Field(
        None,
        description="The item being described is intended to help a person learn the competency or learning"
        "outcome defined by the referenced term.",
    )
    educationalLevel: "Optional[Union[List[Union[AnyUrl, str, DefinedTerm]], Union[AnyUrl, str, DefinedTerm]]]" = Field(
        None,
        description="The level in terms of progression through an educational or training context. Examples"
        "of educational levels include 'beginner', 'intermediate' or 'advanced', and formal"
        "sets of level indicators.",
    )
    assesses: "Optional[Union[List[Union[str, DefinedTerm]], Union[str, DefinedTerm]]]" = Field(
        None,
        description="The item being described is intended to assess the competency or learning outcome defined"
        "by the referenced term.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.DefinedTerm import DefinedTerm

    from pydantic import AnyUrl

    EducationEvent.update_forward_refs()
