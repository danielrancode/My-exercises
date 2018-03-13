text = str(input('Enter text: '))
tag = str(input('enter tag: '))

# Define function to make put text between tags
def make_tags (text, tag):
    new_string = '<' + str(tag) + '>' + str(text) + '</' + str(tag) + '>'
    print (new_string)

# Define main function
def main():
    make_tags(text, tag)

# Execute main function
main()
