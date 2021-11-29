from pydantic import Field
from pydantic_schemaorg.WearableMeasurementTypeEnumeration import WearableMeasurementTypeEnumeration


class WearableMeasurementWidth(WearableMeasurementTypeEnumeration):
    """Measurement of the width, for example of shoes

    See https://schema.org/WearableMeasurementWidth.

    """

    locals().update({"@type": Field("WearableMeasurementWidth", const=True)})


WearableMeasurementWidth.update_forward_refs()
