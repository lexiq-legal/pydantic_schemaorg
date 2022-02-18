PACKAGE_NAME = "pydantic_schemaorg"

# schema.org data types to pydantic https://schema.org/DataType
data_type_map = {
    "Boolean": ("StrictBool", "pydantic", "StrictBool"),
    "False": ("Literal[False]", "typing", "Literal"),
    "True": ("Literal[True]", "typing", "Literal"),
    "Date": ("date", f"datetime", "date"),
    "DateTime": ("datetime", f"datetime", "datetime"),
    "Time": ("time", "datetime", "time"),
    "Number": ("StrictInt, StrictFloat", "pydantic", "StrictInt, StrictFloat"),
    "Float": ("float", "", ""),
    "Integer": ("int", "", ""),
    "Text": ("str", "", ""),
    "CssSelectorType": ("str", "", ""),
    "PronounceableText": ("str", "", ""),
    "URL": ("AnyUrl", "pydantic", "AnyUrl"),
    "XPathType": ("str", "", ""),
}

data_type_specificity = {
    "Boolean": 1,
    "False": 1,
    "True": 1,
    "Date": 4,
    "DateTime": 5,
    "Time": 4,
    "Number": 3,
    "Float": 4,
    "Integer": 5,
    "Text": 1,
    "CssSelectorType": 1,
    "PronounceableText": 1,
    "URL": 2,
    "XPathType": 1,
}
