"""
password_generator.py

Generates cryptographically secure random passwords.
Uses `secrets` (not `random`) because it's designed for security-sensitive use —
`random` is predictable and unsuitable for generating credentials.

Usage:
    python3 password_generator.py
    python3 password_generator.py --length 20 --count 5
"""

import argparse
import secrets
import string


def generate_password(length: int = 16, use_symbols: bool = True) -> str:
    """Generate a single secure random password of the given length."""
    alphabet = string.ascii_letters + string.digits
    if use_symbols:
        alphabet += "!@#$%^&*()-_=+"

    if length < 8:
        raise ValueError("Password length should be at least 8 characters.")

    return "".join(secrets.choice(alphabet) for _ in range(length))


def main():
    parser = argparse.ArgumentParser(description="Generate secure random passwords.")
    parser.add_argument("--length", type=int, default=16, help="Password length (default: 16)")
    parser.add_argument("--count", type=int, default=1, help="Number of passwords to generate")
    parser.add_argument("--no-symbols", action="store_true", help="Exclude special characters")
    args = parser.parse_args()

    for _ in range(args.count):
        pwd = generate_password(length=args.length, use_symbols=not args.no_symbols)
        print(pwd)


if __name__ == "__main__":
    main()
