from pydantic import Field
from pydantic_schema_org.Person import Person
from pydantic_schema_org.Organization import Organization
from typing import Any, Optional, Union, List
from pydantic_schema_org.RealEstateAgent import RealEstateAgent
from pydantic_schema_org.TradeAction import TradeAction


class RentAction(TradeAction):
    """The act of giving money in return for temporary use, but not ownership, of an object such"
     "as a vehicle or property. For example, an agent rents a property from a landlord in exchange"
     "for a periodic payment.

    See https://schema.org/RentAction.

    """

    landlord: Optional[Union[List[Union[Person, Organization]], Union[Person, Organization]]] = Field(
        None,
        description="A sub property of participant. The owner of the real estate property.",
    )
    realEstateAgent: Optional[Union[List[RealEstateAgent], RealEstateAgent]] = Field(
        None,
        description="A sub property of participant. The real estate agent involved in the action.",
    )
    locals().update({"@type": Field("RentAction", const=True)})


RentAction.update_forward_refs()
