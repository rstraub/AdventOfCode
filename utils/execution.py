def read_input_and_execute_solution(file_path, part_one_fn, part_two_fn):
    with open(file_path, "r") as f:
        contents = f.read()
        print(part_one_fn(contents))
        print(part_two_fn(contents))
