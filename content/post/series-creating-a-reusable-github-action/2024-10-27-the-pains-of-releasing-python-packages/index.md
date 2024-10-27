---
title:
  "The Pains of Releasing Python Packages, Version and Changelog Management"
summary: "Introducing the series on creating a reusable github actions workflow"
categories: ["technology"]
series: ["Creating a reusable github action"]
tags: ["python", "changelog", "github-actions", "release-management"]
authors:
  - admin
# url: "/descriptive-and-keyword-rich-url/"
date: 2024-10-27T16:03:02+01:00
lastmod: 2024-10-27T16:03:02+01:00
draft: true
toc: false
---

What I plan to call this github action

AutoRelease

Motivation for AutoRelease

I've found my workflow for maintaining python packages and their release process
to be cumbersome and errorprone. My current process might often leave me in a
partial state, where one or more aspects of the release don’t align—whether due
to missing changelog entries, versioning issues, or initiating the release even
when tests have failed. This often necessitates manual intervention or
corrections that are custom to each type of failure.

I want an automated process to handle the steps for every release, so I don’t
need to manually configure each project. I don't want to think about this
process altogether and clutter each project with custom configs, scripts and
dependencies. The main challenges I see include:

- Ensuring that versioning and changelog updates follow strict, repeatable
  conventions.
- Preventing releases if there’s an incomplete changelog or if tests have
  failed.
- Keeping each release atomic, so failures in any part of the process won’t
  leave the project in a broken state.

Steps in the Ideal Release Process - outside scope of python entrypoint

1. Add Conditional steps prior to running release process - Failing early in
   case of issue:
   1. Testing and Validation: Provide users the ability to verify that all CI
      checks (tests, linting, etc.) have passed before starting the release
      pipeline.
   2. Changelog Verification: Ensure a proper changelog entry in the
      [Unreleased] section, documenting changes according to the Keep a
      Changelog format. Errors in this section (malformed entries etc).
2. Determine Version bump based on Semantic Versioning: Follow semantic
   versioning conventions and use Changelog categories such as Changed, Fixed,
   and Added to determine if we have a major, minor, or patch update.
3. Atomic Version Bumping, Tagging and Commiting:
   1. Make a commit based on the following steps
      1. Bump the version, updating the pyproject.toml and CHANGELOG.md with the
         latest version
      2. Tag Availability Verification: Check if the new tag is already present
         in the repository’s tags and releases. This prevents issues caused by a
         partial release where a tag exists but the release failed. If the tag
         already exists, the process will exit early, and no changes are made.
      3. Move the changelog entry from [Unreleased] section to the one under the
         new release and retrieve release notes for the latest change from the
         changelog for use later.
   2. Tag the commit and push to remote. If any part of this fails, the process
      should exit and reset to prevent a partial release.
4. Post commit actions
   1. Automated Documentation in Release Notes: Pull the latest changelog entry
      into the release notes, so every release includes up-to-date
      documentation.
   2. Build and Release: Prepare the package build and release it by optionally
      specifying additional steps that must succeed, ensuring a reliable and
      repeatable process.

Alternative solutions

While I was previously using bump2version which mentioned in it's Alternatives
documentation, tbump and their offer of pre-post commit hooks. This was an
important advantage since I was looking to incorporate more than just tagging,
committing and version bumping. I wanted some level of checks done on the
changelog and the git tags to prevent a partial state.

Why building a Reusable GitHub Action

There are a few advantages of using this workflow as a github action rather than
as a library that we add to our package. The most important point is that I
don't want additional dependencies and configuration from being added to my
project. However, having a github action perform this atomic process does pose
some challenges for testing.

Challenges posed by testing a Github Action

Since the action would be making commits and pushes to remote, we'd need a
remote git repository. However, to allow testing the github action locally, we
want to simulate a remote environment but isolate the tests from modifying the
repository persistently wherever possible. Therefore, we will let the following
principles guide us:

Take local testing as far as possible for testing the core logic Performing all
tests on a real remote repository incurs setup time to perform perform cleanup
actions. Certain testing scenarios necessitate having the gh cli and a repo. For
example:

- Test that the action isn't triggered when a prior step has failed locally.
- A feature branch isn't merged into main when it contains errors (missing
  changelog entry etc).
- ...

Locally, we can test that a given state of the repo, will raise an exception in
the python entrypoint. The integration test will check the behaviour of the
action when the system under test fails, vs when it doesn't.

To simulate a remote git repo for certain cases, we can look into the option of
a bare repository to act as remote. This way we can point a local repository to
this bare repository as a remote and when tbump pushes to remote, the changes
will go to this local repository instead of to github for example.

Use the python entrypoint via a docker container even locally We will be using
act cli to simulate the CI environment and enable a fully containerized local
setup. This is an important step because users will mostly be interacting with
the action in a CI environment and therefore, it's important that we simulate
this environment as closely as possible.
