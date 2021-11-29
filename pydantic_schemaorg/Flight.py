from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.Person import Person
from pydantic_schemaorg.Duration import Duration
from pydantic_schemaorg.Vehicle import Vehicle
from datetime import datetime
from pydantic_schemaorg.Airport import Airport
from pydantic_schemaorg.Trip import Trip


class Flight(Trip):
    """An airline flight.

    See https://schema.org/Flight.

    """

    boardingPolicy: Any = Field(
        None,
        description="The type of boarding policy used by the airline (e.g. zone-based or group-based).",
    )
    flightDistance: Union[List[Union[str, Any]], Union[str, Any]] = Field(
        None,
        description="The distance of the flight.",
    )
    departureGate: Optional[Union[List[str], str]] = Field(
        None,
        description="Identifier of the flight's departure gate.",
    )
    flightNumber: Optional[Union[List[str], str]] = Field(
        None,
        description="The unique identifier for a flight including the airline IATA code. For example, if describing"
     "United flight 110, where the IATA code for United is 'UA', the flightNumber is 'UA110'.",
    )
    seller: Optional[Union[List[Union[Organization, Person]], Union[Organization, Person]]] = Field(
        None,
        description="An entity which offers (sells / leases / lends / loans) the services / goods. A seller may"
     "also be a provider.",
    )
    estimatedFlightDuration: Optional[Union[List[Union[str, Duration]], Union[str, Duration]]] = Field(
        None,
        description="The estimated time the flight will take.",
    )
    aircraft: Optional[Union[List[Union[str, Vehicle]], Union[str, Vehicle]]] = Field(
        None,
        description="The kind of aircraft (e.g., \"Boeing 747\").",
    )
    carrier: Optional[Union[List[Organization], Organization]] = Field(
        None,
        description="'carrier' is an out-dated term indicating the 'provider' for parcel delivery and flights.",
    )
    arrivalTerminal: Optional[Union[List[str], str]] = Field(
        None,
        description="Identifier of the flight's arrival terminal.",
    )
    webCheckinTime: Optional[Union[List[datetime], datetime]] = Field(
        None,
        description="The time when a passenger can check into the flight online.",
    )
    departureTerminal: Optional[Union[List[str], str]] = Field(
        None,
        description="Identifier of the flight's departure terminal.",
    )
    departureAirport: Optional[Union[List[Airport], Airport]] = Field(
        None,
        description="The airport where the flight originates.",
    )
    mealService: Optional[Union[List[str], str]] = Field(
        None,
        description="Description of the meals that will be provided or available for purchase.",
    )
    arrivalGate: Optional[Union[List[str], str]] = Field(
        None,
        description="Identifier of the flight's arrival gate.",
    )
    arrivalAirport: Optional[Union[List[Airport], Airport]] = Field(
        None,
        description="The airport where the flight terminates.",
    )
    locals().update({"@type": Field("Flight", const=True)})


Flight.update_forward_refs()
