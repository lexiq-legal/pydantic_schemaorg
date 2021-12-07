from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class MeasurementTypeEnumeration(Enumeration):
    """Enumeration of common measurement types (or dimensions), for example \"chest\" for"
     "a person, \"inseam\" for pants, \"gauge\" for screws, or \"wheel\" for bicycles.

    See https://schema.org/MeasurementTypeEnumeration.

    """
    type_: str = Field("MeasurementTypeEnumeration", const=True, alias='@type')
    

MeasurementTypeEnumeration.update_forward_refs()
