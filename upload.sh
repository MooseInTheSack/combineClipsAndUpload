#!/usr/bin/env bash

source config.sh
python3 main.py --file="$fileName" --title="$title" --description="$description" --keywords="$keywords" --category="$category" --privacyStatus="$privacyStatus"
