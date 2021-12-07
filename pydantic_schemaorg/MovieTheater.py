from pydantic import Field
from decimal import Decimal
from typing import Any, Optional, Union, List
from pydantic_schemaorg.CivicStructure import CivicStructure
from pydantic_schemaorg.EntertainmentBusiness import EntertainmentBusiness


class MovieTheater(CivicStructure, EntertainmentBusiness):
    """A movie theater.

    See https://schema.org/MovieTheater.

    """
    type_: str = Field("MovieTheater", const=True, alias='@type')
    screenCount: Optional[Union[List[Decimal], Decimal]] = Field(
        None,
        description="The number of screens in the movie theater.",
    )
    

MovieTheater.update_forward_refs()
