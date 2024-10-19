# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Fixed

- Add documentation for website entrypoints.

## [1.2.0] - 2024-10-15

### Fixed

- Removed poetry from dependencies for building and releasing the package.
- Consolidate the bumping of versions to better leverage `bump2version`.
- `bump_version.py` script is now renamed `release.py`.
- Removed `toml` as a dev dependency.

### Fixed

- Add back series in the `_index.md` when creating a new series and and remove
  the self-reference at the template level in hugo

## [1.0.6] - 2024-08-02

### Changed

- Use `typer` for handling the entrypoints.

## [1.0.5] - 2024-08-02

### Changed

- Add `bumpversion` for managing changelog and version bumping.

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
