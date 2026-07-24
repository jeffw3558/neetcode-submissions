class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=[]
        for s in strs:
            encoded.append(str(len(s)))
            encoded.append("#")
            encoded.append(s)
        return "".join(encoded)
    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        
        while i < len(s):
            # Find the position of the '#' delimiter
            j = i
            while s[j] != "#":
                j += 1
            
            # Extract the length of the string
            length = int(s[i:j])
            
            # Move index past '#'
            i = j + 1
            
            # Read the actual string using the length
            decoded.append(s[i : i + length])
            
            # Move index to the start of the next encoded string
            i += length
            
        return decoded
            
            


            