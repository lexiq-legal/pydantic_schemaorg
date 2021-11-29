from pydantic import Field
from typing import Any, Optional, Union, List
from pydantic_schema_org.ScholarlyArticle import ScholarlyArticle


class MedicalScholarlyArticle(ScholarlyArticle):
    """A scholarly article in the medical domain.

    See https://schema.org/MedicalScholarlyArticle.

    """

    publicationType: Optional[Union[List[str], str]] = Field(
        None,
        description="The type of the medical article, taken from the US NLM MeSH publication type catalog."
     "See also [MeSH documentation](http://www.nlm.nih.gov/mesh/pubtypes.html).",
    )
    locals().update({"@type": Field("MedicalScholarlyArticle", const=True)})


MedicalScholarlyArticle.update_forward_refs()
