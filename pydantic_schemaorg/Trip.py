from pydantic import Field
from pydantic_schemaorg.Demand import Demand
from pydantic_schemaorg.Offer import Offer
from typing import List, Optional, Union
from datetime import datetime, time
from pydantic_schemaorg.ItemList import ItemList
from pydantic_schemaorg.Place import Place
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.Person import Person
from pydantic_schemaorg.Intangible import Intangible


class Trip(Intangible):
    """A trip or journey. An itinerary of visits to one or more places.

    See https://schema.org/Trip.

    """
    type_: str = Field("Trip", const=True, alias='@type')
    offers: Optional[Union[List[Union[Demand, Offer, str]], Union[Demand, Offer, str]]] = Field(
        None,
        description="An offer to provide this item&#x2014;for example, an offer to sell a product, rent the"
     "DVD of a movie, perform a service, or give away tickets to an event. Use [[businessFunction]]"
     "to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can"
     "also be used to describe a [[Demand]]. While this property is listed as expected on a number"
     "of common types, it can be used in others. In that case, using a second type, such as Product"
     "or a subtype of Product, can clarify the nature of the offer.",
    )
    departureTime: Optional[Union[List[Union[datetime, time, str]], Union[datetime, time, str]]] = Field(
        None,
        description="The expected departure time.",
    )
    itinerary: Optional[Union[List[Union[ItemList, Place, str]], Union[ItemList, Place, str]]] = Field(
        None,
        description="Destination(s) ( [[Place]] ) that make up a trip. For a trip where destination order is"
     "important use [[ItemList]] to specify that order (see examples).",
    )
    subTrip: Optional[Union[List[Union['Trip', str]], Union['Trip', str]]] = Field(
        None,
        description="Identifies a [[Trip]] that is a subTrip of this Trip. For example Day 1, Day 2, etc. of a"
     "multi-day trip.",
    )
    arrivalTime: Optional[Union[List[Union[datetime, time, str]], Union[datetime, time, str]]] = Field(
        None,
        description="The expected arrival time.",
    )
    provider: Optional[Union[List[Union[Organization, Person, str]], Union[Organization, Person, str]]] = Field(
        None,
        description="The service provider, service operator, or service performer; the goods producer."
     "Another party (a seller) may offer those services or goods on behalf of the provider."
     "A provider may also serve as the seller.",
    )
    partOfTrip: Optional[Union[List[Union['Trip', str]], Union['Trip', str]]] = Field(
        None,
        description="Identifies that this [[Trip]] is a subTrip of another Trip. For example Day 1, Day 2, etc."
     "of a multi-day trip.",
    )
    

Trip.update_forward_refs()
