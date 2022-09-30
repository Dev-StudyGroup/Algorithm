"""

    낮은 음계 1 => 높은 음계 8

"""

scales = list(map(int, input().split()))

ascending = sorted(scales)
descending = sorted(scales, reverse=True)

if scales == ascending:
    print("ascending")
elif scales == descending:
    print("descending")
else:
    print("mixed")


