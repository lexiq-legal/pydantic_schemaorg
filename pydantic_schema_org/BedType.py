from pydantic import Field
from pydantic_schema_org.QualitativeValue import QualitativeValue


class BedType(QualitativeValue):
    """A type of bed. This is used for indicating the bed or beds available in an accommodation.

    See https://schema.org/BedType.

    """

    locals().update({"@type": Field("BedType", const=True)})


BedType.update_forward_refs()
