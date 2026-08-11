# Security Automation Scripts

## Objective
Write Python scripts to automate two common security tasks: generating secure passwords and
parsing authentication logs to spot brute-force patterns — the kind of scripting a SOC analyst
uses to speed up repetitive parts of the job.

## Scripts

### `password_generator.py`
Generates cryptographically secure random passwords using Python's `secrets` module
(not `random`, which is predictable and unsafe for anything security-related).

```bash
python3 password_generator.py --length 20 --count 5
```

### `log_parser.py`
Parses a Linux-style `auth.log` file, counts failed login attempts per source IP and per
targeted username, and flags IPs that cross a suspicious-activity threshold — a simplified
version of brute-force detection.

```bash
python3 log_parser.py sample_auth.log --threshold 3
```

**Sample output** (using the included `sample_auth.log`):
```
Total failed login attempts: 10

Top source IPs by failed attempts:
  203.0.113.45        6 attempts  <-- SUSPICIOUS
  192.0.2.77          3 attempts  <-- SUSPICIOUS
  198.51.100.22       1 attempts

Top targeted usernames:
  root                4 attempts
  admin               2 attempts
  test                2 attempts
  siyabonga           1 attempts
  oracle              1 attempts
```

## Skills Gained
- Python scripting for security-relevant tasks
- Regex for log parsing
- Using `secrets` over `random` for cryptographic operations
- Basic brute-force detection logic (counting + thresholding)

## Next Steps
- Point `log_parser.py` at real logs generated from your own home lab (e.g. after an SSH
  brute-force attempt against your own Kali → target VM setup)
- Extend the threshold logic to also flag rapid attempts within a short time window, not just
  raw counts
