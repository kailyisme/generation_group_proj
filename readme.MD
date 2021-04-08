# Infinity Cafes Project
##### A final group project from Generation/Infinity Works bootcamp of Jan - Mar 2021
## Project Overview
An ETL Pipeline and Data Analytics for Business Intelligence

Technologies used:
* Amazon Web Services (AWS)
  * S3
  * Lambda
  * CloudFormation
  * CloudWatch
  * Redshift
  * EC2
  * VPC
  * IAM
* Python
* PostgreSQL
* Grafana
* GitHub Actions (CI/CD)
* Docker

## Problem Overview
### Current Situation
* Decentralised data
* No access to live data (Head Office)
  * Data uploaded only once a month
* No access to data but your own (as a franchisee)
* Manual upload of data
  * CSV format
  * No data processing/load into a standard database
* No data analysis
  * Nor available for analysis after upload

#### This leads to not know:
* Who are the customers
* What products sell
* What products to market
* Which franchise is selling what
  * and What's not selling too
### Solution Proposed with this Tool

* Sanitised data for PII (Personal Identifiable Information)
* Formatted data to a single standard
* Loaded data into a single database/data warehouse
  * Shared between all company stakeholders
    * Franchises and
    * Head Office
* Used algorithms to analyse data to look for:
  * Trends
  * Outliers
  * Successes
  * Failures
  * And pipeline usage itself
