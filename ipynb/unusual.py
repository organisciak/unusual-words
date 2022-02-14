from PIL import Image

def img_from_row(row, hpad=6, wpad=25, path_pattern='../data/pages/dictionary-{}.png'):
    ''' Input: series'''
    path = path_pattern.format(row['pagenum'])
    img_file = Image.open(path)
    return img_file.crop((row['left']-wpad, row['top']-hpad, row['right']+wpad, row['bottom']+hpad))

def img_from_match(matches, hpad=6, wpad=25, _debug=False):
    ''' Potentially combine multiple rows'''
    if len(matches) == 1:
        img = img_from_row(matches.iloc[0], hpad=hpad, wpad=wpad)
        return img
    else:
        hsize = (matches['bottom'] - matches['top']).sum() + 2*hpad
        wsize = (matches['right'] - matches['left']).max() + 2*wpad

        new_im = Image.new('RGB', (wsize, hsize),
                           color=((0,0,255) if _debug else (255,255,255)))
        y_offset = 0

        for i, match in matches.iterrows():
            img = img_from_row(match, hpad, wpad)
            new_im.paste(img, (0, y_offset))
            y_offset += img.height
        return new_im
    
def img_from_illustration(row, path_pattern='../data/pages/dictionary-{}.png'):
    return Image.open(path_pattern.format(row['pagenum'])).crop((row['left']-3, row['top']-3, row['right']+3, row['bottom']+3))
