from pydantic import Field
from pydantic_schemaorg.WearableMeasurementTypeEnumeration import WearableMeasurementTypeEnumeration


class WearableMeasurementBack(WearableMeasurementTypeEnumeration):
    """Measurement of the back section, for example of a jacket

    See https://schema.org/WearableMeasurementBack.

    """

    locals().update({"@type": Field("WearableMeasurementBack", const=True)})


WearableMeasurementBack.update_forward_refs()
