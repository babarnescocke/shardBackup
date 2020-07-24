# shardbackup

shardbackup is a Python util for backing up large amounts of files onto some number of other mounted storage. e.g. backing up 12 TB of files onto 4 2 TB, 1 1 TB and 6 500 GB mounted filesystems. My use case is large server and backing up to external drives that are connected only for backup.

This isn't superior to a Tar solution, however; this will provide you with totally usable drives on a given filesystem with no intermediary steps, no need to untar.

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