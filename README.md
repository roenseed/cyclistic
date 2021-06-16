# **Case Study: How does a bike-share company navigate speedy success?**

![people_riding_a_bike](./images/bike.jpg)
*Image: Getty Images/iStock*

## Scenario 

You are a junior data analyst working in the marketing analyst team at Cyclistic, a bike-share company in Chicago. The director of
marketing believes the company’s future success depends on maximizing the number of annual memberships. Therefore, your
team wants to understand how casual riders and annual members use Cyclistic bikes differently. From these insights, your team
will design a new marketing strategy to convert casual riders into annual members. But first, Cyclistic executives must approve
your recommendations, so they must be backed up with compelling data insights and professional data visualizations.

## About Cyclistic 

In 2016, Cyclistic launched a successful bike-sharing offering. Since then, the program has grown to a fleet of **5,824** bicycles that are geotracked and locked into a network of **692** stations across Chicago. The bikes can be unloacked from one station and returned to any other station in the system anytime. 

Until now, Cyclistic’s marketing strategy relied on building general awareness and appealing to broad consumer segments. One approach that helped make these things possible was the flexibility of its pricing plans: single-ride passes, full-day passes, and annual memberships. Customers who purchase single-ride or full-day passes are referred to as casual riders. Customers who purchase annual memberships are Cyclistic members.

## The Stakeholders 

> 1. **Lily Moreno:** The director of marketing and my manager. Moreno is responsible for the development of campaigns and initiatives to promote the bike-share program. 
> 2. **Cyclistic marketing analytics team:** A team of data analysts who are responsible for collecting, analyzing, and reporting data that helps guide Cyclistic marketing strategy. 
> 3. **Cyclistic executive team:** A notoriously detail-oriented team which will decide whether to approve the recommended marketing program.

## The Business Task

The goal of this case study is to provide clear insights for designing marketing strategies aimed at converting casual riders into annual members. Towards this goal, I asked the following questions:

> 1. How do annual members and casual riders use Cyclistic bikes differently?
> 2. Why would casual riders buy Cyclistic annual memberships?
> 3. How can Cyclistic use digital media to influence casual riders to become members? 

## Preparing the Data 

This case study uses Cyclistic's historical trip data (previous 12 months) to analyze and identify trends. The data has been made available by Motivate International Inc. under and open license. The data can be dowloaded [here.](https://divvy-tripdata.s3.amazonaws.com/index.html)

This data is reliable, original, comprehensive and current as it is internally collected and stored safely by Cyclistic from June 2020 to May 2021. Personally identifiable information  such as credit card numbers has been removed because of data-privacy issues.

The data is organized in tabular format and has 13 columns and 4073561 rows. The **member_casual** column will allow me to group, aggregate and compare trends between casual riders and member riders. 

## Processing the Data from Dirty to Clean
