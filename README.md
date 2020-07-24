# shardBackup

shardBackup is a Python util for backing up large amounts of files onto some number of other mounted storage. e.g. backing up 12 TB of files onto 4 2 TB, 1 1 TB and 6 500 GB external drives

This isn't necessarily a superior to a tar solution, however this will provide you with totally usable drives on a given filesystem with no intermediary steps. No need to untar.

Also there will be a hash stored next to every file of the given backup file- optionally off, but default on.

## Installation

TBD

## Usage

```bash
shardbackup [sourcedir] [targetdir] --index [param]
```

## Contributing

Not looking for any assistance or pulls at the moment

## License

BSD 3-Clause is in the repo