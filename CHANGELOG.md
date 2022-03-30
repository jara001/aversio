# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/).

## Unreleased
## 0.2.0 - 2022-03-30
### Added
- Unit tests.
- `get_git_version()` to obtain current git version.
- `fix_version(ver, stored)` to modify current version according to the last used.
- `maintain_version(ver, filename)` to load/save versions and fix them along the way.

### Fixed
- Properly work with X.Y versions.

## 0.1.0 - 2022-03-30
### Added
- Initial version of `aversio`, compatible with `_version`.
