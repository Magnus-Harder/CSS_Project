import pandas as pd
import re
import os

def split_chapter(Book):
    chapters_split = "\n{9}|\n{8}|\n{7}|\n{6}|\n{5}[0-9]+\s?\n{5}"
    chapters = re.split(chapters_split, Book)
    return chapters

def format_pages(Chapter):
    page_pattern = "Page\s\|\s[0-9]+\s[a-zA-Z\s]+-\sJ.K.\sRowling\s"
    chapter_text = re.sub(page_pattern,"", Chapter)
    chapter_text = re.sub("\n{2,}|\t","", Chapter)
    return chapter_text

def preprocess_book(filename: str = "Book 1 - The Philosopher's Stone"):
    filepath = r"data/raw_text/"
    f = open(filepath + filename + '.txt', "r", encoding="utf-8")
    Book = f.read()
    
    returnpath = r"data/book_by_chapter/"
    for i, chapter in enumerate(split_chapter(Book)):
        chapter = format_pages(chapter)
        with open(returnpath + f"{filename}/{i+1}.txt", "w", encoding="utf-8") as f:
            f.write(chapter)
    
    with open(os.path.join(filepath, filename) + '.txt', "w", encoding="utf-8") as f:
        f.write(format_pages(Book))