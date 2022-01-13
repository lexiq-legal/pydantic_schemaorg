from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional, Any

from pydantic_schemaorg.CreativeWork import CreativeWork


class MusicComposition(CreativeWork):
    """A musical composition.

    See: https://schema.org/MusicComposition
    Model depth: 3
    """

    type_: str = Field("MusicComposition", const=True, alias="@type")
    composer: "Optional[Union[List[Union[Person, Organization, str]], Union[Person, Organization, str]]]" = Field(
        None,
        description="The person or organization who wrote a composition, or who is the composer of a work performed"
        "at some event.",
    )
    includedComposition: "Optional[Union[List[Union['MusicComposition', str]], Union['MusicComposition', str]]]" = Field(
        None,
        description="Smaller compositions included in this work (e.g. a movement in a symphony).",
    )
    lyrics: "Optional[Union[List[Union[CreativeWork, str]], Union[CreativeWork, str]]]" = Field(
        None,
        description="The words in the song.",
    )
    musicalKey: "Optional[Union[List[str], str]]" = Field(
        None,
        description="The key, mode, or scale this composition uses.",
    )
    musicArrangement: "Optional[Union[List[Union['MusicComposition', str]], Union['MusicComposition', str]]]" = Field(
        None,
        description="An arrangement derived from the composition.",
    )
    recordedAs: "Optional[Union[List[Union[MusicRecording, str]], Union[MusicRecording, str]]]" = Field(
        None,
        description="An audio recording of the work.",
    )
    iswcCode: "Optional[Union[List[str], str]]" = Field(
        None,
        description="The International Standard Musical Work Code for the composition.",
    )
    firstPerformance: "Optional[Union[List[Union[Event, str]], Union[Event, str]]]" = (
        Field(
            None,
            description="The date and place the work was first performed.",
        )
    )
    lyricist: "Optional[Union[List[Union[Person, str]], Union[Person, str]]]" = Field(
        None,
        description="The person who wrote the words.",
    )
    musicCompositionForm: "Optional[Union[List[str], str]]" = Field(
        None,
        description="The type of composition (e.g. overture, sonata, symphony, etc.).",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.Person import Person

    from pydantic_schemaorg.Organization import Organization

    from pydantic_schemaorg.CreativeWork import CreativeWork

    from pydantic_schemaorg.MusicRecording import MusicRecording

    from pydantic_schemaorg.Event import Event

    MusicComposition.update_forward_refs()
