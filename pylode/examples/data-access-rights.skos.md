# Data Access Rights
### A taxonomy

Markdown documentation created by [pyLODE](http://github.com/rdflib/pyLODE)

## Metadata
* **IRI**
  * `http://linked.data.gov.au/def/data-access-rights`
* **Publisher(s)**
  * Geological Survey of Queensland
* **Creators(s)**
  * Geological Survey of Queensland
* **Created**
  * 2019-04-03
* **Modified**
  * 2019-09-10
* **Source**
  * [access_rights:](http://vocabularies.coar-repositories.org/documentation/access_rights/)
* **Ontology RDF**
  * <a href="data-access-rights.ttl">RDF (turtle)</a>
### Description
<p>Data access rights control how users and systems access a data resource.</p>

**History Note**  
This vocabulary is taken from the COAR Controlled Vocabularies Interest Group (http://vocabularies.coar-repositories.org/documentation/access_rights/) but is redelivered as that vocabulary isn't well presented online.

## Table of Contents
1. [Collections](#collections)
1. [Object Concepts](#concepts)
1. [Namespaces](#namespaces)
1. [Legend](#legend)


## Overview

**Figure 1:** Ontology overview
## Collections
* [Closed data access rights](#closeddataaccessrights)
* [Open data access rights](#opendataaccessrights)
### Closed data access rights
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/data-access-rights/closed-access-rights`
Preferred Labels |Closed data access rights (en)<br />
Members |[Restricted access](restrictedaccess)<sup class="sup-cp" title="concept">cp</sup><br />[Metadata only access](metadataonlyaccess)<sup class="sup-cp" title="concept">cp</sup><br />[Embargoed access](embargoedaccess)<sup class="sup-cp" title="concept">cp</sup><br />[Protected access](protectedaccess)<sup class="sup-cp" title="concept">cp</sup><br />

### Open data access rights
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/data-access-rights/open-access-rights`
Preferred Labels |Open data access rights (en)<br />
Members |[Open access](openaccess)<sup class="sup-cp" title="concept">cp</sup><br />

## Classes
* [Open access](http://linked.data.gov.au/def/data-access-rights/open)
* [Restricted access](http://linked.data.gov.au/def/data-access-rights/restricted)
	* [Embargoed access](http://linked.data.gov.au/def/data-access-rights/embargoed)
	* [Metadata only access](http://linked.data.gov.au/def/data-access-rights/metadata-only)
	* [Protected access](http://linked.data.gov.au/def/data-access-rights/protected)

### Embargoed access
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/data-access-rights/embargoed`
Preferred Labels |Embargoed access (en)<br />
Broader Concepts |[Restricted access](restrictedaccess)<sup class="sup-cp" title="concept">cp</sup><br />
### Metadata only access
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/data-access-rights/metadata-only`
Preferred Labels |Metadata only access (en)<br />
Broader Concepts |[Restricted access](restrictedaccess)<sup class="sup-cp" title="concept">cp</sup><br />
### Open access
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/data-access-rights/open`
Preferred Labels |Open access (en)<br />
Alternate Labels |Open file<br />
### Protected access
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/data-access-rights/protected`
Preferred Labels |Protected access (en)<br />
Broader Concepts |[Restricted access](restrictedaccess)<sup class="sup-cp" title="concept">cp</sup><br />
### Restricted access
Property | Value
--- | ---
IRI | `http://linked.data.gov.au/def/data-access-rights/restricted`
Preferred Labels |Restricted access (en)<br />
Narrower Concepts |[Embargoed access](embargoedaccess)<sup class="sup-cp" title="concept">cp</sup><br />[Metadata only access](metadataonlyaccess)<sup class="sup-cp" title="concept">cp</sup><br />[Protected access](protectedaccess)<sup class="sup-cp" title="concept">cp</sup><br />

## Namespaces
* **default (:)**
  * `http://linked.data.gov.au/def/data-access-rights/`
* **access_rights**
  * `http://vocabularies.coar-repositories.org/documentation/access_rights/`
* **da**
  * `http://linked.data.gov.au/def/data-access-rights/`
* **dc**
  * `http://purl.org/dc/elements/1.1/`
* **dct**
  * `http://purl.org/dc/terms/`
* **def**
  * `http://linked.data.gov.au/def/`
* **org**
  * `http://linked.data.gov.au/org/`
* **owl**
  * `http://www.w3.org/2002/07/owl#`
* **rdf**
  * `http://www.w3.org/1999/02/22-rdf-syntax-ns#`
* **rdfs**
  * `http://www.w3.org/2000/01/rdf-schema#`
* **sdo**
  * `https://schema.org/`
* **skos**
  * `http://www.w3.org/2004/02/skos/core#`
* **xml**
  * `http://www.w3.org/XML/1998/namespace`
* **xsd**
  * `http://www.w3.org/2001/XMLSchema#`

## Legend
* Collections: cl
* Concepts: cp