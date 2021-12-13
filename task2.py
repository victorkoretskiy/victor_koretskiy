# the given function was tested by the 'alphabet.txt'
def file_redactor(file, symbol_qty):
    with open(file) as f:
        all_symbols = str(f.read())
    smb_qty = int(symbol_qty)    
    str_begin = all_symbols[:smb_qty]
    str_end = all_symbols[-1*smb_qty:]
    if len(all_symbols)%2 == 0 and int(symbol_qty)%2 == 0 or len(all_symbols)%2 != 0 and int(symbol_qty)%2 == 0:
        str_middle = all_symbols[((len(all_symbols)//2) - (int(symbol_qty)//2)):((len(all_symbols)//2) + (int(symbol_qty))//2)]
    if len(all_symbols)%2 == 0 and int(symbol_qty)%2 != 0 or len(all_symbols)%2 != 0 and int(symbol_qty)%2 != 0:
        str_middle = all_symbols[((len(all_symbols)//2) - (int(symbol_qty)//2)):((len(all_symbols)//2) + (int(symbol_qty))//2+1)]
    if len(str_middle)+len(str_begin)+len(str_end) > len(all_symbols):
        print('The slices are too long and do not fit into the length of the original string')
    else:
        print([str_begin, str_middle, str_end])
