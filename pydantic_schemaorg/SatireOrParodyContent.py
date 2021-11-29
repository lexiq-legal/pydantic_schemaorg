from pydantic import Field
from pydantic_schemaorg.MediaManipulationRatingEnumeration import MediaManipulationRatingEnumeration


class SatireOrParodyContent(MediaManipulationRatingEnumeration):
    """Content coded 'satire or parody content' in a [[MediaReview]], considered in the context"
     "of how it was published or shared. For a [[VideoObject]] to be 'satire or parody content':"
     "A video that was created as political or humorous commentary and is presented in that"
     "context. (Reshares of satire/parody content that do not include relevant context are"
     "more likely to fall under the “missing context” rating.) For an [[ImageObject]] to be"
     "'satire or parody content': An image that was created as political or humorous commentary"
     "and is presented in that context. (Reshares of satire/parody content that do not include"
     "relevant context are more likely to fall under the “missing context” rating.) For an"
     "[[ImageObject]] with embedded text to be 'satire or parody content': An image that was"
     "created as political or humorous commentary and is presented in that context. (Reshares"
     "of satire/parody content that do not include relevant context are more likely to fall"
     "under the “missing context” rating.) For an [[AudioObject]] to be 'satire or parody"
     "content': Audio that was created as political or humorous commentary and is presented"
     "in that context. (Reshares of satire/parody content that do not include relevant context"
     "are more likely to fall under the “missing context” rating.)

    See https://schema.org/SatireOrParodyContent.

    """

    locals().update({"@type": Field("SatireOrParodyContent", const=True)})


SatireOrParodyContent.update_forward_refs()
