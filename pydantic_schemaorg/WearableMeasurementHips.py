from pydantic import Field
from pydantic_schemaorg.WearableMeasurementTypeEnumeration import WearableMeasurementTypeEnumeration


class WearableMeasurementHips(WearableMeasurementTypeEnumeration):
    """Measurement of the hip section, for example of a skirt

    See https://schema.org/WearableMeasurementHips.

    """

    locals().update({"@type": Field("WearableMeasurementHips", const=True)})


WearableMeasurementHips.update_forward_refs()
