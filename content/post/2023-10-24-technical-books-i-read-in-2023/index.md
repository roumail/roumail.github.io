---
title: "Technical books I read in 2023"
summary:
  "Explore my discussion of a curated list of books delving into python,
  software engineering and software architecture."
categories: ["musings", "technology"]
type: book
tags:
  [
    "books",
    "python",
    "data-engineering",
    "machine-learning",
    "pytorch",
    "scikit-learn",
  ]
authors:
  - admin
url: "/technical-read-list-2023/"
date: 2023-10-24T09:11:37+02:00
draft: true
gallery_item:
  - album: "technical-list-2023"
    image: "python.jpeg"
    caption: "Python Object Oriented Programming"
  - album: "technical-list-2023"
    image: "data-intensive.jpeg"
    caption: "Designing Data-Intensive Applications"
  - album: "technical-list-2023"
    image: "ml-systems.jpg"
    caption: "Designing Machine Learning Systems"
  - album: "technical-list-2023"
    image: "pytorch.jpg"
    caption: "Machine Learning with PyTorch and Scikit-Learn"
---

## Books overview

{{< gallery album="technical-list-2023" resize_options="250x250" >}}

## Leverage Object oriented programming patterns in my code

I started my journey with programming using `R` during my Masters in Statistics.
Now the purists might tell you that `R` is only a scripting or statistical
modelling language but there are a number of different use cases where using R
is very natural. Moreover, with `tidyverse` and a big push over the past few
years towards adding software best practices to `R` by giants like Rstudio, I'm
not sure that argument holds as much weight. There are github organizations like
[r-lib](https://github.com/r-lib) which provide a comprehensive set of tools
that conform to best practices and are very reliable in terms of performance,
documentation and interface.

Since functions are first class citizens in `R`, meaning everything in `R` is a
function, even when I started working with Python, my habit of working with
functions remained intact. Moreover, when using R, I had developed a habit of
making an R package, almost immediately - as soon as I had more than a couple of
functions.

This habit carried over into my python development as well and it's something I
enjoy doing because it really helps having your package dependencies clearly
defined and having your codebase, already in a form that's easy to extend and
add tests to.

However, functions are not first class citizens in `Python`. In fact, everything
in Python is an object and the functional interfaces available to use in
`Python`, let's say something like `len` are actually translated into its object
oriented interface by `Python` under the hood. There's an interesting discussion
on this topic [here](https://lucumr.pocoo.org/2011/7/9/python-and-pola/) for
those who are more interested in this.

Moroever, Object oriented programming (OOP) when used appropriately, helps to
follow software engineering principles such as
[SOLID](https://en.wikipedia.org/wiki/SOLID),
[DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) and
[KISS](https://en.wikipedia.org/wiki/KISS_principle). In the fast few years I
had certain codebases that became big enough that packaging it wasn't enough
anymore. I found that I couldn't embed readability and self-documenting
functions anymore. Having been programming in Python for 5+ years, I wasn't
completely unaware of OOP's usage. However, I now had a use case where it made a
lot more sense to use. Coming from a non-traditional background when it comes to
software development, I thought I'd pick up a book that would give me the
foundations I felt I was lacking. In comes
[Python Object Oriented Programming](https://www.amazon.com/Python-Object-Oriented-Programming-maintainable-object-oriented-ebook/dp/B07JG9BQZC/ref=sr_1_1?crid=195YD6YSF5GE&keywords=Python+Object+Oriented+Programming+dusty&qid=1698135293&s=digital-text&sprefix=python+object+oriented+programming+dusty%2Cdigital-text%2C137&sr=1-1).

Reading this book was quite a treat and I took my sweet time going through it.
Taking the ideas of
[Inheritance](<https://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming)>),
[Composition](https://en.wikipedia.org/wiki/Object_composition) and
[Polymorphism](<https://en.wikipedia.org/wiki/Polymorphism_(computer_science)>).

## Distributed systems, event-driven architecture and asynchronous programming

2023 has been a productive year as far as reading books is concerned. The most
crucial ingredient in achieving this was

## Comments from the books below

Technical Topics

-

[Designing Data-Intensive Applications](https://www.amazon.de/-/en/Designing-Data-Intensive-Applications-Reliable-Maintainable/dp/1449373321/ref=sr_1_1?crid=3FJXGHQ63JL2S&keywords=designing+data-intensive+applications+by+martin+kleppmann&qid=1697911731&sprefix=designing+data%2Caps%2C74&sr=8-1)

## What I'm currently reading

Add current reading
