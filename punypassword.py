def is_pass_puny(password: str) -> bool:
    '''Checks if a password is vulnerable to being instantly solved by brute force attacks.\n
    The word list used can be found at:\n
    '''
    with open("NordEasyPass.txt") as file:
        lines = file.readlines()
        badpasswds = set([line.rstrip() for line in lines])

    if password in badpasswds:
        return True
    return False


if __name__ == "__main__":
    example = "1qaz@WSX"
    print(f"Example puny password: {example}")
    print(f"Password vulnerable to instant-crack: {is_pass_puny(example)}")
