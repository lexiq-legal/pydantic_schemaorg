from pydantic import Field
from pydantic_schemaorg.MediaManipulationRatingEnumeration import MediaManipulationRatingEnumeration


class StagedContent(MediaManipulationRatingEnumeration):
    """Content coded 'staged content' in a [[MediaReview]], considered in the context of how"
     "it was published or shared. For a [[VideoObject]] to be 'staged content': A video that"
     "has been created using actors or similarly contrived. For an [[ImageObject]] to be 'staged"
     "content': An image that was created using actors or similarly contrived, such as a screenshot"
     "of a fake tweet. For an [[ImageObject]] with embedded text to be 'staged content': An"
     "image that was created using actors or similarly contrived, such as a screenshot of a"
     "fake tweet. For an [[AudioObject]] to be 'staged content': Audio that has been created"
     "using actors or similarly contrived.

    See https://schema.org/StagedContent.

    """

    locals().update({"@type": Field("StagedContent", const=True)})


StagedContent.update_forward_refs()
