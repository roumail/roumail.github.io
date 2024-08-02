# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.4] - 2024-08-02

### Changed

- `_index.md` for a series directory now no longer contains the `series` front
  matter. This helps avoid having the series listing contain a link to the
  series listing itself.

### Removed

- Version retrieval now doesn't use toml package

## [1.0.3] - 2024-03-17

### Removed

- retrieving body of changelog using internal function. Defer to function
  keepachangelog
