class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        if '.' in IP:
            if self.is_ipv4(IP):
                return 'IPv4'
        elif ':' in IP:
            if self.is_ipv6(IP):
                return 'IPv6'
        return 'Neither'


    #https://en.wikipedia.org/wiki/IPv4
    def is_ipv4(self, IP):
        try:
            lst = IP.split('.')
            if len(lst) != 4:
                return False
            for ip in lst:
                if len(ip) > 1 and ip.startswith('0') :
                    return False
                tmp = int(ip)
                if tmp < 0 or tmp > 255 or not ip.isdigit():
                    return False
            return True
        except:
            return False


    #https://en.wikipedia.org/wiki/IPv6
    def is_ipv6(self, IP):
        try:
            lst = IP.split(':')
            if len(lst) != 8:
                return False
            if ('::' in IP and IP.count('::') > 1) :
                return False
            for ip in lst:
                tmp = int(ip, 16)
                if len(ip) > 4 or not ip.isalnum():
                    return False

            return True
        except:
            return False
