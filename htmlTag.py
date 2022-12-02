# def htmlTagGenerate(text):
#     text = f'<h2>{text}<h/2>'
#     return text

def htmlTagGenerateDynamic(text,tag_name):
    htmltext = f'<{tag_name}>{text}</{tag_name}>'
    return htmltext

print(htmlTagGenerateDynamic('my name is khan',"h5"))