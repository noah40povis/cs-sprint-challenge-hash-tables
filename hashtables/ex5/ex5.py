# Your code here

paths = [
    "/usr/local/share/foo.txt",
    "/usr/bin/ls",
    "/home/davidlightman/foo.txt",
    "/bin/su"
]
queries = [
    "ls",
    "foo.txt",
    "nosuchfile.txt"
]

def finder(files, queries):
    results = []
    split_paths = files.split('/')
    for files in split_paths:
        if queries[0] == split_paths[0]:
            results += [] 
        

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
