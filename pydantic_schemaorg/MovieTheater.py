from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic import StrictInt, StrictFloat
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.EntertainmentBusiness import EntertainmentBusiness
from pydantic_schemaorg.CivicStructure import CivicStructure


class MovieTheater(EntertainmentBusiness, CivicStructure):
    """A movie theater.

    See: https://schema.org/MovieTheater
    Model depth: 4
    """
    type_: str = Field(default="MovieTheater", alias='@type', const=True)
    screenCount: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', str]], StrictInt, StrictFloat, 'Number', str]] = Field(
        default=None,
        description="The number of screens in the movie theater.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Number import Number
