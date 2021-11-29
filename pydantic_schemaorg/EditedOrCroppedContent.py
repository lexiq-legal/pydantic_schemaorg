from pydantic import Field
from pydantic_schemaorg.MediaManipulationRatingEnumeration import MediaManipulationRatingEnumeration


class EditedOrCroppedContent(MediaManipulationRatingEnumeration):
    """Content coded 'edited or cropped content' in a [[MediaReview]], considered in the context"
     "of how it was published or shared. For a [[VideoObject]] to be 'edited or cropped content':"
     "The video has been edited or rearranged. This category applies to time edits, including"
     "editing multiple videos together to alter the story being told or editing out large portions"
     "from a video. For an [[ImageObject]] to be 'edited or cropped content': Presenting a"
     "part of an image from a larger whole to mislead the viewer. For an [[ImageObject]] with"
     "embedded text to be 'edited or cropped content': Presenting a part of an image from a larger"
     "whole to mislead the viewer. For an [[AudioObject]] to be 'edited or cropped content':"
     "The audio has been edited or rearranged. This category applies to time edits, including"
     "editing multiple audio clips together to alter the story being told or editing out large"
     "portions from the recording.

    See https://schema.org/EditedOrCroppedContent.

    """

    locals().update({"@type": Field("EditedOrCroppedContent", const=True)})


EditedOrCroppedContent.update_forward_refs()
