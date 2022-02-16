# pydantic_schemaorg
[![PyPi version](https://img.shields.io/pypi/v/pydantic-schemaorg.svg)](https://pypi.python.org/pypi/pydantic-schemaorg/) [![](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/) ![t](https://img.shields.io/badge/status-stable-green.svg) [![](https://img.shields.io/github/license/lexiq-legal/pydantic_schemaorg.svg)](https://github.com/lexq-legal/pydantic_schemaorg/blob/master/LICENSE.md)

Use [Schema.org](https://schema.org) types in [pydantic](https://pydantic-docs.helpmanual.io/)! <br> <br>
**Pydantic_schemaorg** contains all the models defined by schema.org. The pydantic classes are auto-generated from the
schema.org model definitions that can be found
on [https://schema.org/version/latest/schemaorg-current-https.jsonld](https://schema.org/version/latest/schemaorg-current-https.jsonld)

## Requirements

Works with python >= 3.8

## How to install

```pip install pydantic-schemaorg```<br><br>
Import any class you want to use by with the following convention<br>
```from pydantic_schemaorg.<SCHEMAORG_MODEL_NAME> import <SCHEMAORG_MODEL_NAME>```<br><br>

A full (hierarchical) list of Schema.org model names can be found [here](https://schema.org/docs/full.html)

## Example usages

```
from pydantic_schemaorg.ScholarlyArticle import ScholarlyArticle

scholarly_article = ScholarlyArticle(url='https://github.com/lexiq-legal/pydantic_schemaorg',
                                    sameAs='https://github.com/lexiq-legal/pydantic_schemaorg',
                                    copyrightNotice='Free to use under the MIT license',
                                    dateCreated='15-12-2021')
print(scholarly_article.json())
```

```
{"@type": "ScholarlyArticle", "url": "https://github.com/lexiq-legal/pydantic_schemaorg", "sameAs": "https://github.com/lexiq-legal/pydantic_schemaorg", "copyrightNotice": "Free to use under the MIT license", "dateCreated": "15-12-2021"}
```