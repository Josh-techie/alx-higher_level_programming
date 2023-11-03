#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    data = dir(hidden_4)
    for i in range(len(data)):
        if (data[i][:2] != "__"):
            print(data[i])
