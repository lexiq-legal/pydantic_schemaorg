from pydantic import Field
from pydantic_schemaorg.WearableMeasurementTypeEnumeration import WearableMeasurementTypeEnumeration


class WearableMeasurementLength(WearableMeasurementTypeEnumeration):
    """Represents the length, for example of a dress

    See https://schema.org/WearableMeasurementLength.

    """

    locals().update({"@type": Field("WearableMeasurementLength", const=True)})


WearableMeasurementLength.update_forward_refs()
