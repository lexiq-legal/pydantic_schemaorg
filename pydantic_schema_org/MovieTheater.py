from pydantic import Field
from decimal import Decimal
from typing import Any, Optional, Union, List
from pydantic_schema_org.EntertainmentBusiness import EntertainmentBusiness
from pydantic_schema_org.CivicStructure import CivicStructure


class MovieTheater(EntertainmentBusiness, CivicStructure):
    """A movie theater.

    See https://schema.org/MovieTheater.

    """

    screenCount: Optional[Union[List[Decimal], Decimal]] = Field(
        None,
        description="The number of screens in the movie theater.",
    )
    locals().update({"@type": Field("MovieTheater", const=True)})


MovieTheater.update_forward_refs()
