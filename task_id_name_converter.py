def camel_to_snake(name):                                 
    a = list(name)                                        
    for c in range(len(a)):                                    
        if a[c].isupper() and c != 0 and a[c-1] != '_':                  
            a.insert(c,'_')                               
            c += 1                                        
            return ''.join(a).lower()       

def snake_to_camel(name):
	name = name.title().replace('_', '')
	return name