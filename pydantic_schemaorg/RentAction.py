from pydantic import Field
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.Person import Person
from typing import Any, Union, List, Optional
from pydantic_schemaorg.RealEstateAgent import RealEstateAgent
from pydantic_schemaorg.TradeAction import TradeAction


class RentAction(TradeAction):
    """The act of giving money in return for temporary use, but not ownership, of an object such"
     "as a vehicle or property. For example, an agent rents a property from a landlord in exchange"
     "for a periodic payment.

    See https://schema.org/RentAction.

    """

    landlord: Optional[Union[List[Union[Organization, Person]], Union[Organization, Person]]] = Field(
        None,
        description="A sub property of participant. The owner of the real estate property.",
    )
    realEstateAgent: Optional[Union[List[RealEstateAgent], RealEstateAgent]] = Field(
        None,
        description="A sub property of participant. The real estate agent involved in the action.",
    )
    locals().update({"@type": Field("RentAction", const=True)})


RentAction.update_forward_refs()
