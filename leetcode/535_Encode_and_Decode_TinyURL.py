# 739 / 739 test cases passed.
# Status: Accepted
# Runtime: 39 ms
class Codec:
    def __init__(self):
        self.urls = []


    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        self.urls.append(longUrl)
        return 'http://tinyurl.com/' + str(hex(len(self.urls) - 1)[2:])


    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.urls[int(shortUrl.split('/')[-1], 16)]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
