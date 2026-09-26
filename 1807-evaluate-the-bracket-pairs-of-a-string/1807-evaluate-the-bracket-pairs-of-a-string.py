class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        key_to_val = {key: val for key, val in knowledge}
        result = []
        key_arr = []
        in_bracket = False

        for i, c in enumerate(s):
            if c == '(':
                in_bracket = True
            elif c == ')':
                key_str = "".join(key_arr)
                if key_str in key_to_val:
                    result.append(key_to_val[key_str])
                else:
                    result.append("?")
                in_bracket = False
                key_arr = []
            elif in_bracket:
                key_arr.append(c)
            else:
                result.append(c)

        return "".join(result)