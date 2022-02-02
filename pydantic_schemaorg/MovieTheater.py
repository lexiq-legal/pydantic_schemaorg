from __future__ import annotations
from typing import TYPE_CHECKING

from decimal import Decimal
from typing import Union, List, Optional


from pydantic import Field
from pydantic_schemaorg.EntertainmentBusiness import EntertainmentBusiness
from pydantic_schemaorg.CivicStructure import CivicStructure


class MovieTheater(EntertainmentBusiness, CivicStructure):
    """A movie theater.

    See: https://schema.org/MovieTheater
    Model depth: 4
    """
    type_: str = Field("MovieTheater", alias='@type')
    screenCount: Optional[Union[List[Union[Decimal, 'Number', str]], Decimal, 'Number', str]] = Field(
        None,
        description="The number of screens in the movie theater.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Number import Number
