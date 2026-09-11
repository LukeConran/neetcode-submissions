class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_list = []
        if strs == []: return "."
        for string in strs:
            if string == "":
                encoded_list.append("-1")
                continue
            string = [f"{ord(char)}" for char in string]
            string = " ".join(string)
            encoded_list.append(string)
        enc_str = "/".join(encoded_list)
        return enc_str

    def decode(self, s: str) -> List[str]:
        if s == ".": return []
        new_s = s.split("/")
        decoded_list = []
        for string in new_s:
            if string == "-1":
                decoded_list.append("")
                continue
            new_str = string.split(" ")
            dec_chars = [chr(int(char)) for char in new_str]
            dec_str = "".join(dec_chars)
            decoded_list.append(dec_str)
        return decoded_list