from pydantic import Field
from pydantic_schemaorg.MeasurementTypeEnumeration import MeasurementTypeEnumeration


class WearableMeasurementTypeEnumeration(MeasurementTypeEnumeration):
    """Enumerates common types of measurement for wearables products.

    See https://schema.org/WearableMeasurementTypeEnumeration.

    """

    locals().update({"@type": Field("WearableMeasurementTypeEnumeration", const=True)})


WearableMeasurementTypeEnumeration.update_forward_refs()
