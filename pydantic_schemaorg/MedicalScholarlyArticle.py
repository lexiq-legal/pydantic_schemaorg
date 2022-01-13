from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional, Any

from pydantic_schemaorg.ScholarlyArticle import ScholarlyArticle


class MedicalScholarlyArticle(ScholarlyArticle):
    """A scholarly article in the medical domain.

    See: https://schema.org/MedicalScholarlyArticle
    Model depth: 5
    """

    type_: str = Field("MedicalScholarlyArticle", const=True, alias="@type")
    publicationType: "Optional[Union[List[str], str]]" = Field(
        None,
        description="The type of the medical article, taken from the US NLM MeSH publication type catalog."
        "See also [MeSH documentation](http://www.nlm.nih.gov/mesh/pubtypes.html).",
    )


if TYPE_CHECKING:

    MedicalScholarlyArticle.update_forward_refs()
