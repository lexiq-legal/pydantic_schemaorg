from pydantic import Field
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.Person import Person
from typing import Any, Union, List, Optional
from pydantic_schemaorg.CreativeWork import CreativeWork
from pydantic_schemaorg.MusicRecording import MusicRecording
from pydantic_schemaorg.Event import Event


class MusicComposition(CreativeWork):
    """A musical composition.

    See https://schema.org/MusicComposition.

    """

    composer: Optional[Union[List[Union[Organization, Person]], Union[Organization, Person]]] = Field(
        None,
        description="The person or organization who wrote a composition, or who is the composer of a work performed"
     "at some event.",
    )
    includedComposition: Any = Field(
        None,
        description="Smaller compositions included in this work (e.g. a movement in a symphony).",
    )
    lyrics: Optional[Union[List[CreativeWork], CreativeWork]] = Field(
        None,
        description="The words in the song.",
    )
    musicalKey: Optional[Union[List[str], str]] = Field(
        None,
        description="The key, mode, or scale this composition uses.",
    )
    musicArrangement: Any = Field(
        None,
        description="An arrangement derived from the composition.",
    )
    recordedAs: Optional[Union[List[MusicRecording], MusicRecording]] = Field(
        None,
        description="An audio recording of the work.",
    )
    iswcCode: Optional[Union[List[str], str]] = Field(
        None,
        description="The International Standard Musical Work Code for the composition.",
    )
    firstPerformance: Optional[Union[List[Event], Event]] = Field(
        None,
        description="The date and place the work was first performed.",
    )
    lyricist: Optional[Union[List[Person], Person]] = Field(
        None,
        description="The person who wrote the words.",
    )
    musicCompositionForm: Optional[Union[List[str], str]] = Field(
        None,
        description="The type of composition (e.g. overture, sonata, symphony, etc.).",
    )
    locals().update({"@type": Field("MusicComposition", const=True)})


MusicComposition.update_forward_refs()
