from pydantic import Field
from typing import Any, Optional, Union, List
from pydantic_schemaorg.CreativeWork import CreativeWork


class Thesis(CreativeWork):
    """A thesis or dissertation document submitted in support of candidature for an academic"
     "degree or professional qualification.

    See https://schema.org/Thesis.

    """
    type_: str = Field("Thesis", const=True, alias='@type')
    inSupportOf: Optional[Union[List[str], str]] = Field(
        None,
        description="Qualification, candidature, degree, application that Thesis supports.",
    )
    

Thesis.update_forward_refs()
