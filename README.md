# shardBackup

shardBackup is a python util for backing up large amounts of files/data onto some number of other mounted storage. e.g. backing up 12 TB of files onto 4 2 TB, 1 1 TB and 6 500 GB external drives

This isn't necessarily superior to a tar solution, however this will provide you with totally usable drives on a given filesystem with no intermediary steps. No need to untar.

Also there will be a hash stored next to every file of the given backup file- optionally off, but default on.

## Installation

TBD

## Usage

from the cli

shardbackup [src] [target] --index [param]

## Contributing

Not looking for any assistance or pulls at the moment

## License

BSD 3-Clause is in the repo