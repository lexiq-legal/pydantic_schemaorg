from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.TradeAction import TradeAction


class RentAction(TradeAction):
    """The act of giving money in return for temporary use, but not ownership, of an object such"
     "as a vehicle or property. For example, an agent rents a property from a landlord in exchange"
     "for a periodic payment.

    See: https://schema.org/RentAction
    Model depth: 4
    """
    type_: str = Field("RentAction", alias='@type')
    landlord: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        None,
        description="A sub property of participant. The owner of the real estate property.",
    )
    realEstateAgent: Optional[Union[List[Union['RealEstateAgent', str]], 'RealEstateAgent', str]] = Field(
        None,
        description="A sub property of participant. The real estate agent involved in the action.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.RealEstateAgent import RealEstateAgent
