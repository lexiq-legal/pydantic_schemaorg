from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.ScholarlyArticle import ScholarlyArticle


class MedicalScholarlyArticle(ScholarlyArticle):
    """A scholarly article in the medical domain.

    See: https://schema.org/MedicalScholarlyArticle
    Model depth: 5
    """
    type_: str = Field(default="MedicalScholarlyArticle", alias='@type', const=True)
    publicationType: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The type of the medical article, taken from the US NLM MeSH publication type catalog."
     "See also [MeSH documentation](http://www.nlm.nih.gov/mesh/pubtypes.html).",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
