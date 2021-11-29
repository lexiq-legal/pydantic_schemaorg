from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.SoftwareApplication import SoftwareApplication


class MobileApplication(SoftwareApplication):
    """A software application designed specifically to work well on a mobile device such as"
     "a telephone.

    See https://schema.org/MobileApplication.

    """

    carrierRequirements: Optional[Union[List[str], str]] = Field(
        None,
        description="Specifies specific carrier(s) requirements for the application (e.g. an application"
     "may only work on a specific carrier network).",
    )
    locals().update({"@type": Field("MobileApplication", const=True)})


MobileApplication.update_forward_refs()
