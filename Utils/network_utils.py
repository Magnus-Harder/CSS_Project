from collections import defaultdict

def get_edge_chapter_weight(character1: list, character2: list, chapter: list):
    weight = 0
    for page in chapter:
        page_text = ' '.join(page)
        if any([char in page_text for char in character1]) and any([char in page_text for char in character2]):
                weight += 1
    
    return weight

def get_edge_book_weight(character1: list, character2: list, book: dict):
    weight = defaultdict(int)
    for chapternr in range(1, len(book)+1):
        weight[chapternr] = get_edge_chapter_weight(character1, character2, book[chapternr])
    return weight

def get_node_size(character: list, book: dict):
    size = defaultdict(int)
    for chapternr, chapter  in book.items():
        for page in chapter:
            page_text = ' '.join(page)
            if any([char in page_text for char in character]):
                size[chapternr] += 1
    return size