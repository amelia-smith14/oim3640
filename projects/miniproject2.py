"""
Modest Proposal Old English Modernizer
Analyzes "A Modest Proposal" and replaces Old English words with modern equivalents
"""

import re
from collections import Counter

# Dictionary of Old English/Archaic words and their modern replacements
OLD_TO_MODERN = {
    'cabbin-doors': 'cabin doors',
    'importuning': 'begging',
    'alms': 'charity',
    'stroling': 'strolling',
    'sustenance': 'food',
    'dropt': 'dropped',
    'dam': 'mother',
    'solar': 'entire',
    'shillings': 'coins',
    'raiment': 'clothing',
    'expence': 'expense',
    'reckoned': 'calculated',
    'breeders': 'mothers',
    'hitherto': 'previously',
    'publick': 'public',
    'prodigious': 'enormous',
    'grievance': 'problem',
    'preserver': 'protector',
    'projectors': 'planners',
    'parish': 'community',
    'bastard': 'illegitimate',
    'alas': 'unfortunately',
    'commonwealth': 'nation',
}

def read_file(filename):
    """Read the text file and return its contents"""
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

def get_word_statistics(text):
    """Generate word frequency statistics from the text"""
    # Remove punctuation and convert to lowercase for counting
    words = re.findall(r'\b[a-z]+(?:-[a-z]+)?\b', text.lower())
    word_freq = Counter(words)
    
    return {
        'total_words': len(words),
        'unique_words': len(word_freq),
        'most_common': word_freq.most_common(20),
        'word_freq': word_freq
    }

def identify_old_english_words(text, dictionary):
    """Identify Old English words found in the text"""
    words = re.findall(r'\b[a-z]+(?:-[a-z]+)?\b', text.lower())
    found_old_words = {}
    
    for old_word in dictionary.keys():
        if old_word.lower() in words:
            count = text.lower().count(old_word.lower())
            found_old_words[old_word] = {
                'count': count,
                'modern': dictionary[old_word]
            }
    
    return found_old_words

def replace_old_english(text, dictionary):
    """Replace Old English words with modern equivalents (case-insensitive)"""
    modified_text = text
    
    for old_word, modern_word in dictionary.items():
        # Handle case-insensitive replacement while preserving case
        pattern = re.compile(re.escape(old_word), re.IGNORECASE)
        
        def replace_func(match):
            original = match.group()
            if original[0].isupper():
                # If the original word starts with uppercase, capitalize the replacement
                return modern_word.capitalize()
            else:
                return modern_word
        
        modified_text = pattern.sub(replace_func, modified_text)
    
    return modified_text

def main():
    """Main execution function"""
    input_file = 'data/pg1080.txt'
    output_file = 'data/pg1080_modernized.txt'
    
    print("=" * 60)
    print("A Modest Proposal - Old English Modernizer")
    print("=" * 60)
    
    # Step 1: Read the file
    print("\n[1] Reading text file...")
    text = read_file(input_file)
    print(f"    ✓ File loaded ({len(text)} characters)")
    
    # Step 2: Get word statistics
    print("\n[2] Analyzing word statistics...")
    stats = get_word_statistics(text)
    print(f"    Total words: {stats['total_words']:,}")
    print(f"    Unique words: {stats['unique_words']:,}")
    print(f"\n    Top 10 most common words:")
    for word, count in stats['most_common'][:10]:
        print(f"        - '{word}': {count} times")
    
    # Step 3: Identify Old English words
    print("\n[3] Identifying Old English words found in text...")
    old_words_found = identify_old_english_words(text, OLD_TO_MODERN)
    print(f"    Found {len(old_words_found)} Old English words:")
    for old_word, info in sorted(old_words_found.items(), key=lambda x: x[1]['count'], reverse=True):
        print(f"        - '{old_word}' ({info['count']}x) → '{info['modern']}'")
    
    # Step 4: Replace Old English words
    print("\n[4] Replacing Old English words with modern versions...")
    modernized_text = replace_old_english(text, OLD_TO_MODERN)
    print(f"    ✓ Replacements completed")
    
    # Step 5: Save the modernized version
    print(f"\n[5] Saving modernized text to '{output_file}'...")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(modernized_text)
    print(f"    ✓ File saved successfully")
    
    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Original file:     {input_file}")
    print(f"Modernized file:   {output_file}")
    print(f"Words replaced:    {len(old_words_found)}")
    print(f"Total replacements: {sum(info['count'] for info in old_words_found.values())}")
    print("=" * 60)

if __name__ == '__main__':
    main()
