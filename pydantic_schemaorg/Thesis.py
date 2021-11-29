from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.CreativeWork import CreativeWork


class Thesis(CreativeWork):
    """A thesis or dissertation document submitted in support of candidature for an academic"
     "degree or professional qualification.

    See https://schema.org/Thesis.

    """

    inSupportOf: Optional[Union[List[str], str]] = Field(
        None,
        description="Qualification, candidature, degree, application that Thesis supports.",
    )
    locals().update({"@type": Field("Thesis", const=True)})


Thesis.update_forward_refs()
