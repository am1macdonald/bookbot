def main():
    path_to_file = "./books/frankenstein.txt"

    with open(path_to_file) as f:
        file_contents = f.read()
        charMap = {}
        tot = 0
        for char in file_contents.lower():
            if char.isalpha():
                tot += 1
            if char in charMap:
                charMap[char] += 1
            else:
                charMap[char] = 1


        print(f'--- Begin report of {path_to_file} ---')
        print(f'{tot} characters found in the document\n')

        for char in reversed(sorted(charMap, key=lambda x: charMap[x])):
            if char.isalpha():
                print(f"The '{char}' character was found {charMap[char]} times")

        print('--- End report ---')


main()
