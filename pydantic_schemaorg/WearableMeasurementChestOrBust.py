from pydantic import Field
from pydantic_schemaorg.WearableMeasurementTypeEnumeration import WearableMeasurementTypeEnumeration


class WearableMeasurementChestOrBust(WearableMeasurementTypeEnumeration):
    """Measurement of the chest/bust section, for example of a suit

    See https://schema.org/WearableMeasurementChestOrBust.

    """

    locals().update({"@type": Field("WearableMeasurementChestOrBust", const=True)})


WearableMeasurementChestOrBust.update_forward_refs()
