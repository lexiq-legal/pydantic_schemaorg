from pydantic import Field
from pydantic_schemaorg.WearableMeasurementTypeEnumeration import WearableMeasurementTypeEnumeration


class WearableMeasurementSleeve(WearableMeasurementTypeEnumeration):
    """Measurement of the sleeve length, for example of a shirt

    See https://schema.org/WearableMeasurementSleeve.

    """

    locals().update({"@type": Field("WearableMeasurementSleeve", const=True)})


WearableMeasurementSleeve.update_forward_refs()
