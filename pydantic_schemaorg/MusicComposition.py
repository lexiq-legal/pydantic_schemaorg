from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class MusicComposition(CreativeWork):
    """A musical composition.

    See: https://schema.org/MusicComposition
    Model depth: 3
    """
    type_: str = Field("MusicComposition", alias='@type')
    composer: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        None,
        description="The person or organization who wrote a composition, or who is the composer of a work performed"
     "at some event.",
    )
    includedComposition: Optional[Union[List[Union['MusicComposition', str]], 'MusicComposition', str]] = Field(
        None,
        description="Smaller compositions included in this work (e.g. a movement in a symphony).",
    )
    lyrics: Optional[Union[List[Union['CreativeWork', str]], 'CreativeWork', str]] = Field(
        None,
        description="The words in the song.",
    )
    musicalKey: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The key, mode, or scale this composition uses.",
    )
    musicArrangement: Optional[Union[List[Union['MusicComposition', str]], 'MusicComposition', str]] = Field(
        None,
        description="An arrangement derived from the composition.",
    )
    recordedAs: Optional[Union[List[Union['MusicRecording', str]], 'MusicRecording', str]] = Field(
        None,
        description="An audio recording of the work.",
    )
    iswcCode: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The International Standard Musical Work Code for the composition.",
    )
    firstPerformance: Optional[Union[List[Union['Event', str]], 'Event', str]] = Field(
        None,
        description="The date and place the work was first performed.",
    )
    lyricist: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        None,
        description="The person who wrote the words.",
    )
    musicCompositionForm: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The type of composition (e.g. overture, sonata, symphony, etc.).",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.CreativeWork import CreativeWork
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.MusicRecording import MusicRecording
    from pydantic_schemaorg.Event import Event
