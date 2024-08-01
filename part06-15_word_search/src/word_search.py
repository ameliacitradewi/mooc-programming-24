# Write your solution here
import re

def find_words(search_term: str) -> list:
  # Read the words from the file
  with open("words.txt") as file:
      words = [line.strip() for line in file]

  # Check for the presence of wildcard characters
  if '*' in search_term:
      if search_term.startswith('*'):
          # Search for words ending with the term (excluding the asterisk)
          term = search_term[1:]
          return [word for word in words if word.endswith(term)]
      elif search_term.endswith('*'):
          # Search for words starting with the term (excluding the asterisk)
          term = search_term[:-1]
          return [word for word in words if word.startswith(term)]
  elif '.' in search_term:
      # Convert the search term to a regular expression
      regex = re.compile(search_term)
      return [word for word in words if regex.fullmatch(word)]
  else:
      # Exact match
      return [word for word in words if word == search_term]

  return []
