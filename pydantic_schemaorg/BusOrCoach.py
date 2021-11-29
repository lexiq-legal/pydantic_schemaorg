from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
from pydantic_schemaorg.Vehicle import Vehicle


class BusOrCoach(Vehicle):
    """A bus (also omnibus or autobus) is a road vehicle designed to carry passengers. Coaches"
     "are luxury busses, usually in service for long distance travel.

    See https://schema.org/BusOrCoach.

    """

    acrissCode: Optional[Union[List[str], str]] = Field(
        None,
        description="The ACRISS Car Classification Code is a code used by many car rental companies, for classifying"
     "vehicles. ACRISS stands for Association of Car Rental Industry Systems and Standards.",
    )
    roofLoad: Optional[Union[List[QuantitativeValue], QuantitativeValue]] = Field(
        None,
        description="The permitted total weight of cargo and installations (e.g. a roof rack) on top of the"
     "vehicle. Typical unit code(s): KGM for kilogram, LBR for pound * Note 1: You can indicate"
     "additional information in the [[name]] of the [[QuantitativeValue]] node. * Note 2:"
     "You may also link to a [[QualitativeValue]] node that provides additional information"
     "using [[valueReference]] * Note 3: Note that you can use [[minValue]] and [[maxValue]]"
     "to indicate ranges.",
    )
    locals().update({"@type": Field("BusOrCoach", const=True)})


BusOrCoach.update_forward_refs()
