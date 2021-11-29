from pydantic import Field
from pydantic_schemaorg.MediaManipulationRatingEnumeration import MediaManipulationRatingEnumeration


class OriginalMediaContent(MediaManipulationRatingEnumeration):
    """Content coded 'as original media content' in a [[MediaReview]], considered in the context"
     "of how it was published or shared. For a [[VideoObject]] to be 'original': No evidence"
     "the footage has been misleadingly altered or manipulated, though it may contain false"
     "or misleading claims. For an [[ImageObject]] to be 'original': No evidence the image"
     "has been misleadingly altered or manipulated, though it may still contain false or misleading"
     "claims. For an [[ImageObject]] with embedded text to be 'original': No evidence the"
     "image has been misleadingly altered or manipulated, though it may still contain false"
     "or misleading claims. For an [[AudioObject]] to be 'original': No evidence the audio"
     "has been misleadingly altered or manipulated, though it may contain false or misleading"
     "claims.

    See https://schema.org/OriginalMediaContent.

    """

    locals().update({"@type": Field("OriginalMediaContent", const=True)})


OriginalMediaContent.update_forward_refs()
