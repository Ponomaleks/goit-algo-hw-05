def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    counter = 0

    while low <= high:
        counter += 1
        mid = (high + low) // 2

        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1

        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            high = mid - 1

        # інакше x присутній на позиції і повертаємо його
        else:
            return (counter, arr[mid])

    # якщо елемент не знайдений
    if low < len(arr):
        upper_bound = arr[low]
    else:
        upper_bound = None

    return (counter, upper_bound)


def main():
    arr = [2.64, 3.66, 4, 10.651, 10.659, 40.15361, 100.1234, 215.23, 400.12, 1000.00]
    x = 11
    result = binary_search(arr, x)
    if result != -1:
        print(f"Founded element or upper bound: {result}")


if __name__ == "__main__":
    main()
