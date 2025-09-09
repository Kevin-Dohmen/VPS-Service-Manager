import re

def formatValidFolderName(input: str) -> str:
    invalidCharsRegex = r'[^a-zA-Z0-9._-]'
    formatted = re.sub(invalidCharsRegex, '_', input)
    return formatted

def formatValidDockerName(input: str) -> str:
    input = input.lower()
    invalidCharsRegex = r'[^a-z0-9_-]'
    formatted = re.sub(invalidCharsRegex, '_', input)
    return formatted
