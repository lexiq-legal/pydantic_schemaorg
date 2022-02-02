from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic import AnyUrl
from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class SoftwareApplication(CreativeWork):
    """A software application.

    See: https://schema.org/SoftwareApplication
    Model depth: 3
    """
    type_: str = Field("SoftwareApplication", alias='@type')
    applicationSubCategory: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        None,
        description="Subcategory of the application, e.g. 'Arcade Game'.",
    )
    processorRequirements: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Processor architecture required to run the application (e.g. IA64).",
    )
    installUrl: Optional[Union[List[Union[AnyUrl, 'URL', str]], AnyUrl, 'URL', str]] = Field(
        None,
        description="URL at which the app may be installed, if different from the URL of the item.",
    )
    screenshot: Optional[Union[List[Union[AnyUrl, 'URL', 'ImageObject', str]], AnyUrl, 'URL', 'ImageObject', str]] = Field(
        None,
        description="A link to a screenshot image of the app.",
    )
    device: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Device required to run the application. Used in cases where a specific make/model is"
     "required to run the application.",
    )
    operatingSystem: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Operating systems supported (Windows 7, OSX 10.6, Android 1.6).",
    )
    softwareAddOn: Optional[Union[List[Union['SoftwareApplication', str]], 'SoftwareApplication', str]] = Field(
        None,
        description="Additional content for a software application.",
    )
    applicationSuite: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The name of the application suite to which the application belongs (e.g. Excel belongs"
     "to Office).",
    )
    storageRequirements: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        None,
        description="Storage requirements (free space required).",
    )
    availableOnDevice: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Device required to run the application. Used in cases where a specific make/model is"
     "required to run the application.",
    )
    softwareRequirements: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        None,
        description="Component dependency requirements for application. This includes runtime environments"
     "and shared libraries that are not included in the application distribution package,"
     "but required to run the application (Examples: DirectX, Java or .NET runtime).",
    )
    softwareHelp: Optional[Union[List[Union['CreativeWork', str]], 'CreativeWork', str]] = Field(
        None,
        description="Software application help.",
    )
    softwareVersion: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Version of the software instance.",
    )
    permissions: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Permission(s) required to run the app (for example, a mobile app may require full internet"
     "access or may run only on wifi).",
    )
    fileSize: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Size of the application / package (e.g. 18MB). In the absence of a unit (MB, KB etc.), KB"
     "will be assumed.",
    )
    releaseNotes: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        None,
        description="Description of what changed in this version.",
    )
    downloadUrl: Optional[Union[List[Union[AnyUrl, 'URL', str]], AnyUrl, 'URL', str]] = Field(
        None,
        description="If the file can be downloaded, URL to download the binary.",
    )
    requirements: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        None,
        description="Component dependency requirements for application. This includes runtime environments"
     "and shared libraries that are not included in the application distribution package,"
     "but required to run the application (Examples: DirectX, Java or .NET runtime).",
    )
    supportingData: Optional[Union[List[Union['DataFeed', str]], 'DataFeed', str]] = Field(
        None,
        description="Supporting data for a SoftwareApplication.",
    )
    countriesNotSupported: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Countries for which the application is not supported. You can also provide the two-letter"
     "ISO 3166-1 alpha-2 country code.",
    )
    featureList: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        None,
        description="Features or modules provided by this application (and possibly required by other applications).",
    )
    applicationCategory: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        None,
        description="Type of software application, e.g. 'Game, Multimedia'.",
    )
    memoryRequirements: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        None,
        description="Minimum memory requirements.",
    )
    countriesSupported: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Countries for which the application is supported. You can also provide the two-letter"
     "ISO 3166-1 alpha-2 country code.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.ImageObject import ImageObject
    from pydantic_schemaorg.CreativeWork import CreativeWork
    from pydantic_schemaorg.DataFeed import DataFeed
