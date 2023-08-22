# IUCN Integrations

Established in 1964, The International Union for Conservation of Nature’s Red List of Threatened Species has evolved to become the world’s most comprehensive information source on the global conservation status of animal, fungi and plant species.

The IUCN Red List is a critical indicator of the health of the world’s biodiversity. Far more than a list of species and their status, it is a powerful tool to inform and catalyze action for biodiversity conservation and policy change, critical to protecting the natural resources we need to survive. It provides information about range, population size, habitat and ecology, use and/or trade, threats, and conservation actions that will help inform necessary conservation decisions.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The IUCN Red List is used by government agencies, wildlife departments, conservation-related non-governmental organisations (NGOs), natural resource planners, educational organisations, students, and the business community. The Red List process has become a massive enterprise involving the IUCN Global Species Program staff, partner organisations and experts in the IUCN Species Survival Commission and partner networks who compile the species information to make The IUCN Red List the indispensable product it is today.

## Features

This package gives you an up to date version of what currently exist on IUCN platform.

## Getting Started

Provide instructions on how to set up and run your project locally. Include prerequisites, installation steps, and any configuration needed.

### Basic information

The Red List API has been recently upgraded to offer more methods for querying the Red List data. Please make sure to use the correct methods for what you need.

The IUCN Red List version is 2022-2.

You will also need a token (https://apiv3.iucnredlist.org/api/v3/token) before being able to use the API. 


## General information

The use of this API is strictly under the Terms of Use of the IUCN Red List of Threatened Species (http://www.iucnredlist.org/info/terms-of-use).

It is advisable wherever possible to use the taxon name (species name) to make your API calls, rather than using IDs. IDs are not immovable are expected to be used mainly by organisations that work closely with the IUCN Red List.

This API now supports querying regional assessments in addition to global assessments. This can achieved by appending a region_identifier parameter to the desired endpoint. Please see specific documentation for further details.

```bash
python requires=">=3.6"
```

## Installation

Use these commands to install the project:

```bash
    pip install IUCN-API
```


## Usage

### Groups


```bash
from IUCN_API.modules.Groups import Groups

```


### Citations

```bash
from IUCN_API.modules.Citations import Citations

```

Conservation

```bash
from IUCN_API.modules.Conservation import Conservation

```


General

```bash
from IUCN_API.modules.General import General

```


Growth Form

```bash
from IUCN_API.modules.GrowthForm import GrowthForm

```


Habitats

```bash
from IUCN_API.modules.Habitats import Habitats

```


History

```bash
from IUCN_API.modules.History import History

```


Narratives

```bash
from IUCN_API.modules.Narratives import Narratives

```


Occurrence

```bash
from IUCN_API.modules.Occurrence import Occurrence

```


Threats

```bash
from IUCN_API.modules.Threats import Threats

```

View

```bash
from IUCN_API.modules.View import View

```


Weblinks

```bash
from IUCN_API.modules.Weblinks import Weblinks

```