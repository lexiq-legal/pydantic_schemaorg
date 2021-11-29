from pydantic import Field, AnyUrl
from typing import Any, Union, List, Optional
from pydantic_schemaorg.CreativeWork import CreativeWork


class SoftwareApplication(CreativeWork):
    """A software application.

    See https://schema.org/SoftwareApplication.

    """

    applicationSubCategory: Optional[Union[List[Union[AnyUrl, str]], Union[AnyUrl, str]]] = Field(
        None,
        description="Subcategory of the application, e.g. 'Arcade Game'.",
    )
    processorRequirements: Optional[Union[List[str], str]] = Field(
        None,
        description="Processor architecture required to run the application (e.g. IA64).",
    )
    installUrl: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None,
        description="URL at which the app may be installed, if different from the URL of the item.",
    )
    screenshot: Union[List[Union[AnyUrl, Any]], Union[AnyUrl, Any]] = Field(
        None,
        description="A link to a screenshot image of the app.",
    )
    device: Optional[Union[List[str], str]] = Field(
        None,
        description="Device required to run the application. Used in cases where a specific make/model is"
     "required to run the application.",
    )
    operatingSystem: Optional[Union[List[str], str]] = Field(
        None,
        description="Operating systems supported (Windows 7, OSX 10.6, Android 1.6).",
    )
    softwareAddOn: Any = Field(
        None,
        description="Additional content for a software application.",
    )
    applicationSuite: Optional[Union[List[str], str]] = Field(
        None,
        description="The name of the application suite to which the application belongs (e.g. Excel belongs"
     "to Office).",
    )
    storageRequirements: Optional[Union[List[Union[AnyUrl, str]], Union[AnyUrl, str]]] = Field(
        None,
        description="Storage requirements (free space required).",
    )
    availableOnDevice: Optional[Union[List[str], str]] = Field(
        None,
        description="Device required to run the application. Used in cases where a specific make/model is"
     "required to run the application.",
    )
    softwareRequirements: Optional[Union[List[Union[AnyUrl, str]], Union[AnyUrl, str]]] = Field(
        None,
        description="Component dependency requirements for application. This includes runtime environments"
     "and shared libraries that are not included in the application distribution package,"
     "but required to run the application (Examples: DirectX, Java or .NET runtime).",
    )
    softwareHelp: Optional[Union[List[CreativeWork], CreativeWork]] = Field(
        None,
        description="Software application help.",
    )
    softwareVersion: Optional[Union[List[str], str]] = Field(
        None,
        description="Version of the software instance.",
    )
    permissions: Optional[Union[List[str], str]] = Field(
        None,
        description="Permission(s) required to run the app (for example, a mobile app may require full internet"
     "access or may run only on wifi).",
    )
    fileSize: Optional[Union[List[str], str]] = Field(
        None,
        description="Size of the application / package (e.g. 18MB). In the absence of a unit (MB, KB etc.), KB"
     "will be assumed.",
    )
    releaseNotes: Optional[Union[List[Union[AnyUrl, str]], Union[AnyUrl, str]]] = Field(
        None,
        description="Description of what changed in this version.",
    )
    downloadUrl: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None,
        description="If the file can be downloaded, URL to download the binary.",
    )
    requirements: Optional[Union[List[Union[AnyUrl, str]], Union[AnyUrl, str]]] = Field(
        None,
        description="Component dependency requirements for application. This includes runtime environments"
     "and shared libraries that are not included in the application distribution package,"
     "but required to run the application (Examples: DirectX, Java or .NET runtime).",
    )
    supportingData: Any = Field(
        None,
        description="Supporting data for a SoftwareApplication.",
    )
    countriesNotSupported: Optional[Union[List[str], str]] = Field(
        None,
        description="Countries for which the application is not supported. You can also provide the two-letter"
     "ISO 3166-1 alpha-2 country code.",
    )
    featureList: Optional[Union[List[Union[AnyUrl, str]], Union[AnyUrl, str]]] = Field(
        None,
        description="Features or modules provided by this application (and possibly required by other applications).",
    )
    applicationCategory: Optional[Union[List[Union[AnyUrl, str]], Union[AnyUrl, str]]] = Field(
        None,
        description="Type of software application, e.g. 'Game, Multimedia'.",
    )
    memoryRequirements: Optional[Union[List[Union[AnyUrl, str]], Union[AnyUrl, str]]] = Field(
        None,
        description="Minimum memory requirements.",
    )
    countriesSupported: Optional[Union[List[str], str]] = Field(
        None,
        description="Countries for which the application is supported. You can also provide the two-letter"
     "ISO 3166-1 alpha-2 country code.",
    )
    locals().update({"@type": Field("SoftwareApplication", const=True)})


SoftwareApplication.update_forward_refs()
