from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class MeasurementTypeEnumeration(Enumeration):
    """Enumeration of common measurement types (or dimensions), for example \"chest\" for"
     "a person, \"inseam\" for pants, \"gauge\" for screws, or \"wheel\" for bicycles.

    See https://schema.org/MeasurementTypeEnumeration.

    """

    locals().update({"@type": Field("MeasurementTypeEnumeration", const=True)})


MeasurementTypeEnumeration.update_forward_refs()
