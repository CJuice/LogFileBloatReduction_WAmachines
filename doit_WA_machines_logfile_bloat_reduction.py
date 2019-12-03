"""

"""


def main():
    # IMPORTS
    import os
    import datetime

    # VARIABLES
    log_file_folders_path = r"D:\inetpub\logs\LogFiles"  # PRODUCTION
    acceptable_age_days = datetime.timedelta(days=120)
    now = datetime.datetime.now()

    # FUNCTIONALITY
    try:
        for root, dirnames, files in os.walk(log_file_folders_path):
            for file in files:

                # For files in the directory, process them.
                full_file_path = os.path.join(root, file)
                time_file_last_modified = os.path.getmtime(full_file_path)
                duration_since_file_last_modified = now - datetime.datetime.fromtimestamp(time_file_last_modified)
                is_older_than_acceptable_age = duration_since_file_last_modified > acceptable_age_days
                if is_older_than_acceptable_age:
                    try:
                        # os.remove(full_file_path)
                        print("FILE: {} REMOVED. Age: {}".format(full_file_path, duration_since_file_last_modified))
                    except Exception as e:
                        print("\tALERT: {} NOT REMOVED. EXCEPTION! {}".format(full_file_path, e))

    except IOError as io_err:
        print(io_err)
        exit()
    except Exception as e:
        print(e)
        exit()
    return


if __name__ == "__main__":
    main()
