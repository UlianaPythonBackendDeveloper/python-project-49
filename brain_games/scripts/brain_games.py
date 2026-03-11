#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from cli import welcome_user

def main():
    welcome_user()

if __name__ == '__main__':
    main()
