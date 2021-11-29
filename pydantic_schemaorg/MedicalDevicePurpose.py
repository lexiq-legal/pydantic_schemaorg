from pydantic import Field
from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration


class MedicalDevicePurpose(MedicalEnumeration):
    """Categories of medical devices, organized by the purpose or intended use of the device.

    See https://schema.org/MedicalDevicePurpose.

    """

    locals().update({"@type": Field("MedicalDevicePurpose", const=True)})


MedicalDevicePurpose.update_forward_refs()
