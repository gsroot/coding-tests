def get_sys_set(syn_set_list, word):
    for syn_set in syn_set_list:
        if word in syn_set:
            return syn_set
    return [word]


def permutation(matches, i, sentence):
    output = []
    if i >= len(matches):
        output.append(sentence)
        return output
    for x in matches[i]:
        output.append(permutation(matches, i + 1, sentence + x))
    return output


def main(syn_set_list, query):
    words = query.split()
    matches = []
    for w in words:
        matches.append(get_sys_set(syn_set_list, w))
    return permutation(matches, 0, '')


if __name__ == '__main__':
    syn_set_list = [['LG', '엘지'], ['티비', '티브이', 'TV', '테레비', '텔레비젼']]
    print(main(syn_set_list, '내방 LG TV 켜줘'))
