# def backspaceCompare(S, T):
#     """
#     :type S: str
#     :type T: str
#     :rtype: bool
#     """
#     # Time Complexity O(n); Space: O(n)
#     def backSpaceFunction(str):
#         ans = []
#         for c in str:
#             if c != "#":
#                 ans.append(c)
#             elif ans:
#                 ans.pop()
#         return ans

#     return backSpaceFunction(S) == backSpaceFunction(T)


def backspaceCompare(S, T):
    # Time Complexity O(n); Space: O(1)
    S_pointer = len(S) - 1
    S_skips = 0
    T_pointer = len(T) - 1
    T_skips = 0

    while(S_pointer >= 0 or T_pointer >= 0):
        while (S_pointer >= 0):
            if S[S_pointer] == '#':
                S_pointer -= 1
                S_skips += 1
            elif S_skips > 0:  # As char !='#' but skips > 0
                S_pointer -= 1
                S_skips -= 1
            else:
                break  # As skip = 0, and char !='#'

        while (T_pointer >= 0):
            if T[T_pointer] == '#':
                T_pointer -= 1
                T_skips += 1
            elif T_skips > 0:
                T_pointer -= 1
                T_skips -= 1
            else:
                break

        if (S_pointer >= 0 and T_pointer >= 0 and S[S_pointer] != T[T_pointer]):
            return False

        # Ensure 2 pointer still >= 0
        # Not expecting to compare char vs nothing
        if (S_pointer >= 0) != (T_pointer >= 0):
            return False

        S_pointer -= 1
        T_pointer -= 1

    return True


if __name__ == '__main__':
    # S = "ab#c"
    # T = "ad#c"

    # S = "a#c"
    # T = "b"

    S = "ab##"
    print(S.replace(S[1], ''))
    T = "c#d#"
    # print(backspaceCompare(S, T))
