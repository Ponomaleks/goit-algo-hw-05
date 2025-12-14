from timeit import timeit
from Boyer_Moore_subst import boyer_moore_search
from KMP_subst_search import kmp_search
from Rabin_Karp_subst import rabin_karp_search as RKS_poly
from os import path

iterations = 100


def main():
    file1_path = path.join(path.dirname(__file__), "стаття_1.txt")
    file2_path = path.join(path.dirname(__file__), "стаття_2.txt")

    with open(file1_path, "r", encoding="utf-8") as f:
        text1 = f.read()
        file_name1 = path.basename(file1_path)

    with open(file2_path, "r", encoding="utf-8") as f:
        text2 = f.read()
        file_name2 = path.basename(file2_path)

    existing_substring = "структури даних"
    non_existing_substring = "nonexistentpattern"

    algorithms = {
        "Boyer-Moore": boyer_moore_search,
        "KMP": kmp_search,
        "Rabin-Karp": RKS_poly,
    }

    for text, text_name in [(text1, file_name1), (text2, file_name2)]:
        print(f"\nResults for {text_name}:")

        for substring, substring_name in [
            (existing_substring, "Existing Substring"),
            (non_existing_substring, "Non-existing Substring"),
        ]:
            print(f"\nSearching for: {substring_name} ('{substring}')")

            for algo_name, algo_func in algorithms.items():
                total_time = timeit(
                    stmt=lambda: algo_func(text, substring), number=iterations
                )
                avg_time = total_time / iterations
                print(f"{algo_name}: {avg_time:.6f} seconds")
                # print(algo_func(text, substring)) # ensure correctness of output


if __name__ == "__main__":
    main()
