import pathlib

def get_cats_info(path) -> list:
    '''function change txt file to structured list of dicts'''
    cats_list = []
    cats_path = pathlib.Path(path) # getting cats doc
    try:
        with open(cats_path, 'r', encoding='utf-8') as cats_txt:   
            all_cats = [cat.strip().split(',') for cat in cats_txt.readlines()]  
            for cat in all_cats:
                if len(cat) == 3:
                    cats_list.append({'id': cat[0], 'name': cat[1], 'age': cat[2]})
        return cats_list
    
    except (FileNotFoundError,TypeError, IndexError):
        raise IndexError(f"something's wrong")   

print(get_cats_info('cats.txt'))
