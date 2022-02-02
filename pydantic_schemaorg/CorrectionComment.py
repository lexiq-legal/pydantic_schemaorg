from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Comment import Comment


class CorrectionComment(Comment):
    """A [[comment]] that corrects [[CreativeWork]].

    See: https://schema.org/CorrectionComment
    Model depth: 4
    """
    type_: str = Field("CorrectionComment", alias='@type')
    

