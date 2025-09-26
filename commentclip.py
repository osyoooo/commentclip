#!/usr/bin/env python3
"""
commentclip - A tool to extract comments from source code files

This utility extracts comments from various programming language source files
and outputs them in different formats.
"""

import argparse
import re
import sys
import json
from pathlib import Path
from typing import List, Dict, Tuple, Optional


class CommentExtractor:
    """Extract comments from source code files based on file extension."""
    
    # Define comment patterns for different languages
    COMMENT_PATTERNS = {
        'python': [
            r'#.*$',  # Single line comments
            r'"""[\s\S]*?"""',  # Multi-line strings (docstrings)
            r"'''[\s\S]*?'''",  # Multi-line strings (docstrings)
        ],
        'javascript': [
            r'//.*$',  # Single line comments
            r'/\*[\s\S]*?\*/',  # Multi-line comments
        ],
        'java': [
            r'//.*$',  # Single line comments
            r'/\*[\s\S]*?\*/',  # Multi-line comments
        ],
        'c': [
            r'//.*$',  # Single line comments (C++)
            r'/\*[\s\S]*?\*/',  # Multi-line comments
        ],
        'cpp': [
            r'//.*$',  # Single line comments
            r'/\*[\s\S]*?\*/',  # Multi-line comments
        ],
        'go': [
            r'//.*$',  # Single line comments
            r'/\*[\s\S]*?\*/',  # Multi-line comments
        ],
        'rust': [
            r'//.*$',  # Single line comments
            r'/\*[\s\S]*?\*/',  # Multi-line comments
        ],
        'html': [
            r'<!--[\s\S]*?-->',  # HTML comments
        ],
        'css': [
            r'/\*[\s\S]*?\*/',  # CSS comments
        ],
        'shell': [
            r'#.*$',  # Shell comments
        ],
        'ruby': [
            r'#.*$',  # Single line comments
            r'=begin[\s\S]*?=end',  # Multi-line comments
        ],
        'php': [
            r'//.*$',  # Single line comments
            r'/\*[\s\S]*?\*/',  # Multi-line comments
            r'#.*$',  # Hash comments
        ],
    }
    
    # File extension to language mapping
    EXTENSION_MAP = {
        '.py': 'python',
        '.js': 'javascript',
        '.jsx': 'javascript',
        '.ts': 'javascript',
        '.tsx': 'javascript',
        '.java': 'java',
        '.c': 'c',
        '.h': 'c',
        '.cpp': 'cpp',
        '.cc': 'cpp',
        '.cxx': 'cpp',
        '.hpp': 'cpp',
        '.go': 'go',
        '.rs': 'rust',
        '.html': 'html',
        '.htm': 'html',
        '.css': 'css',
        '.scss': 'css',
        '.sass': 'css',
        '.sh': 'shell',
        '.bash': 'shell',
        '.zsh': 'shell',
        '.rb': 'ruby',
        '.php': 'php',
    }
    
    def detect_language(self, file_path: Path) -> Optional[str]:
        """Detect programming language based on file extension."""
        suffix = file_path.suffix.lower()
        return self.EXTENSION_MAP.get(suffix)
    
    def extract_comments(self, content: str, language: str) -> List[Dict[str, any]]:
        """Extract comments from source code content."""
        if language not in self.COMMENT_PATTERNS:
            return []
        
        comments = []
        patterns = self.COMMENT_PATTERNS[language]
        
        for pattern in patterns:
            matches = re.finditer(pattern, content, re.MULTILINE)
            for match in matches:
                comment_text = match.group(0)
                start_line = content[:match.start()].count('\n') + 1
                end_line = start_line + comment_text.count('\n')
                
                # Clean up comment text
                cleaned_text = self.clean_comment(comment_text, language)
                
                if cleaned_text.strip():  # Only add non-empty comments
                    comments.append({
                        'text': cleaned_text,
                        'start_line': start_line,
                        'end_line': end_line,
                        'raw': comment_text,
                        'type': self.get_comment_type(comment_text, language)
                    })
        
        # Sort comments by line number
        comments.sort(key=lambda x: x['start_line'])
        return comments
    
    def clean_comment(self, comment: str, language: str) -> str:
        """Clean comment text by removing comment markers."""
        if language == 'python':
            if comment.startswith('#'):
                return comment[1:].strip()
            elif comment.startswith('"""') or comment.startswith("'''"):
                return comment[3:-3].strip()
        
        elif language in ['javascript', 'java', 'c', 'cpp', 'go', 'rust', 'php']:
            if comment.startswith('//'):
                return comment[2:].strip()
            elif comment.startswith('/*'):
                return comment[2:-2].strip()
        
        elif language == 'html':
            if comment.startswith('<!--'):
                return comment[4:-3].strip()
        
        elif language == 'css':
            if comment.startswith('/*'):
                return comment[2:-2].strip()
        
        elif language in ['shell', 'ruby']:
            if comment.startswith('#'):
                return comment[1:].strip()
            elif language == 'ruby' and comment.startswith('=begin'):
                return comment[6:-4].strip()
        
        return comment.strip()
    
    def get_comment_type(self, comment: str, language: str) -> str:
        """Determine the type of comment (single-line, multi-line, docstring)."""
        if language == 'python':
            if comment.startswith('"""') or comment.startswith("'''"):
                return 'docstring'
            else:
                return 'single-line'
        
        elif language in ['javascript', 'java', 'c', 'cpp', 'go', 'rust', 'php']:
            if comment.startswith('/*'):
                return 'multi-line'
            else:
                return 'single-line'
        
        elif language == 'ruby':
            if comment.startswith('=begin'):
                return 'multi-line'
            else:
                return 'single-line'
        
        return 'single-line'


def process_file(file_path: Path, extractor: CommentExtractor) -> Dict[str, any]:
    """Process a single file and extract comments."""
    try:
        content = file_path.read_text(encoding='utf-8')
        language = extractor.detect_language(file_path)
        
        if not language:
            return {
                'file': str(file_path),
                'language': 'unknown',
                'error': 'Unsupported file type',
                'comments': []
            }
        
        comments = extractor.extract_comments(content, language)
        
        return {
            'file': str(file_path),
            'language': language,
            'comments': comments,
            'total_comments': len(comments)
        }
    
    except Exception as e:
        return {
            'file': str(file_path),
            'language': 'unknown',
            'error': str(e),
            'comments': []
        }


def main():
    """Main CLI function."""
    parser = argparse.ArgumentParser(
        description='Extract comments from source code files',
        epilog='Example: commentclip --format json *.py'
    )
    
    parser.add_argument(
        'files',
        nargs='+',
        help='Source code files to process'
    )
    
    parser.add_argument(
        '--format',
        choices=['text', 'json'],
        default='text',
        help='Output format (default: text)'
    )
    
    parser.add_argument(
        '--line-numbers',
        action='store_true',
        help='Include line numbers in output'
    )
    
    parser.add_argument(
        '--type',
        choices=['single-line', 'multi-line', 'docstring'],
        help='Filter comments by type'
    )
    
    parser.add_argument(
        '--language',
        help='Override language detection'
    )
    
    args = parser.parse_args()
    
    extractor = CommentExtractor()
    results = []
    
    # Process all input files
    for file_pattern in args.files:
        path = Path(file_pattern)
        if path.is_file():
            results.append(process_file(path, extractor))
        else:
            # Handle glob patterns
            for file_path in Path('.').glob(file_pattern):
                if file_path.is_file():
                    results.append(process_file(file_path, extractor))
    
    if not results:
        print("No files found to process.", file=sys.stderr)
        sys.exit(1)
    
    # Filter by comment type if specified
    if args.type:
        for result in results:
            result['comments'] = [
                c for c in result['comments'] 
                if c['type'] == args.type
            ]
            result['total_comments'] = len(result['comments'])
    
    # Output results
    if args.format == 'json':
        print(json.dumps(results, indent=2))
    else:
        for result in results:
            if result.get('error'):
                print(f"Error processing {result['file']}: {result['error']}", file=sys.stderr)
                continue
            
            print(f"\n=== {result['file']} ({result['language']}) ===")
            print(f"Total comments: {result['total_comments']}")
            
            for comment in result['comments']:
                print(f"\n[{comment['type'].upper()}]", end="")
                if args.line_numbers:
                    if comment['start_line'] == comment['end_line']:
                        print(f" Line {comment['start_line']}:", end="")
                    else:
                        print(f" Lines {comment['start_line']}-{comment['end_line']}:", end="")
                print()
                print(comment['text'])


if __name__ == '__main__':
    main()