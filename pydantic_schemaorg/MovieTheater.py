from pydantic import Field
from decimal import Decimal
from typing import List, Optional, Union
from pydantic_schemaorg.EntertainmentBusiness import EntertainmentBusiness
from pydantic_schemaorg.CivicStructure import CivicStructure


class MovieTheater(EntertainmentBusiness, CivicStructure):
    """A movie theater.

    See https://schema.org/MovieTheater.

    """
    type_: str = Field("MovieTheater", const=True, alias='@type')
    screenCount: Optional[Union[List[Union[Decimal, str]], Union[Decimal, str]]] = Field(
        None,
        description="The number of screens in the movie theater.",
    )
    

MovieTheater.update_forward_refs()
