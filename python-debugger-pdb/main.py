from helpers import gather_data, process_data

def main():
    data = gather_data()
    # import pdb; pdb.set_trace()
    
    processed_data = process_data(data, foo='abc')
    print("Original Data:", data)
    print("Processed Data:", processed_data)


if __name__ == "__main__":
    main()
