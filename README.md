# Bible Search
Are you a developer who can't open biblegateway.com or bible.com fast enough in bible study?
Well, look no further! This small executable searches the bible for a particular scripture. 

## Usage
To run the project in locally (in project), run
```shell
python3 bible.py John 1:1-3
```
If the file is added to path, simply run
```shell
bible John 1:1-3
```
### Commands
```shell
bible [ref]
```
`$ref` must be in one of the following forms:
- [book]
- [book] [chapter]
- [book] [chapter] : [verse]
- [book] [chapter] : [verseStart] - [verseEnd]

Currently, the project does not support cross-chapter queries.

## Installation
### Windows
Clone this repository and copy `bible.exe`. Or, download the `bible.exe` file directly
from GitHub. 

### Other OSs
If your platform specific file isn't found below, clone this repository, install the requirements,
and run `./build.sh` (in a shell that supports bash scripts).
A `bible.exe` should appear in your root directory. This is the final platform-specific executable.

### Adding to PATH
Now, move this file to your bin, add to path, etc. to use this from anywhere on your machine!
