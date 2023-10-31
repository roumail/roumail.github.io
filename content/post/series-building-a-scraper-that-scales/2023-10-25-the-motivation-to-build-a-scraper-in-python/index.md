---
title: "Part I: The Motivation to Build a Scraper in Python"
summary:
  "Explore the journey of building a robust web scraper for analyzing Belgium's
  property market. Learn how we transitioned from Selenium to Beautiful Soup for
  efficiency, used Poetry and Typer for better dependency management, amongst
  other tools. This blog is part one of a series aimed at creating a scalable
  data collection and analysis tool"
categories: ["technology"]
tags: ["python", "web-scraping"]
series: ["Building a Scraper that scales"]
authors:
  - admin
url: "/a-scraper-that-scales-part-i/"
date: 2023-10-24T16:14:00+02:00
draft: false
---

{{< toc >}}

## Motivation

Remember that period when most parts of the world were in a lockdown due to
COVID? Yes, we're nearing the end of 2023 and COVID seems like a distant memory
at this point. However, like I imagine many of us, I suddenly found that being
restricted in movement and social interaction to a large extent, I had a lot
more time at my disposal. This was also a time where my wife and I realised that
we could have more space for ourselves so each of us could have an office setup
we could be happy with. This also being a time of low interest rates to
encourage consumption in the economy, it was an especially interesting property
market.

This seemed as good a time as any to write a scraper for Belgium's most popular
property listings website: [immoweb](https://immoweb.be). My desire for this
first version was to first, be able to have a very general idea of the Brussels
property market. Thereafter, I would launch this script every few days to look
at the new properties. The output of this script would be a CSV that I'd use to
spot good deals and have all the relevant information I'd need to schedule
visits.

## Implementing the Proof of concept

I was running this script from a windows machine at the time and having done a
scraping project once before already, knew that I'd start with `selenium` for
the browser automation and parsing of the html. The setup required that I choose
a browser and a corresponding geckodriver (with the appropriate version for your
browser) to go along with it. I've used firefox and edge browsers (and their
respective drivers) for different iterations of the scraper implementation.

After messing around with developer tools, looking into the dom's containing the
information I was looking for using `inspect`, I had a script that was doing the
job. I made a conda export of the environment I used for the scraping in case I
ever needed to revisit this work again. This script did the job and I was quite
happy leaving it at that with an environment export so I could pick up from this
analysis when needed. This version of the script can be found
[here](https://github.com/roumail/immoweb-scraper/tree/second_run) for those who
are interested.

## A sidenote on Bayesian statistics

For the longest time I've been a fan of Bayesian statistics. Being able to
explicitly encode your modelling assumptions in the form of priors, as well as
being very deliberate in reconstructing the data generating process of the
phenomenon you're modelling. You can visually verify how well your model is
generalizing by doing what is called a
[posterior predictive check](https://en.wikipedia.org/wiki/Posterior_predictive_distribution).
The computational aspects of MCMC sampling also appeals to the nerd in me, while
the convergence of your sampler gives indications about how well-informed a
hypothesis you have for your data generating process. An ill-formulated model
will simply not converge, unlike a number of other approaches which would always
give a solution and then you're left to figure out if you're overfitting or
underfitting. Then there is the fact that you are always able to work with
distributions of your phenomenon of interest rather than relying solely on point
estimates like we would in most other methods. There's a number of fascinating
things that are possible with these posterior distributions, which include
bayesian decision making. I will link to a great discussion on the subject by
Thomas Wiecki on the subject
[here](https://twiecki.io/blog/2019/01/14/supply_chain/) where we can see how to
use our models to directly show the impact of uncertainy on real business
metrics rather than arcane statistical metrics such as `mean squared error`,
`f1 score` and the like which don't hold any real business meaning.

Naturally, I have my bias for these methods and using these models bring their
own challenges. In some cases, traditional machine learning approaches would
give better performance without sacrificing interpretability and help you reach
a conclusion faster than using these bespoke modelling approaches. Nonetheless,
I was on the lookout for an opportunity to find a dataset where I could exploit
the natural hierarchical structure of data in a
[hierarchical modelling](https://en.wikipedia.org/wiki/Bayesian_hierarchical_modeling)
or the flexiblity of Gaussian process modelling to capture the intricaties of
non-linear processes. The
[link](https://www.pymc.io/projects/examples/en/latest/gaussian_processes/GP-smoothing.html)
shows the distinction between modelling the same problem as a regression vs
using a gaussian process smoothing model.

## Revisiting the implementation once again

Any data scientist or machine learning practitioner will tell you about their
struggles with data. It's either data quality (or lack thereof) or just the lack
of data itself for performing interesting analyses. Then it suddenly occurred to
me: property data is perfect for the experiments I wanted to conduct.

Scraping property prices over time gives the opportunity to model property
prices over time and ask interesting questions, including, but not limited to
the following:

- Are rental property prices growing at the same rate as purchase properties?
- Do we observe a similar growth rate across different communes?
- Are properties in the same commune priced similarly and if so, how much does
  this vary by commune?
- What are the most important determinants of price?

A dataset of this nature contains elements of time series analysis since
property prices evolve over time. There is also a natural structure in the data
that can be exploited since we can indeed expect properties within communes to
be similarly priced. This would be a place where we can use Gaussian process
modelling to capture the underlying trends and fluctuations in property prices
within each commune. We can use property proximity to model the inherent spatial
relationships between properties, assuming that properties closer to each other
are more likely to have similar prices!

By revisiting my initial scraper implementation with this newfound focus, I am
not just enhancing a tool; I am building a robust data collection pipeline that
will serve as the backbone for these sophisticated analytical experiments.

## Areas of improvement

With a clear goal in mind, I identified several key areas to refine the
scraper's implementation. These improvements were aimed at making the scraper
more efficient, easier to manage, and more robust for data collection and
analysis.

### 1. Efficiency in Data Scraping

Switch to Beautiful Soup: I wanted to transition from
[Selenium](https://pypi.org/project/selenium/) to
[Beautiful Soup](https://pypi.org/project/beautifulsoup4/) for parsing raw HTML.
This change ought to significantly reduced the time needed to scrape data.

Parametrization of Postal Codes: Allowing postal codes as an input parameter to
make the scraper more flexible. I was initially only looking into a few communes
in Brussels that I was interested in. However, if I wanted to do some
interesting analyses, I also wanted to consider communes neighboring Brussels.

### 2. Dependency Management

Use of Poetry: To manage the project's dependencies more effectively, I wanted
to convert the script into a Python package and used [Poetry]() for managing the
dependencies. This streamlines the installation process and allows me to manage
the package versions in a systematic version. This would be especially useful as
we dockerize the analysis in the future and build a CI/CD pipeline.

Implementation of Typer: I used [Typer](https://pypi.org/project/typer/) to
create a command-line interface from the main application entrypoint. I've
effectively transitioned to using this instead of
[`click`](https://pypi.org/project/click/) recently.

### 3. Code Refactoring for Readability and Maintainability

Object-Oriented Approach: I wanted to refactor the code to use Python classes
instead of just functions where appropriate. By using meaningful class names,
the code can become self-documenting and easier to maintain and extend in the
long run.

### 5. Data Storage and Validation

SQLite Database: I wanted to use a SQLite database with an initial schema to
store the data I'd be accumulating over time. I've really enjoyed working with
[`SQLAlchemy`](https://pypi.org/project/SQLAlchemy/) as the ORM mapper to
interact with the database.

Data Validation with Pydantic: Before adding the scraped data to the database, I
implemented validation checks using
[Pydantic](https://pypi.org/project/pydantic/). This ensured that only
high-quality, accurate data was stored.

By focusing on these areas, I aimed to build a scraper that was not just a
one-off script but a robust data collection tool capable of supporting more
complex analyses and experiments.

## Final comments

In the next blog [post](/a-scraper-that-scales-part-ii/) in the series, I will
go over the implementation details. For those interested, you can find the
current state of the project
[here](https://github.com/roumail/immoweb-scraper/tree/v1.0.0).
