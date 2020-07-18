# Python3 program to find the
# count of k length substrings
# with k distinct characters
# using sliding window

# Function to return the
# required count of substrings
def countSubstrings(str, K):
    N = len(str)

    # Store the count
    answer = 0

    # Store the count of
    # distinct characters
    # in every window
    map = {}

    # Store the frequency of
    # the first K length substring
    for i in range(K):
        # Increase frequency of
        # i-th character
        map[str[i]] = map.get(str[i], 0) + 1

    # If K distinct characters
    # exist
    if (len(map) == K):
        answer += 1

    # Traverse the rest of the
    # substring
    for i in range(K, N):

        # Increase the frequency
        # of the last character
        # of the current substring
        map[str[i]] = map.get(str[i], 0) + 1

        # Decrease the frequency
        # of the first character
        # of the previous substring
        map[str[i - K]] -= 1

        # If the character is not present
        # in the current substring
        if (map[str[i - K]] == 0):
            del map[str[i - K]]

        # If the count of distinct
        # characters is 0
        if (len(map) == K):
            print(map)
            answer += 1

    # Return the count
    return answer


# Driver code
if __name__ == '__main__':
    str = "aabcdabbcdc"

    # Integer K
    K = 3

    # Print the count of K length
    # substrings with k distinct characters
    print(countSubstrings(str, K))

# This code is contributed by mohit kumar 29
