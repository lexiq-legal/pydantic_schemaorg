from pydantic import Field, AnyUrl
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Review import Review


class MediaReview(Review):
    """A [[MediaReview]] is a more specialized form of Review dedicated to the evaluation of"
     "media content online, typically in the context of fact-checking and misinformation."
     "For more general reviews of media in the broader sense, use [[UserReview]], [[CriticReview]]"
     "or other [[Review]] types. This definition is a work in progress. While the [[MediaManipulationRatingEnumeration]]"
     "list reflects significant community review amongst fact-checkers and others working"
     "to combat misinformation, the specific structures for representing media objects,"
     "their versions and publication context, is still evolving. Similarly, best practices"
     "for the relationship between [[MediaReview]] and [[ClaimReview]] markup has not yet"
     "been finalized.

    See https://schema.org/MediaReview.

    """

    originalMediaLink: Union[List[Union[AnyUrl, Any]], Union[AnyUrl, Any]] = Field(
        None,
        description="Link to the page containing an original version of the content, or directly to an online"
     "copy of the original [[MediaObject]] content, e.g. video file.",
    )
    mediaAuthenticityCategory: Any = Field(
        None,
        description="Indicates a MediaManipulationRatingEnumeration classification of a media object"
     "(in the context of how it was published or shared).",
    )
    originalMediaContextDescription: Optional[Union[List[str], str]] = Field(
        None,
        description="Describes, in a [[MediaReview]] when dealing with [[DecontextualizedContent]],"
     "background information that can contribute to better interpretation of the [[MediaObject]].",
    )
    locals().update({"@type": Field("MediaReview", const=True)})


MediaReview.update_forward_refs()
