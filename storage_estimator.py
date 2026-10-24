"""Storage Estimator - estimates how much storage a set of files needs."""


def estimate_storage_mb(num_files, avg_size_mb):
    """Return the total storage needed in MB."""
    return num_files * avg_size_mb


def main():
    print("=== Storage Estimator ===")
    num_files = int(input("Number of files: "))
    avg_size_mb = float(input("Average file size (MB): "))
    total_mb = estimate_storage_mb(num_files, avg_size_mb)
    print("Total storage needed:", total_mb, "MB")


if __name__ == "__main__":
    main()
