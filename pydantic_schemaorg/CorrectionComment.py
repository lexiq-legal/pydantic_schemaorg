from pydantic import Field
from pydantic_schemaorg.Comment import Comment


class CorrectionComment(Comment):
    """A [[comment]] that corrects [[CreativeWork]].

    See https://schema.org/CorrectionComment.

    """
    type_: str = Field("CorrectionComment", const=True, alias='@type')
    

CorrectionComment.update_forward_refs()
