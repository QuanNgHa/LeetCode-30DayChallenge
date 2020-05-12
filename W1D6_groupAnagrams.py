from collections import defaultdict


def groupAnagrams(strs):
    # Initialize a default dictionary (Hash Table) with value = List
    ans = defaultdict(list)

    for s in strs:
        # sorted(s) => Return a List of sorted character of a string
        # (['a', 'e', 't'], <type 'list'>)
        #print(sorted(s), type(sorted(s)))

        ans[str(sorted(s))].append(s)
    return ans.values()


def main():
    print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


if __name__ == "__main__":
    main()
