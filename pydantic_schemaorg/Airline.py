from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.Organization import Organization


class Airline(Organization):
    """An organization that provides flights for passengers.

    See: https://schema.org/Airline
    Model depth: 3
    """
    type_: str = Field("Airline", alias='@type')
    boardingPolicy: Optional[Union[List[Union['BoardingPolicyType', str]], 'BoardingPolicyType', str]] = Field(
        None,
        description="The type of boarding policy used by the airline (e.g. zone-based or group-based).",
    )
    iataCode: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="IATA identifier for an airline or airport.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.BoardingPolicyType import BoardingPolicyType
    from pydantic_schemaorg.Text import Text
