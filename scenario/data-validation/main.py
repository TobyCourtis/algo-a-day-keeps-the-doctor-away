import re

# scenario question: Create a password validator in Python verifying against typical password checks
class PasswordValidator:
    banned_phrases = ["letmein", "password", "123"]
    capital_letter_regex = r"[A-Z]"
    number_regex = r"[0-9]"

    def __init__(self):
        print("\ninit\n")

    def validate_password(self, password: str) -> bool:
        return all([
            self._validate_length(password),
            self._validate_contains_capital(password),
            self._validate_contains_number(password),
            self._validate_not_contains_common_phrase(password)
        ])

    def _validate_length(self, password: str) -> bool:
        if 31 > len(password) > 10:
            return True
        else:
            print("ERR: Password must be LT 32, GT 9")
            return False

    def _validate_contains_capital(self, password: str) -> bool:
        if len(re.findall(self.capital_letter_regex, password)) > 0:
            return True
        else:
            print("ERR: Password does not contain capital letter")
            return False

    def _validate_contains_number(self, password: str) -> bool:
        if len(re.findall(self.number_regex, password)) > 0:
            return True
        else:
            print("ERR: Password does not contain number")
            return False

    def _validate_not_contains_common_phrase(self, password: str) -> bool:
        password = password.lower()
        for banned_word in self.banned_phrases:
            if banned_word in password:
                print(f"ERR: Password contained banned keyword: {banned_word}")
                return False
        return True


if __name__ == "__main__":
    password_in = "Somethingnovel23"
    p = PasswordValidator()
    print(f"\nPassword valid: {p.validate_password(password_in)}")
