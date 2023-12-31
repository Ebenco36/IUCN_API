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

Use these command below to install the project:

```bash
pip install IUCN-API
```


## Usage

### Groups


```bash
from IUCN_API.modules.Groups import Groups

```

Group Methods you can access 

```bash
group = Groups()
group.get_species_group_list()
group.get_species_by_group_name(group_name)

```


### Citations

```bash
from IUCN_API.modules.Citations import Citations

```

Citation Methods you can access 

```bash
citation = Citations()
citation.get_species_citation_by_name(species_name="loxodonta africana")
citation.get_species_citation_region_by_name(region_identifier="europe", species_name="loxodonta africana")
citation.get_species_citation_by_id(species_id="299929")
citation.get_species_citation_region_by_id(region_identifier="europe", species_id="9929292")

```

### Conservation

```bash
from IUCN_API.modules.Conservation import Conservation

```

Conservation Methods you can access 

```bash
conservation = Conservation()
conservation.get_species_conservation_measure_by_name(species_name)
conservation.get_species_conservation_measure_by_name_by_region(species_name, region_identifier)
conservation.get_species_conservation_measure_by_id(species_id)
conservation.get_species_conservation_measure_by_id_by_region(species_id, region_identifier)

```


### General

```bash
from IUCN_API.modules.General import General

```

General Methods you can access 

```bash
general = General()
general.get_version()
general.get_countries()
general.get_regions()
general.get_species_by_country(country)
general.get_species(page=1, per_page=10)
general.get_species_region(region_identifier="europe", page=1, per_page=10)
general.get_species_count()
general.get_species_count_by_region(region_identifier="europe")
general.get_species_synonyms_by_name(species_name)
general.get_species_common_name_by_name(species_name)
general.get_species_by_category(category)

```


Growth Form

```bash
from IUCN_API.modules.GrowthForm import GrowthForm

```

GrowthForm Methods you can access 

```bash
growth_form = GrowthForm()
growth_form.get_species_growth_forms_by_name(species_name)
growth_form.get_species_growth_forms_by_name_by_region(species_name, region_identifier)
growth_form.get_species_growth_forms_by_id(species_id)
growth_form.get_species_growth_forms_by_id_by_region(species_id, region_identifier)

```



### Habitats

```bash
from IUCN_API.modules.Habitats import Habitats

```
Habitats Methods you can access 

```bash
habitats = Habitats()
habitats.get_species_habitat_by_name(species_name)
habitats.get_species_habitat_by_name_by_region(species_name, region_identifier)
habitats.get_species_habitat_by_id(species_id)
habitats.get_species_habitat_by_id_by_region(species_id, region_identifier)

```


### History

```bash
from IUCN_API.modules.History import History

```
History Methods you can access 

```bash
history = History()
history.get_species_history_by_name(species_name)
history.get_species_history_by_name_by_region(species_name, region_identifier)
history.get_species_history_by_id(species_id)
history.get_species_history_by_id_by_region(species_id, region_identifier)

```

### Narratives

```bash
from IUCN_API.modules.Narratives import Narratives

```
Narratives Methods you can access 

```bash
narratives = Narratives()
narratives.get_species_narrative_by_name(species_name)
narratives.get_species_narrative_by_name_by_region(species_name, region_identifier="europe")
narratives.get_species_narrative_by_id(species_id)
narratives.get_species_narrative_by_id_by_region(species_id, region_identifier="europe")

```


### Occurrence

```bash
from IUCN_API.modules.Occurrence import Occurrence

```
Occurrence Methods you can access 

```bash
occurrence = Occurrence()
occurrence.get_species_country_occurence_by_name(species_name)
occurrence.get_species_country_occurence_by_name_by_region(species_name, region_identifier)
occurrence.get_species_country_occurence_by_id(species_id)
occurrence.get_species_country_occurence_by_id_by_region(species_id, region_identifier)

```


### Threats

```bash
from IUCN_API.modules.Threats import Threats

```

Threats Methods you can access 

```bash
threats = Threats()
threats.get_species_threats_by_name(species_name)
threats.get_species_threats_by_name_by_region(species_name, region_identifier):
threats.get_species_threats_by_id(species_id)
threats.get_species_threats_by_id_by_region(species_id, region_identifier)

```

### View

```bash
from IUCN_API.modules.View import View

```
View Methods you can access 

```bash
view = View()
view.get_species_single_by_name(species_name)
view.get_species_single_by_name_by_region(species_name, region_identifier="europe")
view.get_species_single_by_id(species_id)
view.get_species_single_by_id_by_region(species_id, region_identifier="europe")

```


### Weblinks

```bash
from IUCN_API.modules.Weblinks import Weblinks

```

Weblinks Methods you can access 

```bash
weblinks = Weblinks()
weblinks.get_red_list_website_link_name(species_name:str="")
weblinks.get_red_list_website_redirect_name(species_name:str="")
weblinks.get_red_list_website_link_id(taxon_id:int="")
weblinks.get_red_list_website_redirect_id(taxon_id:int="", region_identifier:str="")

```