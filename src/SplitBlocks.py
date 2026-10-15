
def markdown_to_blocks(markdown):
    fresh_set=[]

    

    header=markdown.split("\n\n")
    
    for item in header:
        newboy=item.strip()
        if newboy!="":
            fresh_set.append(newboy)
        

    return(fresh_set)

    

