from pydantic import Field
from pydantic_schema_org.HealthAspectEnumeration import HealthAspectEnumeration


class UsageOrScheduleHealthAspect(HealthAspectEnumeration):
    """Content about how, when, frequency and dosage of a topic.

    See https://schema.org/UsageOrScheduleHealthAspect.

    """

    locals().update({"@type": Field("UsageOrScheduleHealthAspect", const=True)})


UsageOrScheduleHealthAspect.update_forward_refs()
