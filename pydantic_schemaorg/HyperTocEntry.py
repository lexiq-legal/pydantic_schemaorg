from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.MediaObject import MediaObject
from pydantic_schemaorg.CreativeWork import CreativeWork


class HyperTocEntry(CreativeWork):
    """A HyperToEntry is an item within a [[HyperToc]], which represents a hypertext table"
     "of contents for complex media objects, such as [[VideoObject]], [[AudioObject]]."
     "The media object itself is indicated using [[associatedMedia]]. Each section of interest"
     "within that content can be described with a [[HyperTocEntry]], with associated [[startOffset]]"
     "and [[endOffset]]. When several entries are all from the same file, [[associatedMedia]]"
     "is used on the overarching [[HyperTocEntry]]; if the content has been split into multiple"
     "files, they can be referenced using [[associatedMedia]] on each [[HyperTocEntry]].

    See https://schema.org/HyperTocEntry.

    """

    utterances: Optional[Union[List[str], str]] = Field(
        None,
        description="Text of an utterances (spoken words, lyrics etc.) that occurs at a certain section of"
     "a media object, represented as a [[HyperTocEntry]].",
    )
    tocContinuation: Any = Field(
        None,
        description="A [[HyperTocEntry]] can have a [[tocContinuation]] indicated, which is another [[HyperTocEntry]]"
     "that would be the default next item to play or render.",
    )
    associatedMedia: Optional[Union[List[MediaObject], MediaObject]] = Field(
        None,
        description="A media object that encodes this CreativeWork. This property is a synonym for encoding.",
    )
    locals().update({"@type": Field("HyperTocEntry", const=True)})


HyperTocEntry.update_forward_refs()
